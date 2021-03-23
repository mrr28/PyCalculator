FROM python:3

ADD src /src

CMD [ "python", "./src/calcTests.py"]