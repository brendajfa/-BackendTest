FROM python:3.8-slim

EXPOSE 8000

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY immfly_django/ .

# DOES NOT WORK
# command to run on container start
# ENTRYPOINT ["python"] 
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# docker build -f Dockerfile -t immfly_project .
# docker run immfly_project  or docker compose up

# WORKS
CMD "pytest"
# docker build -f Dockerfile -t immfly_project_pytest .
# docker run immfly_project_pytest 

# WORKS
# CMD ["python", "manage.py", "check", "my_api"]
# docker build -f Dockerfile -t immfly_project_check .
# docker run immfly_project_check 
