from kafka import KafkaConsumer
import json

def start_consumer():
    consumer = KafkaConsumer(
        'user_created',
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        group_id='reservation-group'
    )

    print("Kafka consumer is running...")
    for message in consumer:
        print("NOUVEL UTILISATEUR CRÉÉ :", message.value)

if __name__ == "__main__":
    start_consumer()