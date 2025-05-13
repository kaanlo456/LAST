from config import DATABASE
from config import TOKEN
import sqlite3
import random

DB_PATH = DATABASE

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_random_recommendation(category=None, type=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT title, type, category FROM media"
    conditions = []
    params = []

    if category:
        conditions.append("category = ?")
        params.append(category.lower())

    if type:
        conditions.append("type = ?")
        params.append(type.lower())

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY RANDOM() LIMIT 1"

    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()

    if result:
        title, t, category = result
        return f"🎬 Öneri: **{title}**\nTür: {t.title()}, Kategori: {category.title()}"
    else:
        return "Bu kriterlere uygun bir içerik bulunamadı."
