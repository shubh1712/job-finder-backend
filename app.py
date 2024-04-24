import json
import os
import subprocess
import threading
from flask import Flask, jsonify
import schedule
import time as tm
from telethon.sync import TelegramClient
from flask_cors import CORS  # Import CORS from flask_cors
app = Flask(__name__)


CORS(app)
def run_test_script():
        # Assuming your test.py script contains a function called 'test_function' that you want to execute
        try:
            subprocess.run(["python", "mainScraper.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running test.py: {e}")        
def schedule_loop():
    schedule.every(180).minutes.do(run_test_script)

    while True:
        schedule.run_pending()
        tm.sleep(1)
    
    
@app.route('/get_chat_data', methods=['GET'])
def get_chat_data():
    try:
        with open("data/main_messages1.json", "r") as chat_file:
            chat_data = json.load(chat_file)
            print(len(chat_data))
        return jsonify(chat_data)
        
    except FileNotFoundError:
        return jsonify({'error': 'Chat data file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    

if __name__ == '__main__':


    # Create a separate thread to run the scheduler
    scheduler_thread = threading.Thread(target=schedule_loop)
    scheduler_thread.start()

    # Run the Flask app
    app.run(debug=True)
    scheduler_thread.join()

   
