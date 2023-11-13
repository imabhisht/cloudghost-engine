## This file will be use to run Subprocess Command of Steampipe to export data into CSV format

import subprocess
import os
import sys
import json
import csv
import time

query_data = json.load(open('query.json', 'r'))
# Function to run subprocess command


def query_in_csv(query, profile_name):  

    query = (query_data[query]).replace("{{connection_id}}", profile_name)   

    try:
        command = f'steampipe query "{query}" --output json'
        completed_process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if completed_process.returncode == 0:
            # Access the captured JSON output as a string
            output_str = completed_process.stdout

            # Parse the captured JSON output
            parsed_data = json.loads(output_str)

            # You can now work with the parsed JSON data as a Python dictionary
            # print("Parsed JSON data:")
            # print(type(parsed_data))

        return parsed_data

    except subprocess.CalledProcessError as e:
        print("Error executing Steampipe command:")
        print(e)
        return "Error executing Steampipe command"
        


# print(type(query_data))
# query_in_csv("aws_ec2_instances_metric_cpu_utilization_daily_basic_info_all","aws_aw2413")  