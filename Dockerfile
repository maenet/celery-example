FROM python:3.7

RUN curl -sL -o /tmp/watchexec.deb https://github.com/watchexec/watchexec/releases/download/1.14.1/watchexec-1.14.1-x86_64-unknown-linux-gnu.deb \
 && apt-get install /tmp/watchexec.deb \
 && rm -rf /tmp/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
