FROM ubuntu

RUN apt-get update -y && apt-get install python -y \
     && apt-get install python3-pip -y \
     && apt-get install curl -y \
     && pip3 install flask \
     && pip3 install requests \
     && pip3 install jsonify

ADD app.py /tmp


WORKDIR /tmp


CMD ["python3","app.py"]
