# PythonAnywhere Deployment Guide

## 1. Sign up for PythonAnywhere
- Go to [PythonAnywhere](https://www.pythonanywhere.com/) and sign up for an account
- The free tier is sufficient for starting out

## 2. Upload Your Code
### Using Git
```bash
# On PythonAnywhere bash console
git clone https://github.com/yourusername/yourrepository.git
```

### Using Manual Upload
- Create a ZIP archive of your project
- From PythonAnywhere dashboard, go to Files and upload your ZIP
- Unzip the file in your PythonAnywhere directory

## 3. Create a Virtual Environment
```bash
# On PythonAnywhere bash console
cd ~/djangotutorial
python -m venv venv
source venv/bin/activate
pip install django
pip install -r requirements.txt  # if you have one
```

## 4. Set Up Your Web App
- Go to Web tab in PythonAnywhere dashboard
- Click "Add a new web app"
- Choose "Manual configuration"
- Select the Python version that matches your local environment

## 5. Configure Your WSGI File
- Click on the WSGI configuration file link in the Web tab
- Replace the contents with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/djangotutorial'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable to tell Django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# Set up Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 6. Configure Static Files
- In the Web tab, under "Static files"
- Add:
  - URL: /static/
  - Directory: /home/yourusername/djangotutorial/static
  - URL: /media/
  - Directory: /home/yourusername/djangotutorial/media

## 7. Set Up Database
```bash
# On PythonAnywhere bash console
cd ~/djangotutorial
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
```

## 8. Collect Static Files
```bash
python manage.py collectstatic
```

## 9. Configure Virtual Environment
- In the Web tab, set the path to your virtual environment:
  - /home/yourusername/djangotutorial/venv

## 10. Reload Your Web App
- Click the "Reload" button in the Web tab

## 11. Visit Your Site
- Your site should now be live at: https://yourusername.pythonanywhere.com

## Troubleshooting
- Check the error logs in the Web tab
- Make sure DEBUG = False in settings.py
- Ensure ALLOWED_HOSTS includes your PythonAnywhere domain
- Verify your database configuration
