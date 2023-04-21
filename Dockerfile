FROM python:3.8-slim


WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY immfly_django/ .

# command to run on container start
ENTRYPOINT ["python"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# docker build -f Dockerfile -t immfly_project .
# docker run immfly_project
