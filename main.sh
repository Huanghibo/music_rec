#!/bin/bash
echo "installation"

pip install PyAudio
pip install pydub
pip install ffmpeg
pip install matplotlib
pip install numpy
pip install scipy
sudo apt install mysql-client

pip install virtualenv
virtualenv --system-site-packages env_with_system

pip install pydejavu

