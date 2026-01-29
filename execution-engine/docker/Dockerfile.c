FROM gcc:latest

# Install necessary tools
RUN apt-get update && apt-get install -y \
    time \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /workspace

# Set resource limits
ENV MAX_MEMORY=512m
ENV MAX_TIME=30s

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
