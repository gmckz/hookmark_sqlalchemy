# Hookmark

Hookmark is a web application designed for managing knitting and crochet projects and patterns. The backend utilizes a RESTful API built with Flask and SQLAlchemy for database management, while the frontend is developed using React, ensuring responsiveness across various devices.

![Preview](https://github.com/gmckz/hookmark_sqlalchemy/assets/67702875/a769543e-f8e8-44b9-8067-b99412ed0c33)

## How to Run

### Backend:

1. **Set Up Virtual Environment:**

    ```bash
    cd backend
    python3 -m venv .venv
    ```

2. **Activate Virtual Environment:**

    ```bash
    . ./.venv/bin/activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Server:**
    ```bash
    flask --app server run
    ```

### Frontend:

1. **Install Dependencies:**

    ```bash
    npm install
    ```

2. **Start Development Server:**
    ```bash
    npm start
    ```
