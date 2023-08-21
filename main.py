import requests
from flask import Flask
from pyairtable import Api
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

AIRTABLE_BASE_ID = 'appOzrDS8NIOl0Udk'
AIRTABLE_API_KEY = 'pat5K8rBhWnpuBCSw.0c73ab979d95c55a712c1bf9dc9b5cbfb6a1c1d223f3123e6b169b2703151d5f'
AIRTABLE_TABLE_NAME = 'Asana Task'
airtable_api = Api(AIRTABLE_API_KEY)
base = airtable_api.base(AIRTABLE_BASE_ID)
table = base.table(AIRTABLE_TABLE_NAME)

PAT_TOKEN = '1/1205311326958856:3565d8906e0d21702f989689b58a2cef'
BASE_URL = 'https://app.asana.com/api/1.0'  # The base URL for the Asana API
fields = ['gid', 'name', 'assignee', 'due_on', 'notes']
PROJECT_ID = '1205311401101361'
HEADERS = {
    'Authorization': f'Bearer {PAT_TOKEN}'
}


def getAssigneeName(gid):
    response = requests.get(f'{BASE_URL}/users/{gid}', headers=HEADERS)
    user = response.json()['data']['name']
    return user


@app.route('/', methods=['GET'])
def webhook():
    response = requests.get(f'{BASE_URL}/projects/{PROJECT_ID}/tasks?opt_fields={",".join(fields)}', headers=HEADERS)
    tasks = response.json()['data']
    data = []
    for task in tasks:
        task['assignee']['name'] = getAssigneeName(task['assignee']['gid'] if task['assignee'] else 'None')
        taskData = {
            "Task ID": task['gid'],
            "Name": task['name'],
            "Assignee": task['assignee']['name'],
            "Due Date": task['due_on'],
            "Description": task['notes']
        }
        data.append(taskData)
    # print(json.dumps(data))
    for task_data in data:
        existing_record = table.all(formula=f"{{Task ID}}='{task_data['Task ID']}'")
        print(existing_record)
        if existing_record:
            table.update(existing_record[0]['id'], task_data)
        else:
            table.create(task_data)

    return tasks


scheduler = BackgroundScheduler()
scheduler.add_job(webhook, 'interval', seconds=5)
scheduler.start()
if __name__ == '__main__':
    app.run(debug=True)
