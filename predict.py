import pickle

model = pickle.load(open("notebooks/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("notebooks/vectorizer.pkl", "rb"))

message = input("Enter your message: ")

message_vector = vectorizer.transform([message])

prediction = model.predict(message_vector)

if prediction[0] == 1:
    print("🚨 Spam Message")
else:
    print("✅ Not Spam")