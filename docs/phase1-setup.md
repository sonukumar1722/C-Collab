# Phase 1: Project Setup and Architecture

**Duration**: Week 1-2  
**Status**: 🟡 Pending

## Objectives
- Set up development environment
- Design system architecture
- Create project documentation
- Initialize repositories and tools

## Prerequisites
- Node.js (v18+ or v20+)
- Docker and Docker Compose
- PostgreSQL
- Redis
- Git
- Code editor (VS Code recommended)

---

## Task Breakdown

### 1.1 Repository Setup (Day 1)

#### Tasks
- [x] Initialize Git repository
- [ ] Create comprehensive .gitignore
- [ ] Set up branch protection rules
- [ ] Create CONTRIBUTING.md
- [ ] Create CODE_OF_CONDUCT.md
- [ ] Add LICENSE file (MIT/Apache 2.0)
- [ ] Set up Git hooks (pre-commit, pre-push)

#### Commands
```bash
# Initialize repository
git init
git checkout -b main

# Set up Git hooks with Husky
npm install -D husky
npx husky install
npx husky add .husky/pre-commit "npm run lint"
npx husky add .husky/pre-push "npm test"
```

#### Deliverables
- ✅ Git repository with proper configuration
- ✅ Documentation templates

---

### 1.2 Architecture Design (Day 2-4)

#### Tasks
- [ ] Design system architecture (High-level and detailed)
- [ ] Create component diagrams
- [ ] Design data flow diagrams
- [ ] Define microservices boundaries (if applicable)
- [ ] Create sequence diagrams for key operations

#### Architecture Components

**1. Frontend (React + TypeScript)**
```
User Browser
    ↓
┌─────────────────────────┐
│   React Application     │
│  - Monaco Editor        │
│  - WebSocket Client     │
│  - State Management     │
└─────────────────────────┘
    ↓
API Gateway / Load Balancer
```

**2. Backend (Node.js + Express)**
```
┌─────────────────────────┐
│    API Server           │
│  - REST API             │
│  - WebSocket Server     │
│  - Authentication       │
└─────────────────────────┘
    ↓
┌─────────────────────────┐
│  PostgreSQL Database    │
│  - Users                │
│  - Notebooks            │
│  - Cells                │
└─────────────────────────┘
```

**3. Execution Engine**
```
┌─────────────────────────┐
│   Redis Job Queue       │
│  - Bull Queue           │
└─────────────────────────┘
    ↓
┌─────────────────────────┐
│   Worker Processes      │
│  - Code Compilation     │
│  - Code Execution       │
└─────────────────────────┘
    ↓
┌─────────────────────────┐
│   Docker Containers     │
│  - GCC/Clang            │
│  - Sandboxed Execution  │
└─────────────────────────┘
```

#### Security Architecture
```
┌─────────────────────────────────┐
│     Security Layers             │
├─────────────────────────────────┤
│ 1. Authentication (JWT)         │
│ 2. Authorization (RBAC)         │
│ 3. Rate Limiting                │
│ 4. Input Validation             │
│ 5. Docker Isolation             │
│ 6. Seccomp Profiles             │
│ 7. Resource Limits (cgroups)    │
│ 8. Network Isolation            │
└─────────────────────────────────┘
```

#### Deliverables
- System architecture diagram
- Component interaction diagrams
- Security architecture document
- Scalability plan

---

### 1.3 Database Schema Design (Day 5-6)

#### Database Tables

**Users Table**
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    avatar_url VARCHAR(500),
    is_email_verified BOOLEAN DEFAULT FALSE,
    oauth_provider VARCHAR(50),
    oauth_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login_at TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
```

**Notebooks Table**
```sql
CREATE TABLE notebooks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    is_public BOOLEAN DEFAULT FALSE,
    tags TEXT[], -- Array of tags
    language VARCHAR(10) DEFAULT 'cpp', -- 'c' or 'cpp'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_accessed_at TIMESTAMP
);

