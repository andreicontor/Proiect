import mysql.connector

hostname = "127.0.0.1"
username = "root"
password = ""
port = 33066

conex = mysql.connector.connect(host = hostname,
                                user = username,
                                password = password,
                                port = port)

cursor = conex.cursor()

create_query = "CREATE DATABASE IF NOT EXISTS magazin;"

# cursor.execute(create_query)

select_query = "USE magazin;"

cursor.execute(select_query)

create_query = """
    CREATE TABLE IF NOT EXISTS client(
        id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        nume VARCHAR(30) NOT NULL,
        varsta INT NOT NULL,
        valoare_cos INT NOT NULL
    );
"""

# cursor.execute(create_query)

conex.commit()

conex.close()

conex = mysql.connector.connect(host = hostname,
                                user = username,
                                password = password,
                                port = port,
                                database = "magazin")

cursor = conex.cursor()

add_clients_query = """
    INSERT INTO client (nume, varsta, valoare_cos)
    VALUES
    ('Mihai', 20, 140),
    ('Ionut', 14, 19),
    ('Maria', 43, 180)
"""

# cursor.execute(add_clients_query)
#
# conex.commit()

get_query = "SELECT * FROM client;"

get_special_query = "SELECT varsta FROM client WHERE nume = 'Ionut';"

# cursor.execute(get_special_query)
#
# client = cursor.fetchone()
#
# print(client)

# sa se actualizeze valoarea cosului clientului cu id-ul 2 in 400 .

update_query = "UPDATE client SET valoare_cos = 400 WHERE ID = 2;"

# cursor.execute(update_query)
#
# conex.commit()

add_clients_query = """
    INSERT INTO client (nume, varsta, valoare_cos)
    VALUES
    ('Andreea', 9, 10),
    ('Filip', 49, 189),
    ('Radu', 30, 78)
"""
# cursor.execute(add_clients_query)
#
# conex.commit()

delete_query = "DELETE FROM client WHERE ID = 5;"

# cursor.execute(delete_query)
# conex.commit()
#
# get_query = "SELECT * FROM client;"
# cursor.execute(get_query)

# clienti = cursor.fetchall()
# for client in clienti:
#     print(client)


# Vreau sa se stearga din baza de date id-ul cu numarul 3 doar daca valoarea cosului este mai mare de 100 de lei
# 1. get pe id 3 -> ca sa vedem dacac stergem sau nu
# 2. stergem doar daca valoarea cosului este mai mare de 100

get_query = "SELECT valoare_cos FROM client WHERE ID = 3;"

cursor.execute(get_query)

valoare_cos = cursor.fetchone()
print(valoare_cos)

if int(valoare_cos[0]) > 100:
    delete_query = "DELETE FROM client WHERE ID = 3;"
    cursor.execute(delete_query)
    conex.commit()