# import re
# from telethon.sync import TelegramClient
# import datetime
# import json
# api_id = 20183432
# api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'
# chats = [1001591593758]
# print("Clearing main_messages1.json file...")
# with open("data/test.json", "w") as test_file:
#     test_file.truncate(0)
# # Read chat IDs from the JSON file
# # with open("chat_data.json", "r") as chat_file:
# #     chat_data = json.load(chat_file)
# #     for chat in chat_data:
# #         chats.append(chat['id'])

# client = TelegramClient("test", api_id, api_hash)

# data = []

# client.start()
# try:
#     today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  # Get today's date with timezone-naive
#     for chat_id in chats:
#         for message in client.iter_messages(chat_id, reverse=True):
#             message_date = message.date.replace(tzinfo=None)  # Convert message date to timezone-naive
#             if today - datetime.timedelta(days=20) <= message_date < today:  # Check if message date is within the last 5 days
#                 if message.text:
#                     links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
#                     links_str = ','.join(links)
#                     data.append({'group': chat_id, 'text': message.text, 'date': str(message_date), 'links': links_str})

# finally:
#     client.disconnect()

#     # Write data to JSON file
# with open("D:/Projects/JobFinder/data/test.json", "w") as json_file:
#     json.dump(data, json_file, indent=4)
#     print("Updates done")
        
        
        
# import re
# from telethon.sync import TelegramClient
# import datetime
# import json

# api_id = 20183432
# api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'
# chats = [1001591593758]

# print("Clearing main_messages1.json file...")
# with open("data/test.json", "w") as test_file:
#     test_file.truncate(0)

# client = TelegramClient("test", api_id, api_hash)

# data = []

# client.start()

# try:
#     today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

#     # Keywords related to jobs and internships
#     job_keywords = ['job', 'career', 'opportunity', 'internship']

#     for chat_id in chats:
#         for message in client.iter_messages(chat_id, reverse=True):
#             message_date = message.date.replace(tzinfo=None)

#             # Check if message date is within the last 5 days
#             if today - datetime.timedelta(days=20) <= message_date < today:
#                 if message.text:
#                     # Check if message contains any of the job keywords
#                     if any(keyword in message.text.lower() for keyword in job_keywords):
#                         links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
#                         links_str = ','.join(links)

#                         # Extract date and time separately
#                         date_str = message_date.strftime('%Y-%m-%d')
#                         time_str = message_date.strftime('%H:%M:%S')

#                         data.append({'group': chat_id, 'text': message.text, 'date': date_str, 'time': time_str, 'links': links_str})

# finally:
#     client.disconnect()

#     # Write data to JSON file
#     with open("D:/Projects/JobFinder/backend/data/test.json", "w") as json_file:
#         json.dump(data, json_file, indent=4)
#         print("Updates done")




# test -3 
import re
from telethon.sync import TelegramClient
import datetime
import json

import re

def extract_job_details(text):
    job_details = {}

    # Search for the name of the company
    company_match = re.search(r'(?i)(?<=hiring)(.*?)(?=:|\n)', text)
    if company_match:
        job_details['company'] = company_match.group(1).strip()

    # Search for stipend/package/CTC
    stipend_match = re.search(r'(?i)(stipend|package|ctc):\s*(.*?)(?=\s*(batch|role|$))', text)
    if stipend_match:
        job_details['stipend'] = stipend_match.group(2).strip()

    # Search for batch
    batch_match = re.search(r'(?i)batch:?\s*(.*?)(?=\s*(role|$))', text)
    if batch_match:
        job_details['batch'] = batch_match.group(1).strip()

    # Search for job role
    role_match = re.search(r'(?i)(job\s*role|role):\s*(.*?)(?=\s*$)', text)
    if role_match:
        job_details['role'] = role_match.group(2).strip()

    return job_details


api_id = 20183432
api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'
chats = [1001591593758]

print("Clearing main_messages1.json file...")
with open("data/test.json", "w") as test_file:
    test_file.truncate(0)

client = TelegramClient("test", api_id, api_hash)

data = []

client.start()

try:
    today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    # Keywords related to jobs and internships
    job_keywords = ['job', 'career', 'opportunity', 'internship']

    for chat_id in chats:
        for message in client.iter_messages(chat_id, reverse=True):
            message_date = message.date.replace(tzinfo=None)

            # Check if message date is within the last 5 days
            if today - datetime.timedelta(days=20) <= message_date < today:
                if message.text:
                    # Check if message contains any of the job keywords
                    if any(keyword in message.text.lower() for keyword in job_keywords):
                        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
                        links_str = ','.join(links)

                        # Extract date and time separately
                        date_str = message_date.strftime('%Y-%m-%d')
                        time_str = message_date.strftime('%H:%M:%S')

                        # Extract job details using the function
                        job_details = extract_job_details(message.text)

                        data.append({'group': chat_id, 'text': message.text, 'date': date_str, 'time': time_str, 'links': links_str, **job_details})

finally:
    client.disconnect()

    # Write data to JSON file
    with open("D:/Projects/JobFinder/backend/data/test.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("Updates done")

