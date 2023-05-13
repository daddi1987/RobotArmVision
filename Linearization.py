import math

class LinearAxisRobot():

  #  X = 20.32
  #  Y = 0.12
  #  Z = 1.23
  #  aX = X
  #  aY = Y
  #  aZ = Z
    _highJoint = 0
    _lowJoint = 0


    def CalculateGrade(self,X,Y,Z):
        #LinearMove
        rrot =  math.sqrt((X * X) + (Y * Y))  #raggio dalla vista dall'alto
        rside = math.sqrt((rrot * rrot) + (Z * Z)) #raggio dalla vista laterale. Usa rrot invece di ymm..per tutto

        rot = math.asin(X / rrot)  #Seno di X

        ##Angolo del motore passo-passo più alto. È necessario invertirlo perché questo è il modo in cui il motore gira dal vecchio codice. La compatibilità deve rimanere.
        print(rrot)
        print(rside)
        print(rot)

        high = - math.asin((rside * 0.5) / 120.0) * 2.0
        print(high)

        # Angle of Lower Stepper Motor  (acos()=Angle To Gripper)
        if (Z > 0):   # invece di asin acos è più corretto. Ma questo è stato corretto dall'angolo
            low = -math.acos(rrot / rside) + ((math.pi - high) / 2.0) - (math.pi / 2.0);
        else:
            low = + math.acos(rrot / rside) + ((math.pi - high) / 2.0) - (math.pi / 2.0);

        high = high + low

        print("Angolo Alto: ", high)
        print("Angolo Basso: ", low)

        LinearAxisRobot._highJoint = high *2
        LinearAxisRobot._lowJoint = low *2


        return high,low



