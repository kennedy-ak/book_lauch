# Book Launch Django App

A Django web application for collecting visitor information during a book launch event.

## Features

- **Visitor Registration Form**: Clean, mobile-friendly form with Bootstrap 5 styling
- **Data Collection**: Collects name, phone number, email, and location from visitors
- **Admin Dashboard**: Custom dashboard to view all registered visitors (staff only)
- **Admin Interface**: Full Django admin panel for advanced management
- **Export Functionality**: Export data to CSV and Excel formats from dashboard
- **Thank You Page**: Confirmation message after successful registration
- **Form Validation**: Client-side and server-side validation for all fields
- **Staff-Only Access**: Dashboard and export features are restricted to staff/superusers

## Technology Stack

- **Backend**: Django 4.x (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (easily upgradable to PostgreSQL for production)
- **Export**: Built-in csv module and openpyxl for Excel

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download this project**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser for admin access**:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin username and password.

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Registration form: http://127.0.0.1:8000/
   - Admin dashboard: http://127.0.0.1:8000/dashboard/ (staff only)
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Registering Visitors

1. Open the application in your web browser
2. Fill out the registration form with visitor information:
   - Full Name
   - Phone Number
   - Email Address
   - Location (City, State/Country)
3. Click "Register Now"
4. Visitors will see a thank you confirmation page

### Managing Submissions (Admin Dashboard)

**Using the Custom Dashboard:**

1. Click the "Admin Login" button in the bottom navigation bar
2. Log in with your superuser credentials
3. Access the dashboard at `/dashboard/`
4. You can:
   - View all visitor submissions in a clean table format
   - See total visitor count
   - Export all visitors to CSV
   - Export all visitors to Excel

**Using the Django Admin Panel:**

1. Log in to the admin panel at `/admin/`
2. Navigate to "Visitors" section
3. You can:
   - View all visitor submissions
   - Search by name, email, phone, or location
   - Filter by date or location
   - Export selected submissions to CSV or Excel

### Exporting Data

**From Admin Panel:**
1. Select the visitors you want to export
2. Choose "Export selected to CSV" or "Export selected to Excel" from the action dropdown
3. Click "Go" to download the file

## Project Structure

```
book_launch/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── book_launch/              # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── visitors/                # Visitor registration app
│   ├── __init__.py
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py              # App configuration
│   ├── forms.py             # Form definitions
│   ├── models.py            # Database models
│   ├── urls.py              # App URL routing
│   └── views.py             # View functions
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   └── visitors/
│       ├── register.html   # Registration form
│       ├── thank_you.html  # Thank you page
│       └── dashboard.html  # Admin dashboard
└── static/                 # Static files
    └── css/
        └── custom.css      # Custom CSS
```

## Database Schema

### Visitor Model

| Field        | Type         | Description                    |
|--------------|--------------|--------------------------------|
| name         | CharField    | Visitor's full name            |
| phone_number | CharField    | Visitor's phone number         |
| email        | EmailField   | Visitor's email address        |
| location     | CharField    | Visitor's city/location        |
| created_at   | DateTimeField| Timestamp of registration      |

## Security Notes

- **Important**: Change the `SECRET_KEY` in [`book_launch/settings.py`](book_launch/settings.py:18) before deploying to production
- Set `DEBUG = False` in production settings
- Configure `ALLOWED_HOSTS` with your domain name
- Use environment variables for sensitive configuration
- Use a production database like PostgreSQL instead of SQLite

## Deployment

For detailed deployment instructions, see [`DEPLOYMENT.md`](DEPLOYMENT.md:1).

## Troubleshooting

### Migration Issues

If you encounter migration issues, try:
```bash
python manage.py makemigrations visitors
python manage.py migrate
```

### Static Files Not Loading

Ensure static files are collected:
```bash
python manage.py collectstatic
```

### Port Already in Use

If port 8000 is already in use, run on a different port:
```bash
python manage.py runserver 8001
```

## Support

For issues or questions, please refer to the [Django documentation](https://docs.djangoproject.com/).

## License

This project is open source and available for your book launch event.
