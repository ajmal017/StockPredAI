from download_utils import *
from constants import *
'''
print("Downloading datasets...")
download_file(BASE_URL, AMZN_ENDPOINT + ".zip", STOCKS_LOCATION)
print(" - AMZN download complete.")
download_file(BASE_URL, APPL_ENDPOINT + ".zip", STOCKS_LOCATION)
print(" - APPL download complete.")
download_file(BASE_URL, INTC_ENDPOINT + ".zip", STOCKS_LOCATION)
print(" - INTC download complete.")
'''
download_file(BASE_URL, JPM_ENDPOINT + ".zip", STOCKS_LOCATION)
print(" - JPM download complete.")
download_file(BASE_URL, BAC_ENDPOINT + ".zip", STOCKS_LOCATION)
print(" - BAC download complete.")

print("Unzipping datasets...")
'''
unzip_file_and_delete(STOCKS_LOCATION + AMZN_ENDPOINT + ".zip")
unzip_file_and_delete(STOCKS_LOCATION + APPL_ENDPOINT + ".zip")
unzip_file_and_delete(STOCKS_LOCATION + INTC_ENDPOINT + ".zip")
'''
unzip_file_and_delete(STOCKS_LOCATION + JPM_ENDPOINT + ".zip")
unzip_file_and_delete(STOCKS_LOCATION + BAC_ENDPOINT + ".zip")
print("Unzipping complete.")
