import requests
import getpass
import os
import json
import re
import base64

def create_github_repo(token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Ask for repository name and sanitize it
    repo_name = input("Enter the name for your new repository: ")
    # Replace spaces with hyphens and remove special characters
    repo_name = re.sub(r'[^a-zA-Z0-9-]', '-', repo_name).strip('-')
    print(f"Using repository name: {repo_name}")
    
    # Create repository
    data = {
        'name': repo_name,
        'private': False,
        'description': 'Repository created via script'
    }
    
    response = requests.post(
        'https://api.github.com/user/repos',
        headers=headers,
        json=data
    )
    
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
        return repo_name
    else:
        print(f"Failed to create repository. Status code: {response.status_code}")
        print(f"Error message: {response.json()}")
        return None

def upload_file(token, repo_name):
    with open('SitekeyRecaptch.js', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Get GitHub username
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    user_response = requests.get('https://api.github.com/user', headers=headers)
    if user_response.status_code != 200:
        print("Failed to get user information")
        return
    
    username = user_response.json()['login']
    
    # Create or update file in repository
    url = f'https://api.github.com/repos/{username}/{repo_name}/contents/SitekeyRecaptch.js'
    
    # Properly encode content in base64
    content_bytes = content.encode('utf-8')
    content_base64 = base64.b64encode(content_bytes).decode('utf-8')
    
    data = {
        'message': 'Upload SitekeyRecaptch.js',
        'content': content_base64
    }
    
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code in [201, 200]:
        print(f"File uploaded successfully!")
        print(f"You can find your file at: https://github.com/{username}/{repo_name}")
    else:
        print(f"Failed to upload file. Status code: {response.status_code}")
        print(f"Error message: {response.json()}")

def main():
    print("Please enter your GitHub Personal Access Token:")
    token = getpass.getpass()
    
    # Create new repository
    repo_name = create_github_repo(token)
    if repo_name:
        # Upload file to the new repository
        upload_file(token, repo_name)

if __name__ == "__main__":
    main()