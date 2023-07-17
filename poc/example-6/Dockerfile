# Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app/app

RUN pip install psycopg2

ENV MODULE_NAME=app.main
ENV VARIABLE_NAME=app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
