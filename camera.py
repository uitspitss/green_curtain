#!python
#-*-coding:utf-8-*-
#Time-stamp: <Tue Mar 10 16:01:14 JST 2015>

from datetime import datetime
import time
import picamera
import os

def main():
    now = datetime.now()
    script_dir = os.path.abspath(os.path.dirname(__file__))
    root_dir, _ = script_dir.rsplit("/", 1)
    pic_dir = root_dir + "/pic"
    if not os.path.isdir(save_dir):
        os.makedirs(pic_dir)
    # print(now.strftime("%Y-%m-%d"))
    with picamera.PiCamera() as cam:
        cam.resolution = (800, 600)
        # cam.start_preview()
        # cam.led = True # GPIO required root?
        time.sleep(2)

        # makedir if not day directory
        save_dir = pic_dir + "/" + now.strftime("%Y-%m-%d")
        if not os.path.isdir(save_dir):
            os.makedirs(save_dir)
        save_pic_path = save_dir + "/" + now.strftime("%Y%m%d_%H%M%S.jpg")
        cam.capture(save_pic_path)
        # print(save_pic_path)

if __name__ == '__main__':
    main()
