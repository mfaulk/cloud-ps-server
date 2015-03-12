import os
import time
from kafka import SimpleProducer, KafkaClient, KafkaConsumer
from kafka.common import LeaderNotAvailableError
import logging

logging.basicConfig()
logger = logging.getLogger('cloud-ps-server')

# IP:PORT of a Kafka broker. The typical port is 9092.
KAFKA_BROKER_IP_PORT = os.getenv('KAFKA_BROKER', '192.168.86.10:9092')
print "KAFKA BROKER: " + KAFKA_BROKER_IP_PORT
kafka = KafkaClient(KAFKA_BROKER_IP_PORT)
producer = SimpleProducer(kafka)

# Note that the application is responsible for encoding messages to type str
while True:
	print('Sending...')
	logger.info('Sending...')
	try:
		producer.send_messages("cloud-ps", "{msg:cloud-ps}")
	except LeaderNotAvailableError:
		logger.warning('Caught a LeaderNotAvailableError. This seems to happen when auto-creating a new topic.')
		print('Caught a LeaderNotAvailableError. This seems to happen when auto-creating a new topic.')
	time.sleep(3)

# To consume messages
# consumer = KafkaConsumer("my-topic", group_id="my_group",
#                          metadata_broker_list=[ZOOKEEPER_IP_PORT])
# for message in consumer:
#     # message is raw byte string -- decode if necessary!
#     # e.g., for unicode: `message.decode('utf-8')`
#     print(message)

# kafka.close()
