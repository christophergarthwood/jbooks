#!/bin/sh


sudo $(which conda) env export --from-history --name machine_learning_gpu > striped.yml;
sudo $(which conda) env export --no-builds  --name machine_learning_gpu > ./archless_environment.yml;
sudo $(which conda) env export --name machine_learning_gpu > ./environment.yml;

