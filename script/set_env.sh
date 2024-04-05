#!/bin/sh
#

echo "source ~/.bashrc_lib_paths" >> ~/.bashrc;
touch ~/.bashrc_lib_paths;
echo "export LD_LIBRARY_PATH=\"/usr/lib:/usr/lib64:/usr/lib:/usr/lib64:~/.local/lib/python3.9/site-packages/nvidia/cudnn/lib:~/.local/lib/python3.9/site-packages/tensorrt_libs\"" >> ~/.bashrc_lib_paths;
