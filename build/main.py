import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
import re
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove numbers and punctuation
    text = re.sub('[^a-zA-Z]', ' ', text)
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if not word in stop_words]
    
    # Join the tokens back into a string
    text = ' '.join(tokens)
    
    return text

# Load the IMDB dataset
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

# Pad the sequences to a fixed length
x_train = sequence.pad_sequences(x_train, maxlen=500)
x_test = sequence.pad_sequences(x_test, maxlen=500)

# Define the RNN model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=10000, output_dim=32),
    tf.keras.layers.SimpleRNN(units=32),
    tf.keras.layers.Dense(units=1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.2)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)

# Predict the sentiment of new text data
text = "This is a great movie"
sentiment = model.predict(preprocess_text(text))
if sentiment > 0.5:
    print("Positive sentiment")
else:
    print("Negative sentiment")
