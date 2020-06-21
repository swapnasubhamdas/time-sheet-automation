from twilio.rest import Client 
 
account_sid = 'AC743f543a96f4f7cc2288855483604419' 
auth_token = '50836c38e0fb6d0a3fcd168dac78a1c1' 
client = Client(account_sid, auth_token) 

def time_sheet_reminder():

    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Please Fill Up Your Sheet Immediately',      
                                  to='whatsapp:+918420839807' 
                                  ) 
    print(message.sid)