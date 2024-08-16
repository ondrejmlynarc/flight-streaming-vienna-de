# ViennaFlightKafkaStream

ViennaFlightKafkaStream is a data pipeline project that uses the FlightRadar24 API to collect live flight data from/around Vienna International Airport. The data is streamed using Kafka and stored in an Amazon S3 bucket before it's glued to Athena and used for visualisation. The pipeline provides live update every 15-minute on several aggregated flight metrics. This project is part of my AWS journey to solidify my knowledge of the used services within the AWS, while also learning about popular Kafka library.

![dahsboard_vis.png](img%2Fdahsboard_vis.png)

# Technologies used
- **Python:** Uses FlightRadar API and  the psutil library for collecting metrics data and Kafka Python client for producing and consuming messages.
- **Apache Kafka:** Used as a distributed streaming platform for handling real-time data processing and pipeline management.
- **Apache Zookeeper:** A centralized service for managing and coordinating Kafka brokers in a distributed system.
- **AWS:** Alongside used as virtual machines (EC2) to run Kafka, stores the data into AWS S3 and prepares them for visualisation in a querying form (AWS Crawler->Glue->Athena) 
- **Qucksight:** Used to visualise the data from Athena at 15-minute intercals. 

## Architecture
![kafka-pipeline-vienna-airport.png](img%2Fkafka-pipeline-vienna-airport.png)

The data pipeline consists of the following steps:

- Collects real-time flight data using the FlightRadar24 API
- Streams data to a Kafka topic for processing
- Stores flight data in an Amazon S3 bucket
- Uses Crawler and Glue to query data from Athena
- Visualises the data in Quicksight

## Getting Started: Prerequisites and Setup
For this project, we use a GitHub repository that hosts files for setting up the project, making it easy for anyone to get started.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ondrejmlynarc/flight-streaming-vienna-de.git
   ```

2. **Navigate to the project directory:**
    ```bash
   cd flight-streaming-vienna-de
   ```

3. **Install the required Python packages:**    
    ```bash
   pip install -r requirements.txt
      ```
   
4. **Set up EC2 instance on AWS:** for setting up the instance, t2.Micro instance is sufficient if applied on only one airport. 


5. **Start Zookoper and Kafka Server:** this step requires several steps, including initial installation of Java. The following repo that includes a video tutorial explains these steps in great detail https://github.com/darshilparmar/stock-market-kafka-data-engineering-project.


6. **Run Python scripts:** make sure you replaced your IP from EC2 and bucket information together with creating config.ini with credentials.
    ```bash
   python kafka_consumer.py
   python kafka_producer.py
   ```
4. **Move data to Athena for querying**: Use AWS Crawler -> Glue -> Athena for querying the data.

# Future Improvements
While the ViennaFlightKafkaStream project primarily served my educational purposes for Kafka and AWS, future adjustments could focus on adopting a more robust architecture and advanced technologies:
- **Apache Spark:** Integrate PySpark for scalable and efficient data processing.
- **Apache Airflow:** Implement Airflow for advanced workflow orchestration and automation.
- **Docker:** Use Docker for containerisation to streamline deployment and scaling.
- **Monitoring:** Add comprehensive monitoring and alerting to ensure the health and reliability of the pipeline.
- **Visualisation:** Explore additional tools such as Grafana and Plotly for more interactive and near real-time visualisations.

# Acknowledgments
This project architecture is inspired by the [Stock Market Kafka Data Engineering Project](https://github.com/darshilparmar/stock-market-kafka-data-engineering-project/tree/main) by [Darshil Parmar's GitHub Profile](https://github.com/darshilparmar). We have adapted several key components and processes from this repository, particularly in using Apache Kafka for data streaming, Amazon S3 for data storage, AWS Glue and Athena for data processing.