# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Expose the port that your Django app will run on (default is 8000)
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver"]