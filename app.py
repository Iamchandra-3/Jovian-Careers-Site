from flask import Flask, render_template 

app = Flask(__name__)

JOBS = [

{

    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
},
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'New York',
    'salary': '$100,000'
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Remote',
    # 'salary': '$100,000'
  },
  {
    'id': 4,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '$100,000'
  }
  
]

@app.route("/")
def hello_jovian():
  return render_template('home.html',jobs=JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
