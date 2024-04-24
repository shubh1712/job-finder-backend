import re
from telethon.sync import TelegramClient
import datetime
import json

api_id = 20183432
api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'
chats = []

# Read chat IDs from the JSON file
with open("data/chat_data.json", "r") as chat_file:
    chat_data = json.load(chat_file)
    for chat in chat_data:
        chats.append(chat['id'])
    print("fetched chat id")
    

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
            if today - datetime.timedelta(days=5) <= message_date < today:  # Check if message date is within the last 5 days
                if message.text:
                    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
                    for link in links:
                        if link not in unique_links:  # Check if the link is not already added
                            unique_links.add(link)
                            links_str = ','.join(links)
                            data.append({'group': chat_id, 'text': message.text, 'date': str(message_date), 'links': links_str})

finally:
    client.disconnect()

# Write data to JSON file
with open("D:/Projects/JobFinder/backend/data/main_messages1.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
    print("New Instance of Robo created ")


