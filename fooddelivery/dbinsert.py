import sqlite3

conn = sqlite3.connect('C:/Users/Admin/Desktop/foodizz/fooddelivery/site1.db')
print("DB connected sucessfully")
cursor = conn.cursor()
print("Connected to SQLite")

sqlite_insert_query = """insert into course(coid,catgry_id,coname)values(30,0,"Desserts") """
count=cursor.execute(sqlite_insert_query)
conn.commit()
print("Inserted sucessfully")
cursor.close()

if(conn):
    conn.close()
    print("Connection closed")
'''
def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(pid, name, cost, details, category_id,category_name, course_id, course_name, restro_id, image_file1,quantity,food_type,iaa,ibb,icc,idd,iee,iff):
    try:
        conn = sqlite3.connect('C:/Users/Admin/Desktop/Foodizz/fooddelivery/site1.db')
        cursor = conn.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """INSERT INTO product(pid, name, cost, details, category_id, category_name,course_id,course_name,restro_id, image_file1,quantity,food_type,iaa,ibb,icc,idd,iee,iff) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?)"""
        if image_file1:
            img1 = convertToBinaryData(image_file1)
        else:
            img1=None

        # Convert data into tuple format
        data_tuple = (pid, name, cost, details, category_id,category_name, course_id, course_name, restro_id, img1,quantity,food_type,iaa,ibb,icc,idd,iee,iff)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        conn.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")



insertBLOB(630012,"WINE CAKE",365, 
"Wine cake, known in Spanish as torta envinada, is a cake made with wine in Colombian cuisine.Torta negra Colombiana (Colombian black cake) and Bizcocho Negro are similar cakes with varying ingredients (raisins, candied fruit, and rum)", 
6, "CAKE AND PASTRIES",30,"Desserts",00, "C:/Users/Admin/Desktop/Foodizz/fooddelivery/static/c12.jpg"
,"500 GM","Non Veg","Energy : 470 Cal",
"Proteins : 7g",
"Carbohydrates : 59g",
"Fat : 13g",
"Fiber : 0.5g",
"Cholestrol : 10mg"










)

'''