# Steps:-

#### Make virtual environment

```bash
python3.11 -m venv venv
```

#### Activate virtual environment

```bash
source venv/bin/activate
```

#### to run dvc firstly initialize git 

```bash
git init
```

#### to initialize dvc

```bash
dvc init
```

#### to check the status

```bash
git status
```
-> Automatically created and saved
 - .dvc/.gitignore
 - .dvc/config
 - .dvcignore

 #### to add data/data.csv
 
 ```bash
 dvc add data/data.csv
 ```
-> Automatically create data.csv.dvc

#### to add data/data.csv.dvc
 
```bash
git add data/data.csv.dvc
```

- Runs the files which are in use 
- Make a folder mystoragefile 

#### To add remote storage

```bash
dvc remote add -d remote_storage_1 <path of mystoragefile>
```

#### To push dvc file 

```bash
dvc push
```

#### To dag (to make direct acyclic graph)
```bash
dvc dag
```

 ## Add new data in data.csv file 

 - dvc add data/data.csv
 - git add data/data.csv.dvc
 - git commit -m "my latest version"
 - dvc push
 - dvc repro # for reproducibilty so we have run dvc.yaml file 
 - dvc dag # direct acyclic graph in this to know the dependencies of the stages.
