-- From python we are trying to create a new databse ,schema and one table

# Step 1: Install the Snowflake Python Connector

Open PyCharm
create new project python for Snowflake
create new file with .py extention in pycharm name it as python snowflake test
Inside the python packages install the snowflake-connector-python package.
or 
Open the Terminal in PyCharm (at the bottom left of the PyCharm window).

Run the following command to install the Snowflake Python connector
  
pip install snowflake-connector-python

# Step 2: Set Up Snowflake Credentials
We will need the following credentials to connect to Snowflake
Username
Password
Account identifier

# Step 3: Write the Python Code

Open PyCharm inside a new Python file with name python_snowflake_test

Copy and paste the following code into the script, making sure to replace the placeholders with your actual credentials.

import snowflake.connector as sf
  
connection = sf.connect(user = 'your user name',password = 'your password',account ='your account identifier')
connection.cursor().execute("create or replace database mydb")
connection.cursor().execute("create or replace schema myschema")
connection.cursor().execute("create or replace table mytable (ID Number)")
connection.close()


