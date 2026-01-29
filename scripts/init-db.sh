#!/bin/bash

# Initialize database

echo "Initializing database for C/C++ Notebook..."

# Check if backend directory exists
if [ ! -d "backend" ]; then
    echo "Error: backend directory not found"
    exit 1
fi

# Run database initialization script
cd backend
python -m app.db.init_db

echo "✅ Database initialized successfully!"
