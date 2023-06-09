import time

class AggregatedReader():

    def __init__(self, engine="dynamsoft"):
        self.reader = None
        self.engine = engine
        self.init_reader()
        
    def init_reader(self):
        if self.engine == "dynamsoft" or self.engine == "":
            from barcode_reader.dynamsoft import DynamsoftBarcodeReader
            self.reader = DynamsoftBarcodeReader()

    def decode_bytes(self, file_bytes):
        start_time = time.time()
        results = self.reader.decode_bytes(file_bytes)
        end_time = time.time()
        elapsedTime = int((end_time - start_time) * 1000)
        if "elapsedTime" not in results:
            results["elapsedTime"] = elapsedTime
        return results
    
    def decode_file(self, file_path):
        start_time = time.time()
        results = self.reader.decode_file(file_path)
        end_time = time.time()
        elapsedTime = int((end_time - start_time) * 1000)
        if "elapsedTime" not in results:
            results["elapsedTime"] = elapsedTime
        return results
        