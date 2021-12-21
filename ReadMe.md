### ___Singapore-AirBnb Data Analysis___
######
##### __README__ 
**1. Overview:**  
In this project Airbnb in Singapore listing data is used for data analysis, cleaning and converting into usable form.
Given Data is classified based on their host, review, room type, Neighbourhood_data.Then data transformed into normal form and store it in relational database in Sqlite3. 
Then created a  to perform like insert update delete.Python classes are used for development.

**2. Software Requirement :** Python 3.9.0, Any Python IDE (Pycharm Used), SQLite 3.34.1 for Data Base
Python libraries pandas, numpy, and SQLite3 should be added in AN IDE, MS-Excel for input file
   * Useful Websites:
     1. Python: https://www.python.org/downloads/
     2. SQLite3: https://www.sqlite.org/releaselog/3_34_1.html
     3. Python Numpy Library: https://numpy.org/install/
     4. Python Pandas Library: https://pandas.pydata.org/pandas-docs/
     5. Airbnb listing dataset: https://www.kaggle.com/jojoker/singapore-airbnb

**3. Project folder Contains Below Files:**

****a. listing.csv file =>**** File which have sample uncleaned data  
****b. Airbnb.db =>**** Database which contains all the table   
****c. input_data.xlxs =>**** MS-Excel input file  
****d. ReadMe.md =>**** All the project setup instructions are given  
****e. Python class files :****  
i. Demo.py - This file is used for project run, and we can perform all the operations like
				 check the cleaned data, insert, update, delete data and also used to perform
				 Unit testing. Python class Demo is written in this which is the entry point for all
				 operations.  
ii. HostData.py - In this file hostData python class is written to extract uncleaned host data from given csv file
                      and cleaned host data and perform all the operations on host data using different python functions.   
iii. Neighbourhood_data.py - In this file neighbourhood data is imported and performed all the same operations which we performed for 
								 host data.  
iv. Neighbourhood_group.py - In this file neighbourhood_group class and all his operations on group data given.  
v.  Review.py - Review class is given to perform all operations on review data.    
vi. Roomdata.py - Imported room data and performed all the operations on it.  
vii. Room_type.py - Different type of room data and respective.  
viii. Unittest.py - All unit testing negative and positive cases are added in this file

**4. Usage:**
  Download and extract project folder ==> Open project in python IDE ==> Run the Demo python file for the project entry.

**5. **Support****:  
    *Name:* Yogesh Kashiram Bore  
    *Email:* ybore01@qub.ac.uk  
  
**6. **Date:****
  9th March 2021