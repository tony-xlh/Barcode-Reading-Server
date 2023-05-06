from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import base64
import os
import time
import json
import aggregated_reader
app = Flask(__name__, static_url_path='/', static_folder='./')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

reader = aggregated_reader.AggregatedReader()

@app.route('/', methods=['GET', 'POST'])
@app.route('/readBarcodes', methods=['GET', 'POST'])
@cross_origin()
def read_barcodes():
    if request.method == 'POST':
        data = request.get_json()
        if 'base64' in data:
            bytes_decoded = base64.b64decode(data['base64'])
            start_time = time.time()
            response=reader.decode_bytes(bytes_decoded)
            end_time = time.time()
            elapsed_time = int((end_time - start_time) * 1000)
            response["elapsedTime"] = elapsed_time
            return json.dumps(response)
    else:
        return ""

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 8888) #, ssl_context='adhoc'