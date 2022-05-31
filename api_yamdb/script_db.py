import csv
import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

with open('static/data/category.csv', 'r', encoding='utf-8') as cat:
    dr = csv.DictReader(cat, delimiter=",")
    to_db = [(row['id'], row['name'], row['slug']) for row in dr]
cur.executemany(
    "INSERT INTO reviews_category (id, name, slug) VALUES (?, ?, ?);",
    to_db)

with open('static/data/titles.csv', 'r', encoding='utf-8') as title:
    dr = csv.DictReader(title, delimiter=",")
    to_db = [
        (row['id'],
         row['name'],
            row['year'],
            row['description'],
            row['category_id']) for row in dr]

cur.executemany(
    "INSERT INTO reviews_title (id, name, year, description, category_id) VALUES\
        (?, ?, ?, ?, ?);",
    to_db)

with open('static/data/genre.csv', 'r', encoding='utf-8') as genre:
    dr = csv.DictReader(genre, delimiter=",")
    to_db = [(row['id'], row['name'], row['slug']) for row in dr]

cur.executemany(
    "INSERT INTO reviews_genre (id, name, slug) VALUES (?, ?, ?);",
    to_db)

with open('static/data/genre_title.csv', 'r', encoding='utf-8') as genre_title:
    dr = csv.DictReader(genre_title, delimiter=",")
    to_db = [(row['id'], row['title_id'], row['genre_id']) for row in dr]

cur.executemany(
    "INSERT INTO reviews_title_genre (id, title_id, genre_id)\
        VALUES (?, ?, ?);",
    to_db)

with open('static/data/comments.csv', 'r', encoding='utf-8') as comments:
    dr = csv.DictReader(comments, delimiter=",")
    to_db = [
        (row['id'],
         row['review_id'],
            row['text'],
            row['author_id'],
            row['pub_date']) for row in dr]

cur.executemany(
    "INSERT INTO reviews_comment (id, review_id, text, author_id, pub_date) VALUES\
        (?, ?, ?, ?, ?);",
    to_db)

with open('static/data/review.csv', 'r', encoding='utf-8') as review:
    dr = csv.DictReader(review, delimiter=",")
    to_db = [
        (row['id'],
         row['title_id'],
            row['text'],
            row['author_id'],
            row['score'],
            row['pub_date']) for row in dr]

cur.executemany(
    "INSERT INTO reviews_review (id, title_id, text, author_id, score, pub_date)\
        VALUES (?, ?, ?, ?, ?, ?);",
    to_db)

with open('static/data/users.csv', 'r', encoding='utf-8') as users:
    dr = csv.DictReader(users, delimiter=",")
    to_db = [
        (row['id'],
         row['password'],
            row['is_superuser'],
            row['username'],
            row['email'],
            row['role'],
            row['bio'],
            row['first_name'],
            row['last_name'],
            row['is_staff'],
            row['is_active'],
            row['date_joined'],
            row['confirmation_code']) for row in dr]

cur.executemany("INSERT INTO reviews_user (id,  password, is_superuser, username,\
     email, role, bio, first_name, last_name, is_staff, is_active,\
         date_joined, confirmation_code) VALUES\
             (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

con.commit()
con.close()
