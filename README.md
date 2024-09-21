# NLP App Using Tkinter

This project is a Natural Language Processing (NLP) application built with Python and Tkinter for the GUI. It leverages the **NLP Cloud API** for various NLP tasks and stores user data using a **JSON file** as a local database.

## Features

- **Text Input**: Users can input custom text for processing.
- **NLP Cloud Integration**: The app utilizes the NLP Cloud API for performing advanced NLP tasks such as:
  - Sentiment Analysis
  - Named Entity Recognition (NER)
  - Language Translation
  - Text Summarization
- **Local Storage**: User data is stored locally in a JSON file.
- **Tkinter GUI**: A simple and interactive graphical interface.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Samarth-Bhimani/NLP-APP-USING-TKINTER.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd NLP-APP-USING-TKINTER/Python_Tkinter-Project
    ```

3. **Install dependencies**:
    Ensure Python is installed, then install the required libraries using:
    ```bash
    pip install -r requirements.txt
    ```

4. **API Key Setup**:
   - Sign up for an account on [NLP Cloud](https://nlpcloud.io/).
   - Obtain your API key from the NLP Cloud dashboard.
   - Create a `.env` file in the project directory and add your API key:
     ```bash
     NLP_CLOUD_API_KEY=your_api_key_here
     ```

## How to Run

1. Start the application by running:
    ```bash
    python app.py
    ```

2. The GUI will open, allowing you to input text and select the desired NLP task.

3. Results from the NLP Cloud API will be displayed within the app, and data will be stored in a local JSON file for future reference.

## Dependencies

- **Tkinter**: For building the graphical user interface.
- **NLP Cloud API**: Used for processing various NLP tasks.
- **Requests**: For making API calls to NLP Cloud.
- **JSON**: Used for managing local storage of user data.
- **Python-dotenv**: For managing API key security via environment variables.

## Configuration

Make sure your `.env` file contains the following line with your personal API key:
```bash
NLP_CLOUD_API_KEY=your_api_key_here
