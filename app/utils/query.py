from app import mysql


def execute_query(query):
    try:
        cur = mysql.connection.cursor()
        cur.execute(query)
        result = cur.lastrowid
        mysql.connection.commit()
        cur.close()

        return True, result
    except Exception as e:
        return False, str(e)


def select_query(query):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        rows_data = cursor.fetchall()
        fields = tuple(map(lambda x: str(x[0]), cursor.description))
        data = list(map(lambda row: dict(zip(fields, row)), rows_data))
        cursor.close()

        return True, data
    except Exception as e:
        return False, str(e)
