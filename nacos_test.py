import nacos
import yaml

"""
 pip install pyyaml
"""


def nacos_config():
    try:
        SERVER_ADDRESSES = "10.1.2.178:8848"  # nacos的ip:port
        NAMESPACE = "test"  # 命名空间的id: namespace id
        client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, username="nacos", password="nacos")
        data_id = "elastic"
        group = "DEFAULT_GROUP"
        nacos_config = client.get_config(data_id, group)
        dict_nacos_config = yaml.load(nacos_config, Loader=yaml.FullLoader)
        return dict_nacos_config

    except Exception as e:
        print("connect to nacos failed", e)


if __name__ == "__main__":
    nacos_config()
