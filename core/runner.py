# core/runner.py

from core.session.notebook_session import NotebookSession

session = NotebookSession()

# Cell 1
print(session.run_cell("int x = 10;"))

# Cell 2
print(session.run_cell("x += 5;"))

# Cell 3
print(session.run_cell("std::cout << x << std::endl;"))
