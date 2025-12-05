# URL Safety Assessor Project

This project assesses the safety of URLs by analyzing their components (Full URL, Domain, and Path) using a trained CatBoost model. The application provides a safety message and a percentage indicating the risk level of the URL.

## Project Setup Instructions

### 1. Set Up a Virtual Environment

#### Using venv:
- Open the terminal or command prompt.
- Navigate to the project folder using:
  ```bash
  cd <project-folder>
  ```
- Create a virtual environment:
  ```bash
  python -m venv env
  ```
- Activate the environment:
  - On **Windows**:
    ```bash
    .\env\Scripts\activate
    ```
  - On **macOS/Linux**:
    ```bash
    source env/bin/activate
    ```

#### Using conda:
- Open the terminal or command prompt.
- Create a new environment:
  ```bash
  conda create --name my_env python=3.11.10
  ```
- Activate the environment:
  ```bash
  conda activate my_env
  ```

### 2. Install Required Libraries

Run the following command to install the necessary libraries:
```bash
pip install catboost streamlit pandas
```

### 3. Ensure the Folder Contains These Files
Make sure the project folder contains the following files:
- `test.py` - The main code for running the application.
- `features.py` - Code for extracting features from a URL.
- `cat_url.cbm` - The trained CatBoost model.

### 4. Run the Application
To run the application, execute the following command:
```bash
streamlit run test.py
```

### 5. Use the Application
- A browser window will open automatically. If it doesn't, copy the URL shown in the terminal (e.g., `http://localhost:8501`) and open it in a browser.
- Enter a URL in the input box and press **Enter**.
- The results, including a safety message and the associated risk percentage, will be displayed in the browser.

#### Note: This Project uses Python = 3.11.10
