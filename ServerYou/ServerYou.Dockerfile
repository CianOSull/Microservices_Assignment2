# I think this buiilds a docker image
# also the tag of the image is greeterserver
# docker build -f Server.Dockerfile -t=server .

# This command will run the image and run the server
# docker run -p 50051:50051 server

# Then you can just use python to run the client to get a hello back

# Use an official Python runtime as a parent image - for a list of others see https://hub.docker.com/_/python/
FROM python:3-stretch

# Set the working directory to /app - this is a directory that gets created in the image
WORKDIR /app

# Copy the current host directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r ServerYou/requirements.txt

# Make port 50051 available to the world outside this container
EXPOSE 50051

# Run greeter_server.py when the container launches
CMD ["python", "ServerYou/serveryou.py"]