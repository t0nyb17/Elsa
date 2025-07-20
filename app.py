from flask import Flask, render_template, jsonify
import threading
import queue
from assistant import Assistant

app = Flask(__name__)
log_message_queue = queue.Queue()
assistant_thread = None

assistant_instance = Assistant(log_queue=log_message_queue)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_assistant():
    global assistant_thread
    if assistant_thread is None or not assistant_thread.is_alive():
        assistant_thread = threading.Thread(target=assistant_instance.run)
        assistant_thread.start()
        return jsonify({'status': 'Assistant started successfully'})
        
    return jsonify({'status': 'Assistant is already running'})
@app.route('/stop', methods=['POST'])
def stop_assistant():
    assistant_instance.stop()
    return jsonify({'status': 'Assistant stopped'})

@app.route('/get_logs')
def get_logs():
    logs = []
    while not log_message_queue.empty():
        message = log_message_queue.get()
        logs.append(message)
    return jsonify({'logs': logs})

if __name__ == '__main__':
    app.run(debug=True)
