# core/session/notebook_session.py

from core.kernel.cpp_kernel import CppKernel

class NotebookSession:

    def __init__(self):
        self.kernel = CppKernel()
        self.kernel.start()
        self.execution_count = 0

    def run_cell(self, code: str):
        self.execution_count += 1
        result = self.kernel.execute(code)
        result["execution_count"] = self.execution_count
        return result

    def reset(self):
        self.kernel.shutdown()
        self.kernel = CppKernel()
        self.kernel.start()
        self.execution_count = 0
