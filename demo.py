from host_data import Host_Data
from room_data import Room_Data
from review_data import Review_Data
from room_type_data import Room_type
from neighbourhood_data import Neighbourhood_Data
from neighbourhood_group import Neighbourhood_Group
from unit_test import UnitTesing

# Creating objects for all the class file

Host_obj = Host_Data()
neighbourhood_data_Obj = Neighbourhood_Data()
nbh_grp_Obj = Neighbourhood_Group()
Review_Data_Obj = Review_Data()
Room_Data_Obj = Room_Data()
Room_type_Obj = Room_type()
unit_testing_Obj = UnitTesing()

# Main Menu option for all the operations


def menu():
    ans = True
    while ans:
        print("Menu Form:")
        print("1. Display Data\n2. Insert Data\n3. Update Data\n4. Delete Data\n5. Populate Listing  Data "
              "for 200 or more reviews\n6. Unit Testing \n7. Exit\n")
        ans = input("What would you like to do?: ")
        if ans == "1":

            sub_wh = True
            while sub_wh:
                print("\nDisplay Menu:")
                print(
                    "\n1. Host Data\n2. Neighbourhood Data\n3. Neighbourhood Group\n4. Review\n5. Room"
                    "\n6. Room Type\n7. Go Back")

                subm = input("What would you like to do? ")
                if subm == "1":
                    print("\nDisplaying Host Data")
                    Host_obj.display_host_data()
                elif subm == "2":
                    print("\nDisplaying Neighbourhood Data")
                    neighbourhood_data_Obj.display_nbh_data()
                elif subm == "3":
                    print("\nDisplaying Neighbourhood Group Data")
                    nbh_grp_Obj.display_nbh_Grp_data()
                elif subm == "4":
                    print("\nDisplaying Review Data")
                    Review_Data_Obj.display_review_data()
                elif subm == "5":
                    print("\nDisplaying Room Data")
                    Room_Data_Obj.display_room_data()

                elif subm == "6":
                    print("\nDisplaying Room Type Data")
                    Room_type_Obj.display_roomtype_data()
                elif subm == "7":
                    sub_wh = False
                    print("\nReturning Back to previous menu")
                else:
                    print("\nYou have selected invalid option")
        elif ans == "2":
            sub_wh = True
            while sub_wh:
                print("\nData Inserting Menu")
                print(
                    "\n1. Host Data\n2. Neighbourhood Data\n3. Neighbourhood Group\n4. Review Data"
                    "\n5. Room Data\n6. Room Type\n7. Go Back")
                subm = input("What would you like to do? ")
                if subm == "1":
                    print("\nInserting Host Data")
                    Host_obj.host_insert()
                elif subm == "2":
                    print("\nInserting Neighbourhood Data")
                    neighbourhood_data_Obj.nbh_insert()
                elif subm == "3":
                    print("\nInserting Neighbourhood Group Data")
                    nbh_grp_Obj.nbh_grp_inser()
                elif subm == "4":
                    print("\nInserting Review Data")
                    Review_Data_Obj.Review_Data_insert()
                elif subm == "5":
                    print("\nInserting Room  Data")
                    Room_Data_Obj.room_data_insert()
                elif subm == "6":
                    print("\nInserting Room Type Data")
                    Room_type_Obj.room_type_insert()
                elif subm == "7":
                    sub_wh = False
                    print("\nReturning Back to previous menu")
                else:
                    print("\nYou have selected invalid option")
        elif ans == "3":
            sub_wh = True
            while sub_wh:
                print("\nData Update Menu")
                print(
                    "\n1.Host Data\n2.Neighbourhood Data\n3.Neighbourhood Group Data\n4.Review Data"
                    "\n5.Room Data \n6.Room type \n7. Go Back")
                subm = input("What would you like to do? ")
                if subm == "1":
                    print("\nUpdating Host Data")
                    Host_obj.host_update()
                elif subm == "2":
                    print("\nUpdating Neighbourhood Data")
                    neighbourhood_data_Obj.nbh_data_Update()
                elif subm == "3":
                    print("\nUpdating Neighbourhood Group Data")
                    nbh_grp_Obj.nbh_group_update()
                elif subm == "4":
                    print("\nUpdating Review Group Data")
                    Review_Data_Obj.review_data_update()
                elif subm == "5":
                    print("\nUpdating Room Data")
                    Room_Data_Obj.room_data_update()
                elif subm == "6":
                    print("\nUpdating Room Type")
                    Room_type_Obj.Roomtype_Update()
                elif subm == "7":
                    sub_wh = False
                    print("\nReturning Back to previous menu")
                else:
                    print("\nYou have selected invalid option")
        elif ans == "4":
            sub_wh = True
            while sub_wh:
                print("\nData Delete Menu")
                print(
                    "\n1. Host Data\n2. Neighbourhood Data\n3. Neighbourhood Group\n4. Review Data"
                    "\n5. Room Data"
                    "\n6. Room Type\n7. Go Back")
                subm = input("What would you like to do? ")
                if subm == "1":
                    print("\nDeleting Host Data")
                    Host_obj.host_data_delete()
                elif subm == "2":
                    print("\nDeleting Neighbourhood Data")
                    neighbourhood_data_Obj.nbh_Data_Delete()
                elif subm == "3":
                    print("\nDeleting Neighbourhood Group Data")
                    nbh_grp_Obj.nbh_grp_Delete()
                elif subm == "4":
                    print("\nDeleting Review Data")
                    Review_Data_Obj.Review_Data_Delete()
                elif subm == "5":
                    print("\nDeleting Room Data")
                    Room_Data_Obj.Room_Data_Delete()
                elif subm == "6":
                    print("\nDeleting Room Type Data")
                    Room_type_Obj.room_Data_Delete()
                elif subm == "7":
                    sub_wh = False
                    print("\nReturning Back to previous menu")
                else:
                    print("\nYou have selected invalid option")
        elif ans == "5":
            print("\nPopulate listing that has 200 or above total reviews")
            Review_Data_Obj.pop_data()
        elif ans == "6":
            print("Unit Testing is in Process")
            unit_testing_Obj.do_unit_test()
        elif ans == "7":
            ans = False
            print("\nGoodbye.....!")
        elif ans != "":
            print("\nYou have selected invalid option")


class Demo:
    try:
        print('\n****** Singapore_Airbnb Data-Set Analysis ******\n')

    except Exception as e:
        print(e)


demo_obj = Demo()
menu()
