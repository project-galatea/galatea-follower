FROM python:2.7-onbuild

ADD . /app

WORKDIR /app

RUN pip install git+https://github.com/farizrahman4u/seq2seq.git

RUN apt-get update

RUN apt-get -y install protobuf-compiler

RUN make compile

ENTRYPOINT ["python", "galatea.py"]

EXPOSE 24833
