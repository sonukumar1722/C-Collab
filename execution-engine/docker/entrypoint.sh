#!/bin/bash

# Entrypoint script for C/C++ code execution
set -e

# Execute the command passed to the container
exec "$@"
