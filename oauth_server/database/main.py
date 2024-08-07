import psycopg2

class OAuthDB():
    user = "testusr"
    db_name = "testdb"
    host = "localhost"
    password = "123"

    def __init__(self):
        # use default port for postgres 5432
        self.db_instance = psycopg2.connect(dbname=self.db_name, user=self.user, password=self.password, host=self.host)
        self.cursor = self.db_instance.cursor()

new_db = OAuthDB()

new_db.cursor.execute("SELECT current_user;")
op = new_db.cursor.fetchall()

print(op)