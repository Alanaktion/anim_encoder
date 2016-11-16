#!/usr/bin/env python
# Benjamin James Wright <bwright@cse.unsw.edu.au>
# This is a simple capture program that will capture a section of
# the screen on a decided interval and then output the images
# with their corresponding timestamps. (Borrowed from stackoverflow).
# This will continue to capture for the seconds specified by argv[1]

import gtk.gdk
import time
import sys
import config
import os


print "Starting Capture"
print "================"

captureMethod = None
w = None
sz = None

def useScreenCapture():
    return os.system("type screencapture &> /dev/null") == 0

def useGtk():
    global w, sz
    try:
        import gtk.gdk
        w = gtk.gdk.get_default_root_window()
        sz = w.get_size()

        return True
    except StandardError:
        return False

def takeScreenshot():
    global captureMethod
    if captureMethod == None:
        if useScreenCapture():
            captureMethod = "screen"
        elif useGtk():
            captureMethod = "gtk"
        else:
            print "No capture methods available"
            sys.exit(1)

    if captureMethod == "screen":
        # Change the parameters for the screencapture line below to suit your needs
        # The line below captures an area of 800x450 pixels starting in the top left corner
        # Remove '-x -R0,0,800,450' from the line below to capture the entire screen
        os.system("screencapture -x -R0,97,800,450 capture/screenshot_" + str(int(round(time.time()*1000))) + ".png")
        # Use the line below to capture Slack channel messages at 800x450
        #os.system("screencapture -x -R288,23,800,450 capture/screenshot_" + str(int(round(time.time()*1000))) + ".png")
    elif captureMethod == "gtk":
        import gtk.gdk

        pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
        pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
        if (pb != None):
            pb.save("capture/screenshot_"+ str(int(time.time())) +".png","png")
            print "Screenshot " + str(i) + " saved."
        else:
            print "Unable to get the screenshot."

for i in xrange(0, config.CAPTURE_NUM):
    takeScreenshot();
    time.sleep(config.CAPTURE_DELAY)
