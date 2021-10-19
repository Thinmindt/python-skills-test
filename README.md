# python-skills-test
Basic server layout to evaluate interviewee's skills

## Install
Pull the repository on to your computer. You may use whichever IDE you prefer to conduct the test.
Make sure that you have a recent version of Python (>=3.7 preferred). 

Inside the project directory, run: 
```
python -m venv venv
```
Then, if you are on Linux or Mac, activate the virtual environment with:
```
source venv/bin/activate
```
Or if you are using Windows, activate it with:
```
.\venv\scripts\activate.exe
```
Whichever OS you are running, the next step is the same:
```
pip install -r requirements.txt
```

## Running the Server
Now that you have a virtual enviroment activated with our dependencies installed, you may run the server with:
```
python main.py
```

## Running the Test

Open another shell window, and activate the virtual environment with the command listed above.

Then you may navigate to the ./mockClient directory and run send_request.py. This sends a command intended to update floor_map.json. It is your job to make sure this happens. 

The floor map is a json object where each top level property is a row, second level property is a column, and the third level is a gridpoint. Each gridpoint has a number of properties, including datetimeUpdated. We want to only update each gridpoint where the datetimeUpdated field in the client's request is newer than the one in floor_map.json.

Let me know if you have any questions. This is intended as a test of your Python and reasoning skills, so let me know if anything stands in the way of that. 