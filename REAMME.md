```bash
create the env - 
conda create -n wineq python=3.7 -y
```
```bash

activate the env wineq
```
```bash

create req file
```
```bash

add package name-  dvc, dvc[gdrive], sklearn
```
```bash

run the req.txt - pip install -r req.txt 
```
```bash

Get dataset - https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009
```
```bash

git init
```
```bash

dvc init
```
```bash

dvc add data_given/winequality.csv
```
```bash

git add .
```
```bash

git commit -m 'initial commit'

tox command - 
```bash
tox
```
for rebuilding - 
```bash
tox -r
```
pytest command
```bash
pytest -v
```

setup commands - 
```bash
pip install -e .
```
build your own package commands - 
````bash
python setup.py install sdist bdist_wheel
```