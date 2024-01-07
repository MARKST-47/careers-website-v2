import pymysql

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mst-careers-mst-careers.a.aivencloud.com",
  password="AVNS_YpbojKNuIGzBgdfn43L",
  read_timeout=timeout,
  port=17333,
  user="avnadmin",
  write_timeout=timeout,
)

def load_jobs_from_db():
  jobs = []
  try:
      cursor = connection.cursor()
      cursor.execute("SELECT * FROM jobs")
      for row in cursor.fetchall():
          jobs.append(row)
  except Exception as e:
      # Handle the exception (print, log, or raise if    necessary)
      print(f"Error: {e}")
  return jobs