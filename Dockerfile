FROM python:3.8

ENV PYTHONUNBUFFERED 1

# arbitrary location choice: you can change the directory
RUN mkdir -p /vendas
WORKDIR /vendas

# install psycopg2 dependencies
#RUN apk update  && apk add postgresql-dev gcc python3-dev musl-dev

# copy project
COPY requirements.txt /vendas/

# install denpendencies of django
RUN pip install -r requirements.txt
COPY . .
