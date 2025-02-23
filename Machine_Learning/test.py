import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes

# Load the trained model and tokenizer
MODEL_PATH = "./content/distilbert_sentiment_model"  # Update with your model path
tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

# Sentiment label mapping
label_map = {0: "positive", 1: "neutral", 2: "negative", 3: "irrelevant"}

# Function to predict sentiment probabilities
def predict_sentiment_probabilities(text):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=64)

    # Get model outputs
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits  # Raw predictions (logits)

    # Apply softmax to get probabilities
    probs = torch.nn.functional.softmax(logits, dim=-1).squeeze().numpy()

    # Convert numpy float32 to regular Python float
    prob_dist = {label_map[i]: float(prob) for i, prob in enumerate(probs * 100)}

    return prob_dist




# Route for sentiment prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"error": "Invalid request. 'query' key missing"}), 400

        text = data["query"]
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    # Get the sentiment probabilities
    probabilities = predict_sentiment_probabilities(text)

    # Create the result structure with proper float conversion
    results = {
        "distribution": probabilities,
        "tweets": [
            {
                "id": "1",
                "text": "I love this product!",
                "sentiment": "positive",
                "score": probabilities.get("positive", 0),
            },
            {
                "id": "2",
                "text": "This is the worst experience ever.",
                "sentiment": "negative",
                "score": probabilities.get("negative", 0),
            },
            {
                "id": "3",
                "text": "Just bought a new phone.",
                "sentiment": "neutral",
                "score": probabilities.get("neutral", 0),
            },
            {
                "id": "3",
                "text": "I am going home.",
                "sentiment": "irrelevant",
                "score": probabilities.get("irrelevant", 0),
            },
        ],
    }
    print(results)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
