from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    # Render the main form for personality prediction
    return render_template('index.html')

# Load the trained model
model = pickle.load(open('personality.pkl', 'rb'))

# Define a dictionary to map prediction numbers to personality types
personality_map = {
    1: "Inspiring",
    2: "Entertainer",
    3: "Thinker",
    4: "Idealist",
    5: "Charismatic",
    6: "Innovator",
    7: "Adventurer",
    8: "Craftsman",
    9: "Strategist",
    10: "Visionary",
    11: "Artist",
    12: "Leader",
    13: "Supporter",
    14: "Caretaker",
    15: "Organizer",
    16: "Manager"
}

@app.route('/predict', methods=['GET', 'POST'])
def predict_personality():
    # Retrieve the form data
    age = request.form.get('age')
    gender = request.form.get('gender')
    education = request.form.get('education')
    introversion = request.form.get('introversion')
    sensing = request.form.get('sensing')
    thinking = request.form.get('thinking')
    judging = request.form.get('judging')
    interest = request.form.get('interest')

    print(f"Received form data: age={age}, gender={gender}, education={education}, introversion={introversion}, sensing={sensing}, thinking={thinking}, judging={judging}, interest={interest}")

    # Validate form data
    if None in [age, gender, education, introversion, sensing, thinking, judging, interest]:
        return jsonify({'error': 'All form fields must be provided'}), 400

    # Prepare the input DataFrame for prediction with correct feature names
    input_features = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Education': [education],
        'Introversion Score': [introversion],
        'Sensing Score': [sensing],
        'Thinking Score': [thinking],
        'Judging Score': [judging],
        'Interest': [interest]
    })
    print(f"Input features DataFrame:\n{input_features}")

    # Make prediction
    prediction = model.predict(input_features)
    # Convert prediction to native Python type
    personality_prediction = int(prediction[0])
    print(f"Prediction: {personality_prediction}")

    # Map the prediction number to a personality type
    personality_type = personality_map.get(personality_prediction, "Unknown")

    # Return the prediction and personality type as a JSON response
    return jsonify({
        'personality_type': personality_type
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
