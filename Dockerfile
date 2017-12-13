FROM python:2.7

MAINTAINER lzxz1234 <314946925@qq.com>

COPY requirements.txt /opt/utilities/requirements.txt
RUN pip install -r /opt/utilities/requirements.txt
RUN pip install uwsgi

ADD . /opt/utilities
WORKDIR /opt/utilities
EXPOSE 8001

ENTRYPOINT ["uwsgi"]
CMD ["--http", ":8001", "--wsgi-file", "wsgi.py", "--static-map", "/static=/opt/utilities/static"]