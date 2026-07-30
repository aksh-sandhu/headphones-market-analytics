from database.connection import DB
import pandas as pd

class overview_query(DB):

# overview page queries

  def product_count(self):

    self.mycursor.execute("""
    SELECT COUNT(*) FROM headphones_aksh.headphones
    """)
    data = self.mycursor.fetchone()
    return data[0]

  def avg_price(self):

    self.mycursor.execute("""
    SELECT ROUND(AVG(price),2) FROM headphones_aksh.headphones
    """)
    data = self.mycursor.fetchone()
    return data[0]

  def avg_rating(self):

    self.mycursor.execute("""
    SELECT ROUND(AVG(stars),2) FROM headphones_aksh.headphones
    """)
    data = self.mycursor.fetchone()
    return data[0]


  def total_company(self):

    self.mycursor.execute("""
    SELECT COUNT(*) FROM (SELECT DISTINCT company FROM headphones_aksh.headphones) t1
    """)
    data = self.mycursor.fetchone()
    return data[0]

  def wireless_percent(self):

    self.mycursor.execute("""
    WITH wireless AS(SELECT COUNT(*) AS wireless_count FROM headphones_aksh.headphones WHERE connectivity = 'wireless'),
    total AS (SELECT COUNT(*) AS total FROM headphones_aksh.headphones WHERE connectivity IS NOT NULL)
    SELECT ROUND((w1.wireless_count / t.total*100),2)

    FROM wireless w1
    JOIN total t
    """)

    data = self.mycursor.fetchone()
    return data[0]


  def wired_percent(self):
    self.mycursor.execute("""
    WITH wired AS(SELECT COUNT(*) AS wired_count FROM headphones_aksh.headphones WHERE connectivity = 'wired'),
    total AS (SELECT COUNT(*) AS total FROM headphones_aksh.headphones WHERE connectivity IS NOT NULL)
    SELECT ROUND((w1.wired_count / t.total*100),2)

    FROM wired w1
    JOIN total t
    """)

    data = self.mycursor.fetchone()
    return data[0]


  def top_count_company(self):
    company,count=[],[]

    self.mycursor.execute("""
    SELECT company,COUNT(*) FROM headphones_aksh.headphones
    GROUP BY company
    ORDER BY COUNT(*) DESC LIMIT 20
    """)

    data = self.mycursor.fetchall()
    for i in data:
      company.append(i[0])
      count.append(i[1])

    return company,count


  def price_tier(self):
    tier,count = [],[]
    self.mycursor.execute("""
    SELECT price_tier,COUNT(*) FROM headphones_aksh.headphones
    GROUP BY price_tier
    """)

    data = self.mycursor.fetchall()

    for i in data:
      tier.append(i[0])
      count.append(i[1])

    return tier,count


  def top_avg_price(self):
    company,avg_price=[],[]

    self.mycursor.execute("""
    SELECT company,ROUND(AVG(price),2) FROM headphones_aksh.headphones
    GROUP BY company
    ORDER BY ROUND(AVG(price)) DESC LIMIT 15
    """)

    data = self.mycursor.fetchall()

    for i in data:
      company.append(i[0])
      avg_price.append(i[1])

    return company,avg_price

# market_insights page queries

class market_insights_query(DB):

  def price_distribution_budget(self):
    price = []
    self.mycursor.execute("""
    SELECT price FROM headphones_aksh.headphones
    WHERE price IS NOT NULL AND price_tier = 'budget'
    """)

    data = self.mycursor.fetchall()

    for i in data:
      price.append(i[0])

    return price

  def price_distribution_mid(self):
    price = []
    self.mycursor.execute("""
    SELECT price FROM headphones_aksh.headphones
    WHERE price IS NOT NULL AND price_tier = 'mid range'
    """)

    data = self.mycursor.fetchall()

    for i in data:
      price.append(i[0])

    return price


  def price_distribution_premium(self):
    price = []
    self.mycursor.execute("""
    SELECT price FROM headphones_aksh.headphones
    WHERE price IS NOT NULL AND price_tier = 'premium'
    """)
    data = self.mycursor.fetchall()
    for i in data:
      price.append(i[0])
    return price

  def price_distribution_luxury(self):
    price = []
    self.mycursor.execute("""
    SELECT price FROM headphones_aksh.headphones
    WHERE price IS NOT NULL AND price_tier = 'luxury'
    """)
    data = self.mycursor.fetchall()
    for i in data:
      price.append(i[0])
    return price


# Brand Analysis

class brand_analysis_query(DB):

  def total_brands(self):
    self.mycursor.execute('SELECT COUNT(DISTINCT company) FROM headphones_aksh.headphones')
    data = self.mycursor.fetchone()
    return data[0]

  def largest_brand(self):

    self.mycursor.execute('''
    SELECT company, COUNT(*) AS 'count'
    FROM headphones_aksh.headphones
    GROUP BY company
    ORDER BY COUNT(*) DESC LIMIT 1
    ''')
    data = self.mycursor.fetchall()
    name = data[0][0]
    count = data[0][1]

    return name,count

  def most_expensive_brand(self):

    self.mycursor.execute('''
    SELECT company, ROUND(AVG(price),2) AS average_price FROM headphones_aksh.headphones
    GROUP BY company
    ORDER BY ROUND(AVG(price),2) DESC LIMIT 1
    ''')

    data = self.mycursor.fetchall()
    name = data[0][0]
    price = data[0][1]

    return name,price





# About dataset page queries
class about_dataset_query(DB):

  def data_overview(self):

    self.mycursor.execute("""
    SELECT * FROM headphones_aksh.headphones LIMIT 5
    """)
    data = self.mycursor.fetchall()
    columns = [col[0] for col in self.mycursor.description]
    return pd.DataFrame(data, columns=columns)

  def button_pressed(self):
    self.mycursor.execute("""
    SELECT * FROM headphones_aksh.headphones
    ORDER BY RAND() LIMIT 5
    """)
    data = self.mycursor.fetchall()
    columns = [col[0] for col in self.mycursor.description]
    return pd.DataFrame(data, columns=columns)

