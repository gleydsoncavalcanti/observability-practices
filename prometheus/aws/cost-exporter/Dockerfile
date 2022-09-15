FROM python:3.7
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY aws-cost-exporter.py /app/aws-cost-exporter.py
EXPOSE 9999
CMD [ "python", "/app/aws-cost-exporter.py" ]
