# Use the official Python image as the base image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE fgf.settings

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the application runs on
EXPOSE 8000

# Run the Django application
CMD ["gunicorn", "fgf.wsgi:application", "--bind", "0.0.0.0:8000"]
