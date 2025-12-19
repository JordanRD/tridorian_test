FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
COPY . .

# Create virtual environment and install dependencies
RUN uv venv && \
  . .venv/bin/activate && \
  uv pip install -e .

# Expose port for web interface
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

# Default command to start the web interface
CMD ["adk", "web", "--port", "8000"]