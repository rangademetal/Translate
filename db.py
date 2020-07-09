import mariadb

def insert(sent, sentences, corect):
    try:
        con = mariadb.connect(user='root', password='Sad1996.', host='127.0.0.1', port=3306)

        cursor = con.cursor()
        cursor.execute('USE translate')
        sql = 'INSERT INTO translate(sentences, sentenceexpect, correct) vALUEs(%s, %s, %s)'
        param = (sent, sentences, corect)
        cursor.execute(sql, param)
        con.commit()
    except mariadb.Error as e:
        print(f'Error: {e}')