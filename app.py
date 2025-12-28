from flask import Flask, render_template, request
import pickle

tokenizer = pickle.load(open("cv.pkl", "rb"))
model = pickle.load(open("clf.pkl", "rb"))


app = Flask(__name__, template_folder="Template")

@app.route("/", methods=["GET", "POST"])
def home():
    text=""
    if request.method == "POST":
        text = request.form.get('email-content')
    return render_template("index.html", text=text)
    
if __name__=="__main__":
    app.run(debug=True)
    
    
