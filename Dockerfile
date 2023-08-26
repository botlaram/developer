# # Host Mkdocs using Docker File
# FROM python:3.8-slim

# # Set the working directory in the container
# WORKDIR /app

# COPY mkdocs.yml /app/
# COPY ./docs/ /app/docs/

# # Install any needed packages specified in requirements.txt
# RUN pip install mkdocs mkdocs-material

# # Expose the default MkDocs port
# EXPOSE 8000

# # Define the command to run MkDocs when the container starts
# CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]



# Host Mkdocs by cloning from Git Repo
# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install git and other dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Clone your Git repository
RUN git clone https://github.com/botlaram/developer.git /app/developer

# working directory
WORKDIR /app/developer

RUN git checkout working

# Install MkDocs and required plugins
RUN pip install mkdocs mkdocs-material

# Expose the default MkDocs port
EXPOSE 8000

# Command to serve the MkDocs site
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
