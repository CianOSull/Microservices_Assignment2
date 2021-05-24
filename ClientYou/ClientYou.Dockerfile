# Remember to build an image
# docker build -f Client.Dockerfile -t=client .

# When the server is running you can now do this:
# docker run --network="host" client

# Use an official Python runtime as a parent image
FROM python:3-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the client code into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r ClientYou/requirements.txt

# Run greeter_client.py when the container launches
CMD ["python", "ClientYou/clientyou.py"]

