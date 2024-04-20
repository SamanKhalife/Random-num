from flask import Flask, render_template
import schedule
import time
import random
import string
import logging
from fluent import sender, event
from fluent import event

app = Flask(__name__)

# Configure Fluentd logger
fluentd_host = 'localhost'  # Fluentd host address
fluentd_port = 24224  # Fluentd port
tag = 'myapp.logs'  # Tag used for sending to Fluentd
fluent_logger = sender.FluentSender(tag, host=fluentd_host, port=fluentd_port)

# Set up logging
logging.basicConfig(level=logging.INFO)

random_strings = []

def generate_random_string():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(15))
    return random_string

def send_random_string():
    random_string = generate_random_string()
    random_strings.append(random_string)
    app.logger.info({"message": random_string})  
    fluent_logger.emit(tag, {"message": random_string})  
    print(random_string)

schedule.every(1).seconds.do(send_random_string)

@app.route('/')
def display_random_strings():
    schedule.run_pending()
    return render_template('random_strings.html', random_strings=random_strings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8569)
