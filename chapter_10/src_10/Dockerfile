# Use a lightweight base image with Python.
FROM python:3.9-slim

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements file into the container's working directory.
COPY requirements.txt .

# Install the required Python packages listed in requirements.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container.
COPY . .

# Expose port for access.
EXPOSE 8050

# Define the command to run the Python app.
CMD ["python", "app.py"]
