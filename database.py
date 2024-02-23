import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)  VALUES (2,'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES ('Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)  VALUES ('Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES ('Mark', 25, 'Rich-Mond ', 65000.00 )");
conn.commit()
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID=",row[0])
    print("Name",row[1])
    print("Address=",row[2])
print("Opend Successfully")