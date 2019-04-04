
#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

Ed.LineTrackerLed(Ed.ON)
clap = 0
obstacle = 0

while True:
    if clap == 0:
        waitClap()
        clap = 1
        if Ed.ReadLineState()==Ed.LINE_ON_WHITE:
            Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_1, Ed.DISTANCE_UNLIMITED)
        else:
            Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_1, Ed.DISTANCE_UNLIMITED)
    obstacle = Ed.ReadObstacleDetection()
    if obstacle>Ed.OBSTACLE_NONE:
		Ed.LeftLed(Ed.ON)
		Ed.RightLed(Ed.ON)
		Ed.PlayBeep()
		if obstacle==Ed.OBSTACLE_AHEAD:
		    Ed.Drive(Ed.STOP, Ed.SPEED_1, 0)
		    Ed.TimeWait(3, Ed.TIME_SECONDS)

def waitClap():
	while Ed.ReadClapSensor() != Ed.CLAP_DETECTED:
		pass
