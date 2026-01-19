# Deployment Guide

This guide will help you deploy the Book Launch Django app to your server.

## Prerequisites

- A server with:
  - Python 3.8 or higher
  - pip package manager
  - SSH access (for remote deployment)
- Domain name (optional, but recommended)
- Basic knowledge of command line operations

## Deployment Steps

### 1. Prepare Your Server

#### Update System Packages
```bash
sudo apt update && sudo apt upgrade -y  # Ubuntu/Debian
# OR
sudo yum update -y  # CentOS/RHEL
```

#### Install Python and pip
```bash
sudo apt install python3 python3-pip python3-venv -y  # Ubuntu/Debian
# OR
sudo yum install python3 python3-pip -y  # CentOS/RHEL
```

### 2. Set Up the Project

#### Upload Project Files
Transfer the project files to your server using SCP, SFTP, or Git.

Example using SCP:
```bash
scp -r book_launch/ user@your-server.com:/path/to/deployment/
```

#### Navigate to Project Directory
```bash
cd /path/to/deployment/book_launch
```

### 3. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Production Settings

Edit [`book_launch/settings.py`](book_launch/settings.py:1):

```python
# Set DEBUG to False
DEBUG = False

# Add your domain to ALLOWED_HOSTS
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com', 'your-server-ip']

# Change SECRET_KEY to a secure value
SECRET_KEY = 'your-very-long-and-secure-secret-key-here'
```

**Important**: Generate a secure SECRET_KEY:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 6. Set Up Production Database (Optional but Recommended)

While SQLite works for small events, PostgreSQL is recommended for production.

#### Install PostgreSQL
```bash
sudo apt install postgresql postgresql-contrib -y
```

#### Create Database and User
```bash
sudo -u postgres psql
```

In PostgreSQL prompt:
```sql
CREATE DATABASE book_launch;
CREATE USER book_launch_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE book_launch TO book_launch_user;
\q
```

#### Update [`book_launch/settings.py`](book_launch/settings.py:1):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'book_launch',
        'USER': 'book_launch_user',
        'PASSWORD': 'secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### Install PostgreSQL adapter
```bash
pip install psycopg2-binary
```

### 7. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create Superuser

```bash
python manage.py createsuperuser
```

### 9. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 10. Install and Configure Gunicorn

#### Install Gunicorn
```bash
pip install gunicorn
```

#### Test Gunicorn
```bash
gunicorn --bind 0.0.0.0:8000 book_launch.wsgi:application
```

If this works, press Ctrl+C to stop.

#### Create Gunicorn Systemd Service

Create file `/etc/systemd/system/book-launch.service`:
```ini
[Unit]
Description=Gunicorn instance to serve Book Launch Django app
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/deployment/book_launch
Environment="PATH=/path/to/deployment/book_launch/venv/bin"
ExecStart=/path/to/deployment/book_launch/venv/bin/gunicorn --workers 3 --bind unix:book-launch.sock book_launch.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start and enable the service:
```bash
sudo systemctl start book-launch
sudo systemctl enable book-launch
```

### 11. Set Up Nginx as Reverse Proxy

#### Install Nginx
```bash
sudo apt install nginx -y
```

#### Create Nginx Configuration

Create file `/etc/nginx/sites-available/book-launch`:
```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /path/to/deployment/book_launch;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/deployment/book_launch/book-launch.sock;
    }
}
```

#### Enable Configuration
```bash
sudo ln -s /etc/nginx/sites-available/book-launch /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### 12. Configure Firewall

```bash
sudo ufw allow 'Nginx Full'
```

### 13. Set Up SSL with Let's Encrypt (Recommended)

#### Install Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
```

#### Obtain SSL Certificate
```bash
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

Follow the prompts to configure SSL.

### 14. Verify Deployment

- Visit `http://your-domain.com` - You should see the registration form
- Visit `http://your-domain.com/admin` - You should see the admin login page

## Maintenance

### Update Dependencies
```bash
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

### Restart Services
```bash
sudo systemctl restart book-launch
sudo systemctl restart nginx
```

### View Logs
```bash
sudo journalctl -u book-launch
sudo tail -f /var/log/nginx/error.log
```

### Backup Database
```bash
# For PostgreSQL
pg_dump -U book_launch_user book_launch > backup.sql

# For SQLite
cp db.sqlite3 backup.db.sqlite3
```

## Troubleshooting

### Application Not Loading
```bash
sudo systemctl status book-launch
sudo journalctl -u book-launch
```

### Permission Issues
```bash
sudo chown -R www-data:www-data /path/to/deployment/book_launch
sudo chmod -R 755 /path/to/deployment/book_launch
```

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
sudo systemctl restart nginx
```

## Performance Tips

1. **Use PostgreSQL instead of SQLite** for better performance
2. **Enable caching** with Redis or Memcached
3. **Use CDN** for static files
4. **Optimize database queries** with Django Debug Toolbar
5. **Monitor server resources** with tools like htop

## Security Checklist

- [ ] Changed `SECRET_KEY` to a secure value
- [ ] Set `DEBUG = False`
- [ ] Configured `ALLOWED_HOSTS`
- [ ] Enabled SSL/HTTPS
- [ ] Set up firewall rules
- [ ] Regularly update dependencies
- [ ] Use strong passwords for database and admin
- [ ] Regular backups of database and media files

## Additional Resources

- [Django Deployment Documentation](https://docs.djangoproject.com/en/4.2/howto/deployment/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Let's Encrypt Documentation](https://letsencrypt.org/docs/)

## Support

If you encounter issues during deployment:
1. Check the logs mentioned in the troubleshooting section
2. Verify all configuration files are correct
3. Ensure all services are running
4. Check firewall and network settings
