# Flask Test App

Simple Flask application for testing Docker deployment.

## Quick Start

```bash
# Clone the repository
git clone <your-repo-url>
cd teste-flask

# Run with Docker Compose
docker compose up -d --build
```

## Access

- Local: http://localhost:8080
- Production: http://your-server-ip:8080

## Files

- `app.py` - Flask application
- `Dockerfile` - Docker configuration
- `docker-compose.yml` - Docker Compose setup

## Deploy to VPS

```bash
# On your VPS
git clone <your-repo-url>
cd teste-flask
docker compose up -d --build
```

The app will be available at port 8080.