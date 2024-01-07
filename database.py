import pymysql
import os

db_password = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']

timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host=db_host,
    password=db_password,
    read_timeout=timeout,
    port=17333,
    user="avnadmin",
    write_timeout=timeout,
)


def load_jobs_from_db():
  jobs = []
  try:
    with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM jobs")
      for row in cursor.fetchall():
        jobs.append(row)
  except Exception as e:
    # Handle the exception (print, log, or raise if    necessary)
    print(f"Error: {e}")
  return jobs
