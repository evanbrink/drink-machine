# drink-machine
Raspberry pi and arduino communicate over USB. Serial protocol is outlined in pdf.

# Updating
To download update, go to terminal and run:
```
cd ~/Desktop
sudo rm -R drink-machine
git clone https://github.com/evanbrink/drink-machine
```
The arduino code Main.ino should be uploaded to the arduino.  

# Setup and Running

To run the program, you need to run setup first.  This will help with priming the pumps and can also be used later to empty the pumps.  Just run the following in terminal:
```
cd ~/Desktop/drink-machine
python3 SetupTools.py
```

To open the main User Interface, run the following:
```
cd ~/Desktop/drink-machine
python3 Main.py
```
