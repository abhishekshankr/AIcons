import os
import json

def generate_json_for_directory(directory, username, repository, branch):
    base_url = f"https://github.com/{username}/{repository}/blob/{branch}"
    icons = []

    for filename in os.listdir(directory):
        if filename.endswith('.svg'):
            file_path = os.path.join(directory, filename)
            icon_info = {
                "name": filename,
                "download_url": f"{base_url}/{file_path}"
            }
            icons.append(icon_info)

    with open(os.path.join(directory, 'icons.json'), 'w') as json_file:
        json.dump(icons, json_file, indent=4)

def main():
    username = 'abhishekshankr'
    repository = 'AIcons'
    branch = 'github-actions-test'

    for folder in ['Icons/Fill', 'Icons/Stroke']:
        generate_json_for_directory(folder, username, repository, branch)

if __name__ == "__main__":
    main()