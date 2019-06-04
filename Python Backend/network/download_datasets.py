from network_utils import *

BASE_URL = "https://s3.us-east-2.amazonaws.com/frd001/"

print("Downloading datasets...")
download_file(BASE_URL + "EURUSD_5MIN_99rasp.zip",
              "datasets/forex/EURUSD_5MIN_99rasp.zip")
download_file(BASE_URL + "AMZN_1MIN_ze7avh.zip",
              "datasets/stock/AMZN_1MIN_ze7avh.zip")
download_file(BASE_URL + "SPX_1MIN_8v96zt.zip",
              "datasets/index/SPX_1MIN_8v96zt.zip")

print("Unzipping datasets...")
unzip_file_and_delete("datasets/stock/AMZN_1MIN_ze7avh.zip")
unzip_file_and_delete("datasets/forex/EURUSD_5MIN_99rasp.zip")
unzip_file_and_delete("datasets/index/SPX_1MIN_8v96zt.zip")
print("Unzipping complete.")
