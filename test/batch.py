import base64
import requests
import asyncio
import json
import time
from multiprocessing import Process, Value

def get_picture_base64_data(image_path):
    with open(image_path, 'rb') as image_file:
        base64_data = base64.b64encode(image_file.read())
    return base64_data.decode('utf-8')

def decode(index, completed_number, success_number, files_number, start_time):
    base64 = get_picture_base64_data("../AllSupportedBarcodeTypes.png")
    body = {"base64": base64}
    json_data = json.dumps(body)
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://127.0.0.1:8888', data=json_data, headers=headers)
    completed_number.value = completed_number.value + 1
    if r.status_code == 200:
        success_number.value = success_number.value + 1
        print("success "+str(index))
    if completed_number.value == files_number.value:
        end_time = time.time()
        elapsed_time = int((end_time - start_time.value) * 1000)
        print("Successfully decoded " + str(success_number.value) + " images in " + str(elapsed_time) + "ms.")


if __name__ == "__main__":
    iteration_times = 100
    completed_number = Value('d', 0.0)
    success_number = Value('d', 0.0)
    files_number = Value('d', iteration_times)
    start_time = Value('d', time.time())
    for i in range(iteration_times):
        p = Process(target=decode, args=(i, completed_number, success_number, files_number, start_time))
        p.start()
