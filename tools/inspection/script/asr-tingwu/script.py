import requests
import sys
import time
import os

base_url = sys.argv[1]
url = f"{base_url}/upload-and-transcribe/"

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "test_16k.wav")

files = {'file': open(file_path, 'rb')}
data = {
    'speaker_count': '0',
    'language': 'en'
}

response = requests.post(url, files=files, data=data)

if response.status_code != 200:
    print(f"fail\tasr-tingwu upload status code is {response.status_code}")
    sys.exit(1)
else:
    try:
        response_json = response.json()
        if 'TaskId' not in response_json:
            print("fail\tasr-tingwu upload: no TaskId in response")
            sys.exit(1)
        elif 'TaskStatus' not in response_json:
            print("fail\tasr-tingwu upload: no TaskStatus in response")
            sys.exit(1)
        elif response_json.get('TaskStatus', "") != 'ONGOING':
            print(f"fail\tasr-tingwu upload: TaskStatus is {response_json['TaskStatus']}")
            sys.exit(1)
        else:
            task_id = response_json['TaskId']
            print("success\tasr-tingwu upload: TaskId:", task_id)
    except Exception as e:
        print(f"fail\tasr-tingwu upload: decode json error: {str(e)}")
        sys.exit(1)

time.sleep(30)


get_url = f"{base_url}/get-result/?task_id={task_id}&enable_words=true"

# 使用 TaskId 进行 GET 请求来获取最终结果
get_response = requests.get(get_url)

if get_response.status_code != 200:
    print(f"fail\tasr-tingwu get res status code is {get_response.status_code}")
else:
    try:
        get_response_json = get_response.json()
        if 'diarization_results' not in get_response_json:
            print("fail\tno asr-tingwu res in response")
        elif not get_response_json.get("diarization_results", {}):
            print("fail\tasr-tingwu res is empty")
        else:
            print("success\tasr-tingwu:", get_response_json.get("diarization_results"))
    except Exception as e:
        print(f"fail\tasr-tingwu decode json error: {str(e)}")