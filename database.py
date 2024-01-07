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

try:
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM jobs")
  result_dicts = []
  for row in cursor.fetchall():
    result_dicts.append(row)
  print(result_dicts)
finally:
  connection.close()