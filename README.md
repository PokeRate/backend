This project is a Django-based REST API for user management, including user registration, authentication, and token generation.

## Requirements

- Python 3.8+
- Django 3.2+
- Django REST framework
- PostgreSQL

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL

#### Install PostgreSQL

Follow the instructions for your operating system to install PostgreSQL.

#### Create a Database and User

```bash
sudo -u postgres psql
```

In the PostgreSQL shell, run the following commands:

```sql
CREATE DATABASE yourdatabase;
CREATE USER youruser WITH PASSWORD 'yourpassword';
ALTER ROLE youruser SET client_encoding TO 'utf8';
ALTER ROLE youruser SET default_transaction_isolation TO 'read committed';
ALTER ROLE youruser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE yourdatabase TO youruser;
\q
```

### 5. Configure Django Settings

Update your `.env` file with your PostgreSQL database configuration and secret key (obtain froma developer):

```bash
DB_NAME=yourdatabase
DB_USER=youruser
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY=yoursecretkey
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

### 9. Access the API

You can now access the API at `http://127.0.0.1:8000/`.

## License

This project is licensed under the MIT License.
