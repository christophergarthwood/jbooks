#!/bin/sh


#Stripped down version of the environment, could be machine specific but thin
sudo $(which conda) env export --from-history --name machine_learning_gpu > striped.yml;

#Most secure cross platform method
sudo $(which conda) env export --no-builds  --name machine_learning_gpu > ./archless_environment.yml;
sudo $(which conda) env export --no-builds --name sonya_r > ./sonya_r.yml;
sudo $(which conda) env export --no-builds --name sonya_python > ./sonya_python.yml;

#Most generic method
sudo $(which conda) env export --name machine_learning_gpu > ./environment.yml;

#create generic requirements file
pip list --format=freeze > ./requirements.txt
#pip list --format=freeze --user > ./requirements.txt

