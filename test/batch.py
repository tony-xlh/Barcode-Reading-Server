import base64
import requests
import asyncio
import json
import time
from multiprocessing import Process

def get_picture_base64_data(image_path):
    with open(image_path, 'rb') as image_file:
        base64_data = base64.b64encode(image_file.read())
    return base64_data.decode('utf-8')

def decode(index):
    base64 = get_picture_base64_data("../AllSupportedBarcodeTypes.png")
    body = {"base64": base64}
    json_data = json.dumps(body)
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://127.0.0.1:8888', data=json_data, headers=headers)
    if r.status_code == 200:
        print("success "+str(index))
        return True
    return False


if __name__ == "__main__":
    for i in range(100):
        p = Process(target=decode, args=(i,))
        p.start()