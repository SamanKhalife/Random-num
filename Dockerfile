# Use an official Ubuntu image as a parent image
FROM ubuntu:20.04

# Set the working directory to /app
WORKDIR /app

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 8585 available to the world outside this container
EXPOSE 8569

# Run the application when the container launches
CMD ["python3", "random.num.py"]
