create the env - conda create -n wineq python=3.7 -y
activate the env wineq
create req file
add package name-  dvc, dvc[gdrive], sklearn
run the req.txt - pip install -r req.txt 
Get dataset - https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009
git init
dvc init
dvc add data_given/winequality.csv
git add .
git commit -m 'initial commit'