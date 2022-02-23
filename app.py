from flask import Flask, render_template
from flask_sqlalchemy import  SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///notes.db" #"mysql://root@localhost/notes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] ='False' # to suppress warnings
db=SQLAlchemy(app)

#create model 
class Notes(db.Model):
    srNo = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500))
    date_created = db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.title}"


@app.route("/")
def hello_world():
    #return "<p>Hello, World!</p>"
    return render_template("index.html")

@app.route("/products")
def products():
    return "<p>this is product page</p>"

if __name__ == "__main__":
    app.run(debug=True , port = 8000)  # debug=true helps to give error in browser, default port 5000
