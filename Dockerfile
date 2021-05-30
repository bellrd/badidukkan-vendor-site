FROM python:3.9.0-buster

WORKDIR /backend

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . /backend

EXPOSE 8008

CMD [ "sh", "./run.sh"]
