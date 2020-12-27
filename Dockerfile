FROM python:3.8-alpine
COPY . .
WORKDIR /backend
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "main.py"]