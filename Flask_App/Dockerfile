#Use Python as base image
FROM python:3.12-slim

# Use working directory /app
WORKDIR /app

# Copy all the content of current directory to /app
COPY . /app

# Installing required packages
RUN pip install --no-cache-dir -r requirements.txt

# Open port 5000
EXPOSE 5000

# Set environment variable
ENV NAME OpentoAll

# Run Flask app
CMD ["python", "app.py"]

