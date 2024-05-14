import requests

# Base URL
base_url = "https://example.com"

# Create a session object
s = requests.Session()

# Function to send a POST request
def send_post_request(endpoint, data, headers=None):
    url = f"{base_url}/{endpoint}"
    response = s.post(url, data=data, headers=headers)
    return response.json()

# Function to send a GET request
def send_get_request(endpoint, token=None):
    url = f"{base_url}/{endpoint}"
    if token:
        headers = {'Authorization': 'Bearer ' + token}
        response = s.get(url, headers=headers)
    else:
        response = s.get(url)
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    if response.text:  # Check if the response is not empty
        return response.json()
    else:
        return None  # or return an appropriate value
      
def send_post_request_raw(endpoint, data, headers=None):
    url = f"{base_url}/{endpoint}"
    response = s.post(url, data=data, headers=headers)
    return response.text
# Your token
token = "Admin token"

# Retrieve the session of the specific user
user_id = 2  # ID of the user you want to retrieve
user_session = send_get_request(f"api/session/{user_id}", token)
print("User session:", user_session)

user_session = send_get_request(f"api/session")
print("User session:", user_session)


# Create a new session with a specific token
data = {'expiration': '2024-05-16T22:00:00.000Z'}
new_token_raw = send_post_request_raw(f'api/session/token', data)

print("New token (raw):", new_token_raw)
s.cookies.clear()


s = requests.Session()

user_session = send_get_request(f"api/session?token={new_token_raw}")
print("User session:", user_session)

s.cookies.clear()
