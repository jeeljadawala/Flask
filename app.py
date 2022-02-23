from flask import Flask, render_template, request , redirect
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


@app.route("/", methods=['post','get']) # need to pass he type of req used in func 
def hello_world():
    # in below code, no.of times the browser is reloaded , this entry will be added--> check in sqlite viewer
    # note= Notes(title = "First note", desc ="Lets go")
    # db.session.add(note)
    # db.session.commit() 
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        note = Notes(title=title, desc=desc)
        db.session.add(note)
        db.session.commit()
        
    allNotes = Notes.query.all()
    print(allNotes)
    #return "<p>Hello, World!</p>"
    return render_template("index.html", allNotes=allNotes)  

@app.route('/show')
def list():  # list 
    allNotes = Notes.query.all()
    print(allNotes)
    return 'this is products page'

@app.route('/update/<int:srNo>', methods=['GET', 'POST'])
def update(srNo):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        note = Notes.query.filter_by(srNo=srNo).first()
        note.title = title
        note.desc = desc
        db.session.add(note)
        db.session.commit()
        return redirect("/")
        
    note = Notes.query.filter_by(srNo=srNo).first()
    return render_template('update.html', note=note)

@app.route('/delete/<int:srNo>')
def delete(srNo):
    note = Notes.query.filter_by(srNo=srNo).first()
    db.session.delete(note)
    db.session.commit()
    return redirect("/")


@app.route("/products")
def products():
    return "<p>this is product page</p>"

if __name__ == "__main__":
    app.run(debug=True , port = 8000)  # debug=true helps to give error in browser, default port 5000
