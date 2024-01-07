from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://avnadmin:AVNS_YpbojKNuIGzBgdfn43L@mst-careers-mst-careers.a.aivencloud.com/defaultdb?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ca": "ssl/ca.pem",
    }
  }
)

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs"))
  print(result.all())