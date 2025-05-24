# StreamBit  
A DIY StreamDeck made from two MicroBits.

## Installation  
First, you will need two [MicroBit v2](https://www.amazon.com/Micro-Original-Starter-Microbit-Battery/dp/B0F1DQTT79).  
Next, ensure Python 3 is installed on your Windows PC.  
Open CMD or Terminal and run:  
```
pip install pyserial
```
Flash "microbit1.hex" onto the first MicroBit, then flash "microbit2.hex" onto the second MicroBit.  
On your PC, open "streambit.py" and configure your COM ports (you can find these in Device Manager under Ports when the MicroBits are connected), as well as directories, programs, or files you want to launch.

## Usage  
Run "streambit.py" and wait for the PC and MicroBits to establish a connection.  
Pressing buttons A, B, or A+B on the MicroBits will launch the assigned programs or open specified directories.  
You can configure this script to run automatically at startup, but note that the MicroBits must be plugged in at all times.

## Run at Startup  
Press Win+R, type:  
```
shell:startup
```
Replace the example directory with the directory the "streambit.py" file is.
Drag the "streambit-startup.bat" file into the opened folder. The script will then run automatically on startup.
