# Use the official Airflow image as a template.
FROM apache/airflow:2.10.2

# Switch to airflow user to install packages.
USER airflow

# Copy the requirements file into the container.
COPY requirements.txt .

# Install all dependencies from the requirements file.
RUN pip install -r requirements.txt

# Copy dbt directory into the container.
COPY dbt /opt/airflow/dbt
