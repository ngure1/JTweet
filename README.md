## JTweet readme

[Installation](#installation)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/ngure1/JTweet.git
    cd JTweet
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
    ```or bash
    virtualenv venv    
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.
