# Neighborhood Watch Django Application

This Django application helps you build a neighborhood watch platform.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installing
- Clone the repository

```bash
git clone https://github.com/The-Neighborhood-Watch/nbhw-backend
```

- Change directory to the project root

```bash
cd nbhw-backend
```

- Create a `.env` file in the project root and add the following environment variables

```bash
DATABASE_URL=sqlite:///db.sqlite3
DEBUG=True
```

- Build the Docker image

```bash
docker-compose build
```

- Run the Docker container

```bash
docker-compose up
```
