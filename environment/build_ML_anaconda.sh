#!/usr/bin/env bash

#Builds the Anaconda environment that will be taken with this repo to the target platform for program execution.
#Reference: https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/04-sharing-environments/index.html

#to remove the environment
#conda remove --name "environment name and path" --all

export ROOT_DIR="/opt/conda";
export THE_INSTANCE="${ROOT_DIR}/envs/machine_learning";
export CONDA_EXE="conda";

############################################
#-infrastructure support
############################################
echo "Anaconda Python Instance Virtual Environment Location: ${THE_INSTANCE}";
if [ ! -d "${THE_INSTANCE}" ];
then
    mkdir -p "${THE_INSTANCE}";
    status=$?
    if [ "${status}" -ne 0 ];
    then
        echo "FAILURE, the mkdir -p ${THE_INSTANCE} command did not work returning with a status code of (${status}).  Please investigate further for insight as to why this occurred.  Aborting execution...";
        exit 1;
    fi
fi
echo "...creating environment.";
${CONDA_EXE} env create --prefix "${THE_INSTANCE}" --file "./environment.yml";
echo "...environment created.";

${CONDA_EXE} activate "${the_instance}";
echo "...activating environemnt.";

#required as the original build does not support the later referenced packages as a single release.
echo "...installing geoviews, geopandas, and cmocean.";
${CONDA_EXE} install -y geoviews geopandas cmocean -c conda-forge;
echo "...finished installation of these packages.";

the_version=$(python --version)
echo "Python Version is ${the_version}";

