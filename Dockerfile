# Use an official Python runtime as a parent image
FROM python:2.7

# Config python utf8
RUN sed  -i 's+encoding = "ascii"+encoding = "utf8"+g' /usr/local/lib/python2.7/site.py

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./qa /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
