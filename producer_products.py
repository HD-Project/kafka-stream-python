#kafka stream product
from confluent_kafka import Producer
import requests
import json
import time 

# define url source and request data
url = 'https://dummyjson.com/products'
response = requests.get(url)

# read and parse the data using json()
products = response.json()
 
# define the producer by specifying the port of Kafka cluster
p = Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer Started...')

# Define a callback function for errors. 
# Valid message will be decoded to utf-8 and printed in the
def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        print(message)

# Define topic name here
topic_name = 'products'

def main():
    for product in products['products']: # in the json file products there is key namely 'products'
        p.produce(topic_name, json.dumps(product).encode('utf-8'), callback=receipt) # json.dumps(): convert dict to json file
        p.poll(1)
        p.flush()
        time.sleep(2) # suspends execution for 2 sec.

if __name__ == '__main__':
    main()

