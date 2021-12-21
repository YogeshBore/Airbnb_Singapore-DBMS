import sqlite3
import pandas as pd


class Neighbourhood_Group:
    df = pd.read_csv('listings.csv')
    nbh_grp_df_old = df[["neighbourhood_group"]].copy()
    nbh_grp_df = nbh_grp_df_old["neighbourhood_group"].unique()

    s1 = pd.Series(nbh_grp_df)
    len = len(s1.index)
    # print(len)

    s2 = pd.Series(range(1,len+5))
    # print(s2)

    nbh_grp_df = pd.DataFrame(nbh_grp_df)
    nbh_grp_df.columns = ['neighbourhood_group_name']
    nbh_grp_df['neighbourhood_group_id'] = s2

    # print(nbh_grp_df)
    # Data Cleaning

    conn = sqlite3.connect('MyDB.db',timeout=10)
    c = conn.cursor()

    c.execute("SELECT count(name) from sqlite_master WHERE type='table' AND name='nbh_grp'")
    if c.fetchone()[0] == 1:
         # c.execute("DROP TABLE nbh_grp")
         c.execute("DELETE FROM nbh_grp")
    else:
        c.execute(""" CREATE TABLE nbh_grp(
                  neighbourhood_group_id INTEGER PRIMARY KEY,
                  neighbourhood_group_name TEXT
                  )""")

    nbh_grp_df.to_sql("nbh_grp", conn, if_exists='append', index=False)
    c.execute("SELECT * FROM nbh_grp")
    # print(c.fetchall())
# Insert the data for neighbourhood group

    conn.commit()
    conn.close()

    def nbh_grp_inser(self):

            try:
                conn = sqlite3.connect('MyDB.db', timeout=10)
                c = conn.cursor()

                nbh_grp_id_test = input("Please enter Neighbourhood_group_ID:")
                nbh_grp_name_test=input("Please enter Neighbourhood_group_Name:")


                c.execute("INSERT INTO nbh_grp VALUES(:neighbourhood_group_id,:neighbourhood_group_name)",
                             {"neighbourhood_group_id":nbh_grp_id_test,"neighbourhood_group_name":nbh_grp_name_test})


                c.execute("SELECT neighbourhood_group_id from nbh_grp WHERE neighbourhood_group_id = "
                          ":neighbourhood_group_id",{"neighbourhood_group_id":nbh_grp_id_test})
                temp = c.fetchall()[0][0]

                if str(temp) == nbh_grp_id_test:
                                print("Neighbourhood_group record inserted Successfully")
                                c.execute(
                                    "SELECT * from nbh_grp WHERE neighbourhood_group_id = :neighbourhood_group_id",
                                    {"neighbourhood_group_id": nbh_grp_id_test})
                                temp = c.fetchall()
                                print("[Neighbourhood_group_id , neighbourhood_group_name]==>", temp)
                                conn.commit()
                                return 1
                else:
                    print("Neighbourhood_group record is not inserted successfully")
                    return 0


            except Exception as e:
                print(e)
                print("Please try with different valid data.")
            finally:
                #print("Closing DB Connection")
                conn.commit()
                c.close()
                conn.close()

            # update nbh group

    def nbh_group_update(self):

        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()
            test_res = 1
            print("Sample neighbourhood id:1,2,3 ")
            nbh_id_test = input("Please enter neighbourhood_group_id for which you want update:")
            nbh_id_test = int(nbh_id_test)

            nbh_grp_name_test = input("Please enter updated neighbourhood_group_name:")
            nbh_grp_name_test = str(nbh_grp_name_test)

            c.execute(
                'UPDATE nbh_grp SET neighbourhood_group_name=:neighbourhood_group_name WHERE '
                'neighbourhood_group_id=:neighbourhood_group_id',
                {'neighbourhood_group_name': nbh_grp_name_test, 'neighbourhood_group_id': nbh_id_test})

            # self.conn.commit()
            c.execute("SELECT neighbourhood_group_id from nbh_grp WHERE neighbourhood_group_id = "
                      ":neighbourhood_group_id", {"neighbourhood_group_id": nbh_id_test})
            temp = c.fetchall()[0][0]
            # print(temp)
            # print(type(host_id_test))

            if temp == nbh_id_test:
                c.execute("SELECT * from nbh_grp WHERE neighbourhood_group_id = :neighbourhood_group_id",
                          {"neighbourhood_group_id": nbh_id_test})
                updated = c.fetchall()
                print("\nNeighbourhood Updated Successfully [Neighbourhood_group_id,Neighbourhood_group_name] => ", updated)
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


    # Deleting the neighbourhood group data
    def nbh_grp_Delete(self):
            try:
                conn = sqlite3.connect("MyDB.db", timeout=10)
                c = conn.cursor()
                print("Sample neighbourhood id:1,2,3 ")
                nbh_grp_id_test = input("Please enter neighbourhood_group_id:")
                c.execute("SELECT COUNT(*) from nbh_grp WHERE neighbourhood_group_id = :neighbourhood_group_id",
                          {"neighbourhood_group_id": nbh_grp_id_test})
                rowcount = c.fetchall()[0][0]
                # print(rowcount)
                if rowcount <= 0:
                    print("No records founds for  neighbourhood_group_id:", nbh_grp_id_test)
                else:
                    c.execute("DELETE from nbh_grp WHERE neighbourhood_group_id = :neighbourhood_group_id",
                              {"neighbourhood_group_id": nbh_grp_id_test})

                    c.execute("SELECT COUNT(*) from nbh_grp WHERE neighbourhood_group_id = :neighbourhood_group_id",
                              {"neighbourhood_group_id": nbh_grp_id_test})
                    temp = c.fetchall()[0][0]
                    if temp >= 1:
                        print("Record is not deleted for neighbourhood_group_id :", nbh_grp_id_test)
                    else:
                        print("Record deleted Successfully for neighbourhood_group_id :", nbh_grp_id_test)
                        return 1
            except Exception as e:
                print(e)
                prit("Please try with different valid data")
            finally:
                conn.commit()
                conn.commit()

    def display_nbh_Grp_data(self):
        conn = sqlite3.connect('MyDB.db', timeout=10)
        c = conn.cursor()
        nbh_grp_df = c.execute("SELECT * from nbh_grp")
        nbh_grp_df = pd.DataFrame(nbh_grp_df)
        nbh_grp_df.columns = ['neighbourhood_group_id', 'neighbourhood_group_name']
        # print(nbh_grp_df.info())
        print(nbh_grp_df.head(10))
        # print(hostdata.columns)
        conn.commit()
        c.close()
        conn.close()

# nbh_grp_Obj = neighbourhood_group()
# nbh_grp_Obj.nbh_grp_Delete()
# nbh_grp_Obj.nbh_grp_inser()
# nbh_grp_Obj.display_nbh_Grp_data()
# nbh_grp_Obj.nbh_group_update()