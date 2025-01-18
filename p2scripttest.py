import requests

EC2_DNS = ''
API_URL = f'http://{EC2_DNS}:5000'


def test_get_token(user_id):
    response = requests.post(f"{API_URL}/api/token",headers={"User-ID": user_id})
    print("Get Token Response:", response.json())
    return response.json()

#def get_metrics():

def create_item(user_id, token, item_data):
    """Function to create an item using the provided user_id and token."""
    headers = {
        "User-ID": user_id,
        "Token": token
    }
    
    response = requests.post(f"{API_URL}/api/items", headers=headers, json=item_data)
    
    if response.status_code == 201:
        print("Item Created Successfully:", response.json())
    else:
        print("Failed to Create Item:", response.json())




# Example usage
token = test_get_token("isaac-client")  # Get token for the user
item_data = {
    "name": "New Item-isaac",
    "description": "This is a new item made by isaac"
}
create_item("isaac-client", token["token"], item_data)
