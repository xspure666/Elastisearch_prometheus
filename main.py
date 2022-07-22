from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient

# kafka 集群信息
bootstrap_servers = '10.1.2.175:9092'

consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, )
all_topic = consumer.topics()
# # consumer_group = consumer.partitions_for_topic()
# for i in all_topic:
#     print(i)

print("=====")
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers, client_id='log_run_status')
# print(admin_client.describe_consumer_groups("flow_merge_group_01"))

print("=====")
group = admin_client.list_consumer_groups()
for i in group:

    print(admin_client.list_consumer_group_offsets(i[0]))
# admin_client.describe_topics()