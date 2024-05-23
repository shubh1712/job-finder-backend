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


import re
from telethon.sync import TelegramClient
import datetime
import json
import requests
api_id = 20183432
api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'
chats = []

import requests

def link_shorten(link):
    # Replace 'yourdestinationlink.com' with the actual link to be shortened
    api_url = f"http://ouo.io/api/1QitLQLa?s={link}"
    
    # Make the GET request to the API
    response = requests.get(api_url)
    print(response.text.strip())
    # Check if the request was successful
    if response.status_code == 200:
        # Return the shortened link
        return response.text.strip()
    else:
        # Return an error message if the request was not successful
        return f"Error: Unable to shorten the link, status code {response.status_code}"

# Example usage:
# original_link = "https://www.example.com"
# shortened_link = link_shorten(original_link)
# print(f"Shortened link: {shortened_link}")

def ordinal(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return str(number) + suffix
# Read chat IDs from the JSON file
with open("data/chat_data.json", "r") as chat_file:
    chat_data = json.load(chat_file)
    for chat in chat_data:
        chats.append(chat['id'])
    print("Fetched chat IDs")

print("Initiating emergency self destroy protocol...")
with open("data/main_messages1.json", "w") as test_file:
    test_file.truncate(0)
client = TelegramClient("test", api_id, api_hash)

data = []
unique_links = set()

try:
    client.start()
    today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  # Get today's date with timezone-naive
    for chat_id in chats:
        for message in client.iter_messages(chat_id, reverse=True):
            message_date = message.date.replace(tzinfo=None)  # Convert message date to timezone-naive
            if today - datetime.timedelta(days=20) <= message_date < today:  # Check if message date is within the last 15 days
                if message.text:
                    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
                    for link in links:
                        if link not in unique_links:  # Check if the link is not already added
                            unique_links.add(link)
                            links_str = ','.join(links)
                            # Format the date as "5th May 2024"
                            formatted_date = f"{ordinal(message_date.day)} {message_date.strftime('%B')} {message_date.year}"
                            data.append({'group': chat_id, 'text': message.text, 'date': formatted_date, 'links':link_shorten(links_str)})

finally:
    client.disconnect()

# Write data to JSON file
with open("data/main_messages1.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
    print("New Instance of Robo created ")