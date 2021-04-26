# Send-SMS-Automatically
***
Using twilio and REST API to send messages automatically using python
&&&

Install the Library
The easiest way to install the library is from PyPi using pip, a package manager for Python. Simply run this in the terminal:
***
pip install twilio
***
If you get a pip: command not found error, you can also use easy_install. Run this in your terminal:
***
easy_install twilio
***
Manual Installation
Or, you can download the source code (ZIP) for twilio-python, and then install the library by running:

python setup.py install
***
in the folder containing the twilio-python library.

"Permission Denied"
If the command line gives you a big long error message that says Permission Denied in the middle of it, try running the above commands with sudo (e.g. sudo pip install twilio).

Test Your Installation
Try sending yourself an SMS message. Save the following code sample to your computer with a text editor. Be sure to update the account_sid, auth_token, and from_ phone number with values from your Twilio account. The to phone number can be your own mobile phone.

Python Helper Library SMS Test
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309", 
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
Save the file as send_sms.py. In the terminal, cd to the directory containing the file you just saved then run:

python send_sms.py
You should receive the text message on your phone.

It's okay to hardcode your credentials when testing locally, but you should use environment variables to keep them secret before committing any code or deploying to production. Check out how to set environment variables for more information.

Using this Library
Authenticate Client
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)
Create a New Record
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+14155551212",
    from_="+15017250604",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)
Get Existing Record
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

call = client.calls.get("CA42ed11f93dc08b952027ffbc406d0868")
print(call.to)
Iterate Through Records
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

for sms in client.messages.list():
    print(sms.to)
The library automatically handles paging for you. Collections, such as calls and messages, have list and stream methods that page under the hood. With both list and stream, you can specify the number of records you want to receive (limit) and the maximum size you want each page fetch to be (page_size). The library will then handle the task for you.

list eagerly fetches all records and returns them as a list, whereas stream returns an iterator and lazily retrieves pages of records as you iterate over the collection. You can also page manually using the page method.

For more information about these methods, view the auto-generated library docs.
