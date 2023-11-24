from elasticsearch import Elasticsearch
import os

ELASTIC_PASSWORD = os.environ.get('ELASTIC_PASSWORD')
ELASTIC_CLOUD_ID = os.environ.get('ELASTIC_CLOUD_ID')

client = Elasticsearch(
    cloud_id=ELASTIC_CLOUD_ID,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)
mapping = {
    "properties": {
      "updated_at": {
        "type": "date"
      },
      "type": {
        "type": "keyword"
      },
      "data": {
        "properties": {
          "instance_id": {
            "type": "keyword"
          },
          "arn": {
            "type": "keyword"
        }
      }
    }
  }
}
# client.indices.create(index="aws_ec2_instance",body={
#     "mappings": mapping})

print(f"[ELASTIC CLOUD]: Connected with: {client.info()['cluster_name']}")
print(f"[ELASTIC CLOUD]: Connected Instance: {client.info()['name']}")


def get_client() -> Elasticsearch:
    return client
