from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid='AC079d976786e86ad8557a40d499a3188f'
auth_token='eb25967336ed730bdbcedbd68d19bf0b'

# Initialize Twilio client
client = Client(account_sid, auth_token)

def send_sms(to_number, message):
    try:
        # Send message using Twilio client
        message = client.messages.create(
            body=message,
            from_='+12512921736',  # Your Twilio phone number
            to=to_number  # The recipient's phone number
        )
        print("Message sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send message: {e}")
        return False

# Example usage:
to_number = '+919967210145'  # Replace with the recipient's phone number
message = 'This is a test message from Python!'
send_sms(to_number, message)
