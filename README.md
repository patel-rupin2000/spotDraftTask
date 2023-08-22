### Demonstration
##### https://youtu.be/s1RQoRr3Vgs

### Problem Statement: 
A marketing agency uses Asana for project management and tasks tracking, and Airtable for storing and analyzing data. The agency is facing challenges in maintaining a seamless workflow between project management and data organization. They cannot manually copy over the data from Asana to Airtable.

### Requirements:

Build out a service in the language/framework of your choice that will integrate between Asana and Airtable.
Whenever a new task is created on Asana, it needs to be copied over to Airtable.
The task created in Asana needs to be stored as a new row in an Airtable table called “Asana Tasks”.
The table needs to have the following columns:
Task ID
Name
Assignee
Due Date
Description


### System Overview

> This code is a Python script that uses the Flask web framework to create a web application. The script uses the `pyairtable` library to interact with an Airtable base, and the `requests` library to interact with the Asana API. The script also uses the `BackgroundScheduler` class from the `apscheduler` library to schedule a recurring job that runs every 5 seconds.

> The script defines several global variables, including `AIRTABLE_BASE_ID`, `AIRTABLE_API_KEY`, and `AIRTABLE_TABLE_NAME`, which are used to configure the connection to the Airtable base. The script also defines a `PAT_TOKEN` variable, which is used to authenticate requests to the Asana API.

> The script defines a `getAssigneeName` function, which takes a user ID as an argument and returns the name of the user with that ID. This function makes a GET request to the Asana API's `/users/{gid}` endpoint, using the `requests` library.

> The script also defines a Flask route for the `/` URL path, which is handled by the `webhook` function. This function makes a GET request to the Asana API's `/projects/{PROJECT_ID}/tasks` endpoint, using the `requests` library, to retrieve a list of tasks for a specific project. The function then processes the list of tasks, adding additional information such as the assignee's name and due date, and stores this information in an Airtable table.

> Finally, the script creates an instance of the `BackgroundScheduler` class and uses it to schedule a recurring job that runs the `webhook` function every 5 seconds. The script also starts the Flask development server when it is run as a standalone script.


### Systematic High Level Actions

1. The necessary libraries are imported, including json, requests, Flask, Api from pyairtable, and BackgroundScheduler from apscheduler.

2. An instance of the Flask app is created.

3. The Airtable base ID, API key, and table name are defined as constants.

4. An instance of the Airtable API is created using the API key, and the base and table are retrieved using the base ID and table name.

5. The Asana personal access token, base URL, fields to retrieve, project ID, and headers for requests are defined as constants.

6. A function getAssigneeName is defined that takes in a user ID and returns the user’s name by making a GET request to the Asana API.

7. A route is defined for the Flask app that responds to GET requests at the root URL.

8. Within this route, a GET request is made to the Asana API to retrieve all tasks for the specified project ID, with only the specified fields included in the response.

9. The tasks are retrieved from the response JSON and an empty list data is initialized.

10. For each task in the list of tasks, the assignee’s name is retrieved using the getAssigneeName function if an assignee exists for the task.

11. A dictionary taskData is created with keys corresponding to the columns in the Airtable table and values corresponding to the task data.

12. The taskData dictionary is appended to the data list.

13. The data list is printed as a JSON string for debugging purposes.

14. For each task data dictionary in the data list, a formula is used to check if a record already exists in the Airtable table with the same Task ID.

15. If a record exists, it is updated with the new task data; otherwise, a new record is created with the task data.

16. The list of tasks is returned as the response for the route.

17. A background scheduler is created and a job is added to run the webhook function every 5 seconds.

18. The scheduler is started and if this script is run as the main program, then Flask app will run in debug mode.


### Pseudocode

1. Import necessary libraries
2. Define global variables for Airtable and Asana API
3. Initialize Airtable API and table
4. Define a function to get the name of an assignee from Asana API using their ID
5. Define a Flask route for the '/' URL path
6. In the route function:

    > a. Make a GET request to Asana API to get tasks for a specific project
    
    > b. Process the list of tasks and add additional information such as assignee's name and due date
    
    > c. Store the processed task information in an Airtable table
7. Create an instance of BackgroundScheduler and schedule a recurring job to run the route function every 5 seconds
8. Start the Flask development server when the script is run as a standalone script

### System Summary 

This code is a Python script that uses the Flask web framework to create a web application. The script uses the `pyairtable` library to interact with an Airtable base, and the `requests` library to interact with the Asana API. The script also uses the `BackgroundScheduler` class from the `apscheduler` library to schedule a recurring job that runs every 5 seconds.

The high level system information:
1. A Flask web server, which hosts the web application and handles incoming requests.
2. An Airtable base, which stores the processed task information.
3. The Asana API, which provides access to Asana data such as tasks and assignees.
4. A scheduler, which runs a recurring job to retrieve tasks from Asana API, process them, and store them in Airtable.

The Flask web server would be responsible for handling incoming requests and routing them to the appropriate route function. In this case, there is only one route defined, for the `/` URL path, which is handled by the `webhook` function.

The `webhook` function would make a GET request to the Asana API's `/projects/{PROJECT_ID}/tasks` endpoint to retrieve a list of tasks for a specific project. The function would then process the list of tasks, adding additional information such as the assignee's name and due date, and store this information in an Airtable table.

The scheduler would be responsible for running the `webhook` function at regular intervals, in this case every 5 seconds. This would ensure that the task information in Airtable is kept up-to-date with the latest data from Asana.


