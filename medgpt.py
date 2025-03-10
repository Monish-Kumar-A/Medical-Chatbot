from flask import Flask, request, jsonify, render_template
import pandas as pd
from fuzzywuzzy import process

# Initialize Flask app
app = Flask(__name__)

# Load and preprocess the data
data = pd.read_csv('medicine_data.csv')  # Ensure the correct path
if data['medicine'].isnull().all():
    data['medicine'] = data['uses'].apply(lambda x: str(x).split(' ')[0] if pd.notnull(x) else None)
data['medicine'] = data['medicine'].fillna('Unknown').str.strip()

# Function for fuzzy matching chatbot logic
def chatbot_with_fuzzy(query, data):
    medicine_names = data['medicine'].dropna().tolist()
    extraction = process.extractOne(query, medicine_names)
    if extraction:
        match, score = extraction
    else:
        return "Sorry, I couldn't find information on that medicine."

    if score > 70:
        matched_row = data[data['medicine'] == match].iloc[0]
        if 'side effect' in query.lower():
            return f"Side effects of {match}: {matched_row['side effects']}"
        elif 'use' in query.lower():
            return f"Uses of {match}: {matched_row['uses']}"
        elif 'warning' in query.lower():
            return f"Warnings for {match}: {matched_row['warnings']}"
        elif 'dosage' in query.lower():
            return f"Dosage of {match}: {matched_row['dosage']}"
        else:
            return f"I found {match}. Please specify if you're asking about uses, side effects, warnings, or dosage."
    return "Sorry, I couldn't find information on that medicine."

# Routes
@app.route("/")

def home():

    return render_template("index.html")

@app.route("/chat", methods=["POST"])

def chat():

    user_input = request.json.get("query")

    if user_input.lower() in ["hi", "hello", "hey"]:
 
        return jsonify({"response": "Hello! How can I assist you today?"})
 
    elif user_input.lower() in ["bye", "quit", "exit"]:
 
        return jsonify({"response": "Thank you for chatting with me. Goodbye!"})
 
    response = chatbot_with_fuzzy(user_input, data)

    return jsonify({"response": response})

if __name__ == "__main__":

    app.run(debug=True)
