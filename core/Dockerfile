# Use the latest Ubuntu base image
FROM ubuntu:latest

# Update package lists and install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    unzip 

# Download and install the AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && rm -rf awscliv2.zip \
    && ./aws/install

# Install Steampipe
# RUN /bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/turbot/steampipe/main/install.sh)"

# Set the working directory
WORKDIR /app

COPY src /app/src

RUN chmod +x /app/src/install.sh
RUN /bin/sh /app/src/install.sh

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
COPY app.py /app/app.py
RUN chmod +x /entrypoint.sh

# Create a non-root user and switch to that user
RUN useradd -m -s /bin/bash steampipe
USER steampipe

# Set the PATH to include the Steampipe plugins directory
ENV PATH="/home/steampipe/.steampipe/plugins:${PATH}"

# Install the Steampipe AWS plugin
RUN steampipe plugin install steampipe aws

# Install Flask Python package
RUN pip3 install flask

RUN pip3 install python-dotenv

# Expose ports for Flask and Steampipe (adjust as needed)
EXPOSE 5000
EXPOSE 9193

# Define the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
