# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container to /app
WORKDIR /app

# Install FFmpeg
RUN apt-get update \
&& apt-get install -y ffmpeg git \
&& rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
# Make sure you have a requirements.txt file at your project root that includes Flask and moviepy
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

CMD ["python", "app.py"]
