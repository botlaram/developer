# FROM python:3.10-slim as builder

# WORKDIR /data

# COPY mkdocs.yml ./
# COPY /docs/ ./
# COPY requirements.txt ./

# USER root
# RUN apt-get update && apt-get install -y \
#     graphviz \
#     && rm -rf /var/lib/apt/lists/*

# RUN pip install -r requirements.txt
# RUN mkdocs serve

# FROM nginxinc/nginx-unprivileged:alpine
# COPY --from=builder /data/public /usr/share/nginx/html


# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

COPY mkdocs.yml /app/
COPY ./docs/ /app/docs/
COPY requirements.txt /app/


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Expose the default MkDocs port
EXPOSE 8000

# Define the command to run MkDocs when the container starts
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
