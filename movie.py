#!python
#-*-coding:utf-8-*-

from subprocess import call
from datetime import datetime, date, timedelta
from os.path import isfile, isdir
import os
import shutil

def main():
    pic_dir = "/home/john/Job/green_curtain/pic"
    tmp_dir = "/home/john/Job/green_curtain/tmp_mov"

    time_list = (
        "06:00", "07:00", "08:00", "09:00", "10:00",
        "06:30", "07:30", "08:30", "09:30", "10:30",
        "11:00", "12:00", "13:00", "14:00", "15:00",
        "11:30", "12:30", "13:30", "14:30", "15:30",
        "16:00", "17:00", "18:00",
        "16:30", "17:30", "18:30",
    )

    set(time_list)

    begin_date = datetime(2014, 6, 25)

    _date = begin_date
    # date_now = datetime.now()
    date_now = datetime(2014, 7, 14) # test

    image_format = ".jpg"

    time_list = [x.replace(":","") for x in time_list]
    img_count = 0

    # make tmp_dir
    if not os.path.isdir(tmp_dir):
        os.makedirs(tmp_dir)

    while True:
        _date = begin_date + timedelta(days = count)

        if (date_now - _date).days < 0: break

        date_dir = _date.strftime("%Y-%m-%d")

        current_dir = "/".join((pic_dir, date_dir))
        if os.path.isdir(current_dir):
            for file_name in sorted(os.listdir(current_dir)):
                fn_hm = (file_name.split(".")[0].split("_")[1])[0:4] # ファイル名のHHMM
                fn_date = (file_name.split(".")[0].split("_")[0])    # ファイル名のmmdd
                # if fn_hm in time_list:
                if True:
                    print(file_name)
                    img_count += 1

                    # time stamp
                    ts = "-".join((fn_date[0:4], fn_date[4:6], fn_date[6:8]))+ "\ " + ":".join((fn_hm[0:2], fn_hm[2:4])) # タイムスタンプ文字列の生成
                    timestamp("/".join((current_dir,file_name)),
                              "/".join((tmp_dir, str(img_count).zfill(6) + image_format)),
                              ts)

    print("img_count : " + str(img_count))

    call("ffmpeg -y -r 5 -i {:s}/%06d{:s} movie{:s}.mp4".format(tmp_dir, image_format, datetime.now().strftime("%H%M%S")), shell=True)

def timestamp(input_img, output_img, ts):
    # inpath[string], outpath[string], timestamp[string]
    '''画像にタイムスタンプ文字列を合成'''

    output = "convert"

    cmd = {# '-background': 'black',
           '-fill' : 'white',
           '-font' : 'font/ipag.ttf',
           '-pointsize' : '24',
           '-gravity' : 'south',
           '-annotate' : '0 ' + ts,
    }

    for k,v in cmd.items():
        output += " {} {}".format(k,v)

    output = " ".join((output, input_img, output_img))
    res = call(output, shell=True)
    print(ts)

if __name__ == '__main__':
    main()
