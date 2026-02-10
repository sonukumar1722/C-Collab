# Quick Reference Guide

Quick links and commands for C-Collab development.

## 📚 Documentation Quick Links

- **[Project Plan](../PROJECT_PLAN.md)** - Complete 8-phase implementation plan
- **[Project Structure](../STRUCTURE.md)** - Directory structure and organization
- **[Technology Stack](TECHNOLOGY_STACK.md)** - Tech choices and comparisons
- **[Getting Started](../GETTING_STARTED.md)** - Setup and development guide
- **[Contributing](../CONTRIBUTING.md)** - Contribution guidelines
- **[Phase 1: Setup](phase1-setup.md)** - Current phase documentation
- **[Security](SECURITY.md)** - Security considerations and best practices

## 🚀 Quick Start Commands

### Initial Setup
```bash
# Clone repository
git clone https://github.com/sonukumar1722/C-Collab.git
cd C-Collab

# Quick start with Docker
docker-compose -f infrastructure/docker/docker-compose.dev.yml up
```

### Development (Manual Setup)
```bash
# Backend
cd backend
npm install
npm run dev

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

### Testing
```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# E2E tests
npm run test:e2e
```

### Code Quality
```bash
# Lint
npm run lint

# Format
npm run format

# Type check
npm run type-check
```

## 📦 Project Phases

| Phase | Duration | Focus |
|-------|----------|-------|
| **Phase 1** | Week 1-2 | Project Setup & Architecture |
| **Phase 2** | Week 3-5 | Backend Infrastructure |
| **Phase 3** | Week 6-8 | C/C++ Execution Engine |
| **Phase 4** | Week 9-12 | Frontend Development |
| **Phase 5** | Week 13-15 | Advanced Features |
| **Phase 6** | Week 16-17 | Testing & QA |
| **Phase 7** | Week 18-19 | Deployment |
| **Phase 8** | Week 20+ | Maintenance & Growth |

## 🛠️ Tech Stack at a Glance

```
Frontend:  React + TypeScript + Vite + MUI + Monaco
Backend:   Node.js + Express + TypeScript + Prisma
Database:  PostgreSQL + Redis
Execution: Docker + GCC/Clang + Seccomp + AppArmor
DevOps:    GitHub Actions + Kubernetes + Prometheus
```

## 🔐 Security Checklist

Critical security measures:
- [ ] Docker isolation with non-root user
- [ ] Seccomp profile applied
- [ ] AppArmor profile applied
- [ ] Resource limits (CPU, memory, processes)
- [ ] Network isolation (--network=none)
- [ ] Read-only filesystem
- [ ] Execution timeout (30s)
- [ ] Rate limiting on API
- [ ] Input validation and sanitization
- [ ] HTTPS everywhere
- [ ] JWT authentication
- [ ] CSRF protection

## 📊 Key Metrics

### Performance Targets
- Execution time: < 5 seconds for basic programs
- Page load time: < 2 seconds
- API response: < 200ms (95th percentile)
- Uptime: 99.9%

### Resource Limits
- **CPU**: 0.5 cores per execution
- **Memory**: 256MB per execution
- **Timeout**: 30 seconds
- **Processes**: Max 50
- **Code size**: Max 50KB

## 🌐 URLs (Development)

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:3000
- **API Docs**: http://localhost:3000/api-docs
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

## 📝 Common Commands

### Docker
```bash
# Start services
docker-compose up

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild
docker-compose build --no-cache
```

### Database
```bash
# Run migrations
npm run migrate

# Seed data
npm run seed

# Reset database
npm run db:reset
```

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/your-feature

# Commit with conventional commits
git commit -m "feat: add new feature"

# Push and create PR
git push origin feature/your-feature
```

## 🎯 Commit Message Format

```
<type>(<scope>): <subject>

Types: feat, fix, docs, style, refactor, perf, test, chore
Scope: Optional (notebook, auth, execution, etc.)

Examples:
feat(notebook): add markdown cell support
fix(execution): handle timeout errors correctly
docs: update API documentation
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find process
lsof -i :3000

# Kill process
kill -9 <PID>
```

### Docker Issues
```bash
# Remove all containers and volumes
docker-compose down -v

# Prune system
docker system prune -a
```

### Database Connection Issues
```bash
# Check PostgreSQL status
pg_isready

# Reset database
npm run db:reset
```

## 📞 Getting Help

1. Check [Documentation](../README.md#documentation)
2. Search [GitHub Issues](https://github.com/sonukumar1722/C-Collab/issues)
3. Ask in [Discussions](https://github.com/sonukumar1722/C-Collab/discussions)
4. Contact maintainers

## 🎓 Learning Resources

### React + TypeScript
- [React Docs](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)

### Node.js + Express
- [Node.js Docs](https://nodejs.org/docs/)
- [Express Guide](https://expressjs.com/en/guide/routing.html)
- [Prisma Docs](https://www.prisma.io/docs/)

### Docker
- [Docker Docs](https://docs.docker.com/)
- [Docker Security](https://docs.docker.com/engine/security/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

### C/C++
- [GCC Manual](https://gcc.gnu.org/onlinedocs/)
- [Clang Documentation](https://clang.llvm.org/docs/)
- [C++ Reference](https://en.cppreference.com/)

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────┐
│           User Browser                  │
│  (React + Monaco Editor + WebSocket)    │
└────────────────┬────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────┐
│        Load Balancer / CDN              │
└────────────────┬────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────┐
│       Backend API Server                │
│   (Node.js + Express + WebSocket)       │
└────────────┬────────────────┬───────────┘
             │                │
             ↓                ↓
    ┌────────────┐    ┌──────────────┐
    │ PostgreSQL │    │    Redis     │
    │  Database  │    │ Cache+Queue  │
    └────────────┘    └──────┬───────┘
                             │
                             ↓
                   ┌──────────────────┐
                   │  Worker Process  │
                   │  (Bull Queue)    │
                   └─────────┬────────┘
                             │
                             ↓
                   ┌──────────────────┐
                   │ Docker Container │
                   │   (Isolated)     │
                   │  - GCC/Clang     │
                   │  - Seccomp       │
                   │  - AppArmor      │
                   └──────────────────┘
```

## 📋 Development Checklist

### Before Starting Development
- [ ] Read [Getting Started](../GETTING_STARTED.md)
- [ ] Read [Contributing Guidelines](../CONTRIBUTING.md)
- [ ] Set up development environment
- [ ] Run project successfully locally
- [ ] Read relevant phase documentation

### Before Committing
- [ ] Code follows style guidelines
- [ ] Tests added for new features
- [ ] All tests pass
- [ ] Code is linted and formatted
- [ ] Documentation updated
- [ ] No console.log statements
- [ ] No commented-out code

### Before Creating PR
- [ ] Branch up to date with develop
- [ ] Meaningful commit messages
- [ ] PR description filled
- [ ] Tests pass in CI
- [ ] No merge conflicts
- [ ] Documentation reviewed

## 🎉 Quick Wins for Contributors

Easy first contributions:
1. Fix typos in documentation
2. Add code comments
3. Improve error messages
4. Add unit tests
5. Update dependencies
6. Add examples to docs
7. Improve UI/UX

Medium difficulty:
1. Add new compiler version
2. Implement code snippets
3. Add keyboard shortcuts
4. Improve error handling
5. Add new API endpoints

Advanced:
1. Implement collaborative editing
2. Add performance optimizations
3. Implement new security features
4. Add mobile support
5. Implement caching strategies

---

**Happy coding! 🚀**

For detailed information, always refer to the main documentation files.
