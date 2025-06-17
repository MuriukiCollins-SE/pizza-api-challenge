# Pizza Restaurant API

A simple Flask REST API for managing restaurants, pizzas, and their associations.

## Features

- List all restaurants and pizzas
- Get details of a restaurant (including its pizzas)
- Create, delete restaurants and pizzas
- Create restaurant-pizza associations with price validation

## Setup

1. Install dependencies:
   ```
   pipenv install
   ```

2. Run migrations:
   ```
   flask --app server.app db upgrade
   ```

3. Start the server:
   ```
   flask --app server.app run
   ```

## API Endpoints

- `GET /restaurants` - List all restaurants
- `GET /restaurants/<id>` - Get restaurant details and its pizzas
- `POST /restaurants` - Create a new restaurant
- `DELETE /restaurants/<id>` - Delete a restaurant

- `GET /pizzas` - List all pizzas
- `GET /pizzas/<id>` - Get pizza details
- `POST /pizzas` - Create a new pizza

- `POST /restaurant_pizzas` - Create a restaurant-pizza association
  - JSON body: `{ "price": 7, "pizza_id": 1, "restaurant_id": 5 }`

## Notes

- Use `Content-Type: application/json` for POST requests.
- Price for restaurant-pizza must be between 1 and 30.
- Use Postman or curl to test the endpoints.

---
