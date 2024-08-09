# Car Price Prediction API

## Overview

This project implements a Flask-based API for predicting car prices using a machine learning model. It accepts car features via JSON, predicts the price, and stores predictions in an SQLite database. The API also provides Swagger documentation for easy integration and usage.

## Features

- **Price Prediction**: Predicts car prices based on input features.
- **Data Storage**: Stores predicted prices and car features in an SQLite database.
- **API Documentation**: Accessible Swagger UI for API interaction.

## Endpoints

### `/prever_preco` (POST)

- **Description**: Predicts the price of a car based on provided features.
- **Request Body**:
  ```json
  {
      "marca": "string",
      "modelo": "string",
      "transmissao": "string",
      "combustivel": "string",
      "ano": integer,
      "quilometragem": integer,
      "moto_size": float
  }

## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## API Reference

#### Get all items

```http
  GET /
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  POST /prever_proco/items
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |
| `id`      | `string` | **Required**. Id of item to fetch |
| `id`      | `string` | **Required**. Id of item to fetch |
| `id`      | `string` | **Required**. Id of item to fetch |
| `id`      | `string` | **Required**. Id of item to fetch |
| `id`      | `string` | **Required**. Id of item to fetch |
| `id`      | `string` | **Required**. Id of item to fetch |


#### add(num1, num2)

Takes two numbers and returns the sum.


## Deployment

To deploy this project run

```bash
  npm run deploy
```


## Documentation

[Documentation](https://linktodocumentation)


## Appendix

Any additional information goes here


## Authors

- [@octokatherine](https://www.github.com/octokatherine)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

