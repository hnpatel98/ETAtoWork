

import googlemaps
from datetime import datetime
from twilio.rest import Client

def get_commute_duration():
    # Define your home and work locations
    home_address = 'YOUR_HOME_ADDRESS'
    work_address = 'YOUR_WORK_ADDRESS'

    # Set up Google Maps API client
    google_maps_api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
    gmaps = googlemaps.Client(key=google_maps_api_key)

    # Get the directions
    directions = gmaps.directions(home_address, work_address, departure_time='now')

    # Get the duration of the first leg
    duration = directions[0]['legs'][0]['duration']['text']
    return duration

def send_twilio_message(message):
    # Set up Twilio client
    twilio_account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    twilio_auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'
    your_phone_number = 'YOUR_PHONE_NUMBER_TO_RECEIVE_TEXTS'
    client = Client(twilio_account_sid, twilio_auth_token)

    client.messages.create(
        to=your_phone_number,
        from_=twilio_phone_number,
        body=message
    )

def main():
    duration = get_commute_duration()
    # Calculate the estimated arrival time
    now = datetime.now()
    arrival_time = (now + duration).strftime('%I:%M %p')

    # Send the estimated commute time
    message = (
    f"Good morning!\n\n"
    f"Estimated commute time from home to work at 9 am: {duration}.\n\n"
    f"Leave now for work at 9am to arrive at approximately {arrival_time}.\n"
    )
    send_twilio_message(message)

if __name__ == "__main__":
    main()