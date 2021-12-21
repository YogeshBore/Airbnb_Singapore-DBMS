import pandas as pd
import sqlite3


class Host_Data:
    # Read csv file and import it into data frame host_df
    df = pd.read_csv('listings.csv')
    host_df = df[["host_id", "host_name", "calculated_host_listings_count"]].copy()

    # Data Cleaning drop duplicate values
    host_df = host_df.drop_duplicates()
    host_df.reset_index(drop=True, inplace=True)

    conn = sqlite3.connect("MyDB.db", timeout=10)
    c = conn.cursor()

    c.execute("SELECT count(name) from sqlite_master WHERE type='table' AND name='host'")
    if c.fetchone()[0] == 1:
        c.execute("DELETE FROM host")
        # c.execute("DROP TABLE host")

    else:
        c.execute('''CREATE TABLE host(
           host_id INTEGER PRIMARY KEY,
           host_name TEXT,
           calculated_host_listings_count INTEGER)''')

    host_df.to_sql('host', conn, if_exists='append', index=False)

    conn.commit()
    conn.close()

    # c.execute("SELECT * FROM host")
    # print(c.fetchall())
    # Insert Host data

    @staticmethod
    def host_insert():
        conn = sqlite3.connect("MyDB.db", timeout=10)
        c = conn.cursor()

        try:

            test_res = 1
            host_id_test = input("Please enter Host_ID:")
            host_name_test = input("Please enter Host name:")
            list_count_test = input("calculated_host_listings_count:")

            c.execute("INSERT INTO host VALUES(:host_id,:host_name,:calculated_host_listings_count)",
                      {"host_id": host_id_test, "host_name": host_name_test,
                       "calculated_host_listings_count": list_count_test})
            # self.conn.commit()
            c.execute("SELECT host_id from host WHERE host_id = :host_id", {"host_id": host_id_test})
            temp = c.fetchall()[0][0]
            # print(temp)
            # print(type(host_id_test))

            if str(temp) == host_id_test:
                c.execute("SELECT * from host WHERE host_id = :host_id", {"host_id": host_id_test})
                inserted = c.fetchall()
                print("\nHost inserted Successfully:[host_id,host_name,calculated_host_listings_count] => ", inserted)
                conn.commit()
                return test_res
            else:
                print("Host Record is not inserted successfully")
                # self.conn.commit()
                test_res = 0
                return test_res

        except Exception as e:
            print(e)
            print("Please try with different valid data.")
        finally:
            conn.commit()
            conn.close()

    # update host
    @staticmethod
    def host_update():

        conn = sqlite3.connect("MyDB.db", timeout=10)
        c = conn.cursor()

        try:
            test_res = 1
            print("Host ID Test Data:266763,367042")
            host_id_test = input("Please enter Host_ID for which you want update:")
            host_id_test = int(host_id_test)

            host_name_test = input("Please enter updated Host Name:")
            host_name_test = str(host_name_test)

            list_count_test = input("Please enter updated calculated_host_listings_count:")
            list_count_test = float(list_count_test)

            """self.c.execute(
                'UPDATE host SET host_name=:host_name WHERE host_id=:host_id',
                {'host_name': host_name_test,'host_id': host_id_test })"""

            c.execute(
                'UPDATE host SET host_name=:host_name,calculated_host_listings_count=:calculated_host_listings_count '
                'WHERE host_id=:host_id',
                {'host_name': host_name_test, 'host_id': host_id_test,
                 'calculated_host_listings_count': list_count_test})

            # self.conn.commit()
            c.execute("SELECT host_id from host WHERE host_id = :host_id", {"host_id": host_id_test})
            temp = c.fetchall()[0][0]
            # print(temp)
            # print(type(host_id_test))

            if temp == host_id_test:
                c.execute("SELECT * from host WHERE host_id = :host_id", {"host_id": host_id_test})
                updated = c.fetchall()
                print("\nHost Updated Successfully [host_id,host_name,calculated_host_listings_count] => ", updated)
                # self.conn.commit()

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

    @staticmethod
    def display_host_data():
        conn = sqlite3.connect("MyDB.db", timeout=10)
        c = conn.cursor()
        print("\nDisplaying the host data:")
        hostdata = c.execute("SELECT * from host")
        hostdata = pd.DataFrame(hostdata)
        hostdata.columns = ["host_id", 'host_name', 'calculated_host_listings_count']
        print(hostdata.head(10))
        conn.commit()
        conn.close()

    # Delete host data

    @staticmethod
    def host_data_delete():
        conn = sqlite3.connect("MyDB.db", timeout=10)
        c = conn.cursor()

        try:
            print("Host ID Test Data:266763,227796,367042")
            host_id_test = input("Please enter Host_id:")
            c.execute("SELECT COUNT(*) from host WHERE host_id = :host_id", {"host_id": host_id_test})
            rowcount = c.fetchall()[0][0]
            # print(rowcount)
            if rowcount <= 0:
                print("No records founds for  host_id:", host_id_test)
            else:

                c.execute("DELETE from host WHERE host_id = :host_id", {"host_id": host_id_test})

                c.execute("SELECT COUNT(*) from host WHERE host_id = :host_id", {"host_id": host_id_test})

                conn.commit()

                temp = c.fetchall()[0][0]
                # print(temp)
                if temp >= 1:
                    print("Record is not deleted for Host id :", host_id_test)

                else:
                    print("Record deleted Successfully for host id :", host_id_test)

                    return 1

        except Exception as e:
            print("Please try with different data")
            print(e)

        finally:
            conn.commit()
            conn.close()


# Host_Obj = Host_Data()
# Host_Obj.host_data_delete()

# Host_Obj = host_Data()

# Host_Obj.Host_Data_Delete()
"""
Host_Obj.host_insert()
Host_Obj.display_host_data()
Host_Obj.host_Update()
Host_Obj.display_host_data()
#Host_Obj.host_insert()

Host_Obj.host_Update() # Test data for valid scenario:23666


Host_Obj.display_host_data()"""
