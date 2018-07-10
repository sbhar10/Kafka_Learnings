from pykafka import KafkaClient

import ConfigParser as conf

config = conf.ConfigParser()
config.read('settings.conf')

print config.get('servers','kafka_host')
    
client = KafkaClient(hosts=config.get('servers','kafka_host'))
#client = KafkaClient(hosts="127.0.0.1:9092")
print client.topics
topic = client.topics[config.get('topics','measuretopicBCS')] #List of members for given measure
with topic.get_sync_producer() as producer:
    for i in range(4):
        producer.produce('member id - ' + str(i * 2))
        
consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        print message.offset, message.value #Domain service consume this for aggregation
