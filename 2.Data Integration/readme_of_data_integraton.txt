Stage 2: Data Integration
--------------------
Here we have integrated the files of our two dataset - Census and HMIS. Output files from the Data Transformation step are copied inside this folder and arranged state-wise in the folders "Census" and "HMIS". 

Contents of the Folder
--------------------
Folder - "Census": stores all the csv files for the data set Census generated from the Data Transformation stage of the project. These files are categorized by thier state names.

Folder - "HMIS": stores all the csv files for the data set HMIS generated from the Data Transformation stage of the project. These files are categorized by thier state names.

"mapping_census_and_hmis.py": is the python script which maps the census and hmis data and generate a single file for a state inside the folder - "MergedFiles".

"merge_files.py": is the python script which merge all the states files present inside the folder "MergedFiles" and generate a single file - "all_states_merged_8to18.csv". This generated file is used in the input of the stage 3 - Data Exploration and Prediction. 


Step 1 : Mapping Census and HMIS Data
------------------------------------
Here we merge each state Census and HMIS files into one file. 35 output csv files are generated inside the folder "MergedFiles". 

Input: All csv files inside the Folders - "Census" and "HMIS"

Executable: mapping_census_and_hmis.py

Ouput: csv files are generated in the Folder - "MergedFiles". One for each state.

How to run:
python3 mapping_census_and_hmis.py


Step 2: Merging all state files into one
----------------------------------------
Here we merge the above generated files inside the folder "MergeFiles" into one single file - "all_states_merged_8to18.csv".

Input: All csv files in the Folder - "MergeFiles"

Executable: merge_files.py

Ouput: all_states_merged_8to18.csv

How to run:
python3 merge_files.py



------------------------- End ---------------------------
------------------------ Thank You ------------------------
