# Animation Encoder
## Overview
anim_encoder creates small JavaScript+HTML animations from a series on PNG images.
This is a modification of that original post, that adds some actual documentation
cleans up the code base a bit and attempts to make it slightly more reliable. So that
if anyone actually wants to use this is a project they can get up and running really
quickly.

## Installation

### Linux

Installing on Linux is relatively straightforward:
```
sudo apt-get install pngcrush python-opencv python-numpy python-scipy
git clone https://github.com/baronomasia/anim_encoder
cd anim_encoder
```

### MacOS
Installing on MacOS requires significantly more steps. Tested on MacOS Sierra 10.12.0. Requires [homebrew](http://brew.sh/).
```
brew install python
# Add brew path to bash_profile if not already present
echo "export PATH=/usr/local/bin:$PATH" >> ~/.bash_profile
source ~/.bash_profile
# virtualenv steps below recommended but not required
pip install virtualenv virtualenvwrapper
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile
source ~/.bash_profile
mkvirtualenv anim_encoder
# Install dependencies
pip install numpy
brew install gcc
pip install scipy
# Install PIL
pip install http://effbot.org/media/downloads/Imaging-1.1.7.tar.gz
brew tap homebrew/science && brew install —HEAD opencv3
brew install libpng libjpeg pygtk pngcrush
# Commands directly below required for virtualenv users only (parts of the paths below may be different for you)
cp /usr/local/Cellar/opencv3/HEAD-2038434_4/lib/python2.7/site-packages/cv2.so ~/.virtualenvs/anim_encoder/lib/python2.7/site-packages/.
workon anim_encoder
# Clone this repo and enter the directory
git clone https://github.com/baronomasia/anim_encoder
cd anim_encoder
```

Original details of this endeavor are available at http://www.sublimetext.com/~jps/animated_gifs_the_hard_way.html

## Getting Started

### Capturing your own images
Images will be saved to capture, you simply need to run capture.py and then go about your task.
Note you can just delete frames you don't want as you initially set up, which may save you some
time. Run the command below to start capturing images (hit Ctrl + C to stop capture).

```
python capture.py path/to/screenshot/directory
```

### Generating the animation
```
python anim_encoder.py path/to/screenshot/directory
firefox example.html
```

If you need to change any settings it should be pretty simple just jump over to config.py
and edit the configuration options.

## Attributions
Thanks to [sublimeHQ](https://github.com/sublimehq/anim_encoder) for starting this project.
Thanks to the following GitHub users for their helpful commits now incorporated into this fork:
* [Alanaktion](https://github.com/Alanaktion/anim_encoder)
* [ioben](https://github.com/ioben/anim_encoder/)