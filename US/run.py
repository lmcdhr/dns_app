from flask import Flask, url_for, request, render_template, Response
import requests
app = Flask(__name__)

@app.route('/')
def hello():
    return ('Hello from Mucheng, welcome to my DNS_app')

@app.route('/fibonacci')
def US():
    host_name = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    x = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    if(host_name == None or fs_port == None or x == None or as_ip == None or as_port == None):
        return Response("Bad request", status = 400)
    else:
        print('Success, info input: '+host_name+ ','+fs_port+','+x+','+as_ip+','+as_port)
    ## ask address from AS
        ip_info = {'name':host_name, 'fs_port':fs_port}
        r = requests.get('http://'+as_ip+':'+as_port, params = ip_info)
        if r.status_code == 404:
            return "hostname not found, Status:404"
    ## send request to FS
        ip_address_FS = 'http://'+r.text+':'+fs_port+'/fabonacci?number='+x
        print(ip_address_FS)
        r = requests.get(ip_address_FS)
    ## output result
        return r.text
    
    
app.run(host='0.0.0.0',
        port=8080,
        debug=True)
