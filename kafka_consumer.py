from kafka import KafkaConsumer
from json import dumps,loads
import json
from s3fs import S3FileSystem
import configparser

consumer = KafkaConsumer(
    'demo_test',
     bootstrap_servers=['{REPLACE}:9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# credentials from config file / alternatively use aws config in aws CLI
config = configparser.ConfigParser()
config.read('config.ini')

aws_key = config['aws']['key']
aws_secret = config['aws']['secret']

fs = s3fs.S3FileSystem(
    key=aws_key,
    secret=aws_secret
)

bucket = "kafka-flights-vienna-ondrej"

for count, i in enumerate(consumer):
    # Use the fs instance to open a file on S3
    file_path = f"{bucket}/flight-data{count}.json"
    with fs.open(file_path, 'w') as file:
        json.dump(i.value, file)
    print(f"File {file_path} written successfully.")
