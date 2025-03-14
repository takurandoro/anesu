🚀 Green Academy API - Deployment Guide
📌 Deployment Overview
This document outlines the process of deploying the Green Academy API to a cloud platform, including configuration, database setup, monitoring, and best practices for secure deployment.

1️⃣ Deployment Platform Selection
Why Render?
We selected Render as our deployment platform for the following reasons:
✅ Free tier for small projects
✅ Automatic deployment from GitHub
✅ Supports PostgreSQL databases (reliable & scalable)
✅ Built-in HTTPS support (secure API communication)
✅ Environment variable management (easy secrets handling)
✅ Simple CI/CD integration for smooth updates

2️⃣ Deployment Steps
Step 1: Push Code to GitHub
Ensure your latest code is pushed to a GitHub repository:

bash
Copy
Edit
git add .
git commit -m "Final deployment version"
git push origin main
Step 2: Create a Render Web Service
Log in to Render and navigate to New Web Service.
Connect your GitHub repository and select your API project.
Choose the starter free plan for initial deployment.
Step 3: Set Deployment Settings
Runtime: Python 3.11
Build Command:
bash
Copy
Edit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
Start Command:
bash
Copy
Edit
gunicorn green_academy.wsgi:application --bind 0.0.0.0:10000
Environment Variables:
Add these in Render Dashboard → Environment → Secret Variables:
ini
Copy
Edit
DJANGO_SECRET_KEY=your-secure-secret-key
DEBUG=False
ALLOWED_HOSTS=summative-green-academy-api-final-phase.onrender.com
DATABASE_URL=your-production-database-url
Step 4: Configure the Database (PostgreSQL)
Go to Render → Databases → Create New Database
Select PostgreSQL
Copy the database connection string and update DATABASE_URL in environment variables.
3️⃣ Configuration & Security Best Practices
🔐 Secure API Settings
Disable Debug Mode:
Ensure DEBUG=False in production to prevent sensitive data leaks.
Use Environment Variables:
Store secrets securely in Render’s Environment Variables, not in code.
HTTPS Only:
Render automatically enforces HTTPS; no additional setup required.
⚡ Performance Optimization
Static Files Handling
Use Whitenoise for serving static files efficiently:
python
Copy
Edit
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
Enable Query Caching
Utilize Django caching for improved response times:
python
Copy
Edit
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}
4️⃣ Monitoring & Logging
🔍 Error Logging
To track errors, configure logging to store errors in a file:

python
Copy
Edit
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
📊 Health Monitoring
Use Render’s Built-in Logs to monitor server activity.
Enable API Request Logs in Django for tracking requests.
Optional: Integrate Sentry for real-time error tracking.
5️⃣ Deployment Troubleshooting
Issue	Possible Cause	Solution
Deployment fails	Missing environment variables	Ensure DJANGO_SECRET_KEY and DATABASE_URL are set
Database errors	Migrations not applied	Run python manage.py migrate
Static files not loading	Whitenoise misconfiguration	Ensure STATICFILES_STORAGE is set properly
CORS Issues	API restricted to allowed origins	Check CORS_ALLOWED_ORIGINS in settings
6️⃣ Future Improvements
🚀 Scalability Enhancements: Move to AWS or DigitalOcean for production-grade infrastructure.
🔐 Enhanced Security: Implement rate limiting and stricter CORS policies.
📈 Performance Monitoring: Use New Relic or Prometheus for API monitoring.

🎉 Deployment Complete!
Your API is now live on Render at:
🔗 https://summative-green-academy-api-final-phase.onrender.com 🚀