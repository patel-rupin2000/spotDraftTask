from flask import Flask, request
import requests
from pyairtable import Api

app = Flask(__name__)

ASANA_ACCESS_TOKEN = '1/1205311326958856:eafb9ef4d2c125a7af1a0c1d1c4f59a5'
AIRTABLE_API_KEY = 'pat5K8rBhWnpuBCSw.0c73ab979d95c55a712c1bf9dc9b5cbfb6a1c1d223f3123e6b169b2703151d5f'
AIRTABLE_BASE_ID = 'appOzrDS8NIOl0Udk'
AIRTABLE_TABLE_NAME = 'Asana Task'
ASANA_HEADERS = {
    'Authorization': f'Bearer {ASANA_ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

airtable_api = Api(AIRTABLE_API_KEY)
base = airtable_api.base(AIRTABLE_BASE_ID)
table = base.table(AIRTABLE_TABLE_NAME)


@app.route('/', methods=['POST'])
def webhook():
    x_hook_secret = request.headers.get('X-Hook-Secret')

    # If the X-Hook-Secret header is present, return it in the response
    if x_hook_secret:
        response = app.response_class(status=200)
        response.headers['X-Hook-Secret'] = x_hook_secret
        return response
    data = request.get_json()
    print(data)
    event = data['events'][0]
    if event['resource']['resource_type'] == 'task' and event['action'] == 'added':
        task_id = event['resource']['gid']
        task = get_task_data(task_id)
        create_airtable_record(task)
    return '', 200


def get_task_data(task_gid):
    url = f'https://app.asana.com/api/1.0/tasks/{task_gid}'
    response = requests.get(url, headers=ASANA_HEADERS)
    data = response.json()
    task_data = data.get('data', {})
    return {
        'Task ID': task_data.get('gid'),
        'Name': task_data.get('name'),
        'Assignee': task_data.get('assignee', {}).get('name'),
        'Due Date': task_data.get('due_on'),
        'Description': task_data.get('notes')
    }


def create_airtable_record(task_data):
    print("Task Data \n")
    print(task_data)
    if task_data['Task ID'] is None:
        return
    existing_record = table.all(formula=f"{{Task ID}}='{task_data['Task ID']}'")
    print(existing_record)
    if existing_record:
        table.update(existing_record[0]['id'], task_data)
    else:
        table.create(task_data)


if __name__ == '__main__':
    app.run(debug=True)
