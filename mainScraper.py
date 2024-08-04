# import re
# from telethon.sync import TelegramClient
# import datetime
# import json
# # from ouo.api import Ouo

# api_id = 20183432
# api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'
# chats = []
# # ouo = Ouo("1QitLQLa")

# # Read chat IDs from the JSON file
# with open("data/chat_data.json", "r") as chat_file:
#     chat_data = json.load(chat_file)
#     for chat in chat_data:
#         chats.append(chat['id'])
#     print("fetched chat id")
    

# print("Initiating emergency self destroy protocol...")
# with open("data/main_messages1.json", "w") as test_file:
#     test_file.truncate(0)
# client = TelegramClient("test", api_id, api_hash)

# data = []
# unique_links = set()

# try:
#     client.start()
#     today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  # Get today's date with timezone-naive
#     for chat_id in chats:
#         for message in client.iter_messages(chat_id, reverse=True):
#             message_date = message.date.replace(tzinfo=None)  # Convert message date to timezone-naive
#             if today - datetime.timedelta(days=5) <= message_date < today:  # Check if message date is within the last 5 days
#                 if message.text:
#                     links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
#                     for link in links:
#                         if link not in unique_links:  # Check if the link is not already added
#                             unique_links.add(link)
#                             links_str = ','.join(links)
#                             data.append({'group': chat_id, 'text': message.text, 'date': str(message_date), 'links': links_str})

# finally:
#     client.disconnect()

# # Write data to JSON file
# with open("D:/Projects/JobFinder/backend/data/main_messages1.json", "w") as json_file:
#     json.dump(data, json_file, indent=4)
#     print("New Instance of Robo created ")


# import re
# from telethon.sync import TelegramClient
# import datetime
# import json
# import subprocess
# import requests
# api_id = 20183432
# api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'
# chats = []

# import requests

# def link_shorten(link):
#     # Replace 'yourdestinationlink.com' with the actual link to be shortened
#     api_url = f"http://ouo.io/api/1QitLQLa?s={link}"
    
#     # Make the GET request to the API
#     response = requests.get(api_url)
#     print(response.text.strip())
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Return the shortened link
#         return response.text.strip()
#     else:
#         # Return an error message if the request was not successful
#         return f"Error: Unable to shorten the link, status code {response.status_code}"

# # Example usage:
# # original_link = "https://www.example.com"
# # shortened_link = link_shorten(original_link)
# # print(f"Shortened link: {shortened_link}")

# def ordinal(number):
#     if 10 <= number % 100 <= 20:
#         suffix = 'th'
#     else:
#         suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
#     return str(number) + suffix
# # Read chat IDs from the JSON file
# with open("D:\Projects\JobFinder\backend\data\chat_data.json", "r") as chat_file:
#     chat_data = json.load(chat_file)
#     for chat in chat_data:
#         chats.append(chat['id'])
#     print("Fetched chat IDs")

# print("Initiating emergency self destroy protocol...")
# with open("D:\Projects\JobFinder\backend\data\main_messages1.json", "w") as test_file:
#     test_file.truncate(0)
# client = TelegramClient("test", api_id, api_hash)

# data = []
# unique_links = set()

# try:
#     client.start()
#     today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  # Get today's date with timezone-naive
#     for chat_id in chats:
#         for message in client.iter_messages(chat_id, reverse=True):
#             message_date = message.date.replace(tzinfo=None)  # Convert message date to timezone-naive
#             if today - datetime.timedelta(days=20) <= message_date < today:  # Check if message date is within the last 15 days
#                 if message.text:
#                     links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
#                     for link in links:
#                         if link not in unique_links:  # Check if the link is not already added
#                             unique_links.add(link)
#                             links_str = ','.join(links)
#                             # Format the date as "5th May 2024"
#                             formatted_date = f"{ordinal(message_date.day)} {message_date.strftime('%B')} {message_date.year}"
#                             data.append({'group': chat_id, 'text': message.text, 'date': formatted_date, 'links':link_shorten(links_str)})

# finally:
#     client.disconnect()

# # Write data to JSON file
# with open("D:\Projects\JobFinder\backend\data\main_messages1.json", "w") as json_file:
#     json.dump(data, json_file, indent=4)
#     print("New Instance of Robo created ")
    
# # Git operations: add, commit, and push changes
# repo_path = "D:\Projects\JobFinder\backend"  # Replace with your actual local repo path
# commit_message = "Automated commit from script"

# subprocess.run(["git", "add", "."])
# subprocess.run(["git",  "commit", "-m", commit_message])
# subprocess.run(["git", "push"])





# import re
# from telethon.sync import TelegramClient
# import datetime
# import json
# import subprocess
# import requests
# import logging

# # Configure logging
# logging.basicConfig(filename='D:/path/to/your/logfile.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# api_id = 20183432
# api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'
# chats = []

# def link_shorten(link):
#     api_url = f"http://ouo.io/api/1QitLQLa?s={link}"
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         return response.text.strip()
#     else:
#         return f"Error: Unable to shorten the link, status code {response.status_code}"

