FROM python:3.10.12

# Install system dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Set the working directory
WORKDIR /

# Copy requirements file and install dependencies
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port used by your application (if any)
EXPOSE 8000

# Command to run the application
CMD ["python3", "run.py", "run"]
