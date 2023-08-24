FROM ubuntu:latest

RUN apt-get clean && apt-get autoclean

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
RUN /bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/turbot/steampipe/main/install.sh)"


# Set the working directory
WORKDIR /app

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
COPY app.py /app/app.py
RUN chmod +x /entrypoint.sh


# Create a non-root user and switch to that user
RUN useradd -m -s /bin/bash steampipe
USER steampipe
RUN steampipe plugin install steampipe aws

# # Set environment variables
# ENV STEAMPIPE_DATABASE_PASSWORD=admin
# ENV STEAMPIPE_INTROSPECTION=info
RUN steampipe service start --show-password
RUN pip3 install flask
EXPOSE 5000
EXPOSE 9193

ENTRYPOINT [ "/entrypoint.sh" ]
