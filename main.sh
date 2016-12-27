#!/bin/bash
echo "NAMASTE"


#installing ffmpeg libraries for chromaprint. This may take few minutes
cd ffmpeg-3.2.2
tar xvjf ffmpeg-3.2.2.tar.bz2
./configure --disable-yasm --enable-shared
sudo make
sudo make install
cd ..

#installing chromaprint
cd chromaprint-1.4
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TOOLS=ON
make
sudo make install
cd ..
#installation complete

echo "INSTALLATION COMPLETE"
