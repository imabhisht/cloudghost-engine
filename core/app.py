from flask import Flask, request
import os;
import subprocess;
import json;
app = Flask(__name__)
base_route = '/cq/core'
@app.route('/', methods=['GET'])
def info():
    # Get Env Variable
    steampipe_introspection = os.environ.get('STEAMPIPE_INTROSPECTION')
    return {
        "status": "success",
        "message": "Steampipe is running",
        "steampipe_introspection": steampipe_introspection
    }


@app.route('/cq/core/start', methods=['POST'])
def start_steampipe():
    try:
        subprocess.run(["steampipe", "service", "start", "--show-password" ], check=True)
        return {
            "status": "success",
            "message": "Steampipe started successfully"
        }
    except subprocess.CalledProcessError as e:
        print("Error executing Steampipe command:")
        print(e)
        return "Error executing Steampipe command"

@app.route('/cq/core/stop', methods=['POST'])
def stop_steampipe():
    try:
        subprocess.run(["steampipe", "service", "stop"], check=True)
        return {
            "status": "success",
            "message": "Steampipe stopped successfully"
        }
    except subprocess.CalledProcessError as e:
        print("Error executing Steampipe command:")
        print(e)
        return "Error executing Steampipe command"

@app.route('/cq/core/config/aws', methods=['POST'])
def update_config():
    config_file_path = os.path.expanduser('~/.steampipe/config/aws.spc')
    # config_file_path = os.path.expanduser('./test/aws.spc')    

    request_data = request.get_json()
    connections = request_data.get('connections', [])

    new_config_content = ''
    for connection in connections:
        new_config_content += f'''
        connection "{connection['name']}" {{
            plugin     = "aws"
            secret_key = "{connection['secret_key']}"
            access_key = "{connection['access_key']}"
            regions    = {json.dumps(connection['regions'])}
        }}
        '''

    # Write the new config content back to the file
    with open(config_file_path, 'w') as config_file:
        config_file.write(new_config_content)

    return 'Config updated successfully'
if __name__ == '__main__':
    ##PORT FROM ENV
    PORT = int(os.environ.get('API_PORT'))
    app.run(host='0.0.0.0', port=PORT, debug=True)

