import subprocess
import tempfile
import os

class CppCompiler:
    """Compiler for C++ code"""
    
    def __init__(self, compiler: str = "g++"):
        self.compiler = compiler
        self.flags = ["-Wall", "-Wextra", "-std=c++17"]
    
    def compile(self, code: str) -> tuple[bool, str]:
        """Compile C++ code and return success status and message"""
        with tempfile.TemporaryDirectory() as temp_dir:
            source_file = os.path.join(temp_dir, "source.cpp")
            output_file = os.path.join(temp_dir, "program")
            
            # Write code to temporary file
            with open(source_file, 'w') as f:
                f.write(code)
            
            # Compile
            try:
                cmd = [self.compiler] + self.flags + [source_file, "-o", output_file]
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0:
                    return True, "Compilation successful"
                else:
                    return False, result.stderr
            except subprocess.TimeoutExpired:
                return False, "Compilation timeout"
            except Exception as e:
                return False, f"Compilation error: {str(e)}"
