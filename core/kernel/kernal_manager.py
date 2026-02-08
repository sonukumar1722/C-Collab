# core/kernel/kernel_manager.py

from core.kernel.cpp_kernel import CppKernel
from core.utils.timeout import run_with_timeout, ExecutionTimeout

class KernelManager:

    def __init__(self):
        self.kernel = CppKernel()
        self.kernel.start()

    def execute(self, code: str, timeout=3):
        try:
            return run_with_timeout(
                lambda: self.kernel.execute(code),
                timeout
            )

        except ExecutionTimeout:
            # Attempt soft interrupt
            self.kernel.interrupt()

            return {
                "stdout": "",
                "stderr": "Execution timed out",
                "status": "timeout"
            }

        except Exception as e:
            return {
                "stdout": "",
                "stderr": str(e),
                "status": "error"
            }

    def restart_kernel(self):
        self.kernel.shutdown()
        self.kernel = CppKernel()
        self.kernel.start()
