#Dockerfile with basic configurations spelled out

#ARG IMG=python:3.9
#FROM $IMG AS base
#ARG IMG
#RUN echo "...installed $IMG"

#ARG IMG=bitnami/git:latest
#FROM $IMG
#ARG IMG
#RUN echo "...installed $IMG"

ARG IMG=continuumio/anaconda3
FROM $IMG
ARG IMG
RUN echo "...installed $IMG"

#ARG IMG=hasicorp/terraform:latest
#FROM $IMG
#ARG IMG
#RUN echo "...installed $IMG"

#ARG IMG=amazon/aws-cli:latest
#FROM $IMG
#ARG IMG
#RUN echo "...installed $IMG"

#ARG IMG=mcr.microsoft.com/azure-cli:latest
#FROM $IMG
#ARG IMG
#RUN echo "...installed $IMG"

#ARG IMG=gcr.io/google.com/cloudsdktool/google-cloud-cli:410.0.0
#FROM $IMG
#ARG IMG
#RUN echo "...installed $IMG"


#########################################
#- Ensure everything is up to date
#########################################
RUN apt-get update -y

#########################################
#- Install VIM
#########################################
ARG PACKAGES=vim
RUN apt-get install ${PACKAGES} -y

#########################################
#- Install libraries for Python needs
#########################################
ARG PACKAGES=libgeos-dev
RUN apt-get install ${PACKAGES} -y

#########################################
#- Python Dependencies Installed (faster with Codespaces this way)
#########################################
RUN pip install --no-cache-dir --upgrade pip 

#CGW -> Unable to get requirements file visible during image build
#       Moved pip installs to this location to "hopefully" speed up codespace
#       setup using pre-builds.  These routines remain in bootstrap but are commented
#       out to show where they could be
#ARG REQ_FILE="/var/lib/docker/codespacemount/workspaces/jbooks/environment/requirements.txt"
#RUN pip install --no-cache-dir -r ${REQ_FILE} 
RUN pip install --no-cache-dir nvidia-cudnn-cu11==8.6.0.163
RUN pip install --no-cache-dir tensorflow==2.13.1
RUN pip install --no-cache-dir tensorrt
RUN pip install --no-cache-dir svgling
RUN pip install --no-cache-dir PyMuPDF


#########################################
#- Final clean-up
#########################################
RUN apt-get clean -y

CMD ["rm", "-rf", "/var/lib/apt/lists/*"]

