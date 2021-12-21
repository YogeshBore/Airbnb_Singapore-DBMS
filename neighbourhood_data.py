import sqlite3
import pandas as pd


class Neighbourhood_Data:
    # Read csv file and save it into data frame neighbourhood_df
    df = pd.read_csv('listings.csv')
    neighbourhood_df = df[["neighbourhood", "neighbourhood_group"]].copy()

    # Data cleaning
    neighbourhood_df = neighbourhood_df.drop_duplicates()
    neighbourhood_df.reset_index(drop=True, inplace=True)

    s1 = pd.Series(range(1, len(neighbourhood_df.index) + 1))

    neighbourhood_df['neighbourhood_id'] = s1

    def makeid(data):
        if data['neighbourhood_group'] == 'North Region':
            return 1
        elif data['neighbourhood_group'] == 'Central Region':
            return 2

        elif data['neighbourhood_group'] == 'East Region':
            return 3
        elif data['neighbourhood_group'] == 'West Region':

            return 4
        else:
            return 5

    neighbourhood_df['neighbourhood_group_id'] = neighbourhood_df.apply(makeid, axis=1)

    # print(neighbourhood_df)
    del neighbourhood_df['neighbourhood_group']
    # print(neighbourhood_df)

    conn = sqlite3.connect("MyDB.db", timeout=10)
    c = conn.cursor()

    c.execute("SELECT count(name) from sqlite_master WHERE type='table' AND name='nbh_data'")
    if c.fetchone()[0] == 1:
        # c.execute("DROP TABLE nbh_data")
        c.execute("DELETE FROM nbh_data")
    else:
        c.execute("""CREATE TABLE nbh_data(
                   neighbourhood_id INTEGER PRIMARY KEY,
                   neighbourhood_group_id INTEGER,
                   neighbourhood TEXT,
                   FOREIGN KEY("neighbourhood_group_id") REFERENCES nbh_grp("neighbourhood_group_id")            
                    )""")

    neighbourhood_df.to_sql("nbh_data", conn, if_exists='append', index=False)
    c.execute("SELECT * FROM nbh_data")
    # print(c.fetchall())

    conn.commit()
    conn.close()

    # Insert New neighbourhood record

    def nbh_insert(self):

        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()

            nbh_id_test = input("Please enter neighbourhood_id:")
            nbh_grp_id_test = input("Please enter neighbourhood_group_id:")
            nbh_test = input("Please enter neighbourhood:")

            c.execute("INSERT INTO nbh_data VALUES(:neighbourhood_id,:neighbourhood_group_id,:neighbourhood)",
                      {"neighbourhood_id": int(nbh_id_test), "neighbourhood_group_id": int(nbh_grp_id_test),
                       "neighbourhood": nbh_test})

            c.execute("SELECT neighbourhood_id from nbh_data WHERE neighbourhood_id = :neighbourhood_id",
                      {"neighbourhood_id": int(nbh_id_test)})
            temp = c.fetchall()[0][0]

            if str(temp) == nbh_id_test:
                print("Record inserted Inserted Successfully")

                c.execute("SELECT * from nbh_data WHERE neighbourhood_id = :neighbourhood_id",
                          {"neighbourhood_id": int(nbh_id_test)})
                temp = c.fetchall()
                print("\nNeighbourhood inserted Successfully:[neighbourhood_id,neighbourhood_grp_id,neighbourhood] =>",
                      temp)
                conn.commit()
                return 1
            else:
                print("NeighbourhoodRecord is not inserted successfully")
                return 0

        except Exception as e:
            print("Got Exception as ", e)
            print("Please try with different data")
        finally:
            conn.commit()
            conn.close()

    # Updating the neighbourhood data:
    def nbh_data_Update(self):
        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()
            test_res = 1
            print("Test Data for neighbourhood_id:1,2,3")
            nbh_id_test = input("Please enter neighbourhood_id for which you want update:")
            nbh_id_test = int(nbh_id_test)

            neighbourhood = input("Please enter neighbourhood Name:")
            neighbourhood = str(neighbourhood)

            c.execute(
                'UPDATE nbh_data SET neighbourhood=:neighbourhood WHERE neighbourhood_id=:neighbourhood_id',
                {'neighbourhood': neighbourhood, 'neighbourhood_id': nbh_id_test})

            c.execute("SELECT neighbourhood_id from nbh_data WHERE neighbourhood_id = :neighbourhood_id",
                      {"neighbourhood_id": nbh_id_test})
            temp = c.fetchall()[0][0]
            if temp == nbh_id_test:
                c.execute("SELECT * from nbh_data WHERE neighbourhood_id = :neighbourhood_id", {"neighbourhood_id":
                                                                                                    nbh_id_test})
                updated = c.fetchall()
                print("\nNeighbourhood Updated Successfully [neighbourhood_id, neighbourhood_group_id,"
                      "neighbourhood] "
                      " => ", updated)
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

    def display_nbh_data(self):
        conn = sqlite3.connect("MyDB.db")
        c = conn.cursor()
        neighbourhood_df = c.execute("SELECT * from nbh_data")
        neighbourhood_df = pd.DataFrame(neighbourhood_df)
        neighbourhood_df.columns = ["neighbourhood_id", 'neighbourhood_group_id', 'neighbourhood']
        print(neighbourhood_df.head(10))
        conn.commit()
        conn.close()

    def nbh_Data_Delete(self):

        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()
            print("Test Data for neighbourhood_id:1,2,3")
            nbh_id_test = input("Please enter neighbourhood_id:")
            c.execute("SELECT COUNT(*) from nbh_data WHERE neighbourhood_id = :neighbourhood_id",
                      {"neighbourhood_id": nbh_id_test})
            rowcount = c.fetchall()[0][0]
            # print(rowcount)
            if rowcount <= 0:
                print("No records founds for  neighbourhood_id:", nbh_id_test)
            else:

                c.execute("DELETE from nbh_data WHERE neighbourhood_id = :neighbourhood_id",
                          {"neighbourhood_id": nbh_id_test})

                c.execute("SELECT COUNT(*) from nbh_data WHERE neighbourhood_id = :neighbourhood_id",
                          {"neighbourhood_id": nbh_id_test})

                conn.commit()

                temp = c.fetchall()[0][0]
                # print(temp)
                if temp >= 1:
                    print("Record is not deleted for neighbourhood_id :", nbh_id_test)

                else:
                    print("Record deleted Successfully for neighbourhood_id :", nbh_id_test)

                    return 1

        except Exception as e:
            print("Please try with different data")
            print(e)
        finally:
            conn.commit()
            conn.close()

# neighbourhood_data_Obj = neighbourhood_data()

# neighbourhood_data_Obj.display_nbh_data()
# neighbourhood_data_Obj.nbh_data_Update()
# print(neighbourhood_data_Obj.nbh_insert())
# neighbourhood_data_Obj.nbh_Data_Delete()
