# Contributing to C-Collab

First off, thank you for considering contributing to C-Collab! It's people like you that make C-Collab such a great tool.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [How to Contribute](#how-to-contribute)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Docker and Docker Compose
- PostgreSQL (or use Docker)
- Redis (or use Docker)
- Git

### Setting Up Your Development Environment

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/C-Collab.git
   cd C-Collab
   ```

3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/sonukumar1722/C-Collab.git
   ```

4. Set up the development environment:
   ```bash
   ./scripts/setup-dev.sh
   ```

5. Start the development servers:
   ```bash
   # In one terminal - Backend
   cd backend && npm run dev

   # In another terminal - Frontend
   cd frontend && npm run dev
   ```

## Development Process

### Branching Strategy

We follow a simplified Git Flow:

- `main` - Production-ready code
- `develop` - Main development branch
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgent production fixes

### Workflow

1. Create a new branch from `develop`:
   ```bash
   git checkout develop
   git pull upstream develop
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them (see [Commit Messages](#commit-messages))

3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request against the `develop` branch

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected behavior**
- **Actual behavior**
- **Screenshots** (if applicable)
- **Environment details** (OS, browser, Node version, etc.)

Use the bug report template when creating a new issue.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case** - Why this enhancement would be useful
- **Detailed description** of the proposed functionality
- **Mockups or examples** (if applicable)

### Pull Requests

1. **Small, focused changes**: Each PR should address a single concern
2. **Tests**: Add tests for new features or bug fixes
3. **Documentation**: Update documentation for user-facing changes
4. **Code quality**: Follow the style guidelines
5. **Clean commit history**: Squash commits if necessary

## Style Guidelines

### TypeScript/JavaScript

We use ESLint and Prettier for code formatting. Configuration files are included in the repository.

```bash
# Run linter
npm run lint

# Auto-fix linting issues
npm run lint:fix

# Format code
npm run format
```

#### Code Style

- Use **TypeScript** for type safety
- Use **functional components** with hooks in React
- Use **async/await** instead of callbacks
- Prefer **const** over let, avoid var
- Use **descriptive variable names**
- Add **JSDoc comments** for complex functions

Example:
```typescript
/**
 * Executes C/C++ code in a sandboxed environment
 * @param code - The source code to execute
 * @param compiler - Compiler to use (gcc or clang)
 * @param options - Compilation options
 * @returns Promise with execution result
 */
async function executeCode(
  code: string,
  compiler: CompilerType,
  options: CompilationOptions
): Promise<ExecutionResult> {
  // Implementation
}
```

### File Naming

- **Components**: PascalCase (e.g., `NotebookEditor.tsx`)
- **Utilities**: camelCase (e.g., `executionService.ts`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_EXECUTION_TIME`)
- **Interfaces/Types**: PascalCase with 'I' prefix for interfaces (e.g., `IUser`, `ExecutionResult`)

### CSS/Styling

- Use **CSS Modules** or **styled-components**
- Follow **BEM naming convention** if using plain CSS
- Use **semantic class names**

## Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that don't affect code meaning (formatting, etc.)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Performance improvement
- **test**: Adding or updating tests
- **chore**: Changes to build process or auxiliary tools

### Examples

```
feat(notebook): add markdown cell support

Add support for markdown cells in notebooks. Users can now
create and edit markdown cells alongside code cells.

Closes #123
```

```
fix(execution): handle timeout errors correctly

Previously, timeout errors were not being caught properly,
causing the execution to hang. This fix ensures timeouts
are handled and reported to the user.

Fixes #456
```

## Pull Request Process

1. **Update documentation** for any user-facing changes
2. **Add tests** for new features or bug fixes
3. **Ensure all tests pass**: `npm test`
4. **Ensure code is formatted**: `npm run lint && npm run format`
5. **Update the README.md** with details of changes if needed
6. **Reference related issues** in the PR description
7. **Request review** from maintainers
8. **Address review comments** promptly

### PR Title Format

Use the same format as commit messages:

```
feat(component): brief description
```

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing tests pass locally

## Screenshots (if applicable)

## Related Issues
Closes #123
```

## Testing

### Running Tests

```bash
# Backend tests
cd backend && npm test

# Frontend tests
cd frontend && npm test

# E2E tests
npm run test:e2e

# Coverage
npm run test:coverage
```

### Writing Tests

- Write **unit tests** for individual functions and components
- Write **integration tests** for API endpoints
- Write **E2E tests** for critical user flows
- Aim for **>80% code coverage**

## Questions?

Feel free to:
- Open an issue with your question
- Join our community discussions
- Contact the maintainers

Thank you for contributing to C-Collab! 🎉
