import sqlite3

# Connect to DB
conn = sqlite3.connect("cp-store.db")
# Es necesario un cursor 
c = conn.cursor()

c.execute(
    '''
    SELECT * FROM usuarios;
    '''
)

print(c.fetchmany(2))


conn.commit()
conn.close()