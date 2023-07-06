import json
import time
from faker import Faker
from confluent_kafka import Producer

fake = Faker()


def get_registered_data():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }


conf = {'bootstrap.servers': '192.168.31.67:9092'}

producer = Producer(conf)


if __name__ == "__main__":
    while True:
        registered_data = get_registered_data()
        print(registered_data)
        producer.produce('registered_user', json.dumps(registered_data))
        producer.flush()  # Ensure any buffered messages are sent.
        time.sleep(3)
