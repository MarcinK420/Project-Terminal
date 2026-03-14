FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache

COPY . .

RUN chmod +x your_program.sh

ENV PYTHONPATH=/app

ENTRYPOINT [ "./your_program.sh" ]