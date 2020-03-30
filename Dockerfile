FROM python:3

 ADD dnstlsproxy.py /
 RUN pip install dnslib
 EXPOSE 8888/tcp
 CMD [ "python", "./dnstlsproxy.py" ]