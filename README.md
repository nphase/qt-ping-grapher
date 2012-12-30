# qt-ping-grapher

This is a super basic, super dumb PyQT app designed to take over your Raspberry Pi's external display and show just how terrible your ISP is.

## Installation and usage on Rasbpian (rasbmc)

Simple:

    % sudo apt-get install git pyqt-tools pyqt4-dev-tools python-setuptools python-rrdtool # just in case
    % git clone git@github.com:nphase/qt-ping-grapher.git
    % cd qt-ping-grapher
    % ./start

## FAQ

#### Help! My screen keeps going blank!
I had luck after modifiying `/etc/lightdm/lightdm.conf` to: `xserver-command=X -s 0 -dpms` under `[SeatDefaults]`

#### What does ./start's `export DISPLAY=:0.0` do?
Just sets the default X server target in case you want to run it from the terminal instead of a local console. I don't have a keyboard attached to my Rasperry Pi, so this makes it simpler for me. 

#### What if I don't have X installed?
Then you can't run qt-ping-grapher.

#### Who is getting pinged?
`www.google.com`. You can change that at the top of `app.py`

#### Why did you build this?
A convenient and useful excuse to play with QT and build something in python. It's been a while.
