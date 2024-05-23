# from telethon.sync import TelegramClient

# api_id = 20183432
# api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'

# client = TelegramClient('session_name', api_id, api_hash)
# client.start()
# async def get_chat_id(chat_name):
#     async for dialog in client.iter_dialogs():
#         if dialog.name == chat_name:
#             return dialog.id

# # Replace 'YourChatName' with the name of the chat whose ID you want to find
# chat_id = client.loop.run_until_complete(get_chat_id("OffCampus Phodenge : Aman Chowdhury 😊❤️"))

# print("Chat ID:", chat_id)
 
# client.disconnect()



from telethon.sync import TelegramClient
import json

api_id = 20183432
api_hash = 'a7ca0c26fd2e3ec7b400af99844156d3'

# Define your list of chat names
chat_names = [
    "Talentboxjob", 
    "OffCampus Phodenge : Aman Chowdhury 😊❤️", 
    "Off Campus Drive | Fresher & Experience - Your Career",
    "Off Campus Drive & Internship Updates, Udemy Coupons",
    "Smarthunt4u JOBs",
    "OffCampusJobs4u.com- India's #1 Off Campus Job Portal for Freshers.",
    "Go Careers",
    "DotAware: Off-Campus Tech Jobs 👨‍💻",
    "Freshers Off Campus",
    "Jobs/Internship/Hiring/ updates - Fresher / IT / Non-IT",
    "INDIA Job Seekers (IJS)",
    "Jobshob Nest / जॉबशोब नेस्ट",
    "Fresherstech - Off Campus Drive Updates",
    "HR Group India"
    ]

client = TelegramClient('session_name', api_id, api_hash)
client.start()

async def get_chat_ids(chat_names):
    chat_ids = {}
    async for dialog in client.iter_dialogs():
        if dialog.name in chat_names:
            chat_ids[dialog.name] = dialog.id
    return chat_ids

# Get chat IDs for the specified chat names
chat_ids = client.loop.run_until_complete(get_chat_ids(chat_names))

# Print and store chat names along with their IDs in JSON format
chat_data = [{'name': name, 'id': chat_ids[name]} for name in chat_ids]

print("Chat Data:", chat_data)

# Export chat data to a JSON file
with open("data/chat_data.json", "w") as json_file:
    json.dump(chat_data, json_file, indent=4)

client.disconnect()
