from flask import Flask, jsonify, render_template
from database import load_jobs_from_db

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist', 
    'location': 'Texas, USA',
    'salary': 'Rs. 16,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': 'Rs. 14,00,000'
  }
]

@app.route("/")
def hello_world():
  Jobs = load_jobs_from_db()
  return render_template('home.html', jobs=Jobs, company_name='MST')

@app.route("/api/jobs")
def list_jobs():
  Jobs = load_jobs_from_db()
  return jsonify(Jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)