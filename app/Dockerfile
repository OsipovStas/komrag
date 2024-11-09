# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY ../requirements.txt /app/

RUN pip install streamlit
# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY ../app /app

COPY ../.streamlit /app/.streamlit

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run bootstrapp.py when the container launches
CMD ["streamlit", "run", "bootstrap.py"]