import schedule
import time
import random
import string
import subprocess
import logging
import pymysql.cursors
import pika



# Set up logging
logging.basicConfig(level=logging.INFO)


# RabbitMQ configuration
rabbitmq_host = 'rabbitmq'  # RabbitMQ service name in Kubernetes
rabbitmq_port = 5672
rabbitmq_queue = 'random_num_queue'


# MariaDB configuration
db_host = 'mariadb'  # MariaDB service name in Kubernetes
db_user = 'sername'
db_password = 'password'
db_name = 'database_name'

rabbitmq_channel = None



# Attempt to connect to MariaDB
try:
    connection = pymysql.connect(host=db_host,
                                 user=db_user,
                                 password=db_password,
                                 db=db_name,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    app.logger.info("Successfully connected to MariaDB.")
except Exception as e:
    connection = None
    app.logger.error(f"Failed to connect to MariaDB: {e}")

# Attempt to connect to RabbitMQ
try:
    rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
    rabbitmq_channel = rabbitmq_connection.channel()
    rabbitmq_channel.queue_declare(queue=rabbitmq_queue)
    app.logger.info("Successfully connected to RabbitMQ.")
except Exception as e:
    rabbitmq_channel = None
    app.logger.error(f"Failed to connect to RabbitMQ: {e}")





def generate_random_string():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(15))
    return random_string





def send_to_mariadb_and_rabbitmq():
    random_string = generate_random_string()

    if connection:
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO random_strings (random_string) VALUES (%s)"
                cursor.execute(sql, (random_string,))
                connection.commit()
            app.logger.info("Random string inserted into MariaDB.")
        except Exception as e:
            app.logger.error(f"Failed to insert random string into MariaDB: {e}")

    if rabbitmq_channel:
        try:
            rabbitmq_channel.basic_publish(exchange='',
                                           routing_key=rabbitmq_queue,
                                           body=random_string)
            app.logger.info("Random string sent to RabbitMQ.")
        except Exception as e:
            app.logger.error(f"Failed to send random string to RabbitMQ: {e}")
            # If sending to RabbitMQ fails, emit message directly to Flask
            emit_to_flask(random_string)
    else:
        # If RabbitMQ connection is not established, emit message directly to Flask
        emit_to_flask(random_string)

    app.logger.info({"message": random_string})

def emit_to_flask(random_string):
    # Function to emit messages to Flask
    pass  # Implement the function to emit messages to Flask

# Schedule random string generation every 1 second
schedule.every(1).seconds.do(send_to_mariadb_and_rabbitmq)



def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

