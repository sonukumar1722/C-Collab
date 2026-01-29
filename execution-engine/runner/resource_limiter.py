class ResourceLimiter:
    """Manage resource limits for code execution"""
    
    def __init__(self):
        self.default_cpu_quota = 50000  # 50% of CPU
        self.default_memory_limit = "512m"
        self.default_timeout = 30
    
    def get_limits(self, custom_limits: dict = None) -> dict:
        """Get resource limits with defaults"""
        limits = {
            "cpu_quota": self.default_cpu_quota,
            "memory_limit": self.default_memory_limit,
            "timeout": self.default_timeout
        }
        
        if custom_limits:
            limits.update(custom_limits)
        
        return limits
    
    def validate_limits(self, limits: dict) -> bool:
        """Validate resource limits"""
        if limits.get("timeout", 0) > 60:
            return False
        if limits.get("cpu_quota", 0) > 100000:
            return False
        return True
