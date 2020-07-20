from twilio.rest import Client 
 
account_sid = 'AC823ecf37b0382860040e057b4f9997b8' 
auth_token = '1d07bad206dfd06b7a5452c17e2e5194' 
client = Client(account_sid, auth_token) 

def send():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+919080586183' 
                          ) 
    print(message.sid)