# AI Chat Assistant Backend

## Setting Up the Development Environment

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-repo/ai-chat-backend.git
    cd ai-chat-backend
    ```

2. **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    # For Windows
    .\venv\Scripts\activate
    # For MacOS/Linux
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Django Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

## Troubleshooting

### Common Errors:

1. **ModuleNotFoundError: No module named 'backend-ai-chat'**
    - Ensure that `PYTHONPATH` is correctly set.
    - Verify that the Procfile points to the correct WSGI application.

2. **Database Issues:**
    - Ensure that the database environment variables are correctly set in Railway.

3. **Static Files Not Loading:**
    - Verify that `STATIC_URL`, `STATIC_ROOT`, and `STATICFILES_DIRS` are correctly set in `settings.py`.
