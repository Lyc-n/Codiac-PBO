import hashlib
import os
import sqlite3

class AuthDB:
    def __init__(self):
        self.db_path = "data/users.db"
        self.__init_db()

    def __connect(self):
        return sqlite3.connect(self.db_path)

    def __init_db(self):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                nama TEXT PRIMARY KEY,
                email TEXT NOT NULL,
                salt TEXT NOT NULL,
                paswd TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def __hash_password(self, password, salt=None):
        if not salt:
            salt = os.urandom(16).hex()  # Salt acak baru
        combined = salt + password
        hashed = hashlib.sha256(combined.encode()).hexdigest()
        return salt, hashed

    def register_user(self, nama, email, password):
        conn = self.__connect()
        c = conn.cursor()

        salt, hashed = self.__hash_password(password)
        try:
            c.execute("INSERT INTO users (nama, email, salt, paswd) VALUES (?, ?, ?, ?)", (nama, email, salt, hashed))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    def login_user(self, nama, password):
        conn = self.__connect()
        c = conn.cursor()
        c.execute("SELECT salt, paswd FROM users WHERE nama = ?", (nama,))
        row = c.fetchone()
        conn.close()

        if row:
            salt, stored_hash = row
            _, hashed_input = self.__hash_password(password, salt)
            return hashed_input == stored_hash
        return False
        
        
#auth = HashlibAuth()

#auth.register_user("joko", "hamdal25")
# if auth.login_user("joko", "hamdal25"):
#   print("login sukses")
# else:
#   print("gagal bro...")