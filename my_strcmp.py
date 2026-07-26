import sys

weather="sunny"
def my_strcmp():
  wethr = sys.argv[1:]
  if wethr.lower() == weather:
      print("Wow u matched the weather compare variable now go play")
  elif wethr.lower() == "cloudy":
      print("the weather is cloudy take your umbrella")
  elif wethr.lower() == "cold":
      print("get your coat:")
  else:
      print("take it easy and go for a walk if its not raining")

my_strcmp()
