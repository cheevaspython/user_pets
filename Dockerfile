FROM python:3.11

ARG MY_ENV
ENV MY_ENV=${MY_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.4.0

RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /user_pets
COPY poetry.lock pyproject.toml /user_pets/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /user_pets
EXPOSE 8000
RUN adduser --disabled-password docker-admin
USER docker-admin
