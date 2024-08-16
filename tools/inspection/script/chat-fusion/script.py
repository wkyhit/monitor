import requests
import json
import sys

api_key = sys.argv[1]
base_url = sys.argv[2]

# 拼接URL
url1 = base_url + "/api/v1/chat/completions"
url2 = base_url + "/api/v1/tools/chat/completions"

# url1 = "http://127.0.0.1:8000/api/v1/chat/completions"
# url2 = "http://127.0.0.1:8000/api/v1/tools/chat/completions"


json_data = {
    "stream": False,
    "messages": [
        {
            "role": "user",
            "content": "世界最深的湖泊是什么？"
        }
    ],
    "temperature": 1,
    "top_p": 1,
    "n": 1,
    "max_tokens": 4096
}

json_data_tools = {
    "stream": False,
    "messages": [
        {
            "role": "user",
            "content": "2028奥运会在哪"
        }
    ],
    "temperature": 1,
    "top_p": 1,
    "n": 1,
    "max_tokens": 4096
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url1, headers=headers, json=json_data)
if response.status_code != 200:
    print(f"fail\tllm status code is {response.status_code}")
else:
    try:
        response_json = response.json()
        if "choices" not in response_json or len(response_json["choices"]) == 0:
            print(f"fail\tllm no response or empty response")
        else:
            response_text = response_json["choices"][0]["message"]["content"]
            if not response_text:
                print(f"fail\tllm no content in response")
            else:
                print(f"success\tllm response received: {response_text}")
    except Exception as e:
        print(f"fail\tllm decode json error: {e}")


response = requests.post(url2, headers=headers, json=json_data_tools)
if response.status_code != 200:
    print(f"fail\tllm tools status code is {response.status_code}")
else:
    try:
        response_json = response.json()
        if "choices" not in response_json or len(response_json["choices"]) == 0:
            print(f"fail\tllm tools no response or empty response")
        else:
            response_text = response_json["choices"][0]["message"]["content"]
            if not response_text:
                print(f"fail\tllm tools no content in response")
            else:
                print(f"success\tllm tools response received: {response_text}")
    except Exception as e:
        print(f"fail\tllm tools decode json error: {e}")