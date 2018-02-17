import secure
import pymysql

class DatabaseConnection:
   
    host = secure.host
    db = secure.db
    username = secure.username
    password = secure.password
    
    conn = None

    def __init__(self):
        self.conn = pymysql.connect(self.host, user=self.username, passwd=self.password, db=self.db, connect_timeout=5)

    def insert_torrent(self, torrent):
        cur = self.conn.cursor()
        sql = 'INSERT INTO torrent VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        cur.execute(sql, (torrent.id, torrent.exists, torrent.title, torrent.desc, torrent.magnet, torrent.seeders, torrent.leachers, torrent.upload_date, torrent.num_comments, torrent.user, torrent.info_hash))
        self.conn.commit()
        
