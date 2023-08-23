import json

import requests

PAT_TOKEN = '1/1205311326958856:eafb9ef4d2c125a7af1a0c1d1c4f59a5'
BASE_URL = 'https://app.asana.com/api/1.0'  # The base URL for the Asana API
fields = ['gid', 'name', 'assignee', 'due_on', 'notes']
PROJECT_ID = '1205311401101361'
ASANA_WORKSPACE_ID = '1205311326958866'
ASANA_HEADERS = {
    'Authorization': f'Bearer {PAT_TOKEN}',
    'Content-Type': 'application/json'
}
WEBHOOK_TARGET_URL = 'https://abeb-103-251-226-26.ngrok-free.app/'


def create_asana_webhook():
    url = f'https://app.asana.com/api/1.0/webhooks'
    data = {
        'data': {
            'resource': PROJECT_ID,
            'target': WEBHOOK_TARGET_URL,
            'filters': [
                {
                    'resource_type': 'task',
                    'resource_subtype': 'default_task',
                    'action': 'added'
                }
            ]
        }
    }
    response = requests.post(url, headers=ASANA_HEADERS, data=json.dumps(data))
    if response.status_code == 201:
        print('Webhook created successfully')
    else:
        print('Error creating webhook:', response.text)


# Print the webhook ID
create_asana_webhook()
