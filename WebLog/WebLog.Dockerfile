# This will create a image of the output py file i guess
# This file is part of making logs

# Use an official Python runtime as a parent image
FROM python:3-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r WebLog/requirements.txt

# Make port 50051 available to the world outside this container
# Here we are mapping flask's port of 5000 to the more
# common port of 8080 on the host
EXPOSE 8080:5000

# Run app.py when the container launches
CMD ["python", "WebLog/output_logs.py"]