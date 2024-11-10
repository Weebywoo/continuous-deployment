FROM python:3.12.0-slim

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

COPY . .
RUN apt-get -y update
RUN apt-get -y install git
RUN python -m pip install -r ./requirements.txt

EXPOSE 8000
ENTRYPOINT ["python", "main.py"]
