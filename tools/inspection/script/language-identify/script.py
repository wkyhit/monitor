import websocket
import sys
import time
import os
import json

api_key = sys.argv[1] 
base_url = sys.argv[2]

url = base_url + "/language-identification"
# url = "wss://vk-hk-api.4paradigm.com:31001/api/v1/language-identification"

try:
    ws = websocket.create_connection(url, timeout=20)
    start_tag = {"parameter": {
            "enable_words":False,
    }}

    ws.send(json.dumps(start_tag))
    rec_info = ws.recv()
    print(f"success\tlanguage-identification, recv msg: {rec_info}")
    ws.close()
except Exception as e:
    print(f"fail\tlanguage-identification error - {e}")
    exit(1)