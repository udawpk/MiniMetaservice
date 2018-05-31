#!/usr/bin/env python
from os import path
import sys
import re

sys.path.append(path.dirname(path.dirname(path.abspath(__file__)))+'/lib')
from flask import Flask
from flask import abort


if len(sys.argv) != 2:
    print ("usage: "+sys.argv[0]+" path_to_conf_root")
    exit (1)


def getData (path):
    regionFile=str()
    error=False
    try:
        regionFile=open(path, 'r').read()
    except IOError:
        error=True
        regionFile=None

    return {'data':regionFile, 'error':error}


app = Flask(__name__)

@app.route('/<string:region>/<string:service>', methods=['GET', 'POST'])
def getRegionData (region, service):
    
    key=getData(sys.argv[1]+'/'+region+'/authKey')
    
    if not key['error']:
        abort(403)

    regionData=getData(sys.argv[1]+'/'+region+'/'+service)
    
    if regionData['error']:
        abort(404)
    return(regionData['data'], 200)


@app.route('/<string:region>/<string:service>/<string:secret>', methods=['GET', 'POST'])
def getRegionSecretData (region, service, secret):
    
    key=getData(sys.argv[1]+'/'+region+'/authKey')
    
    if key['error']:
        abort(404)
    else:
        regionKey=re.sub('\n', '', key['data'])
        if regionKey != secret:
            abort(403)
        
    regionPath=sys.argv[1]+'/'+region+'/'+service
    regionData=getData(regionPath)
    if regionData['error']:
        abort(404)
    
    return(regionData['data'], 200)

@app.errorhandler(404)
def notFound(error):
    return ("404", 404)

@app.errorhandler(403)
def forbidden(error):
    return ("403", 403)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("1488"), debug=True)