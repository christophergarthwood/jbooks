#!/usr/bin/env bash

#Most secure cross platform method
#sudo $(which conda) env export --no-builds  --name machine_learning_gpu > ./archless_environment.yml;

#Most generic method
the_repos=( machine_learning_gpu usfs_aiml_loaded usfs_aiml_basic usfs_aiml_nlp usfs_aiml_llm usfs_r_env );
for repo in ${the_repos[@]}
do
    echo "Processing ${repo}..."
    conda env export --name "${repo}" > "./${repo}.yml";
    status=$?
    if [ "${status}" -ne 0 ];
    then
        echo "........FAILURE";
	echo "........conda env export --name ${repo} failed with status code of (${status}).";
    else
        echo "........SUCCESS";
    fi
done

#create generic requirements file
echo "Copy of pip/python System libs to requirements file.";
pip list --format=freeze > ./requirements.txt
echo "Copy of pip/python User libs to requirements file.";
pip list --format=freeze --user > ./user_requirements.txt
