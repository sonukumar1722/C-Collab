# C-Collab Project Structure

## Overview
This document describes the recommended directory structure for the C-Collab project.

## Root Directory Structure

```
C-Collab/
├── .github/
│   ├── workflows/              # GitHub Actions CI/CD
│   │   ├── backend-tests.yml
│   │   ├── frontend-tests.yml
│   │   ├── security-scan.yml
│   │   └── deploy.yml
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── architecture/           # Architecture diagrams and docs
│   │   ├── system-design.md
│   │   ├── database-schema.md
│   │   └── api-design.md
│   ├── api/                    # API documentation
│   │   └── openapi.yaml
│   ├── deployment/             # Deployment guides
│   │   ├── docker.md
│   │   ├── kubernetes.md
│   │   └── cloud-deployment.md
│   └── user-guide/             # User documentation
│       ├── getting-started.md
│       ├── features.md
│       └── tutorials/
├── backend/
│   ├── src/
│   │   ├── api/                # API routes
│   │   │   ├── auth/
│   │   │   ├── notebooks/
│   │   │   ├── execution/
│   │   │   └── users/
│   │   ├── models/             # Database models
│   │   │   ├── User.ts
│   │   │   ├── Notebook.ts
│   │   │   ├── Cell.ts
│   │   │   └── Execution.ts
│   │   ├── services/           # Business logic
│   │   │   ├── authService.ts
│   │   │   ├── notebookService.ts
│   │   │   ├── executionService.ts
│   │   │   └── compilerService.ts
│   │   ├── middleware/         # Express middleware
│   │   │   ├── auth.ts
│   │   │   ├── validation.ts
│   │   │   ├── errorHandler.ts
│   │   │   └── rateLimiter.ts
│   │   ├── utils/              # Utility functions
│   │   │   ├── logger.ts
│   │   │   ├── constants.ts
│   │   │   └── helpers.ts
│   │   ├── config/             # Configuration
│   │   │   ├── database.ts
│   │   │   ├── redis.ts
│   │   │   └── env.ts
│   │   ├── workers/            # Background job workers
│   │   │   ├── executionWorker.ts
│   │   │   └── compilationWorker.ts
│   │   ├── websocket/          # WebSocket handlers
│   │   │   └── executionSocket.ts
│   │   └── index.ts            # Entry point
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── e2e/
│   ├── prisma/                 # Prisma ORM (if using)
│   │   ├── schema.prisma
│   │   └── migrations/
│   ├── package.json
│   ├── tsconfig.json
│   ├── .env.example
│   └── Dockerfile
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── assets/
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── common/
│   │   │   │   ├── Button/
│   │   │   │   ├── Input/
│   │   │   │   └── Modal/
│   │   │   ├── auth/
│   │   │   │   ├── Login.tsx
│   │   │   │   ├── Register.tsx
│   │   │   │   └── Profile.tsx
│   │   │   ├── notebook/
│   │   │   │   ├── NotebookEditor.tsx
│   │   │   │   ├── CodeCell.tsx
│   │   │   │   ├── MarkdownCell.tsx
│   │   │   │   ├── OutputPanel.tsx
│   │   │   │   └── CellToolbar.tsx
│   │   │   ├── dashboard/
│   │   │   │   ├── Dashboard.tsx
│   │   │   │   ├── NotebookList.tsx
│   │   │   │   └── NotebookCard.tsx
│   │   │   └── layout/
│   │   │       ├── Header.tsx
│   │   │       ├── Sidebar.tsx
│   │   │       └── Footer.tsx
│   │   ├── pages/              # Page components
│   │   │   ├── HomePage.tsx
│   │   │   ├── DashboardPage.tsx
│   │   │   ├── NotebookPage.tsx
│   │   │   └── SettingsPage.tsx
│   │   ├── hooks/              # Custom React hooks
│   │   │   ├── useAuth.ts
│   │   │   ├── useNotebook.ts
│   │   │   ├── useWebSocket.ts
│   │   │   └── useExecution.ts
│   │   ├── store/              # State management
│   │   │   ├── slices/
│   │   │   │   ├── authSlice.ts
│   │   │   │   ├── notebookSlice.ts
│   │   │   │   └── executionSlice.ts
│   │   │   └── store.ts
│   │   ├── services/           # API services
│   │   │   ├── api.ts
│   │   │   ├── authService.ts
│   │   │   ├── notebookService.ts
│   │   │   └── executionService.ts
│   │   ├── utils/              # Utility functions
│   │   │   ├── constants.ts
│   │   │   ├── helpers.ts
│   │   │   └── validators.ts
│   │   ├── types/              # TypeScript types
│   │   │   ├── notebook.ts
│   │   │   ├── user.ts
│   │   │   └── execution.ts
│   │   ├── styles/             # Global styles
│   │   │   ├── global.css
│   │   │   └── theme.ts
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── tests/
│   │   ├── components/
│   │   └── e2e/
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── Dockerfile
├── execution-engine/
│   ├── docker/
│   │   ├── compilers/
│   │   │   ├── gcc-11.Dockerfile
│   │   │   ├── gcc-12.Dockerfile
│   │   │   ├── gcc-13.Dockerfile
│   │   │   ├── clang-15.Dockerfile
│   │   │   └── clang-16.Dockerfile
│   │   └── runner/
│   │       └── runner.Dockerfile
│   ├── scripts/
│   │   ├── compile.sh
│   │   ├── execute.sh
│   │   └── cleanup.sh
│   ├── sandbox/
│   │   ├── seccomp-profile.json
│   │   └── apparmor-profile
│   └── README.md
├── infrastructure/
│   ├── docker/
│   │   ├── docker-compose.dev.yml
│   │   ├── docker-compose.prod.yml
│   │   └── docker-compose.test.yml
│   ├── kubernetes/
│   │   ├── backend/
│   │   │   ├── deployment.yaml
│   │   │   ├── service.yaml
│   │   │   └── ingress.yaml
│   │   ├── frontend/
│   │   │   ├── deployment.yaml
│   │   │   └── service.yaml
│   │   ├── database/
│   │   │   ├── postgres-deployment.yaml
│   │   │   ├── postgres-service.yaml
│   │   │   └── postgres-pvc.yaml
│   │   └── redis/
│   │       ├── redis-deployment.yaml
│   │       └── redis-service.yaml
│   ├── terraform/              # Infrastructure as Code
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── monitoring/
│       ├── prometheus/
│       │   └── prometheus.yml
│       └── grafana/
│           └── dashboards/
├── scripts/
│   ├── setup-dev.sh            # Development setup script
│   ├── run-tests.sh            # Test runner script
│   ├── deploy.sh               # Deployment script
│   └── seed-data.sh            # Database seeding
├── examples/
│   └── notebooks/              # Example notebooks
│       ├── hello-world.json
│       ├── data-structures/
│       ├── algorithms/
│       └── cpp-features/
├── .gitignore
├── .dockerignore
├── .eslintrc.js
├── .prettierrc
├── LICENSE
├── README.md
├── PROJECT_PLAN.md
├── CONTRIBUTING.md
└── CODE_OF_CONDUCT.md
```

