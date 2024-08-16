import websocket
import sys
import time
import os
import json

api_key = sys.argv[1] 
base_url = sys.argv[2]

url = base_url + "/aggregation/recognition"

try:
    ws = websocket.create_connection(url, timeout=20)
    start_tag = {
        "parameter": {
            "lang": "en",
            "enable_words":True,
            "enable_diarization": True,
            "speaker_count": 0
        }
    }
    

    ws.send(json.dumps(start_tag))
    rec_info = ws.recv()
    print(f"success\tai-gateway-recognition, recv msg: {rec_info}")
    ws.close()
except Exception as e:
    print(f"fail\tai-gateway-recognition error - {e}")
    exit(1)


url2 = base_url + "/aggregation/interpretation"
try:
    ws = websocket.create_connection(url2, timeout=20)
    start_tag = {
        "parameter": {
            "asr": {
            "lang": "zh",
            "enable_words":True,
            },
            "trans": {
            "to": "en"
            },
            "tts": {
            "voice_name": "default"
            }
        }
    }
    
    ws.send(json.dumps(start_tag))
    rec_info = ws.recv()
    print(f"success\tai-gateway-interpretation, recv msg: {rec_info}")
    ws.close()
except Exception as e:
    print(f"fail\tai-gateway-interpretation error - {e}")
    exit(1)