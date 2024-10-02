import requests

# Set your GitLab PAT 
headers = {
    'PRIVATE-TOKEN': '<token>'
}

# Send a request to the GitLab API
response = requests.get('https://gitlab.com/api/v4/groups', headers=headers)

# Check for successful response
if response.status_code == 200:
    groups = response.json()
    for group in groups:
        print(f"Group Name: {group['name']}, Group ID: {group['id']}")
else:
    print(f"Error: {response.status_code}, {response.text}")
