FROM python:3
COPY server /
COPY requirements.txt /
RUN pip install -r requirements.txt
CMD ["python", "-u" ,"server.py"]
