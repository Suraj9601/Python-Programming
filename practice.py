import requests

def get_phone_info(phone_number, api_key):
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=US&format=1"
    
    response = requests.get(url)
    data = response.json()
    
    if data['valid']:
        return data  # Returns all the info like carrier, location, etc.
    else:
        return "Invalid phone number."

# Example usage
api_key = "YOUR_API_KEY"  # Replace with your actual API key
phone_number = "1234567890"  # Phone number without country code
info = get_phone_info(phone_number, api_key)

print(info)
