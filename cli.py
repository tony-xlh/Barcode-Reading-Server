from dbr import *
error = BarcodeReader.init_license("DLS2eyJoYW5kc2hha2VDb2RlIjoiMjAwMDAxLTE2NDk4Mjk3OTI2MzUiLCJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInNlc3Npb25QYXNzd29yZCI6IndTcGR6Vm05WDJrcEQ5YUoifQ==")
if error[0] != EnumErrorCode.DBR_OK:
    print("License error: "+ error[1])
    
reader = BarcodeReader()

try:
   image_path = r"./AllSupportedBarcodeTypes.png"
   results = reader.decode_file(image_path)
   if results != None:
      i = 1
      for result in results:
         print("{}. {}: {}".format(i, result.barcode_format_string, result.barcode_text))
         i = i+1
except BarcodeReaderError as bre:
   print(bre)