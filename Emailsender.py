from mailjet_rest import Client

def send_email(api_key, api_secret, sender_email, receiver_email, subject, message):
    try:
        # Create a Mailjet client using your API key and secret
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')

        # Compose the email
        data = {
            'Messages': [
                {
                    'From': {
                        'Email': sender_email,
                    },
                    'To': [
                        {
                            'Email': receiver_email,
                        }
                    ],
                    'Subject': subject,
                    'TextPart': message,
                }
            ]
        }

        # Send the email using the Mailjet API
        response = mailjet.send.create(data=data)

        if response.status_code == 200:
            print("Email sent successfully!")
        else:
            print(f"Failed to send email. Status Code: {response.status_code}, Response: {response.json()}")

    except Exception as e:
        print("An error occurred while sending the email:", str(e))

# Replace the following variables with your Mailjet API key and secret, and the email details
mailjet_api_key = '2879f4a5d4fc268a8777a0f5951629dc'
mailjet_api_secret = 'e99dc68b55483a6c91f3e523b7ad2fd4'
sender_email = 'manicdon7@gmail.com'
receiver_email = 'manikandan05082003@gmail.com'
subject = 'Automated Email from Python using Mailjet'
message = 'This is an automated email sent from Python using Mailjet. Have a nice day!'

# Call the function to send the email
send_email(mailjet_api_key, mailjet_api_secret, sender_email, receiver_email, subject, message)
