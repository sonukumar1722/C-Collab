# Getting Started with C-Collab

This guide will help you get started with C-Collab development.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v18 or higher) - [Download](https://nodejs.org/)
- **Docker** and **Docker Compose** - [Download](https://www.docker.com/products/docker-desktop)
- **Git** - [Download](https://git-scm.com/downloads)
- **Code Editor** - We recommend [VS Code](https://code.visualstudio.com/)

### Optional but Recommended
- **PostgreSQL** (if not using Docker) - [Download](https://www.postgresql.org/download/)
- **Redis** (if not using Docker) - [Download](https://redis.io/download)

## Quick Start (Using Docker)

The fastest way to get started is using Docker, which will set up all services automatically.

### 1. Clone the Repository

```bash
git clone https://github.com/sonukumar1722/C-Collab.git
cd C-Collab
```

### 2. Set Up Environment Variables

```bash
# Backend
cp backend/.env.example backend/.env

# Frontend
cp frontend/.env.example frontend/.env
```

Edit the `.env` files as needed. Default values should work for local development.

### 3. Start All Services

```bash
# Start all services (PostgreSQL, Redis, Backend, Frontend)
docker-compose -f infrastructure/docker/docker-compose.dev.yml up
```

This will:
- Start PostgreSQL database on port 5432
- Start Redis on port 6379
- Start Backend API on port 3000
- Start Frontend on port 5173

### 4. Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:3000
- **API Documentation**: http://localhost:3000/api-docs

## Manual Setup (Without Docker)

If you prefer to run services manually:

### 1. Install Dependencies

```bash
# Install backend dependencies
cd backend
npm install

# Install frontend dependencies
cd ../frontend
npm install
```

### 2. Set Up Database

Start PostgreSQL and create a database:

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE ccollab_dev;

# Exit
\q
```

Update `backend/.env` with your database credentials:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/ccollab_dev
```

### 3. Run Database Migrations

```bash
cd backend
npm run migrate
```

### 4. Start Redis

```bash
redis-server
```

### 5. Start Backend Server

```bash
cd backend
npm run dev
```

Backend will be available at http://localhost:3000

### 6. Start Frontend

In a new terminal:

```bash
cd frontend
npm run dev
```

Frontend will be available at http://localhost:5173

## Project Structure

```
C-Collab/
├── backend/          # Backend API (Node.js/Express)
├── frontend/         # Frontend (React/TypeScript)
├── docs/             # Documentation
├── execution-engine/ # C/C++ execution system
├── infrastructure/   # Docker and Kubernetes configs
└── scripts/          # Utility scripts
```

## Development Workflow

### Creating a New Feature

1. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes**
   - Write code
   - Add tests
   - Update documentation

3. **Test your changes**
   ```bash
   # Backend tests
   cd backend && npm test
   
   # Frontend tests
   cd frontend && npm test
   ```

4. **Lint and format**
   ```bash
   npm run lint
   npm run format
   ```

5. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: your feature description"
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**

## Available Scripts

### Backend

```bash
npm run dev          # Start development server
npm run build        # Build for production
npm start            # Start production server
npm test             # Run tests
npm run lint         # Run linter
npm run format       # Format code
npm run migrate      # Run database migrations
```

### Frontend

```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build
npm test             # Run tests
npm run lint         # Run linter
npm run format       # Format code
```

## Testing

### Running Tests

```bash
# All tests
npm test

# Watch mode
npm run test:watch

# Coverage
npm run test:coverage

# E2E tests
npm run test:e2e
```

### Writing Tests

Example test structure:

```typescript
import { describe, it, expect } from 'vitest';
import { executeCode } from './executionService';

describe('executionService', () => {
  it('should execute C code successfully', async () => {
    const code = '#include <stdio.h>\nint main() { printf("Hello"); return 0; }';
    const result = await executeCode(code, 'gcc', {});
    
    expect(result.stdout).toBe('Hello');
    expect(result.exitCode).toBe(0);
  });
});
```

## Debugging

### VS Code Debug Configuration

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Debug Backend",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "dev"],
      "cwd": "${workspaceFolder}/backend",
      "console": "integratedTerminal"
    },
    {
      "type": "chrome",
      "request": "launch",
      "name": "Debug Frontend",
      "url": "http://localhost:5173",
      "webRoot": "${workspaceFolder}/frontend/src"
    }
  ]
}
```

### Backend Debugging

```bash
cd backend
npm run dev:debug
```

Then attach your debugger to port 9229.

### Frontend Debugging

Use Chrome DevTools or React Developer Tools extension.

## Common Issues

### Port Already in Use

If ports 3000 or 5173 are already in use:

```bash
# Find process using port
lsof -i :3000

# Kill the process
kill -9 <PID>
```

Or change ports in `.env` files:

```env
# Backend .env
PORT=3001

# Frontend .env
VITE_PORT=5174
```

### Database Connection Issues

1. Check PostgreSQL is running:
   ```bash
   pg_isready
   ```

2. Verify credentials in `.env`

3. Check database exists:
   ```bash
   psql -U postgres -l
   ```

### Docker Issues

```bash
# Stop all containers
docker-compose down

# Remove volumes (WARNING: deletes data)
docker-compose down -v

# Rebuild images
docker-compose build --no-cache

# View logs
docker-compose logs -f
```

## Environment Variables

### Backend `.env`

```env
# Server
NODE_ENV=development
PORT=3000

# Database
DATABASE_URL=postgresql://developer:devpassword@localhost:5432/ccollab_dev

# Redis
REDIS_URL=redis://localhost:6379

# JWT
JWT_SECRET=your-secret-key-change-in-production
JWT_EXPIRES_IN=7d

# OAuth (optional)
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GITHUB_CLIENT_ID=
GITHUB_CLIENT_SECRET=

# Execution
MAX_EXECUTION_TIME=30000
MAX_MEMORY_MB=512
```

### Frontend `.env`

```env
# API URL
VITE_API_URL=http://localhost:3000

# WebSocket URL
VITE_WS_URL=ws://localhost:3000
```

## Next Steps

1. **Read the [Architecture Documentation](docs/phase1-setup.md)**
2. **Check out [Contributing Guidelines](CONTRIBUTING.md)**
3. **Review [Project Plan](PROJECT_PLAN.md)**
4. **Join our community** (Discord/Slack link)
5. **Start coding!**

## Need Help?

- **Documentation**: Check the `docs/` folder
- **Issues**: [GitHub Issues](https://github.com/sonukumar1722/C-Collab/issues)
- **Discussions**: [GitHub Discussions](https://github.com/sonukumar1722/C-Collab/discussions)

Happy coding! 🚀
