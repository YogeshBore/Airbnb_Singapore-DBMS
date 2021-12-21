import pandas as pd
import sqlite3


class Room_Data:

    df = pd.read_csv('listings.csv')

    room_df = df[["id", "name", "latitude", "longitude", "price", "minimum_nights", "availability_365", "room_type",
                  "host_id"]].copy()

    # Data Cleaning - Adding values to room name for blank values
    room_df = room_df.drop_duplicates()
    room_df['name'] = room_df['name'].fillna("No-Name" + "_" + room_df['room_type'])

    room_df.reset_index(drop=True, inplace=True)

    # Create a roomtype id
    def makermid(data):
        if data['room_type'] == 'Private room':
            return 1
        elif data['room_type'] == 'Entire home/apt':
            return 2
        elif data['room_type'] == 'Shared room':
            return 3
        else:
            return 0

    room_df['room_type_id'] = room_df.apply(makermid, axis=1)
    del room_df['room_type']

    conn = sqlite3.connect("MyDB.db", timeout=10)
    c = conn.cursor()

    c.execute("SELECT count(name) from sqlite_master WHERE type='table' AND name='room'")
    if c.fetchone()[0] == 1:
        # c.execute("DELETE FROM room")
        c.execute("DROP Table room")
    else:
        c.execute(
            """CREATE TABLE room(id INTEGER,name TEXT,latitude REAL,longitude REAL,price REAL, minimum_nights INTEGER,
            availability_365 INTEGER,room_type_id INTEGER, host_id INTEGER,neighbourhood_id INTEGER,
             PRIMARY KEY(id),
             FOREIGN KEY (room_type_id) REFERENCES roomtype(room_type_id),
             FOREIGN KEY (host_id) REFERENCES host(host_id) ,    
             FOREIGN KEY (neighbourhood_id) REFERENCES nbh_data(neighbourhood_id)                                           
                 )""")

    room_df.to_sql('room', conn, if_exists='append', index=False)

    c.execute("SELECT * FROM room")

    conn.commit()
    conn.close()
    # Inserting multiple records using input_data excel file


    def room_data_insert(self):
        print("Please update the given input file for room data(Multiple Records can also update:")
        print("Inserting the room data from input file input_data ")
        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()

            room_input_data = pd.read_excel('input_data.xlsx')
            print(room_input_data.head())
            # id_test=room_input_data.loc['id']

            # print("Room ID",id_test,"\n")
            print("\n--------------------------------------")
            room_input_data.to_sql('room', conn, if_exists='append', index=False)

        except Exception as exp:
            print(exp)
        finally:
            conn.commit()
            conn.close()

    # Del func

    def Room_Data_Delete(self):

        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()
            print("Room ID Test Data:71907,56334")
            room_id_test = input("Please enter room_id:")
            c.execute("SELECT COUNT(*) from room WHERE id = :id", {"id": room_id_test})
            rowcount = c.fetchall()[0][0]
            # print(rowcount)
            if rowcount <= 0:
                print("No records founds for room id:", room_id_test)
            else:

                c.execute("DELETE from room WHERE id = :id", {"id": room_id_test})

                c.execute("SELECT COUNT(*) from room WHERE id = :id", {"id": room_id_test})

                conn.commit()

                temp = c.fetchall()[0][0]
                # print(temp)
                if temp >= 1:
                    print("Record is not deleted for Review id :", room_id_test)

                else:
                    print("Record deleted Successfully for room id :", room_id_test)

                    return 1

        except Exception as e:
            print(e)
            print("Please enter the valid data")
        finally:
            conn.commit()
            conn.commit()

        # update room Data

    def room_data_update(self):

        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()
            test_res = 1
            print("Room ID Test Data:71907,56334")
            room_id_test = int(input("Please enter Room_ID for which you want update:"))
            room_name_test = input("Please enter updated Room Name:")
            min_night_test = int(input("Please enter updated minimum nights  count:"))
            availability_test = int(input("Please enter the availability_test out of 365 days:"))
            room_price_test = int(input("Please enter room price:"))
            c.execute("Update room set name = :name, minimum_nights =:minimum_nights, availability_365 "
                      "=:availability_365, price =:price ""  where id = :id",
                      {"name": room_name_test,
                       "minimum_nights": min_night_test,
                       "availability_365": availability_test,
                       "price": room_price_test,
                       "id": room_id_test})

            c.execute("SELECT id from room WHERE id = :id", {"id": room_id_test})
            temp = c.fetchall()[0][0]
            print(temp)
            if temp == room_id_test:
                c.execute("SELECT * from room WHERE id = :id", {"id": room_id_test})
                updated = c.fetchall()
                print("\nRoom Data Updated Successfully \n['id','name','latitude, 'longitude',Price, "
                      "'minimum_nights','availability_365',host id,room id] => \n", updated)
                return test_res
            else:
                print("Record is not updated successfully")
                test_res = 0
                return test_res
        except Exception as e:
            print(e)
            print("\nPlease try with different data")
        finally:
            conn.commit()
            conn.close()

    def display_room_data(self):
        conn = sqlite3.connect("MyDB.db", timeout=10)
        c = conn.cursor()
        room_df = c.execute("SELECT * from room")
        room_df = pd.DataFrame(room_df)
        room_df.columns = ["id", "name", "latitude", "longitude", "price", "minimum_nights", "availability_365",
                           "host_id", "room_type_ID"]
        # print(room_df.info())
        print((room_df).head(10))
        conn.commit()
        conn.close()


#Room_Data_Obj = Room_Data()
# Room_Data_Obj.Room_Data_Delete()
# Room_Data_Obj.room_data_insert()

# Room_Data_Obj.Room_Data_Delete()
#Room_Data_Obj.display_room_data()
# Room_Data_Obj.room_data_update()
