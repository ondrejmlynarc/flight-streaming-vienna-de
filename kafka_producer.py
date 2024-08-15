from FlightRadar24 import FlightRadar24API
from kafka import KafkaProducer
import json
import time

# start kafka producer
producer = KafkaProducer(
    bootstrap_servers='{REPLACE}:9092',  # replace with your IPv4 address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_flights_around_vienna_airport():
    fr_api = FlightRadar24API()
    # define the bounding box for Vienna airport
    zone = "48.1410,48.0910,16.5370,16.5870"
    print(f"Bounding Box: {zone}")

    try:
        # get flights from the bounds
        flights = fr_api.get_flights(bounds=zone)

        if not flights:
            print("no flights found in the specified area")
            return []

        print(f"found {len(flights)} flights:")
        flight_data = []
        current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        for flight in flights:
            # Assuming flight object has 'latitude' and 'longitude' attributes
            flight_info = {
                'timestamp': current_time,  # Add timestamp in ISO 8601 format
                'latitude': getattr(flight, 'latitude', 'N/A'),
                'longitude': getattr(flight, 'longitude', 'N/A'),
                **{attr: getattr(flight, attr, 'N/A') for attr in
                   ['id', 'callsign', 'origin_airport_iata', 'destination_airport_iata',
                    'altitude', 'ground_speed', 'heading', 'aircraft_code',
                    'registration', 'on_ground']}
            }

            # Collect flight info to return
            flight_data.append(flight_info)

        return flight_data

    except Exception as e:
        print(f"error: {e}")
        return []

def continuous_flight_data_producer(interval=60):
    while True:
        flight_data = get_flights_around_vienna_airport()
        if flight_data:
            for flight_info in flight_data:
                # send flight info to Kafka topic
                producer.send('flights_vienna', flight_info)
            # flush the producer to ensure all messages are sent
            producer.flush()

        # wait for the specified interval
        time.sleep(interval)

continuous_flight_data_producer(interval=60)
