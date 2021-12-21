import sqlite3
import pandas as pd
import datetime


class Review_Data:
    df = pd.read_csv('listings.csv')
    review_df = df[["id", "number_of_reviews", "last_review", "reviews_per_month"]].copy()

    review_df = review_df.dropna()
    review_df = review_df.drop_duplicates()

    # print(review_df)

    conn = sqlite3.connect("MyDB.db", timeout=10)
    c = conn.cursor()

    c.execute("SELECT count(name) from sqlite_master WHERE type='table' AND name='review'")
    if c.fetchone()[0] == 1:
        c.execute("DELETE FROM review")
    else:
        c.execute(""" CREATE TABLE review(
                    id INTEGER,
                    number_of_reviews INTEGER,
                    last_review TEXT,
                    reviews_per_month REAL,
                    FOREIGN KEY('id') REFERENCES room('id')
                    )""")

    review_df.to_sql("review", conn, if_exists='append', index=False)

    c.execute("SELECT * FROM review")
    # print(c.fetchall())

    conn.commit()
    conn.close()

    # Insert New review record

    def Review_Data_insert(self):

        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()

            test_res = 1
            print("Sample room id's: 49091, 50646, 56334")
            review_id_test = input("Please enter room_id:")
            review_id_test = int(review_id_test)
            number_of_reviews_test = input("Please enter number_of_reviews:")
            number_of_reviews_test = int(number_of_reviews_test)
            last_review_test = input("Please enter last_review date(YYYY-MM-DD):")
            reviews_per_month_test = input("Please enter reviews_per_month: ")
            reviews_per_month_test = float(reviews_per_month_test)

            date_format = '%Y-%m-%d'
            try:
                date_obj = datetime.datetime.strptime(last_review_test, date_format)
                # print(date_obj)
            except ValueError:
                print("Incorrect date format, should be YYYY-MM-DD")
                test_res = 0
                return test_res

            if test_res != 0:
                c.execute("INSERT INTO review VALUES(:id,:number_of_reviews,:last_review,:reviews_per_month)",
                          {"id": review_id_test, "number_of_reviews": number_of_reviews_test,
                           "last_review": last_review_test, "reviews_per_month": reviews_per_month_test})

                c.execute("SELECT id from review WHERE id = :id", {"id": review_id_test})

                temp = c.fetchall()[0][0]

                if temp == review_id_test:
                    print("Record inserted Successfully")
                    c.execute("SELECT * from review WHERE id = :id", {"id": review_id_test})

                    temp = c.fetchall()
                    conn.commit()
                    print("[Id,no of review,last review,review per month]==>", temp)
                    return 1
                else:
                    print("Reviews record is not inserted successfully")
                    conn.commit()
                    return 0
        except Exception as e:
            print("Please enter valid data")
            print(e)
        finally:
            conn.commit()
            conn.close()

    def Review_Data_Delete(self):

        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()

            test_res = 1
            print("Review Test Data : Room ID's: 241510,241503,50646")
            review_id_test = input("Please enter room_id:")
            c.execute("SELECT COUNT(*) from review WHERE id = :id", {"id": review_id_test})
            rowcount = c.fetchall()[0][0]
            # print(rowcount)
            if rowcount <= 0:
                print("No records founds for :", review_id_test, "review id")
            else:

                c.execute("DELETE from review WHERE id = :id", {"id": review_id_test})

                c.execute("SELECT COUNT(*) from review WHERE id = :id", {"id": review_id_test})

                conn.commit()

                temp = c.fetchall()[0][0]
                # print(temp)
                if temp >= 1:
                    # c.execute("DELETE from review WHERE id = :id", {"id": review_id_test})
                    # print(c.fetchall())
                    print("Record is not deleted Successfully for Room_id :", review_id_test)
                    test_res = 0
                    return test_res
                else:
                    print("Record deleted Successfully for id :", review_id_test)
                    conn.commit()
                    return test_res

        except Exception as e:
            print("Please try with different valid data")
            print(e)
        finally:
            conn.commit()
            conn.close()

        # update host

    def review_data_update(self):

        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()
            test_res = 1
            print("Review Test Data : Room ID's: 241510,241503,50646")
            review_id_test = input("Please enter Room ID for which you want update:")
            review_id_test = int(review_id_test)

            no_reviews_test = input("Please enter number of reviews:")
            no_reviews_test = str(no_reviews_test)
            # Validating the date format is correct or not before data insertion
            last_review_date = input("Please enter last_review date(YYYY-MM-DD):")
            date_format = '%Y-%m-%d'
            try:
                date_obj = datetime.datetime.strptime(last_review_date, date_format)
            except ValueError:
                print("Incorrect date format, should be YYYY-MM-DD")
                test_res = 0
                return test_res

            if test_res != 0:
                reviews_per_month_test = input("Please enter reviews_per_month: ")
                reviews_per_month_test = float(reviews_per_month_test)

                c.execute(
                    'UPDATE review SET number_of_reviews=:number_of_reviews,last_review=:last_review,'
                    'reviews_per_month=:reviews_per_month WHERE id=:id',
                    {'number_of_reviews': no_reviews_test, 'last_review': last_review_date,
                     'reviews_per_month': reviews_per_month_test, 'id': review_id_test})

                # self.conn.commit()
                c.execute("SELECT id from review WHERE id = :id", {"id": review_id_test})
                temp = c.fetchall()[0][0]
                # print(temp)
                # print(type(host_id_test))

                if temp == review_id_test:
                    c.execute("SELECT * from review WHERE id = :id", {"id": review_id_test})
                    updated = c.fetchall()
                    print("\nReview Updated Successfully [Review_id,No of review,last review date,Reviews per month] "
                          "=> "
                          "", updated)
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

    def display_review_data(self):

        conn = sqlite3.connect("MyDB.db", timeout=10)
        c = conn.cursor()
        review_df = c.execute("SELECT * from review")
        review_df = pd.DataFrame(review_df)
        review_df.columns = ['id', 'number_of_reviews', 'last_review', 'reviews_per_month']
        print(review_df.head(10))
        conn.commit()
        conn.close()
    # Populate all the data/listing that has 200 or above total reviews

    def pop_data(self):
        try:
            conn = sqlite3.connect("MyDB.db", timeout=10)
            c = conn.cursor()
            pop_df = c.execute("SELECT * from review LEFT JOIN room ON review.id = room.id WHERE number_of_reviews >= "
                               "200")
            pop_df = pd.DataFrame(pop_df)
            pop_df.columns = ['id', 'number_of_reviews', 'last_review', 'reviews_per_month', 'id', 'name', 'latitude',
                              'longitude', 'price', 'min nights', 'availability', 'hostid', 'roomtypeid']
            # pop_df.columns == ['id', 'number_of_reviews', 'last_review', 'reviews_per_month']
            print("\nPopulating all the data that has 200 or above total reviews and creating csv file:")
            print("\nDisplaying 10 rows from 200totalreview.csv file.\n")
            print(pop_df.head(10))
            pop_df.to_csv('200totalreview.csv')
            print("\nPlease check project folder for 200totalreview.csv file.\n")

        except Exception as e:
            print(e)
            print("Please try with valid data")
        finally:
            conn.commit()
            conn.close()

# Review_Data_Obj = Review_Data()
# print(Review_Data_Obj.Review_Data_insert())
# Review_Data_Obj.Review_Data_Delete()
# Review_Data_Obj.Review_Data_insert()
# Review_Data_Obj.review_data_update()
# Review_Data_Obj.display_review_data()
# Review_Data_Obj.pop_data()
