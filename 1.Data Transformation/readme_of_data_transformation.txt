Data Transformation
--------------------
Here we have transformed the unstructed excel files into csv files. It contains of 7 folders and 5 py files and 1 csv and 1 txt file.

Step 1 : Cleaning of Census Data
--------------------------------

Folder - "All States Census 2001 Unprocessed xls files" stores all the excel files downloaded from the Census website for the Census data 2001.

Folder - "All States Census 2011 Unprocessed xls files" stores all the excel files downloaded from the Census website for the Census data 2011.

census-transform.py is a python script which transforms and preprocess the 70 files in the above mentioned two folders and store the clean csv files in the following folders:
	Folder - "All States Census 2001 Unprocessed xls files"
	Folder - "All States Census 2011 Unprocessed xls files"

Input: All excel files inside the Folders - "All States Census 2001 Unprocessed xls files" and "All States Census 2011 Unprocessed xls files"

Executable: census-transform.py

Ouput: 70 files are generated in the Folders - "All States Census 2001 Unprocessed xls files" and "All States Census 2011 Unprocessed xls files"

Dependencies: 
	xlrd package
		pip3 install xlrd

How to run:
pip3 install xlrd
python3 census-transform.py


Step 2: Generation of Census Files for the years 2008-2018
----------------------------------------------------------
Here we generate the census files for each year between 2008 and 2018 from the census files of 2001 and 2011. 

Input: All 70 csv files in the Folders - "All States Census 2001 Unprocessed xls files" and "All States Census 2011 Unprocessed xls files"

Executable: generate-progression.py

Ouput: 385 files are generated in the Folder - "All States Census progression from 2008 to 2018"

How to run:
python3 generate-progression.py

Step 3: Transformation of HMIS Files
------------------------------------
Here we transform and clean the unstructered excel files of HMIS data into cleaned csv files.

There was no way of processing the excel files as they we embedded in xml. So we manually copied them into csv files and then run python script on them. Folder - "uncleaned_hmis_csv" contains these csv files. Following steps are performed to clean and preprocess these csv files.

We have 3 different types of input data files in the folder - "uncleaned_hmis_csv". So this step is divided into 3 parts: 
	1. Files before the year 2017.
	2. Files for year 2017.
	3. Files after the year 2017. 

Case 1: Files before the year 2017.
------------------------------------
Input: csv files before the year 2017 inside the folder uncleaned_hmis_csv

Executable: processhmis_before-2017.py

Output: csv files are generated inside the folder "cleaned_hmis_csv"

How to run:
python3 processhmis_before-2017.py

Case 2: Files for the year 2017.
------------------------------------
Input: csv files for the year 2017 inside the folder uncleaned_hmis_csv

Executable: processhmis_2017.py

Output: csv files are generated inside the folder "cleaned_hmis_csv"

How to run: 
python3 processhmis_2017.py

Case 3: Files after the year 2017.
------------------------------------
Input:csv files after the year 2017 inside the folder uncleaned_hmis_csv

Executable: processhmis_after-2018.py

Output: csv files are generated inside the folder "cleaned_hmis_csv"

How to run:
python3 processhmis_after-2018.py

------------------------- End ---------------------------
------------------------ Thank You ------------------------
