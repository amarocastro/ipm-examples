#!/usr/bin/env python

import numpy
import cv2
import sys


class VideoGrabber():

  def __init__(self, roi, filename):
    self.cam=cv2.VideoCapture(0)
    self.roi = roi
    self.filename = filename
         
      
  def run(self):    


    if self.cam.isOpened():
      width = int(self.cam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
      height = int(self.cam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
      writer = cv2.VideoWriter(self.filename, 
        cv2.cv.CV_FOURCC('M', 'P', '4', '2'), # MPEG-4 codec
        15, # FPS
        (width, height) )
      if writer.isOpened():  
      
        stop = False
        while not stop: # Hit ESC for stop the capture!
          frame = self._get_frame()
          writer.write(frame)
        
          self._draw_buttons(frame, self.roi)
          frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          cv2.imshow("win", frame)
          key = cv2.waitKey(30)
          if key == 27:
            stop = True
          
      else:
        print "Error: cam not opened"
      
      

  def _get_frame(self):
     _, frame = self.cam.read()  
     frame_flipped = cv2.flip(frame, 1)
     return frame_flipped

  def _draw_buttons(self, frame, roi, color=(255,0,255)):
    for r in roi:
      cv2.rectangle(frame, (r[0],r[1]), (r[2],r[3]), color,4)
      


roi = [ (0,0, 50, 50)]
if len(sys.argv) > 1:
  vid = VideoGrabber(roi, sys.argv[1])
  print "Press ESC to exit..."
  vid.run()
else:
  print "Usage: VideoGrabber output-file.avi"



