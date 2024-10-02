# personality_prediction
Here’s a more detailed and technical description of your project:

This project is an end-to-end machine learning solution designed to predict personality types based on users’ responses to questions about social behaviors. The dataset, sourced from Kaggle, includes features such as age, gender, education, introvertness, sensitivity, thinking style, judgment preferences, and specific interests like sports, technology, and arts.

The Random Forest algorithm was selected due to its ability to handle complex data structures and prevent overfitting through ensemble learning. Key libraries used include pandas and numpy for data preprocessing, file type conversion, and feature engineering. Feature selection ensured that the most relevant variables, such as personality traits and interests, contributed to the prediction model.

The model achieved an accuracy of 80% following hyperparameter tuning and was evaluated using metrics like accuracy, precision, recall, and F1-score. Flask was used for the development of a web interface, where users can input their behavioral characteristics to receive real-time predictions. The entire application was deployed on AWS EC2, leveraging its scalability for web hosting. Although no specific techniques were implemented for class imbalance, the model performed reliably on the provided dataset, demonstrating strong predictive power for personality classification.
