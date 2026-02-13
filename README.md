# C-Collab

An online notebook for C and C++, similar to Google Colab running Jupyter Notebook online.

## Overview

C-Collab is a web-based interactive development environment for C and C++ programming. It provides a notebook-style interface where you can write, compile, and execute C/C++ code in isolated sandboxed environments.

## Features

- 📝 Interactive notebook interface for C/C++ development
- 🔒 Secure sandboxed code execution
- 🚀 Real-time code compilation and execution
- 💾 Notebook persistence and management
- 🔐 User authentication and authorization
- 🐳 Docker-based execution engine

## Project Structure

```
c-collab/
├── docs/                     # Documentation & diagrams
├── frontend/                 # React-based Web Notebook UI
├── backend/                  # FastAPI backend (API + Auth + Notebook manager)
├── execution-engine/         # Code execution & sandboxing service
├── kernels/                  # Language kernels (C, C++)
├── storage/                  # Local storage abstraction
├── scripts/                  # Development & deployment scripts
└── tests/                    # Integration & E2E tests
```

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js 16+ (for frontend development)
- Python 3.11+ (for backend development)

### Running with Docker Compose

```bash
# Start all services
./scripts/start-dev.sh

# Stop all services
./scripts/stop.sh

# Clean up everything
./scripts/clean.sh
```

### Services

Once started, the following services will be available:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Execution Engine**: http://localhost:8001

### Manual Setup

#### Backend

```bash
cd backend
pip install -r requirements.txt
python -m app.db.init_db  # Initialize database
uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
npm start
```

#### Execution Engine

```bash
cd execution-engine
pip install -r requirements.txt
uvicorn api:app --port 8001 --reload
```

## Architecture

### Components

1. **Frontend**: React-based notebook interface with Monaco Editor
2. **Backend**: FastAPI server handling authentication, notebook management, and API routing
3. **Execution Engine**: Isolated code execution service using Docker containers
4. **Kernels**: Language-specific compilers and runtime managers for C and C++
5. **Storage**: Local filesystem-based storage for notebooks and uploads

### Security

- Code execution in isolated Docker containers
- Seccomp profiles for system call filtering
- Resource limits (CPU, memory, execution time)
- Network isolation for untrusted code
- Input sanitization and validation

## API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

### Environment Variables

Copy `.env` file and update the values:

```bash
cp .env .env.local
# Edit .env.local with your configuration
```

### Database Initialization

```bash
./scripts/init-db.sh
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Roadmap

- [ ] Add support for C++20/23 features
- [ ] Implement collaborative editing
- [ ] Add visualization tools for data structures
- [ ] Support for external libraries
- [ ] Enhanced debugging capabilities
- [ ] Cloud storage integration
- [ ] Export notebooks to various formats
