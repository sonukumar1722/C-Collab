#!/bin/bash

# Clean up development environment

echo "Cleaning up C/C++ Notebook development environment..."

# Stop and remove containers
echo "Stopping and removing containers..."
docker-compose down -v

# Remove Docker images
echo "Removing Docker images..."
docker-compose down --rmi all

# Clean up storage (notebooks and uploads)
echo "Cleaning up storage..."
rm -rf storage/local/notebooks/*
rm -rf storage/local/uploads/*

# Recreate .gitkeep files
touch storage/local/notebooks/.gitkeep
touch storage/local/uploads/.gitkeep

# Clean up Python cache
echo "Cleaning up Python cache..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null

# Clean up Node modules (if needed)
# echo "Cleaning up Node modules..."
# rm -rf frontend/node_modules

echo "✅ Cleanup completed successfully!"
