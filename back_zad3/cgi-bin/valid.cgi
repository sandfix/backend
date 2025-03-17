#!/usr/bin/python3


import cgi
import re
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="u68796",
    password="8163276",
    database="u68796",
    ssl_disabled=True
)

cursor = conn.cursor()
user_query = "INSERT INTO users(fio,phone,email,dob,gender,bio) VALUES(%s,%s,%s,%s,%s,%s)"

fav_lang_query= """INSERT INTO fav_langs(user_id,lang_id)
SELECT u.id, l.id FROM
users u JOIN langs l ON l.name=%s
WHERE u.fio=%s"""

form = cgi.FieldStorage()
name = form.getvalue("fio")
phone = form.getvalue("phone")
email = form.getvalue("email")
dob = form.getvalue("dob")
gender = form.getvalue("gender")
lang = form.getvalue("languages")
bio = form.getvalue("biography","empty")
error = ""
flag = 0

data = (name,phone,email,dob,gender,bio)

if name is None or not re.fullmatch(r"[a-zA-Z ]{,150}",name):
    error = "name"
    flag = 1
if phone is None or not re.fullmatch(r"[0-9+]{1}[0-9- ]{0,20}", phone):
    error = "phone"
    flag = 1
if email is None or not re.fullmatch(r"^\S+@\S+$", email):
    error = "email"
    flag = 1
if dob is None or not re.fullmatch(r"^\d{4}-\d\d-\d\d$", dob):
    error = "date of birthday"
    flag = 1
if lang is None:
    error = "language"
    flag = 1
if gender is None:
    error = "gender"

print("Content-Type: text/html\n")

if flag==1:
    print(f"""
    <html lang="ru">
    <head>
    <meta charset="UTF-8">
    </head>
    <body>
    <h1>Error: {error}</h1>
    </body>
    </html>
    """) 
else:
    if not isinstance(lang, list):
        lang = [lang]
    # tp = type(lang[0])
    print(f"""
    <html>
    <body>
    <h1>ALL GOOD</h1>
    </body>
    </html>
    """)
    cursor.execute(user_query,data)
    conn.commit()
    for item in lang:
        cursor.execute(fav_lang_query,(item, name))
        conn.commit()
cursor.close()
conn.close()
