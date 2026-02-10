# Example Notebooks for C-Collab

This directory contains example notebooks to help users get started with C-Collab.

## Categories

### 1. **Getting Started**
- `hello-world.json` - Basic Hello World program
- `input-output.json` - Taking input and producing output
- `compilation-options.json` - Using different compiler flags

### 2. **Data Structures**
- `arrays.json` - Array operations
- `linked-lists.json` - Linked list implementation
- `stacks-queues.json` - Stack and queue implementations
- `trees.json` - Binary tree operations
- `graphs.json` - Graph algorithms

### 3. **Algorithms**
- `sorting.json` - Various sorting algorithms
- `searching.json` - Binary search, linear search
- `dynamic-programming.json` - DP problems
- `greedy.json` - Greedy algorithms
- `recursion.json` - Recursive solutions

### 4. **C++ Features**
- `cpp11-features.json` - C++11 features demo
- `cpp17-features.json` - C++17 features demo
- `cpp20-features.json` - C++20 features demo
- `stl-containers.json` - STL containers
- `stl-algorithms.json` - STL algorithms
- `templates.json` - Template programming
- `oop.json` - Object-oriented programming

### 5. **System Programming**
- `file-io.json` - File input/output
- `memory-management.json` - Dynamic memory
- `pointers.json` - Pointer operations

### 6. **Tutorials**
- `beginner-tutorial.json` - Tutorial for beginners
- `intermediate-tutorial.json` - Intermediate concepts
- `advanced-tutorial.json` - Advanced topics

## Notebook Format

Example notebook structure:

```json
{
  "title": "Hello World Example",
  "description": "A simple Hello World program in C++",
  "language": "cpp",
  "compiler": "gcc-12",
  "compilerFlags": "-std=c++17 -Wall",
  "cells": [
    {
      "type": "markdown",
      "content": "# Hello World\n\nThis is a simple C++ program that prints 'Hello, World!' to the console."
    },
    {
      "type": "code",
      "content": "#include <iostream>\n\nint main() {\n    std::cout << \"Hello, World!\" << std::endl;\n    return 0;\n}"
    },
    {
      "type": "markdown",
      "content": "## Explanation\n\nThe program includes the iostream library and uses std::cout to print text."
    }
  ],
  "tags": ["beginner", "tutorial", "hello-world"],
  "isPublic": true
}
```

## How to Use Examples

1. **Import**: Use the import feature to load these examples
2. **Modify**: Feel free to modify and experiment
3. **Share**: Fork and share your modifications

## Contributing Examples

To contribute a new example notebook:

1. Create a well-documented notebook
2. Test it thoroughly
3. Export as JSON
4. Submit a PR with the notebook in the appropriate category
5. Update this README with the new example

## Guidelines for Example Notebooks

- **Clear documentation**: Use markdown cells to explain concepts
- **Working code**: Ensure all code cells execute successfully
- **Comments**: Add comments in code for clarity
- **Progressive complexity**: Start simple, add complexity gradually
- **Good practices**: Demonstrate best practices
- **Multiple examples**: Show different approaches when applicable

## License

All example notebooks are released under the MIT License, same as the main project.
