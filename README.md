Audio Fingerprinting and Recognition
====================================

Implementation of dejavu["https://github.com/worldveil/dejavu"] for audio fingerprinting and recognition on Python 2.7
Audio files can be added to mysql database in the form of audio fingerprints.
Input of audio to be recognized can be taken using either an audio file or via microphone. After listening to the audio, it is matched against fingerprints already stored in the database and a match, if found, is returned.
The UI is created using PyQt5 



Installation
============

1.	Run main.sh to install the required libraries.
##List of dependencies PyAudio, pydub, ffmpeg, matplotlib, scipy, numpy, mysql-client, virtualenv, pydejavu

2.	Open mysql from command line : 	$mysql -u root -p

3.	Create a database			 :	mysql> CREATE DATABASE nameofdb;
##This database will be used for storing fingerprinting data

Execute main.py to access the program. 
"Add folder to database"		 :	All .mp3 files in the folder will be fingerprinted and added
"File Input"					 :	Select a file to recognize
"Mic Input"						 :	Microphone is switched on instantly for specified number of seconds to listen to audio. 
##Recognition may take a while

dbconfig file is created after the first run. It stores the last used mysql config data to autofill in UI.


To contribute : Project Link["https://github.com/basu96/music_rec"]
Thanks to "worldveil"["https://github.com/worldveil"] for creating dejavu
