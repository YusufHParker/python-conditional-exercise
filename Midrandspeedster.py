speed = float(input("What is your average speed in km/h ?"))
roadSpeed = float(input("What is average speed of road ?"))
points = (speed - roadSpeed)/5
if speed <= 60:
    print("OK")
elif speed > roadSpeed:
    if points > 12:
        print("Time to go to jail!. Demerits Points" + str(points))
else:
    print("Demerit points:" + str(points))
