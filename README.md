# Streamlit MVC Application

This is a simple Streamlit application structured using the Model-View-Controller (MVC) architecture. The application interacts with a database and presents data through a user-friendly interface.

## Project Structure

```
streamlit-mvc-app
├── app
│   ├── controllers
│   │   └── main_controller.py
│   ├── models
│   │   └── database_model.py
│   ├── views
│   │   └── main_view.py
│   └── __init__.py
├── requirements.txt
├── .streamlit
│   └── config.toml
├── main.py
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd streamlit-mvc-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run main.py
   ```

## Usage

- Upon running the application, the main interface will be displayed.
- The application fetches data from the database and presents it using Streamlit components.
- You can modify the database interactions in `app/models/database_model.py` and the application logic in `app/controllers/main_controller.py`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.