CREATE INDEX idx_notebooks_user_id ON notebooks(user_id);
CREATE INDEX idx_notebooks_created_at ON notebooks(created_at);
CREATE INDEX idx_notebooks_is_public ON notebooks(is_public);
```

**Cells Table**
```sql
CREATE TABLE cells (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    notebook_id UUID REFERENCES notebooks(id) ON DELETE CASCADE,
    cell_type VARCHAR(20) NOT NULL, -- 'code' or 'markdown'
    content TEXT NOT NULL,
    position INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_cells_notebook_id ON cells(notebook_id);
CREATE INDEX idx_cells_position ON cells(notebook_id, position);
```

**Executions Table**
```sql
CREATE TABLE executions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cell_id UUID REFERENCES cells(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    compiler VARCHAR(50) NOT NULL, -- 'gcc-11', 'gcc-12', 'clang-15', etc.
    compiler_flags TEXT,
    status VARCHAR(20) NOT NULL, -- 'pending', 'running', 'success', 'error', 'timeout'
    stdout TEXT,
    stderr TEXT,
    exit_code INTEGER,
    execution_time_ms INTEGER,
    memory_used_kb INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);

CREATE INDEX idx_executions_cell_id ON executions(cell_id);
CREATE INDEX idx_executions_user_id ON executions(user_id);
CREATE INDEX idx_executions_status ON executions(status);
```

**Shares Table** (for sharing notebooks)
```sql
CREATE TABLE notebook_shares (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    notebook_id UUID REFERENCES notebooks(id) ON DELETE CASCADE,
    share_token VARCHAR(100) UNIQUE NOT NULL,
    is_public BOOLEAN DEFAULT TRUE,
    access_level VARCHAR(20) DEFAULT 'read', -- 'read' or 'write'
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_shares_notebook_id ON notebook_shares(notebook_id);
CREATE INDEX idx_shares_token ON notebook_shares(share_token);
```

#### Deliverables
- Complete database schema
- ER diagram
- Migration scripts
- Seed data scripts

---

### 1.4 API Design (Day 7-8)

#### API Endpoints Specification

**Authentication Endpoints**
```
POST   /api/auth/register          - Register new user
POST   /api/auth/login             - Login user
POST   /api/auth/logout            - Logout user
POST   /api/auth/refresh-token     - Refresh JWT token
POST   /api/auth/forgot-password   - Request password reset
POST   /api/auth/reset-password    - Reset password
GET    /api/auth/oauth/:provider   - OAuth login (Google, GitHub)
GET    /api/auth/me                - Get current user info
```

**Notebook Endpoints**
```
GET    /api/notebooks              - List user's notebooks
POST   /api/notebooks              - Create new notebook
GET    /api/notebooks/:id          - Get notebook details
PUT    /api/notebooks/:id          - Update notebook
DELETE /api/notebooks/:id          - Delete notebook
POST   /api/notebooks/:id/fork     - Fork a notebook
GET    /api/notebooks/:id/export   - Export notebook (PDF/HTML)
```

**Cell Endpoints**
```
GET    /api/notebooks/:id/cells       - Get all cells
POST   /api/notebooks/:id/cells       - Create new cell
PUT    /api/cells/:id                 - Update cell content
DELETE /api/cells/:id                 - Delete cell
PUT    /api/cells/:id/position        - Update cell position
```

**Execution Endpoints**
```
POST   /api/execute                - Execute code
GET    /api/execute/:id            - Get execution status
GET    /api/execute/:id/output     - Get execution output
DELETE /api/execute/:id            - Cancel execution
GET    /api/cells/:id/executions   - Get execution history
```

**Sharing Endpoints**
```
POST   /api/notebooks/:id/share    - Create share link
GET    /api/share/:token           - Access shared notebook
DELETE /api/share/:id              - Delete share link
```

#### API Response Format
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation successful",
  "timestamp": "2026-01-29T12:00:00Z"
}
```

#### Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": { ... }
  },
  "timestamp": "2026-01-29T12:00:00Z"
}
```

#### Deliverables
- OpenAPI/Swagger specification
- API documentation
- Postman collection

---

### 1.5 Development Environment Setup (Day 9-10)

#### Docker Development Environment

**docker-compose.dev.yml**
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: ccollab_dev
      POSTGRES_USER: developer
      POSTGRES_PASSWORD: devpassword
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    volumes:
      - ./backend:/app
      - /app/node_modules
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://developer:devpassword@postgres:5432/ccollab_dev
      REDIS_URL: redis://redis:6379
    depends_on:
      - postgres
      - redis

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
    volumes:
      - ./frontend:/app
      - /app/node_modules
    ports:
      - "5173:5173"
    environment:
      VITE_API_URL: http://localhost:3000

volumes:
  postgres_data:
```

#### Setup Scripts

**setup-dev.sh**
```bash
#!/bin/bash

echo "Setting up C-Collab development environment..."

# Check prerequisites
command -v node >/dev/null 2>&1 || { echo "Node.js is required but not installed."; exit 1; }
command -v docker >/dev/null 2>&1 || { echo "Docker is required but not installed."; exit 1; }

# Install backend dependencies
echo "Installing backend dependencies..."
cd backend && npm install && cd ..

# Install frontend dependencies
echo "Installing frontend dependencies..."
cd frontend && npm install && cd ..

# Set up environment files
echo "Setting up environment files..."
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Start Docker services
echo "Starting Docker services..."
docker-compose -f infrastructure/docker/docker-compose.dev.yml up -d

# Run database migrations
echo "Running database migrations..."
cd backend && npm run migrate && cd ..

echo "Setup complete! Run 'npm run dev' in backend and frontend directories to start development."
```

#### Deliverables
- Docker development environment
- Setup automation scripts
- Development documentation
- VS Code workspace configuration

---

## Phase 1 Checklist

- [ ] Repository initialized with proper structure
- [ ] Git hooks configured
- [ ] Architecture documentation complete
- [ ] Database schema designed and documented
- [ ] API specification created
- [ ] Development environment configured
- [ ] All team members can run the project locally

## Next Phase
After completing Phase 1, proceed to [Phase 2: Backend Infrastructure](./phase2-backend.md)
