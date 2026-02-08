# core/kernel/cpp_kernel.py

import subprocess
import signal
from core.kernel.base_kernel import BaseKernel

class CppKernel(BaseKernel):

    """Kernel wrapper for running C/C++ code via Cling."""

    def __init__(self):
        # Track the Cling subprocess instance.
        self.process = None

    def start(self):
        # Start the Cling REPL process.
        self.process = subprocess.Popen(
            ["cling", "--nologo"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        # Consume the initial prompt so reads are clean.
        self._drain_prompt()

    def execute(self, code: str) -> dict:
        # Send code to Cling and flush to ensure execution.
        self.process.stdin.write(code + "\n")
        self.process.stdin.flush()

        # Read output until the next prompt is seen.
        stdout, stderr = self._read_until_prompt()

        return {
            "stdout": stdout,
            "stderr": stderr,
            "status": "ok" if not stderr else "error"
        }

    def interrupt(self):
        # Forward SIGINT to stop current execution.
        if self.process and self.process.poll() is None:
            self.process.send_signal(signal.SIGINT)

    def shutdown(self):
        # Terminate the Cling process.
        self.process.terminate()

    # ---- internal helpers ----

    def _wait_for_prompt(self):
        while True:
            if "cling>" in self.process.stdout.readline():
                break   

    def _drain_prompt(self):
        """Read until the initial Cling prompt appears."""
        while "cling>" not in self.process.stdout.readline():
            pass

    def _read_until_prompt(self):
        """Collect stdout/stderr output until the prompt is encountered."""
        out, err = [], []

        while True:
            line = self.process.stdout.readline()
            if "cling>" in line:
                break
            out.append(line)

        while self.process.stderr.peek():
            err.append(self.process.stderr.readline())

        return "".join(out), "".join(err)
