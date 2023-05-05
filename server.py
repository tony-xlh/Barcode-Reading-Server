from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from PIL import Image
import base64
from io import BytesIO
import base64
import os
import time
import json
import aggregated_reader
app = Flask(__name__, static_url_path='/', static_folder='./')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

reader = aggregated_reader.AggregatedReader()

@app.route('/read-barcodes', methods=['POST'])
@cross_origin()
def read_barcodes():
    if request.method == 'POST':
        data = request.get_json()
        if 'base64' in data:
            path = './uploaded/'
            if os.path.exists(path)==False:
                os.makedirs(path)
            bytes_decoded = base64.b64decode(data['base64'])
            img = Image.open(BytesIO(bytes_decoded))
            # to jpg
            out_jpg = img.convert('RGB')
            filename = str(int(time.time()*1000))+'.jpg'
            # save file
            out_jpg.save(os.path.join(path,filename))
            start_time = time.time()
            response=reader.decode_file(os.path.join(path,filename))
            end_time = time.time()
            elapsed_time = int((end_time - start_time) * 1000)
            response["elapsedTime"] = elapsed_time
            return json.dumps(response)
    else:
        return ""

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 8888, ssl_context='adhoc')