
#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

Ed.LineTrackerLed(Ed.ON)
Ed.ObstacleDetectionBeam(Ed.ON)
obstacle = 0

while True:
	if Ed.ReadLineState()==Ed.LINE_ON_WHITE:
		Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_5, Ed.DISTANCE_UNLIMITED)
	else:
		Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_5, Ed.DISTANCE_UNLIMITED)
	obstacle = Ed.ReadObstacleDetection()
	if obstacle>Ed.OBSTACLE_NONE:
		Ed.LeftLed(Ed.ON)
		Ed.RightLed(Ed.ON)
		Ed.PlayBeep()
		Ed.Drive(Ed.STOP, Ed.SPEED_1, 0)
		if obstacle==Ed.OBSTACLE_AHEAD:
			Ed.Drive(Ed.STOP, Ed.SPEED_1, 0)
			Ed.TimeWait(3, Ed.Tb955IME_SECONDS)
	Ed.LeftLed(Ed.OFF)
	Ed.RightLed(Ed.OFF)
