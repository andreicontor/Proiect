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
# conex.commit()


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
    ('Maria', 43, 100)
"""

get_query = "SELECT varsta FROM client;"

get_special_query = "SELECT varsta FROM client WHERE nume = 'Ionut';"

# cursor.execute(get_special_query)
#
# client = cursor.fetchall()
#
# print(client)

# sa se actualizeze valoarea cosului clientului cu id-ul 2 in 400.

update_query = "UPDATE client SET valoare_cos = 400 WHERE ID = 2;"

cursor.execute(update_query)
conex.commit()

add_clients_query = """
    INSERT INTO client (nume, varsta, valoare_cos)
    VALUES
    ('Andrei', 25, 240),
    ('Alexa', 24, 59),
    ('Madalin', 33, 600)
"""

# cursor.execute(add_clients_query)
# conex.commit()

delete_query = "DELETE FROM client WHERE ID = 5;"

# cursor.execute(delete_query)
# conex.commit()

# get_query = "SELECT * FROM client;"
# cursor.execute(get_query)

# clienti = cursor.fetchall()
# for client in clienti:
#     print(client)


# Vreau sa se starga din baza de date id-ul cu numarul 3 doar daca valoare cosului este mai mare decat 100
# V1
# get_id = "SELECT id FROM client IF valoare_cos > 100;"
# if get_id:
#     delete_id = "DELETE FROM client WHERE ID = 3;"
#     cursor.execute(delete_id)
#     conex.commit()  

# V2
get_query = "SELECT * FROM client;"

cursor.execute(get_query)
#
valoare_cos = cursor.fetchone()
print(valoare_cos)


if int(valoare_cos[0]) > 100:
    delete_query = "DELETE FROM client WHERE ID = 4;"
    cursor.execute(delete_query)
    conex.commit()