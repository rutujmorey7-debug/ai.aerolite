# Use a lightweight, official Python runtime
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /code

# Copy requirements file first to utilize Docker build caching
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy all project files (including templates, core, training, etc.)
COPY . .

# Grant write permissions to the cache directory for downloading models
RUN mkdir -p /.cache && chmod -R 777 /.cache

# Expose the mandatory Hugging Face port
EXPOSE 7860

# Run the application with Gunicorn, optimized for a 16GB free tier instance
CMD ["gunicorn", "-b", "0.0.0.0:7860", "--workers", "1", "--timeout", "120", "main:app"]
