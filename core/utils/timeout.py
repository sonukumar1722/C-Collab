# core/utils/timeout.py

import threading

class ExecutionTimeout(Exception):
    pass

def run_with_timeout(func, timeout_sec):
    result = {}
    error = {}

    def target():
        try:
            result["value"] = func()
        except Exception as e:
            error["exception"] = e

    thread = threading.Thread(target=target)
    thread.start()
    thread.join(timeout_sec)

    if thread.is_alive():
        raise ExecutionTimeout("Execution timed out")

    if "exception" in error:
        raise error["exception"]

    return result.get("value")
