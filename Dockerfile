FROM python:3.12-slim as builder
WORKDIR /bot
RUN apt update \
    && apt upgrade -y  \
    && pip install --no-cache-dir --upgrade poetry
COPY poetry.lock pyproject.toml ./
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt


FROM python:3.12-slim
RUN groupadd -r choose_or_challenge_bot  \
    && useradd --no-log-init -r -g choose_or_challenge_bot choose_or_challenge_bot
USER choose_or_challenge_bot
WORKDIR /bot
COPY --from=builder /bot/requirements.txt ./requirements.txt
RUN apt update \
    && apt upgrade -y \
    && pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY ./ ./
EXPOSE 8080
CMD ["python3", "-m", "bot"]