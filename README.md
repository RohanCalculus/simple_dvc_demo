
### Step 1: Create and Activate the project Environment
* `conda create -n wineq python=3.7 -y`
* `conda activate wineq`

### Step 2: Create requirements.txt and install them
* `echo. > requirements.txt` 
* `pip install -r requirements.txt`

### Step 3: Create template.py file
* `This will generate the project directories and file setup`

### Step 4: Add the data given
* `Using the google drive link download the winequality.csv and upload it to data_given folder`

### Step 5: Install dvc and Degrade fsspec before initilizing dvc (specially for 2023)
* `pip install dvc==2.10.2`
* `pip uninstall fsspec`
* `pip install fsspec==2022.11.0`

### Step 6: Git Commands
* `git init`
* `dvc init`
* `dvc add data_given/winequality.csv`
* `git add .`
* `git commit -m "first commit"`

### Step 7: Add a remote repo
* `git remote add origin https://github.com/RohanCalculus/simple_dvc_demo.git`
* `git branch -M main`
* `git push origin main`

### Step 8: Tox and Tox Rebulding Commands
* `tox`
* `tox -r`

### Step 9: Pytest Command
* `pytest -v`

### Step 10: Setup Command
* `pip install -e .`

### Step 11: Build your own Package
* `python setup.py sdist bdist_wheel`