# twilio_msg_demo
Demo of how to use the Twilio service

For SQLite3
1. (optional) Download and install DB Browser https://sqlitebrowser.org/dl/ to view the database

For Twilio:
1. Create a trial account at https://www.twilio.com/; include a phone number that can receive SMS texts
2. Create a new project
3. Make note of your Account SID, Auth Token and My Twilio phone number
4. Verify your registered phone number

For Python:
1. Install python from https://www.python.org/downloads/
2. Clone this repo
3. Open your new project with a command prompt
4. Create a new virtual environment by running `python -m venv venv` (optional but recommended)
5. Download and install all the needed modules by running `pip install -r requirements.txt`
6. Copy .env.sample into .env and update its values from the Twilio section above step 3
7. Run `python test.py`
