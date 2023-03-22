# kafka-stream-python

Step 1: Install Kafka

First, you need to download and install Apache Kafka on your Windows machine. You can download it from the official Apache Kafka website.

Step 2: Start Zookeeper and Kafka servers

After installing Kafka, you need to start Zookeeper and Kafka servers. To start Zookeeper, open a command prompt and run the following command:
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

To start Kafka, open another command prompt and run the following command:
.\bin\windows\kafka-server-start.bat .\config\server.properties

Step 3: Create Topics 
(optional since the python code could create if it not exist yet)
You can create with the following code on command prompt
.\bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic products
.\bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic users
.\bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic carts

Step 4: Create Producers
After creating topics, you need to create two producers, one for each topic. (Check the uploaded "producer____.py" python code on the repo for example) 

Step 5: Create Consumers
Finally, you need to create consumers or consumer groups to consume data from the created topics. (Check the uploaded "consumer____.py" python code on the repo for example)

step 6: Run the Code:
Open two new terminal windows, navigate to the directory where the producer and consumer code files are saved, and run the following commands to start them:
-> python producer_products.py
-> python producer_users.py

step 7 check the created file .json
