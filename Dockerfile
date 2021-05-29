FROM python:3.6

RUN useradd -m yatra

ADD ./requirements.txt /home/yatra

WORKDIR /home/yatra

ENV PYTHONUNBUFFERED 0

RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt && \
    python -m spacy download en_core_web_sm

ADD . /home/yatra

USER yatra

EXPOSE 9999

CMD ["/bin/bash", "./run.sh"]