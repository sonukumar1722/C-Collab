# Security Considerations for C-Collab

Security is paramount when allowing users to execute arbitrary C/C++ code on your servers. This document outlines critical security measures and best practices.

## Table of Contents
- [Threat Model](#threat-model)
- [Security Layers](#security-layers)
- [Implementation Details](#implementation-details)
- [Security Checklist](#security-checklist)
- [Incident Response](#incident-response)

---

## Threat Model

### Potential Threats

1. **Malicious Code Execution**
   - Buffer overflows
   - Fork bombs
   - Infinite loops
   - Resource exhaustion
   - File system attacks

2. **Container Escape**
   - Kernel exploits
   - Docker vulnerabilities
   - Privilege escalation

3. **Network Attacks**
   - DDoS from execution environment
   - Port scanning
   - Data exfiltration

4. **Application-Level Attacks**
   - SQL injection
   - XSS attacks
   - CSRF
   - Authentication bypass

5. **Data Breaches**
   - Unauthorized access to notebooks
   - Credential theft
   - Session hijacking

---

## Security Layers

### Layer 1: Application Security

#### Authentication & Authorization

```typescript
// JWT-based authentication with refresh tokens
interface JWTPayload {
  userId: string;
  email: string;
  role: 'user' | 'admin';
  iat: number;
  exp: number;
}

// Short-lived access tokens (15 minutes)
const ACCESS_TOKEN_EXPIRY = '15m';

// Longer-lived refresh tokens (7 days)
const REFRESH_TOKEN_EXPIRY = '7d';
```

**Best Practices:**
- Use bcrypt or argon2 for password hashing (min 12 rounds)
- Implement rate limiting on login attempts
- Enforce strong password policies
- Use HTTPS everywhere
- Implement CSRF protection
- Set secure HTTP-only cookies

#### Input Validation

```typescript
// Validate all user inputs
import { z } from 'zod';

const CodeExecutionSchema = z.object({
  code: z.string()
    .min(1, 'Code cannot be empty')
    .max(50000, 'Code too large'),
  compiler: z.enum(['gcc-11', 'gcc-12', 'gcc-13', 'clang-15', 'clang-16']),
  language: z.enum(['c', 'cpp']),
  compilerFlags: z.string().optional(),
  stdin: z.string().max(10000).optional(),
});
```

**Validation Rules:**
- Sanitize all user inputs
- Validate file uploads
- Limit payload sizes
- Check MIME types
- Escape SQL queries (use parameterized queries)

#### Rate Limiting

```typescript
import rateLimit from 'express-rate-limit';

// General API rate limit
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  message: 'Too many requests, please try again later',
});

// Execution rate limit (stricter)
const executionLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 10, // 10 executions per minute per user
  keyGenerator: (req) => req.user.id, // Per user
});

app.use('/api/', apiLimiter);
app.use('/api/execute', executionLimiter);
```

### Layer 2: Docker Container Isolation

#### Dockerfile Best Practices

```dockerfile
FROM gcc:12-alpine

# Don't run as root
RUN adduser -D -H -s /sbin/nologin coderunner

# Set working directory
WORKDIR /sandbox

# Copy only necessary files
COPY compile.sh /usr/local/bin/

# Remove unnecessary tools
RUN apk del apk-tools

# Switch to non-privileged user
USER coderunner

# Set read-only filesystem
ENTRYPOINT ["/usr/local/bin/compile.sh"]
```

#### Container Execution Limits

```bash
docker run \
  --rm \
  --name execution-${UUID} \
  # CPU limits
  --cpus="0.5" \
  --cpu-shares=512 \
  # Memory limits
  --memory="256m" \
  --memory-swap="256m" \
  --memory-reservation="128m" \
  --oom-kill-disable=false \
  # Disable networking
  --network="none" \
  # Read-only root filesystem
  --read-only \
  # Temporary filesystem for /tmp
  --tmpfs /tmp:size=50m,noexec,nosuid,nodev \
  # Drop all capabilities
  --cap-drop=ALL \
  # No new privileges
  --security-opt="no-new-privileges:true" \
  # Seccomp profile
  --security-opt="seccomp=/etc/seccomp/profile.json" \
  # AppArmor profile
  --security-opt="apparmor=ccollab-executor" \
  # Process limits
  --pids-limit=50 \
  # Execution timeout
  --stop-timeout=30 \
  ccollab/gcc-12:latest
```

### Layer 3: Seccomp Profile

**seccomp-profile.json** - Whitelist allowed system calls:

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": [
    "SCMP_ARCH_X86_64",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X32"
  ],
  "syscalls": [
    {
      "names": [
        "read", "write", "open", "close", "stat", "fstat", "lstat",
        "poll", "lseek", "mmap", "mprotect", "munmap", "brk",
        "rt_sigaction", "rt_sigprocmask", "rt_sigreturn",
        "access", "pipe", "select", "sched_yield", "mremap",
        "msync", "mincore", "madvise", "dup", "dup2", "pause",
        "nanosleep", "getitimer", "alarm", "setitimer", "getpid",
        "sendfile", "socket", "connect", "accept", "sendto",
        "recvfrom", "sendmsg", "recvmsg", "shutdown", "bind",
        "listen", "getsockname", "getpeername", "socketpair",
        "setsockopt", "getsockopt", "clone", "fork", "vfork",
        "execve", "exit", "wait4", "kill", "uname", "semget",
        "semop", "semctl", "shmdt", "msgget", "msgsnd", "msgrcv",
        "msgctl", "fcntl", "flock", "fsync", "fdatasync",
        "truncate", "ftruncate", "getdents", "getcwd", "chdir",
        "fchdir", "rename", "mkdir", "rmdir", "creat", "link",
        "unlink", "symlink", "readlink", "chmod", "fchmod",
        "chown", "fchown", "lchown", "umask", "gettimeofday",
        "getrlimit", "getrusage", "sysinfo", "times", "ptrace",
        "getuid", "syslog", "getgid", "setuid", "setgid",
        "geteuid", "getegid", "setpgid", "getppid", "getpgrp",
        "setsid", "setreuid", "setregid", "getgroups", "setgroups",
        "setresuid", "getresuid", "setresgid", "getresgid",
        "getpgid", "setfsuid", "setfsgid", "getsid", "capget",
        "capset", "rt_sigpending", "rt_sigtimedwait", "rt_sigqueueinfo",
        "rt_sigsuspend", "sigaltstack", "utime", "mknod",
        "uselib", "personality", "ustat", "statfs", "fstatfs",
        "sysfs", "getpriority", "setpriority", "sched_setparam",
        "sched_getparam", "sched_setscheduler", "sched_getscheduler",
        "sched_get_priority_max", "sched_get_priority_min",
        "sched_rr_get_interval", "mlock", "munlock", "mlockall",
        "munlockall", "vhangup", "modify_ldt", "pivot_root",
        "_sysctl", "prctl", "arch_prctl", "adjtimex", "setrlimit",
        "chroot", "sync", "acct", "settimeofday", "mount",
        "umount2", "swapon", "swapoff", "reboot", "sethostname",
        "setdomainname", "iopl", "ioperm", "create_module",
        "init_module", "delete_module", "get_kernel_syms",
        "query_module", "quotactl", "nfsservctl", "getpmsg",
        "putpmsg", "afs_syscall", "tuxcall", "security",
        "gettid", "readahead", "setxattr", "lsetxattr",
        "fsetxattr", "getxattr", "lgetxattr", "fgetxattr",
        "listxattr", "llistxattr", "flistxattr", "removexattr",
        "lremovexattr", "fremovexattr", "tkill", "time",
        "futex", "sched_setaffinity", "sched_getaffinity",
        "set_thread_area", "io_setup", "io_destroy", "io_getevents",
        "io_submit", "io_cancel", "get_thread_area", "lookup_dcookie",
        "epoll_create", "epoll_ctl_old", "epoll_wait_old",
        "remap_file_pages", "getdents64", "set_tid_address",
        "restart_syscall", "semtimedop", "fadvise64", "timer_create",
        "timer_settime", "timer_gettime", "timer_getoverrun",
        "timer_delete", "clock_settime", "clock_gettime",
        "clock_getres", "clock_nanosleep", "exit_group",
        "epoll_wait", "epoll_ctl", "tgkill", "utimes",
        "vserver", "mbind", "set_mempolicy", "get_mempolicy",
        "mq_open", "mq_unlink", "mq_timedsend", "mq_timedreceive",
        "mq_notify", "mq_getsetattr", "kexec_load", "waitid",
        "add_key", "request_key", "keyctl", "ioprio_set",
        "ioprio_get", "inotify_init", "inotify_add_watch",
        "inotify_rm_watch", "migrate_pages", "openat", "mkdirat",
        "mknodat", "fchownat", "futimesat", "newfstatat",
        "unlinkat", "renameat", "linkat", "symlinkat", "readlinkat",
        "fchmodat", "faccessat", "pselect6", "ppoll", "unshare",
        "set_robust_list", "get_robust_list", "splice", "tee",
        "sync_file_range", "vmsplice", "move_pages", "utimensat",
        "epoll_pwait", "signalfd", "timerfd_create", "eventfd",
        "fallocate", "timerfd_settime", "timerfd_gettime",
        "accept4", "signalfd4", "eventfd2", "epoll_create1",
        "dup3", "pipe2", "inotify_init1", "preadv", "pwritev",
        "rt_tgsigqueueinfo", "perf_event_open", "recvmmsg",
        "fanotify_init", "fanotify_mark", "prlimit64",
        "name_to_handle_at", "open_by_handle_at", "clock_adjtime",
        "syncfs", "sendmmsg", "setns", "getcpu", "process_vm_readv",
        "process_vm_writev"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

**Important Blocked Syscalls:**
- `socket`, `connect`, `bind` - Prevent network access
- `ptrace` - Prevent debugging other processes
- `reboot`, `shutdown` - Prevent system control
- `mount`, `umount` - Prevent filesystem manipulation

### Layer 4: AppArmor Profile

**apparmor-profile** - Mandatory Access Control:

```
#include <tunables/global>

profile ccollab-executor flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>

  # Deny network access
  deny network,

  # Deny capability
  deny capability,

  # Allow read access to system libraries
  /lib/** r,
  /usr/lib/** r,
  /lib64/** r,
  /usr/lib64/** r,

  # Allow access to compilers
  /usr/bin/gcc ix,
  /usr/bin/g++ ix,
  /usr/bin/clang ix,
  /usr/bin/clang++ ix,

  # Allow read-only access to system files
  /etc/ld.so.cache r,
  /etc/ld.so.conf r,
  /etc/ld.so.conf.d/ r,
  /etc/ld.so.conf.d/** r,

  # Allow access to /tmp and /sandbox
  /tmp/** rw,
  /sandbox/** rw,

  # Deny access to sensitive directories
  deny /proc/** w,
  deny /sys/** w,
  deny /dev/** rw,
  deny /home/** rw,
  deny /root/** rw,

  # Allow reading from stdin, writing to stdout/stderr
  /dev/null rw,
  /dev/zero r,
  /dev/random r,
  /dev/urandom r,
}
```

### Layer 5: Resource Limits (cgroups)

Implemented via Docker:

```typescript
const RESOURCE_LIMITS = {
  // CPU: 0.5 cores (50% of one core)
  cpus: '0.5',
  
  // Memory: 256MB
  memory: '256m',
  memorySwap: '256m', // Disable swap
  
  // Processes: Max 50
  pidsLimit: 50,
  
  // Execution timeout: 30 seconds
  timeout: 30000,
  
  // Disk I/O: Limit write operations
  deviceWriteBps: '10mb',
};
```

### Layer 6: Network Isolation

```bash
# No network access in containers
--network="none"

# Or use custom network with firewall rules
docker network create \
  --driver bridge \
  --subnet 172.25.0.0/16 \
  --opt "com.docker.network.bridge.enable_ip_masquerade=false" \
  --opt "com.docker.network.bridge.enable_icc=false" \
  isolated-network
```

### Layer 7: Input Sanitization

```typescript
// Sanitize compiler flags
function sanitizeCompilerFlags(flags: string): string {
  // Whitelist allowed flags
  const allowedFlags = [
    '-std=c++11', '-std=c++14', '-std=c++17', '-std=c++20', '-std=c++23',
    '-O0', '-O1', '-O2', '-O3', '-Os',
    '-Wall', '-Wextra', '-Werror',
    '-g', '-ggdb',
    '-pedantic',
    '-march=native',
  ];
  
  const flagsArray = flags.split(' ').filter(Boolean);
  const sanitized = flagsArray.filter(flag => 
    allowedFlags.some(allowed => flag.startsWith(allowed))
  );
  
  return sanitized.join(' ');
}

// Prevent path traversal
function sanitizeFilename(filename: string): string {
  // Remove path traversal attempts
  const clean = filename.replace(/[^a-zA-Z0-9._-]/g, '_');
  
  // Limit length
  return clean.substring(0, 100);
}
```

---

## Implementation Details

### Execution Flow with Security

```typescript
async function executeCode(request: ExecutionRequest): Promise<ExecutionResult> {
  // 1. Validate input
  const validated = CodeExecutionSchema.parse(request);
  
  // 2. Check rate limits
  await checkRateLimit(request.userId);
  
  // 3. Sanitize inputs
  const sanitizedCode = sanitizeCode(validated.code);
  const sanitizedFlags = sanitizeCompilerFlags(validated.compilerFlags || '');
  
  // 4. Create unique execution ID
  const executionId = uuid.v4();
  
  // 5. Queue job
  await executionQueue.add('execute', {
    executionId,
    code: sanitizedCode,
    compiler: validated.compiler,
    flags: sanitizedFlags,
    userId: request.userId,
  }, {
    timeout: 35000, // 35 seconds (5 seconds buffer)
    attempts: 1, // No retries for security
    removeOnComplete: true,
    removeOnFail: false,
  });
  
  // 6. Worker processes job in isolated Docker container
  // 7. Return results (sanitized)
  
  return {
    executionId,
    status: 'queued',
  };
}

// Worker
executionQueue.process('execute', async (job) => {
  const { executionId, code, compiler, flags } = job.data;
  
  try {
    // Execute in Docker container with all security measures
    const result = await dockerExecute({
      executionId,
      code,
      compiler,
      flags,
      timeout: 30000,
      resources: RESOURCE_LIMITS,
      seccomp: '/etc/seccomp/profile.json',
      apparmor: 'ccollab-executor',
    });
    
    return {
      stdout: sanitizeOutput(result.stdout),
      stderr: sanitizeOutput(result.stderr),
      exitCode: result.exitCode,
      executionTime: result.executionTime,
    };
  } catch (error) {
    // Log error for monitoring
    logger.error('Execution failed', { executionId, error });
    
    throw error;
  } finally {
    // Cleanup: Remove container immediately
    await cleanupContainer(executionId);
  }
});
```

### Monitoring & Alerting

```typescript
// Monitor for suspicious activity
const suspiciousPatterns = [
  /system\s*\(/,      // system() calls
  /popen\s*\(/,       // popen() calls
  /exec[lv]p?\s*\(/,  // exec family
  /__asm__/,          // Assembly injection
  /\/proc\//,         // /proc access
  /\/sys\//,          // /sys access
];

function detectSuspiciousCode(code: string): string[] {
  const alerts: string[] = [];
  
  for (const pattern of suspiciousPatterns) {
    if (pattern.test(code)) {
      alerts.push(`Suspicious pattern detected: ${pattern}`);
    }
  }
  
  return alerts;
}

// Log and alert
if (alerts.length > 0) {
  logger.warn('Suspicious code detected', {
    userId: request.userId,
    executionId,
    alerts,
  });
  
  // Could block or flag for review
}
```

---

## Security Checklist

### Application Security
- [ ] HTTPS everywhere (enforce with HSTS)
- [ ] Strong password policies (min 12 chars, complexity)
- [ ] Password hashing with bcrypt/argon2 (cost factor ≥ 12)
- [ ] JWT with short expiration (15 min access, 7 day refresh)
- [ ] CSRF protection enabled
- [ ] XSS protection (Content Security Policy)
- [ ] SQL injection protection (parameterized queries)
- [ ] Rate limiting on all endpoints
- [ ] Input validation on all inputs
- [ ] Output sanitization
- [ ] Secure session management
- [ ] HTTP security headers (Helmet.js)

### Container Security
- [ ] Non-root user in containers
- [ ] Read-only root filesystem
- [ ] No network access
- [ ] Resource limits (CPU, memory, processes)
- [ ] Seccomp profile applied
- [ ] AppArmor profile applied
- [ ] Capabilities dropped
- [ ] No new privileges flag
- [ ] Process limits enforced
- [ ] Execution timeout enforced

### Infrastructure Security
- [ ] Regular security updates
- [ ] Firewall configured
- [ ] Monitoring and alerting
- [ ] Encrypted database connections
- [ ] Encrypted Redis connections
- [ ] Secrets management (not in code)
- [ ] Regular backups
- [ ] Disaster recovery plan
- [ ] Security audit logs
- [ ] Intrusion detection system

### Code Security
- [ ] Dependency scanning (npm audit, Snyk)
- [ ] Static code analysis
- [ ] Security testing in CI/CD
- [ ] Regular penetration testing
- [ ] Code review process
- [ ] Security training for developers

---

## Incident Response

### Incident Response Plan

1. **Detection**
   - Monitor logs for suspicious activity
   - Alert on security events
   - User reports

2. **Containment**
   - Isolate affected systems
   - Block malicious users
   - Stop compromised containers

3. **Investigation**
   - Analyze logs
   - Identify attack vector
   - Assess damage

4. **Eradication**
   - Remove malicious code/users
   - Patch vulnerabilities
   - Update security measures

5. **Recovery**
   - Restore from backups
   - Verify system integrity
   - Resume normal operations

6. **Lessons Learned**
   - Document incident
   - Update security measures
   - Train team

### Emergency Contacts

- Security Team Lead: [email]
- Infrastructure Lead: [email]
- On-call Engineer: [phone]

---

## Regular Security Tasks

### Daily
- Monitor security alerts
- Review failed login attempts
- Check execution logs for anomalies

### Weekly
- Review user-reported issues
- Update dependencies
- Review access logs

### Monthly
- Security audit
- Penetration testing
- Backup verification
- Rotate secrets/keys

### Quarterly
- Full security assessment
- Compliance review
- Update security documentation
- Security training

---

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [Seccomp Documentation](https://docs.docker.com/engine/security/seccomp/)
- [AppArmor Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation)
- [CWE Top 25](https://cwe.mitre.org/top25/)

---

**Remember**: Security is an ongoing process, not a one-time task. Stay vigilant and keep systems updated!
