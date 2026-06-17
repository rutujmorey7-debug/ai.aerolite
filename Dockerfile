# Use a lightweight official Python runtime
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /code

# Copy requirements file first to utilize Docker caching
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy all your project files (including templates, core, training, etc.)
COPY . .

# Grant permission to the HF user home directory just in case weights need to be written
RUN mkdir -p /.cache && chmod -R 777 /.cache

# Expose the mandatory Hugging Face port
EXPOSE 7860

# Run the application with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:7860", "--workers", "1", "--timeout", "120", "main:app"]
