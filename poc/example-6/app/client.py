import requests

# Define the URL for the create_item API
url = "http://192.168.39.56:30000/items/"

# Create a sample item payload
item_payload = {
    "name": "Example Item",
    "price": 9.99
}

# Send a POST request to create the item
response = requests.post(url, json=item_payload)

# Check the response status code
if response.status_code == 200:
    # Item created successfully
    print("Item created successfully")
else:
    # Error occurred
    print("Error creating item:", response.text)