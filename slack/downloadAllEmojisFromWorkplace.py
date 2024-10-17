import json
import os
import pathlib
from urllib.request import urlretrieve

EMOJI_LIST_FOLDER_PATH = './emoji-files'
EMOJI_LIST_RESULT_FOLDER_PATH = './emojis'


def download_emojis_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    emojis = data['emoji']
    print(f'\tDownloading {len(emojis)} custom emojis')

    for emoji in emojis:
        if emoji['is_alias'] == 0:
            file_type = pathlib.Path(emoji['url']).suffix
            urlretrieve(emoji['url'], f'{EMOJI_LIST_RESULT_FOLDER_PATH}/{emoji['name']}{file_type}')

    return len(emojis)


emoji_list_folder = os.listdir(EMOJI_LIST_FOLDER_PATH)
emoji_list_folder.remove('.gitignore')

if len(emoji_list_folder) == 0:
    exit(f'Add JSON files containing the emojis from Slack to the folder called "{EMOJI_LIST_FOLDER_PATH}"')

print(f'Found {len(emoji_list_folder)} files in folder "{EMOJI_LIST_FOLDER_PATH}"\n')
if not os.path.exists(EMOJI_LIST_RESULT_FOLDER_PATH):
    os.makedirs(EMOJI_LIST_RESULT_FOLDER_PATH)

number_of_emojis = 0
for file_name in emoji_list_folder:
    print(f'Downloading emojis from file "{file_name}"')
    number_of_emojis += download_emojis_from_file(f'{EMOJI_LIST_FOLDER_PATH}/{file_name}')
print(
    f'\nFinished downloading {number_of_emojis} custom emojis. They can be found in "{EMOJI_LIST_RESULT_FOLDER_PATH}"')
