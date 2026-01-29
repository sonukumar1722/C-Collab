#!/bin/bash

# Start development environment for C/C++ Notebook

echo "Starting C/C++ Notebook Development Environment..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Error: Docker is not running. Please start Docker first."
    exit 1
fi

# Build Docker images
echo "Building Docker images..."
docker-compose build

# Start services
echo "Starting services..."
docker-compose up -d

# Wait for services to be ready
echo "Waiting for services to be ready..."
sleep 5

# Check service status
echo "Checking service status..."
docker-compose ps

echo ""
echo "✅ Development environment started successfully!"
echo ""
echo "Services running at:"
echo "  Frontend: http://localhost:3000"
echo "  Backend:  http://localhost:8000"
echo "  Execution Engine: http://localhost:8001"
echo ""
echo "To view logs: docker-compose logs -f"
echo "To stop: ./scripts/stop.sh"
