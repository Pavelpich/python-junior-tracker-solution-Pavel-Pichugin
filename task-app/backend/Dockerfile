FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-pip \
    pipx \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"
RUN pipx install uv

WORKDIR /app

COPY requirements.txt .

RUN uv pip install --system -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DATABASE_URL=postgresql+psycopg://postgres:postgres@db:5432/tasks

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
