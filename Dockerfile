# Use an official Python runtime as a parent image
FROM python:3.11.3-slim

RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y -q \
    git && apt-get clean

# Set the working directory in the container to /app
WORKDIR $PYSETUP_PATH

# Install Poetry
# RUN pip install poetry

# Copy only the necessary files for installing dependencies
# COPY pyproject.toml poetry.lock* /app/

# Disable virtual environments creation by Poetry
# as Docker itself provides isolation
# RUN poetry config virtualenvs.create false

# Install dependencies using Poetry
# RUN poetry install --no-dev

# Copy the rest of your application's code
# COPY . /app

# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
# CMD ["python", "app.py"]
