import pymysql


class DBConnect:

    def __init__(self):
        pass

    def __connect(self, db):
        """

        :param db:
        :return:
        """
        user = 'wp487'
        port = '3306'
        port_int = int(port)
        host = '127.0.0.1'

        conn = pymysql.connect(host=host, port=port_int, user=user, password='Sl4C[!g4p3', db=db)
        return conn

    def select(self, db, query):
        """

        :param db:
        :param query:
        :return:
        """
        conn = self.__connect(db)
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()

        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col))  # convert each variable
            # row_list = list(row)
            all_rows.append(row)
            return all_rows

        conn.close()  # closing the DB connection
        cur.close()  # clearing the cursor

    def update(self, db, query):
        """

        :param db:
        :param query:
        :return:
        """
        # create connection
        conn = self.__connect(db)
        cur = conn.cursor()

        # execute the query
        result = cur.execute(query)
        conn.commit()
        conn.close()
        cur.close()

        return result
