from flask import Flask, render_template, request
import pickle

cv = pickle.load(open("Models/cv.pkl", "rb"))
clf = pickle.load(open("Models/clf.pkl", "rb"))


app = Flask(__name__, template_folder="Template")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])

def predict():
    email = request.form.get("content")
    tokenized_email = cv.transform([email])
    prediction = clf.predict(tokenized_email)
    prediction = 1 if prediction == 1 else -1
    return render_template("index.html", prediction=prediction, email_text=email)
    
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    