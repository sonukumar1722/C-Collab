# core/kernel/base_kernel.py

from abc import ABC, abstractmethod

class BaseKernel(ABC):

    """Abstract interface for language execution kernels."""

    @abstractmethod
    def start(self):
        """Initialize and start the kernel process or session."""
        pass

    @abstractmethod
    def execute(self, code: str) -> dict:
        """Execute code and return stdout/stderr/status output.
        Returns:
        {
          stdout: str,
          stderr: str,
          status: "ok" | "error"
        }
        """

    @abstractmethod
    def interrupt(self):
        """Interrupt the currently running execution, if any."""
        pass

    @abstractmethod
    def shutdown(self):
        """Gracefully shut down the kernel and release resources."""
        pass
