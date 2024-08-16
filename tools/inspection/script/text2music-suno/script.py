import requests
import sys

api_key = sys.argv[1] 
base_url = sys.argv[2]

# 拼接URL
url = base_url + "/generate/description-mode"

json_data = {
    "gpt_description_prompt":"citypop and trap slap guitar experimental flamenco math rock with layered harmonics, songs by japanese",
    "make_instrumental": False,
    "wait_audio": True
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json=json_data, timeout=180)
if response.status_code != 200:
    print(f"fail\ttext2music-suno status code is {response.status_code}")
else:
    try:
        response_json = response.json()
        if (not response_json):
            print(f"fail\ttext2music-suno response is empty")
        elif not isinstance(response_json, list):
            print(f"fail\ttext2music-suno response is not a list")
        elif len(response_json) != 2:
            print(f"fail\ttext2music-suno response length is not 2")
        print(f"success\ttext2music-suno response: {response_json[0]}")
    except Exception as e:
        print(f"fail\ttext2music-suno decode json error: {e}")