#Time-stamp: <Wed Mar 11 11:18:47 JST 2015>

*** What's it? ***
植物の成長観察日記を付けるために、
raspberry pi でタイムラプス撮影し、
撮られた画像からタイムラプス動画を自動生成する
プログラムを作成した。

* USAGE
次の２つのプログラムからなります。
- camera.py : 画像を撮影する
- movie.py  : 撮影された画像から動画を生成する


camera.pyは```python camera.py```で、次のような動作をする仕様になっています。
・camera.pyと同ディレクトリ内に"pic"ディレクトリが無ければ、作成する
・その"pic"ディレクトリ内に"YYYY-mm-dd"ディレクトリが無ければ、作成する
・"YYYY-mm-dd"ディレクトリ内に"YYYYmmdd_HHMMSS.jpg"の画像を保存する

movie.pyは```python movie.py```で、次のような動作をする仕様になっています。
・camera.pyで撮影された画像から動画を生成します。
　この際、camera.pyで撮影するときにつけるファイル名への依存があります。


* タイムラプス撮影するには
 "camera.py"と"movie.py"をcronで動かします。
 - cron設定例
