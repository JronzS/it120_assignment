from twilio.rest import Client

def send_sms(phone_number, message):
    # Twilio credentials
    account_sid = 'ACaf90cef83cb654308749fec374c96e03'
    auth_token = '13097dde094440db8db39167b799adef'

    client = Client(account_sid, auth_token)
    try:
        client.messages.create(
            to=phone_number,
            from_='+1 775 368 2614',
            body=message
        )
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False
