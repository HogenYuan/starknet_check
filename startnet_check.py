import requests
import time

headers = {
    'authority': 'starkscan.stellate.sh',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://starkscan.co',
    'referer': 'https://starkscan.co/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

data = {
    "query": "query RowSequencerDataSummaryLatestSequencerStatsQuery {\n  latestSequencerStats {\n    latest {\n      timestamp\n      number_of_transactions_in_backlog\n      oldest_transaction_age\n    }\n  }\n}\n",
    "variables": {}
}

while True:
    response = requests.post('https://starkscan.stellate.sh/', headers=headers, json=data)
    if response.status_code == 200:
        response_dict = response.json()
        number_of_transactions_in_backlog = response_dict["data"]["latestSequencerStats"]["latest"]["number_of_transactions_in_backlog"]
        print("number_of_transactions_in_backlog: ", number_of_transactions_in_backlog)
        if number_of_transactions_in_backlog < 2900:
            print("[!!!!!!!!!!!!!!!!!!!] less than 2900.")
    else:
        print(f"Request failed with status code: {response.status_code}, message: {response.text}")
    time.sleep(10)
