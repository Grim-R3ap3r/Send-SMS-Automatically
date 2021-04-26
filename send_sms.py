from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="recipientphonenumber", 
    #format +91(phonenumber)
    from_="urphonenumber",
    #should be added(purchase) in twilio or else it wont work
    body="hello frnd")

print(message.sid)
