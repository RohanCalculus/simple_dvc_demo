
### Step 1: Create and Activate the project Environment
* conda create -n wineq python=3.7 -y
* conda activate wineq

### Step 2: Create requirements.txt and install them
* echo. > requirements.txt 
* pip install -r requirements.txt

### Step 3: Create template.py file
* This will generate the project directories and file setup

### Step 4: Add the data given
* Using the google drive link download the winequality.csv and upload it to data_given folder

### Step 5: Install dvc and Degrade fsspec before initilizing dvc (specially for 2023)
* pip install dvc==2.10.2
* pip uninstall fsspec
* pip install fsspec==2022.11.0

### Step 6: Git Commands
* git init
* dvc init
* dvc add data_given/winequality.csv
* git add .
* git commit -m "first commit"