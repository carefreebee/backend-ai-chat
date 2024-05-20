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
