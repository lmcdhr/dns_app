from flask import Flask, request, Response
from time import gmtime, strftime
import json
import os
import requests

app = Flask(__name__)

@app.route('/home')
def AS_home():
    return "welcome to AS home page"
    
@app.route('/', methods = ['GET', 'POST'])
def AS():

    ## open or new the json file
    ## tje json file will store the name-ip pairs
    file = 'address_map.json'
    if not os.path.exists(file):
        os.system(r'touch address_map.json')
        file = 'address_map.json'
    
    ## test
#    dict = {}
#    dict['fibonacci.com'] = '0.0.0.0:9090'
#    with open(file, 'w') as f:
#        json.dump(dict, f)
    ## test input finish
    
    ## US ask ip address of a hostname
    if request.method == 'GET':
        key = request.args.get('name')
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            if key not in data:
                return Response("hostname not found", status = 404)
            else:
                address = data.get(key)
                return Response(address, status = 200)
    ## FS register information in AS
    else:
        data_get = request.form
        host_name = data_get['name']
        ip_address = data_get['address']
        dict = {}
        dict[host_name] = ip_address
        with open(file, 'w') as json_file:
            json.dump(dict, json_file)
        return Response("successfully registered", status = 200)


app.run(host='0.0.0.0',
        port=53533,
        debug=True)
