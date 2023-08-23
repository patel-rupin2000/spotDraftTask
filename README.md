### Demonstration
##### https://www.youtube.com/watch?v=GYJj45hVQZk

### Problem Statement: 
A marketing agency uses Asana for project management and tasks tracking, and Airtable for storing and analyzing data. The agency is facing challenges in maintaining a seamless workflow between project management and data organization. They cannot manually copy over the data from Asana to Airtable.

### Requirements:

Build out a service in the language/framework of your choice that will integrate between Asana and Airtable.
Whenever a new task is created on Asana, it needs to be copied over to Airtable.
The task created in Asana needs to be stored as a new row in an Airtable table called “Asana Tasks”.
The table needs to have the following columns:
- Task ID

- Name

- Assignee

- Due Date

- Description


### System Overview

Imports:

    Flask: A micro web framework in Python for building web applications.
    requests: A library for making HTTP requests to external resources.
    pyairtable.Api: A library to interact with the Airtable API.

Flask Application Setup:

    An instance of the Flask application is created.
    Constants are defined for Asana API access and Airtable configuration.

Webhook Endpoint:

    A single endpoint '/' is defined to handle incoming POST requests.
    The webhook() function is executed upon receiving a POST request.

X-Hook-Secret Handling:

    The X-Hook-Secret header from the request is extracted.
    If this header is present, the endpoint returns a response with a 200 status code and sets the X-Hook-Secret header in the response. This is done to acknowledge the webhook and validate the endpoint.

Task Data Processing:

    The incoming JSON payload from the POST request is retrieved.
    The first event within the payload is extracted.
    If the event corresponds to a newly added task, the task's data is fetched using the get_task_data() function.

Fetching Task Data from Asana:

    The get_task_data() function sends an HTTP GET request to the Asana API using the provided task ID.
    The task data is extracted from the JSON response, including the task's ID, name, assignee, due date, and description.
    The extracted data is returned as a dictionary.

Airtable Record Handling:

    The create_airtable_record() function is responsible for handling Airtable records.
    It takes the task data dictionary as an argument.
    If the task ID is not present in the task data, the function returns early.
    The function checks if a record with the same task ID already exists in the Airtable table.
    If an existing record is found, it is updated with the new task data.
    If no existing record is found, a new record is created in the Airtable table with the task data.

Flask Response:

    After processing the data and performing any necessary actions, the endpoint returns an empty response with a 200 status code.
    In summary, this Flask application acts as a webhook endpoint to receive new task events from Asana. It processes the received task data, fetches additional details from the Asana API, and then stores the processed task data in an Airtable database. This system can be used to keep track of new tasks added to Asana and maintain a synchronized record in an Airtable table.

### Establishing the WebHook Python Script Summary
Imports:

    json: The JSON module for working with JSON data.
    requests: A library for making HTTP requests to external resources.
Configuration:

    Constants are defined for the Personal Access Token (PAT) used to authenticate with the Asana API, the base URL for the API, a list of field names, the project ID, workspace ID, headers for API requests, and the target URL for the webhook.

Webhook Creation:

    The create_asana_webhook() function is defined to create a webhook in Asana.
    The URL for creating webhooks is constructed using the base URL.
    The data for creating the webhook is structured in a dictionary.

This data includes:

    resource: The project ID to which the webhook will be attached.
    target: The URL where webhook notifications will be sent.
    filters: A list of filters specifying the conditions under which the webhook will be triggered. In this case, the filter indicates that the webhook should be triggered when a new task is added to the project.
    An HTTP POST request is made to the Asana API to create the webhook. The json.dumps() function is used to convert the data to JSON format for the request body.
    If the response status code is 201 (Created), a success message is printed. Otherwise, an error message with the response text is printed.

Webhook Initialization:

    The create_asana_webhook() function is called to create the webhook.

Output:

    Depending on the response from the Asana API, either a success message ("Webhook created successfully") or an error message ("Error creating webhook") is printed.

The Python script sets up a webhook in Asana to notify the provided target URL whenever a new task is added to a specific project. This allows external systems to receive real-time notifications about task additions in the specified project and take further actions based on these notifications.


### Algorithm for Flask API Service

1. **Initialize Application and Configuration:**
   - Create a Flask application instance.
   - Set constants for Asana access token, Airtable API key, base ID, table name, and Asana headers.
   - Create an instance of the Airtable API with the provided API key.
   - Obtain a reference to the specific table within the Airtable base.

2. **Define Webhook Route:**
   - Define a route within the Flask application to handle incoming POST requests.
   - Define the `webhook()` function to handle the webhook logic.

3. **Handle X-Hook-Secret Header:**
   - Extract the `X-Hook-Secret` header from the incoming request.
   - If the header is present:
     - Create a response with a 200 status code.
     - Set the `X-Hook-Secret` header in the response.
     - Return the response.

4. **Process Incoming Data:**
   - Retrieve the JSON data from the incoming request.
   - Extract the first event from the events list in the data.
   - Check if the event corresponds to an added task.

5. **Fetch Task Data from Asana API:**
   - Define the `get_task_data(task_gid)` function.
   - Construct the URL for the Asana API request using the task ID.
   - Send an HTTP GET request to the Asana API with the constructed URL and headers.
   - Parse the JSON response and extract relevant task data, including ID, name, assignee, due date, and description.
   - Return the extracted task data as a dictionary.

6. **Create or Update Airtable Record:**
   - Define the `create_airtable_record(task_data)` function.
   - Print the task data for debugging purposes.
   - Check if the 'Task ID' field is present in the task data dictionary.
   - If the 'Task ID' is not present, return early.
   - Query the Airtable table for an existing record with a formula matching the 'Task ID'.
   - If an existing record is found:
     - Update the existing record with the new task data.
   - If no existing record is found:
     - Create a new record in the Airtable table using the task data.

7. **Start the Application:**
   - Check if the script is being run as the main module.
   - If it is, start the Flask application in debug mode.

The code primarily revolves around setting up a Flask server to receive webhook notifications from Asana, fetching task details from the Asana API, and storing the information in an Airtable table. The described algorithm outlines the logical steps involved in each part of the code's functionality.

### Algorithm for Establish Webhook Python Script

1. **Configuration:**
   - Set constants for Personal Access Token (PAT), base URL for the Asana API, desired fields, project ID, workspace ID, headers for API requests, and target URL for the webhook.

2. **Webhook Creation:**
   - Define the `create_asana_webhook()` function.
   - Construct the URL for creating webhooks using the base URL.
   - Define the data dictionary for creating the webhook:
      - 'resource': Set to the specified project ID.
      - 'target': Set to the provided target URL where webhook notifications will be sent.
      - 'filters': A list containing a dictionary with filter criteria:
         - 'resource_type': Set to 'task'.
         - 'resource_subtype': Set to 'default_task'.
         - 'action': Set to 'added'.
   - Send an HTTP POST request to the Asana API to create the webhook using the constructed URL, headers, and JSON-encoded data.
   - Check the response status code:
      - If the status code is 201 (Created), print "Webhook created successfully".
      - Otherwise, print "Error creating webhook:" followed by the response text.

3. **Webhook Initialization:**
   - Call the `create_asana_webhook()` function to create the webhook.

The code sets up a webhook in Asana to trigger notifications to a specified URL when new tasks are added to a specific project. The algorithm outlines the steps to configure and create the webhook using the Asana API.