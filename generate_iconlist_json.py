import os
import json

def generate_json_for_directory(directory, username, repository, branch):
    base_url = f"https://raw.githubusercontent.com/{username}/{repository}/{branch}"
    icons = []

    for filename in os.listdir(directory):
        if filename.endswith('.svg'):
            file_path = os.path.join(directory, filename).replace('\\', '/')
            icon_info = {
                "name": filename,
            }
            icons.append(icon_info)

    with open(os.path.join(directory, 'iconlist.json'), 'w') as json_file:
        json.dump(icons, json_file, indent=4)

def main():
    username = 'abhishekshankr'
    repository = 'AIcons'
    branch = 'update-github-actions'

    for folder in ['Icons/Fill', 'Icons/Stroke']:
        generate_json_for_directory(folder, username, repository, branch)

if __name__ == "__main__":
    main()