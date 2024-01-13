import psycopg2

class PostgresDB:
    def __init__(self, dbname, user, password, host):
        self.connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        self.cursor = self.connection.cursor()

    def insert(self, query, values):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        except psycopg2.Error as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()

    def update(self, query, values):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        except psycopg2.Error as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()

    def delete(self, query, values):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        except psycopg2.Error as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()

    def select(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"An error occurred: {e}")
            return None

    def close(self):
        self.cursor.close()
        self.connection.close()


if __name__=='__main__':
    #conn=psycopg2.connect(host='0.0.0.0', database='eco_behavior', user='postgres',password='123456')
    pd=PostgresDB(dbname='eco_behavior',user='postgres',host='0.0.0.0',password='123456')
    #insert test
    #value=(123,'ali','ali', False, False,'2023-04-29','','',10,10,10,'2023-12-01')
    #pd.insert("""insert into users (user_id,user_name, acct, bot, group_, create_datetime, url, uri, followers_count, following_count,status_count, last_status) values (%s,%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)""",values=value)
    #pd.close()

    #select text

    #data=pd.select("""select * from users""")
    #print(data)
    #pd.close()

    #update test

    pd.update("""update users set user_name=%s where user_id=%s""",('ali123',123))
    pd.close()