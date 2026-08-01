import mysql.connector
from config import config

class DB():

  def __init__(self):
    try:
      self.conn = mysql.connector.connect(
          host = config.HOST,
          user = config.USER,
          password = config.PASSWORD,
          database = config.DATABASE
        )
      self.mycursor = self.conn.cursor()
      print('Connection Successful')

    except Exception as e:
      print("Connection Error")
      print(e)

