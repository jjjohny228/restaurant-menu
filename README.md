## Installation

Usage
1. Clone the repository:

```python
https://github.com/jjjohny228/restaurant-menu.git
```

1. Go to the project directory:

```python
cd restaurant-menu
```

1. Create .env file in project. Use .env.exaple as a template.
2. Run docker compose file

```python
docker compose up --build
```

## **API Endpoints:**

### **Authentication:**

- `api/user/register/`: User registration
- `api/user/me/`: Retrieve or update users own profile information
- `api/user/token/`: Obtain JWT token pair (access and refresh tokens)
- `api/user/token/refresh/`: Refresh the JWT token
- `api/user/token/verify/`: Verify the JWT token

### **Restaurants:**

- `api/restaurant/`: List all restaurants or create a new restaurant
- `api/restaurant/<int:pk>/`: Retrieve, update, or delete a specific restaurant by its primary key (id)

### **Menus:**

- `api/restaurant/menus/`: List all menus or create a new menu
- `api/restaurant/menus/<int:pk>/`: Retrieve, update, or delete a specific menu by its primary key (id)
- `api/restaurant/get-today-menu/`: Retrieve the menu for the current day

### **Votes:**

- `api/restaurant/menus/<int:pk>/vote/`: To add employee vote
- `api/restaurant/menus/<int:pk>/result`: To retrieve daily vote result

### **Testing:**

Run tests with: `docker-compose run web pytest`