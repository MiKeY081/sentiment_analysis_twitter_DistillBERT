
# Sentiment Analysis of Tweets

This project performs sentiment analysis on tweets using a machine learning model trained on DistilBERT. It consists of a backend API built with Flask that processes text input, runs sentiment analysis, and returns results. The frontend is a React application that displays sentiment distribution and lists of tweets categorized by sentiment.

## Features

- Sentiment distribution visualized using a pie chart.
- Categorizes tweets into Positive, Negative, Neutral, and Irrelevant sentiments.
- Interactive search bar to analyze sentiment for specific keywords or hashtags.
  
## Tech Stack

- **Frontend**: React, TypeScript, Recharts, Tailwind CSS
- **Backend**: Flask, PyTorch, Transformers (DistilBERT)
- **Machine Learning Model**: DistilBERT for sequence classification

## Prerequisites

Ensure you have the following installed on your machine:

- [Node.js](https://nodejs.org/) (v14 or later)
- [Python](https://www.python.org/downloads/) (v3.7 or later)
- [pip](https://pip.pypa.io/en/stable/) (Python package manager)
- [git](https://git-scm.com/)

## Project Structure

```
Sentiment_Analysis/
├── backend/                  # Flask Backend
│   ├── app.py                # Flask API entry point
│   ├── model/                # Trained DistilBERT model
│   ├── requirements.txt      # Backend dependencies
│   └── ...
└── frontend/                 # React Frontend
    ├── src/
    ├── public/
    ├── package.json          # Frontend dependencies
    └── ...
```

## Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/sentiment-analysis.git
cd sentiment-analysis
```

### Step 2: Backend Setup

1. Navigate to the `backend` folder:

    ```bash
    cd backend
    ```

2. Create and activate a Python virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install required backend dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have your trained DistilBERT model in the `backend/model` directory. If not, update the `MODEL_PATH` in `app.py` with the correct path to the model.

5. Run the Flask API:

    ```bash
    python app.py
    ```

The backend will be running on `http://127.0.0.1:5000`.

### Step 3: Frontend Setup

1. Navigate to the `frontend` folder:

    ```bash
    cd frontend
    ```

2. Install required frontend dependencies:

    ```bash
    npm install
    ```

3. Start the frontend React application:

    ```bash
    npm start
    ```

The frontend will be running on `http://localhost:3000`.

### Step 4: Testing the Application

1. Open your browser and navigate to `http://localhost:3000`.
2. Enter a keyword or hashtag into the search bar to perform sentiment analysis.
3. View the sentiment distribution chart and tweet lists categorized by sentiment.

### Step 5: Optional Configuration

- To modify the sentiment analysis model, update the model files in the `backend/model` directory.
- You can change the frontend styling or chart colors by modifying the `SentimentChart` component in the `frontend` folder.

## Usage

- **POST Request**: Send a POST request to `http://127.0.0.1:5000/predict` with a JSON payload containing the query for sentiment analysis.

    Example request:

    ```json
    {
      "query": "iPhone"
    }
    ```

# sentiment_analysis_twitter_DistillBERT
