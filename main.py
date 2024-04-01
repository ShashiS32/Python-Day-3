age = int(input("How old are you? "))
height = int(input("How tall are you? "))

if age <= 8:
  print("Sorry you are too young to ride this ride")
else:
  if height <= 40:
    print("Sorry you are too short to ride this ride")
  else:
    print("You are tall and old enough for this ride")