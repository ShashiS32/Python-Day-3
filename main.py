age = int(input("How old are you? "))
if age <= 8:
  print("Sorry you are too young to ride this ride")
else:
  height = int(input("How tall are you? "))


  if height <= 40 and age > 8:
    print("You are tall and old enough for this ride")
  else:
    print ("Sorry you are too short for this")
