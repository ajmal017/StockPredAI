from download_utils import *
from constants import *

print("Downloading datasets...")
download_file(BASE_URL, AMZN_ENDPOINT + ".zip", STOCKS_LOCATION)
print(" - AMZN download complete.")
download_file(BASE_URL, APPL_ENDPOINT + ".zip", STOCKS_LOCATION)
print(" - APPL download complete.")
download_file(BASE_URL, INTC_ENDPOINT + ".zip", STOCKS_LOCATION)
print(" - INTC download complete.")

download_file(BASE_URL, EUR_USD_ENDPOINT + ".zip", FOREX_LOCATION)
print(" - EUR_USD download complete.")
download_file(BASE_URL, SPX_ENDPOINT + ".zip", INDEX_LOCATION)
print(" - SPX download complete.")

print("Unzipping datasets...")
unzip_file_and_delete(STOCKS_LOCATION + AMZN_ENDPOINT + ".zip")
unzip_file_and_delete(STOCKS_LOCATION + APPL_ENDPOINT + ".zip")
unzip_file_and_delete(STOCKS_LOCATION + INTC_ENDPOINT + ".zip")

unzip_file_and_delete(FOREX_LOCATION + EUR_USD_ENDPOINT + ".zip")
unzip_file_and_delete(INDEX_LOCATION + SPX_ENDPOINT + ".zip")
print("Unzipping complete.")
