# Real-time Data Monitoring Pipeline

This project builds a real-time data pipeline using Kafka, Elasticsearch, and Logstash. It creates a pipeline to ingest data into Elasticsearch via Kafka. It uses the python script to generate fake log data and publishes it to Kafka. Logstash, then, consumes these messages and forwards them to Elasticsearch.

## **Architecture**

The architecture of the data pipeline is as follows:

- A Python script uses Faker to generate fake log data.
- The Python script publishes the fake data to a Kafka topic.
- Logstash consumes the data from the Kafka topic.
- Logstash sends the consumed data to Elasticsearch.
- Kibana is used to visualize the data in Elasticsearch.

![Real-time Data Monitoring Pipeline](/Users/xiaorui/文档/系统设计/Real-time Data Monitoring Pipeline.png)
