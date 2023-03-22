#kafka stream carts
from confluent_kafka import Producer
import requests
import json
import time 

# define url source and request data
url = 'https://dummyjson.com/carts'
response = requests.get(url)

# read and parse the data using json()
carts = response.json()
 
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
topic_name = 'carts'

def main():
    for cart in carts['carts']: # in the json file carts there is key namely 'carts'
        p.produce(topic_name, json.dumps(cart).encode('utf-8'), callback=receipt) # json.dumps(): convert dict to json file
        p.poll(1)
        p.flush()
        time.sleep(2) # suspends execution for 2 sec.

if __name__ == '__main__':
    main()

