#!/bin/sh


export environment="aiml"
sudo $(which conda) env export --from-history --name "${environment}" > striped.yml;
sudo $(which conda) env export --no-builds  --name "${environment}" > ./archless_environment.yml;
sudo $(which conda) env export --name "${environment}" > ./environment.yml;

