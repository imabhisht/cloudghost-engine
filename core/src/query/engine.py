from src.steampipe.query_engine import excute_query as aws_query_executor
import json
import os
from src.elasticsearch.app import get_client as get_elastic_client
from elasticsearch.helpers import bulk
from datetime import datetime

elastic_client = get_elastic_client()


file_path = os.path.join(os.path.dirname(__file__), '../config/steampipe_query.json')
query_file = open(file_path, 'r')
steampipe_query = json.load(query_file)

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

# elastic_client.indices.put_mapping(index="aws_ec2_instance",body=mapping)


def doc_generator(data, index_name, doc_type):
    for item in data:
        yield {
            "_op_type": "index",
            "_index": index_name,
            "_source": {
                "updated_at": datetime.now(),
                "type": doc_type,
                "data": item
            }
        }



def excute_scheduler_query(query,force,connection_id,variables) -> (dict , int):
    try:
        result_steampipe , raw_query_data = aws_query_executor({
            "connection_id": connection_id,
            "query": query,
            "variables": variables
        })

        success, failed = bulk(elastic_client, doc_generator(result_steampipe, raw_query_data['index'], raw_query_data['type']))
            
        print(f"Successfully indexed {success} documents.")
        print(f"Failed to index {failed} documents.")

        return {
            "status": "success",
            "message": "AWS Query executed successfully",
            "data": result_steampipe
        } , 200

    except Exception as e:
        print(str(Exception(e)))
        return {
            "status": "error",
            "message": e.__str__(),
            "data": None
        }, 500
    


def excute_client_query(query,force,connection_id,variables) -> dict:

    steampipe_raw_query_data = steampipe_query[query]
    try:



        result = aws_query_executor({
            "connection_id": connection_id,
            "query": query,
            "variables": query_variables
        })

        return {
            "status": "success",
            "message": "AWS Query executed successfully",
            "data": result
        } , 200

    except Exception as e:
        print("Error: ",e)
        return {
            "status": "error",
            "message": str(Exception(e)),
            "data": None
        }, 500