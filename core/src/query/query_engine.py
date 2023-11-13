import json
from src.query.engine import SteampipeDatabase
from sqlalchemy import text
import os
import re

db = SteampipeDatabase()
db = db.connection
file_path = os.path.join(os.path.dirname(__file__), 'query.json')

query_file = open(file_path, 'r')
steampipe_query = json.load(query_file)



def excute_query(config: dict) -> dict:
    connection_id:str = config['connection_id']
    query_name:str = config['query']
    raw_query:str = steampipe_query[query_name]
    query_variables:dict  = config['variables']

    query_variables['connection_id'] = connection_id
    
    ## Replace the variables with the Raw Query values 
    formatted_query = re.sub(r"{{(.*?)}}", lambda x: query_variables.get(x.group(1), x.group(0)), raw_query)

    
    try:
        # Run the query
        result = db.execute(text(formatted_query))

        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result]

        return data

    except Exception as e:
        return Exception(e)




    

    
