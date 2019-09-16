FROM python
RUN mkdir /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD myApp.py /app/myApp.py
RUN chmod +x /app/myApp.py
CMD ["/app/myApp.py"]