## Directory Descriptions

### Root Level
- **`.github/`**: GitHub-specific files (Actions, templates)
- **`docs/`**: All project documentation
- **`backend/`**: Backend server code (Node.js/Express)
- **`frontend/`**: Frontend application (React)
- **`execution-engine/`**: C/C++ compilation and execution system
- **`infrastructure/`**: DevOps and infrastructure configuration
- **`scripts/`**: Utility scripts for development and deployment
- **`examples/`**: Example notebooks and tutorials

### Backend (`backend/`)
- **`src/api/`**: RESTful API routes and controllers
- **`src/models/`**: Database models and schemas
- **`src/services/`**: Business logic layer
- **`src/middleware/`**: Express middleware functions
- **`src/workers/`**: Background job processors
- **`src/websocket/`**: WebSocket event handlers
- **`tests/`**: Unit, integration, and E2E tests

### Frontend (`frontend/`)
- **`src/components/`**: Reusable React components
- **`src/pages/`**: Page-level components
- **`src/hooks/`**: Custom React hooks
- **`src/store/`**: Redux/Zustand state management
- **`src/services/`**: API client services
- **`src/types/`**: TypeScript type definitions

### Execution Engine (`execution-engine/`)
- **`docker/`**: Docker images for different compilers
- **`scripts/`**: Shell scripts for compilation and execution
- **`sandbox/`**: Security profiles and configurations

### Infrastructure (`infrastructure/`)
- **`docker/`**: Docker Compose files for different environments
- **`kubernetes/`**: Kubernetes manifests for production deployment
- **`terraform/`**: Infrastructure as Code for cloud resources
- **`monitoring/`**: Monitoring and observability configuration

## File Naming Conventions

1. **Components**: PascalCase (e.g., `NotebookEditor.tsx`)
2. **Utilities**: camelCase (e.g., `authService.ts`)
3. **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_EXECUTION_TIME`)
4. **Test files**: `*.test.ts` or `*.spec.ts`
5. **Configuration**: kebab-case (e.g., `docker-compose.yml`)

## Best Practices

1. **Separation of Concerns**: Keep business logic separate from routes
2. **Modular Design**: Each module should have a single responsibility
3. **Type Safety**: Use TypeScript throughout the project
4. **Testing**: Maintain test files alongside source files or in parallel structure
5. **Documentation**: Document complex logic and API endpoints
6. **Version Control**: Use meaningful commit messages and branch names

## Getting Started

To set up this structure:

```bash
# Create all directories at once (run from project root)
mkdir -p .github/workflows .github/ISSUE_TEMPLATE
mkdir -p docs/{architecture,api,deployment,user-guide/tutorials}
mkdir -p backend/src/{api/{auth,notebooks,execution,users},models,services,middleware,utils,config,workers,websocket}
mkdir -p backend/tests/{unit,integration,e2e}
mkdir -p backend/prisma/migrations
mkdir -p frontend/public/assets
mkdir -p frontend/src/{components/{common/{Button,Input,Modal},auth,notebook,dashboard,layout},pages,hooks,store/slices,services,utils,types,styles}
mkdir -p frontend/tests/{components,e2e}
mkdir -p execution-engine/{docker/{compilers,runner},scripts,sandbox}
mkdir -p infrastructure/{docker,kubernetes/{backend,frontend,database,redis},terraform,monitoring/{prometheus,grafana/dashboards}}
mkdir -p scripts
mkdir -p examples/notebooks/{data-structures,algorithms,cpp-features}
```

## Next Steps

1. Initialize each component with basic configuration files
2. Set up database migrations
3. Create Docker development environment
4. Implement authentication system
5. Build the execution engine
6. Develop the frontend interface

Refer to `PROJECT_PLAN.md` for detailed phase-wise implementation.
