import sqlite3
import os
from config import DATABASE
DB_PATH = DATABASE

def get_connection():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Veritabanı dosyası bulunamadı: {DB_PATH}")
    return sqlite3.connect(DB_PATH)

def get_random_recommendation(category=None, media_type=None):
    """
    large_database.db veritabanından rastgele bir film, dizi ya da belgesel önerir.
    İsteğe bağlı olarak kategori ve tür filtreleri uygulanabilir.
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT title, type, category FROM media"
    conditions = []
    params = []

    if category:
        conditions.append("LOWER(category) = ?")
        params.append(category.lower())

    if media_type:
        conditions.append("LOWER(type) = ?")
        params.append(media_type.lower())

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY RANDOM() LIMIT 1"

    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()

    if result:
        title, mtype, category = result
        return f"🎬 Öneri: {title}\n📺 Tür: {mtype.title()}\n🎭 Kategori: {category.title()}"
    else:
        return "❌ Uygun içerik bulunamadı."

# Test için çalıştırıldığında birkaç örnek öneri üretir
if __name__ == "__main__":
    print(get_random_recommendation())  # Rastgele öneri
    print(get_random_recommendation(media_type="dizi"))  # Sadece dizilerden
    print(get_random_recommendation(category="komedi"))  # Sadece komedi
    print(get_random_recommendation(category="bilim kurgu", media_type="film"))  # Bilim kurgu filmleri
