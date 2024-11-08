FROM python:3.8
# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
#COPY . .
COPY requirements.txt /usr/src/app/
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 8080

# run the command
#CMD ["python", "./app.py"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
