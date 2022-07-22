from elasticsearch6 import Elasticsearch
import time
from nacos_test import nacos_config

nacos_info = nacos_config()["elastisearch"]
elastic_ip = str(nacos_info["ip"]).split(",")
time_differ = nacos_info["time_late"]


def elastic():
    index_name = "oneevent_log_index"
    es = Elasticsearch(elastic_ip, request_timeout=200)
    # es = Elasticsearch("http://10.1.2.172:9200", request_timeout=200)
    start_timestamp = round(time.time() * 1000)
    time_late = time_differ * 60 * 1000
    end_timestamp = start_timestamp - time_late

    body = {
        "query": {
            "range": {
                "lOccurTime": {
                    "gte": end_timestamp,
                    "lte": start_timestamp
                }
            }
        }
    }

    result = es.search(index=index_name, body=body)
    total_message = result['hits']['total']  # es查询出的结果第一页
    return total_message, index_name


if __name__ == "__main__":
    abc = elastic()
    print(abc)
