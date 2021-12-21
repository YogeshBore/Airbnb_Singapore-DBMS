import pandas as pd
import sqlite3


class Room_type:
    df = pd.read_csv('listings.csv')
    room_type_df = df[["room_type"]].copy()

    room_type_df = room_type_df.drop_duplicates()
    room_type_df.reset_index(drop=True, inplace=True)

    # print(room_type_df)

    # Make a roomtypeid
    def makermid(data):
        if data['room_type'] == 'Private room':
            return 1
        elif data['room_type'] == 'Entire home/apt':
            return 2
        elif data['room_type'] == 'Shared room':
            return 3
        else:
            return 4

    room_type_df['room_type_id'] = room_type_df.apply(makermid, axis=1)
    # del room_df['room_type']
    # print(room_df['room_type_id'])

    conn = sqlite3.connect("MyDB.db", timeout=10)
    c = conn.cursor()

    c.execute("SELECT count(name) from sqlite_master WHERE type='table' AND name='roomtype'")
    if c.fetchone()[0] == 1:
        c.execute("DELETE FROM roomtype")
    else:
        c.execute("""CREATE table roomtype(room_type_id INTEGER, room_type TEXT,PRIMARY KEY(room_type_id))""")

    room_type_df.to_sql("roomtype", conn, if_exists='append', index=False)

    # c.execute("SELECT * FROM roomtype")
    # print(c.fetchall())

    conn.commit()
    conn.close()

    # Insert New roomtype
    def room_type_insert(self):
        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()
            room_type_id_test = int(input("Please enter room_type_id:"))
            room_type_name_test = input("Please enter room_type_name:")
            print(room_type_id_test)
            c.execute("INSERT INTO roomtype VALUES(:room_type_id,:room_type)",
                      {"room_type_id": room_type_id_test, "room_type": room_type_name_test})
            c.execute("SELECT room_type_id from roomtype WHERE room_type_id = :room_type_id",
                      {"room_type_id": int(room_type_id_test)})
            temp = c.fetchall()[0][0]

            if str(temp) == str(room_type_id_test):
                print("Record inserted Successfully")
                c.execute("SELECT * from roomtype WHERE room_type_id = :room_type_id",
                          {"room_type_id": int(room_type_id_test)})
                temp = c.fetchall()
                print("[Room type ID, Room type]=>", temp)
                # conn.commit()
                return 1
            else:
                print("Record is not inserted successfully")
                # conn.commit()
                return 0
        except Exception as e:
            print("Please try with different data")
            print(e)
        finally:
            conn.commit()
            conn.close()

    def Roomtype_Update(self):
        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()
            print("Sample roomtype id: 1,2,3")
            roomtype_id_test = input("Please enter Roomtype_ID for which you want update:")
            roomtype_id_test = int(roomtype_id_test)

            ls = [1, 2, 3, 4]

            if (roomtype_id_test in ls):
                roomtype_test = input("Please enter updated room type name given room id:")
                roomtype_test = str(roomtype_test)

                c.execute(
                    'UPDATE roomtype SET room_type=:room_type WHERE room_type_id=:room_type_id',
                    {'room_type_id': roomtype_id_test, 'room_type': roomtype_test})

                conn.commit()
                c.execute("SELECT room_type_id from roomtype WHERE room_type_id = :room_type_id",
                          {"room_type_id": roomtype_id_test})
                temp = c.fetchall()[0][0]
                # print(temp)
                # (type(roomtype_id_test))

                if temp == roomtype_id_test:
                    print("Record updated Successfully")
                    c.execute("SELECT * from roomtype WHERE room_type_id = :room_type_id",
                              {"room_type_id": roomtype_id_test})
                    temp = c.fetchall()
                    print(temp)
                    conn.commit()
                    return 1
                else:
                    print("Record is not updated successfully")
                    conn.commit()
                    return 0
            else:
                print("Sorry for given room id no records available ")

        except Exception:
            # print(e)
            print("Please try with different data entered Host-ID is not exist")
        finally:
            conn.commit()
            conn.close()

        # Delete host data

        # Del func

    def room_Data_Delete(self):

        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()
            print("Sample roomtype id: 1,2,3")
            room_id = input("Please enter room_id:")
            c.execute("SELECT COUNT(*) from roomtype WHERE room_type_id = :room_type_id", {"room_type_id": room_id})
            rowcount = c.fetchall()[0][0]
            # print(rowcount)
            if rowcount <= 0:
                print("No records founds for  room_type_id:", room_id)
            else:

                c.execute("DELETE from roomtype WHERE room_type_id = :room_type_id", {"room_type_id": room_id})

                c.execute("SELECT COUNT(*) from roomtype WHERE room_type_id = :room_type_id", {"room_type_id": room_id})

                conn.commit()

                temp = c.fetchall()[0][0]
                # print(temp)
                if temp >= 1:
                    print("Record is not deleted for room_type_id :", room_id)

                else:
                    print("Record deleted Successfully for room_type_id :", room_id)

                    return 1

        except Exception as e:
            print(e)
            print("Please try with different data")
        finally:
            conn.commit()
            conn.commit()

    def display_roomtype_data(self):
        conn = sqlite3.connect("MyDB.db", timeout=10)
        c = conn.cursor()
        print("\nDisplaying the host data:")
        room_type_df = c.execute("SELECT * from roomtype")
        room_type_df = pd.DataFrame(room_type_df)
        print(room_type_df.info())
        room_type_df.columns = ["room_type_id", 'room_type']
        print(room_type_df.head(10))
        conn.commit()
        conn.close()

# update fun


# Room_type_Obj = Room_type()
# Room_type_Obj.display_roomtype_data()

# Room_type_Obj.room_Data_Delete()

# print(Room_type_Obj.room_type_insert())

# print(Room_type_Obj.Roomtype_Update())
