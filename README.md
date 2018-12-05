# Driver-Fatigue-Detection

### Motivation:
	The risk, danger and sometimes tragic results of drowsy driving are alarming. The National Highway Traffic Safety 
	Administration conservatively estimates that 100,000 police-reported crashes resulted in an estimated 1,550 deaths,
	71,000 injuries, and $12.5 billion in monetary losses due to driver fatigue.
	This application detects blinks and alerts of the driver's drowsiness. It handles variable lighting conditions and 
	works pretty well in day as well as in the dark. It uses histogram equalization and gamma correction to eliminate 
	the effect of lighting.

### Create a virtual environment and activate it:
	virtualenv -p python env
	/env/Scripts/activate

### Install the required packages to run the project:
	python -m pip install -r requirements.txt

### Run blinkDetect.py:
	python blinkDetect.py


A blink is supposed to last for 300 to 400 milliseconds. So, if the eye remains closed for more than 800-900 ms, we can say that
the person is either drowsy or sleeping. On the other hand, if the eye reopens after just 100ms, its considered an invalid blink 
discarded.

P.S: Press 'r' key to reset drowsiness alert and 'esc' to exit.

Project still in progress. Next step is to detect driver's gaze direction.