# def ordinal(number):
#     if 10 <= number % 100 <= 20:
#         suffix = 'th'
#     else:
#         suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
#     return str(number) + suffix

# # Read chat IDs from the JSON file
# with open("D:/path/to/data/chat_data.json", "r") as chat_file:
#     chat_data = json.load(chat_file)
#     for chat in chat_data:
#         chats.append(chat['id'])
#     logging.info("Fetched chat IDs")

# logging.info("Initiating emergency self destroy protocol...")
# with open("D:/path/to/data/main_messages1.json", "w") as test_file:
#     test_file.truncate(0)

# client = TelegramClient("test", api_id, api_hash)

# data = []
# unique_links = set()

# try:
#     client.start()
#     today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
#     for chat_id in chats:
#         for message in client.iter_messages(chat_id, reverse=True):
#             message_date = message.date.replace(tzinfo=None)
#             if today - datetime.timedelta(days=20) <= message_date < today:
#                 if message.text:
#                     links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
#                     for link in links:
#                         if link not in unique_links:
#                             unique_links.add(link)
#                             links_str = ','.join(links)
#                             formatted_date = f"{ordinal(message_date.day)} {message_date.strftime('%B')} {message_date.year}"
#                             data.append({'group': chat_id, 'text': message.text, 'date': formatted_date, 'links': link_shorten(links_str)})
# finally:
#     client.disconnect()

# # Write data to JSON file
# with open("D:/path/to/data/main_messages1.json", "w") as json_file:
#     json.dump(data, json_file, indent=4)
#     logging.info("New instance of Robo created and data saved")

# # Git operations: add, commit, and push changes
# repo_path = "D:/Projects/JobFinder/backend"  # Replace with your actual local repo path
# commit_message = "Automated commit from script"

# try:
#     result_add = subprocess.run(["git", "-C", repo_path, "add", "."], capture_output=True, text=True)
#     logging.info(result_add.stdout)
#     logging.error(result_add.stderr)

#     result_commit = subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message], capture_output=True, text=True)
#     logging.info(result_commit.stdout)
#     logging.error(result_commit.stderr)

#     result_push = subprocess.run(["git", "-C", repo_path, "push"], capture_output=True, text=True)
#     logging.info(result_push.stdout)
#     logging.error(result_push.stderr)

# except Exception as e:
#     logging.error(f"An error occurred: {e}")


import re
from telethon.sync import TelegramClient
import datetime
import json
import subprocess
import requests
import logging
import os

# Ensure log directory exists
log_directory = r'D:\Projects\JobFinder\backend'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging
logging.basicConfig(filename=r'D:\Projects\JobFinder\backend\logfile.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

api_id = 20183432
api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'
chats = []

def link_shorten(link):
    api_url = f"http://ouo.io/api/1QitLQLa?s={link}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return f"Error: Unable to shorten the link, status code {response.status_code}"

def ordinal(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return str(number) + suffix

try:
    # Read chat IDs from the JSON file
    with open(r"D:\Projects\JobFinder\backend\data\chat_data.json", "r") as chat_file:
        chat_data = json.load(chat_file)
        for chat in chat_data:
            chats.append(chat['id'])
        logging.info("Fetched chat IDs")

    logging.info("Initiating emergency self destroy protocol...")
    with open(r"D:\Projects\JobFinder\backend\data\main_messages1.json", "w") as test_file:
        test_file.truncate(0)

    client = TelegramClient("test", api_id, api_hash)

    data = []
    unique_links = set()

    client.start()
    today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    for chat_id in chats:
        for message in client.iter_messages(chat_id, reverse=True):
            message_date = message.date.replace(tzinfo=None)
            if today - datetime.timedelta(days=20) <= message_date < today:
                if message.text:
                    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
                    for link in links:
                        if link not in unique_links:
                            unique_links.add(link)
                            links_str = ','.join(links)
                            formatted_date = f"{ordinal(message_date.day)} {message_date.strftime('%B')} {message_date.year}"
                            data.append({'group': chat_id, 'text': message.text, 'date': formatted_date, 'links': link_shorten(links_str)})

    client.disconnect()

    # Write data to JSON file
    with open(r"D:\Projects\JobFinder\backend\data\main_messages1.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
        logging.info("New instance of Robo created and data saved")

    # Git operations: add, commit, and push changes
    repo_path = r"D:\Projects\JobFinder\backend"  # Use your actual local repo path
    commit_message = "Automated commit from script - Updated Data"

    result_add = subprocess.run(["git", "-C", repo_path, "add", "."], capture_output=True, text=True)
    logging.info(result_add.stdout)
    logging.error(result_add.stderr)

    result_commit = subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message], capture_output=True, text=True)
    logging.info(result_commit.stdout)
    logging.error(result_commit.stderr)

    result_push = subprocess.run(["git", "-C", repo_path, "push"], capture_output=True, text=True)
    logging.info(result_push.stdout)
    logging.error(result_push.stderr)

except Exception as e:
    logging.error(f"An error occurred: {e}")
