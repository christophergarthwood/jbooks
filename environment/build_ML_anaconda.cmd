ECHO OFF
PUSHD "%~dp0"
cls

REM ###########################################################
REM To remove the environment-> conda remove --name "environment name" --all
REM ###########################################################

ECHO ANACONDA3 Environment Setup Script

REM ###########################################################
REM Establish Variables
REM ###########################################################
SET ScriptPath=%~dp0
SET ROOT_DIR=C:\Users\%USERNAME%\Anaconda3
SET THE_INSTANCE_NAME=machine_learning
SET THE_INSTANCE=%ROOT_DIR%\envs\%THE_INSTANCE_NAME%
SET THE_ENV_FILENAME=environment.yml
SET CONDA_EXE=%ROOT_DIR%\scripts\conda.exe
ECHO ...setting environment variables for %THE_INSTANCE_NAME%

REM ###########################################################
REM Create target directory
REM ###########################################################
IF EXIST %THE_INSTANCE% (
    ECHO ...directory exists, removing your previous installation.
    ECHO ......del /s /f /q %THE_INSTANCE%
    del /s /f /q %THE_INSTANCE%
    ECHO ......rmdir %THE_INSTANCE%
    rmdir %THE_INSTANCE%
    ECHO:
)

ECHO ...creating %THE_INSTANCE%
mkdir %THE_INSTANCE% 
IF EXIST %THE_INSTANCE% (
    ECHO ......directory created.
)

ECHO:
ECHO ...adding Anaconda scripts to your PATH
set PATH=%ROOT_DIR%\Scripts;%ROOT_DIR%\;%PATH%


REM ECHO ...activating Anaconda base environment
REM %ROOT_DIR%\Scripts\activate.bat

ECHO ...creating Anaconda %THE_INSTANCE_NAME% environment
REM %CONDA_EXE% env create --prefix "%THE_INSTANCE%" --file "%ScriptPath%\%THE_ENV_FILENAME%"
REM %CONDA_ENV% env create --prefix "%THE_INSTANCE%" --file "%ScriptPath%\%THE_ENV_FILENAME%"
conda env create --prefix "%THE_INSTANCE%" --file "%ScriptPath%\%THE_ENV_FILENAME%"

REM ECHO ...activating the new %THE_INSTANCE_NAME% environment.
REM %CONDA_EXE% activate "%THE_INSTANCE_NAME%"

REM ECHO ...installing additional packages
REM %CONDA_EXE% install -y geoviews geopandas cmocean -c conda-forge
REM ECHO ...finished final installation

REM SET THE_VERSION=start python --version .\version.txt
REM ECHO Python version is  < .\version.txt

REM PROMPT
REM EXIT 
