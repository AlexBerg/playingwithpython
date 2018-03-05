From python:3
Copy server.py /
Copy requirements.txt /
RUN pip install -r requirements.txt
CMD ["python", "-u", "server.py"]
