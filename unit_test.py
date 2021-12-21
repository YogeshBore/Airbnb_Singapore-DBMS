from host_data import Host_Data
from review_data import Review_Data

class UnitTesing:
    def do_unit_test(Self ):
        print("\n***** Unit Testing ******")
        print("==========================")

        def test_host_insertion(test_function,input, expected):
            print("Test valid data insert for HOST")
            print("\nEnter valid HOST DATA e.g: 101,John,1")
            actual=test_function()

            if(actual==expected):
                print("Test Passed")
            else:
                print("Test Failed")
            print("-----------------------------------")


        def test_host_update(test_function,input, expected):
            print("\nTest valid Data update case for HOST:")
            print("\nEnter valid HOST Data e.g:ID:23666,John,1")
            actual=test_function()

            if(actual==expected):
                print("Test Passed")
            else:
                print("Test Failed")
            print("-----------------------------------")

        def test_review_data_delete(test_function,input, expected):
            print("\nTest  Delete case for Review:")
            print("\nEnter valid Review Data e.g:ID's:56334,71896,71907")
            actual=test_function(input)

            if(actual==expected):
                print("Test Passed")
            else:
                print("Test Failed")
            print("-----------------------------------")


        # Invalid input

        def test_In_host_insertion(test_function, input, expected):
                print("Test Invalid data insert for HOST")
                print("\nEnter Invalid HOST DATA e.g: John,John,John or Duplicate ID:184596")
                actual = test_function()

                if (actual == expected):
                    print("Test Passed")
                else:
                    print("Test Failed")
                print("-----------------------------------")


        def test_review_date_validate(test_function, input, expected):
            print("\nTest Invalid Review Date:")
            print("\nReview ID Test Data e.g:ID's:56334,71896,71907")
            print("\nEnter Invalid Review Date e.g: 32-26-0011")
            actual = test_function(input)

            if (actual == expected):
                print("Test Passed")
            else:
                print("Test Failed")
            print("-----------------------------------")


        host_Data_Obj = Host_Data()
        user_input_host = host_Data_Obj
        expected_output = 1
        print("Scenario 1: To Test valid host data insertion:")
        test_host_insertion(Host_Data.host_insert,user_input_host, expected_output)


        print("Scenario 2: To Test Invalid host data insertion for duplicate Host ID:")
        test_In_host_insertion(Host_Data.host_insert,user_input_host, expected_output)


        print("Scenario 3: To Test Invalid host data insertion:")
        test_In_host_insertion(Host_Data.host_insert, user_input_host, expected_output)


        print("Scenario 4: To Test Valid host data update:")
        test_host_update(Host_Data.host_update,user_input_host, expected_output)


        review_data_Obj = Review_Data()
        #user_input_review = review_data_Obj
        print("Scenario 5: To Test Review Data Delete:")
        test_review_data_delete(Review_Data.Review_Data_Delete,review_data_Obj, expected_output)


        print("Scenario 6: To Test Review Date validation:")
        test_review_date_validate(Review_Data.Review_Data_insert,review_data_Obj, expected_output)



#unit_Obj = UnitTesing()
#unit_Obj.do_unit_test()