from flask import Flask, jsonify, render_template
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  Jobs = load_jobs_from_db()
  return render_template('home.html', jobs=Jobs, company_name='MST')

@app.route("/api/jobs")
def list_jobs():
  Jobs = load_jobs_from_db()
  return jsonify(Jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  return jsonify(job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)