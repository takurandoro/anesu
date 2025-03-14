# Use the latest stable Python version
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by Gunicorn
EXPOSE 8000

# Start the API with Gunicorn
CMD ["gunicorn", "--config", "gunicorn.conf.py", "green_academy.wsgi:application"]
