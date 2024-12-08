def get_int(prompt):
  while True:
    try: 
      return int(input(prompt))
    except ValueError:
      print("Not an integer")



def main():
  #keep asking for a number between 0 and 8
  while True:
    height = get_int("Height: ")
    if 0 < height <= 8:
      break

  for i in range(height + 1):
    space = " "
    brick = "#"
    print((space * (height-i)) + (brick * i) + (space * 2) + (brick * i)) 


main()
