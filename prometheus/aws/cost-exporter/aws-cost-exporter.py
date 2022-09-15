from logging import ERROR, INFO
import boto3
import logging
from datetime import datetime, timedelta
import requests 
import json 
import time 
from prometheus_client import start_http_server, Gauge 

client = boto3.client('ce')
aws_cost_usage =  Gauge('aws_today_day_usage', 'Today day usage from AWS')		 


def collect_cost():
    now = datetime.now()
    yesterday = datetime.today() - timedelta(days=1)
    two_days_ago = datetime.today() - timedelta(days=2)
    try: 
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': yesterday.strftime("%Y-%m-%d"),
                'End':  now.strftime("%Y-%m-%d")
            },
            Granularity="DAILY",
            Metrics=["BlendedCost"]
        )
        return response["ResultsByTime"][0]["Total"]["BlendedCost"]["Amount"]
    except Exception as e: 
        logging.basicConfig(level=ERROR)
        logging.error("Collect Unavailable") 
        raise e 

def update_metrics(): 
    try:
        while True: 
            aws_cost_usage.set(collect_cost())
            time.sleep(3600) 
            logging.basicConfig(level=INFO)
            logging.info("The Actual Cost is: %s" % collect_cost()())
    except Exception as e: 
        logging.basicConfig(level=ERROR)
        logging.error("Update of cost is unavailable") 
        raise e 
        
def start_exporter(): 
    try:
        start_http_server(8899) 
        return True 
    except Exception as e: 
        logging.basicConfig(level=ERROR)
        logging.error("Server error") 
        raise e 

def main(): 
    try:
        start_exporter() 
        logging.basicConfig(level=INFO)
        logging.info('Exporter Running... \n\n http://127.0.0.0:9999/metrics \n\n ===MY EXPORTER=== \n') 
        update_metrics() 
    except Exception as e: 
        logging.basicConfig(level=ERROR)
        logging.error('\nExporter Failed and was finished! \n\n======> %s\n' % e) 
        exit(1) # Finaliza o programa com err


if __name__ == '__main__': 
    main() 
    exit(0)
