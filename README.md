# E-commerce Car Listing API

## Introduction

This project implements a Python API for managing car listings in an e-commerce platform. The API allows users to perform CRUD operations on car and broker entities, retrieve car status, and more.

## Requirements

- Docker
- MongoDB (optional)

  - create database
    - name : mydatabase
      - collection :
        - cars
        - brokers
        - listing

- Python 3.9 or higher

## Setup

```bash
git clone https://github.com/gdimoo/zrch_test.git
cd zrch_test

# Run with Docker
docker docker-compose up --build

API will be accessible at http://127.0.0.1:8000.

API Endpoints
Car Endpoints:

Create: POST /cars
Read: GET /cars/{car_id}
Update: PUT /cars/{car_id}
Delete: DELETE /cars/{car_id}

Broker Endpoints:

Create: POST /brokers
Read: GET /brokers/{broker_id}
Update: PUT /brokers/{broker_id}
Delete: DELETE /brokers/{broker_id}

Listing Endpoints:

Retrieve Car Status: GET /listings/{car_id}
API Documentation
Access Swagger documentation at http://127.0.0.1:8000/docs for detailed information on available endpoints and request/response formats.

```
