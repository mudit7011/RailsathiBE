# RailSathiBE – Django Backend with Docker

This project is a containerized Django application with PostgreSQL, providing basic CRUD functionality through an `/items/` API endpoint. It is built to demonstrate backend capabilities in a clean, modular, and production-friendly way.

## Project Setup

1. Clone the repository:
   git clone https://github.com/mudit7011/RailsathiBE.git
   cd RailSathiBE

2. Create a `.env` file in the root directory with the following content:
   DB_NAME=railsathidb  
   DB_USER=postgres  
   DB_PASSWORD=postgres  
   DB_HOST=db  
   DB_PORT=5432

3. Start Docker containers:
   docker compose up --build

4. In a separate terminal, apply migrations:
   docker compose exec web python manage.py makemigrations  
   docker compose exec web python manage.py migrate

The application will be available at http://localhost:8000/items/

## API Endpoints

GET /items/  
Returns a list of all items.  
Response:
[
  {
    "id": 1,
    "name": "Sample Item",
    "description": "This is a test item"
  }
]

POST /items/  
Creates a new item.  
Headers: Content-Type: application/json  
Body:
{
  "name": "Pen",
  "description": "A blue ink pen"
}

## Key Features Implemented

- Dockerized Django application
- PostgreSQL as the backend database
- REST API to GET and POST items
- Environment-based configuration using .env
- Stateless and easily portable project setup

## Assumptions and Limitations

- The project does not include user authentication or admin panel
- CSRF protection is exempted for POST endpoint to allow easy testing from Postman
- The frontend is not in scope for this assignment
- Only GET and POST methods are implemented; PUT/DELETE are not part of this version

## How to Test in Postman

1. Run the server via Docker
2. Open Postman and hit GET:  
   http://localhost:8000/items/

3. To create an item, use POST:
   URL: http://localhost:8000/items/  
   Body (raw JSON):
   {
     "name": "Notebook",
     "description": "A 100-page ruled notebook"
   }

4. Set Headers:  
   Content-Type: application/json

## Recording Links

project-technical: https://drive.google.com/file/d/1nA_10AhoJTFhnT91mupYe-LVA9Wc4-ru/view?usp=sharing

## Author

Mudit Kumar  
GitHub: https://github.com/mudit7011  
LinkedIn: https://linkedin.com/in/mudit-dev
