import re

def main():
  #ask for valid creditcardnumber
  while True:
    card_number = input('Give your creditcardnumber: ')
    if card_number.isdigit():
      break
    else:
      print('not a valid number')
      card_number = input("Give your creditcardnumber: ")
  
  #variables
  first_two_characters = card_number[:2]
  first_character = card_number[:1]
  
  length = len(card_number)
  
  American_Express = ['34', '37']
  length_AE = [15]
  
  MasterCard = ['51', '52', '53', '54', '55']
  length_MC = [16]
  
  Visa = ['4']
  length_V = [13, 16]

  product = 0
  
  #check length and first characters
  if first_two_characters in American_Express and length in length_AE and luhns_algoritm(card_number): 
      print("American Express")
  elif first_two_characters in MasterCard and length in length_MC and luhns_algoritm(card_number): 
      print("Mastercard")
  elif first_character in Visa and length in length_V and luhns_algoritm(card_number):
      print("Visa")
  else:
      print('INVALID')





#luhns algoritme
#def luhns_algoritm(string, leng):
 # tot = 0
  #pr = 0
  
  #for i in range(0, leng - 1, 2):
   # pr = int(string[i]) * 2
    #if pr >=10:
     #  str_pr = str(pr)
      # pr = int(str_pr[0]) + int(str_pr[1])
    #tot = tot + pr
  
  #for i in range(1, leng, 2):
   #   tot = tot + int(string[i])

  #last_digit = tot % 10

  #if last_digit == 0:
   #   return True

def luhns_algoritm(card_number: str) -> bool:
    # Convert card number to a list of integers
    digits = [int(d) for d in card_number]

    # Reverse the list of digits
    digits = digits[::-1]

    # Double every second digit
    doubled_digits = []
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            doubled_digits.append(digit)
        else:
            doubled_digits.append(digit * 2)
            # If doubled digit is greater than 9, subtract 9
            if doubled_digits[-1] > 9:
                doubled_digits[-1] -= 9

    # Calculate the sum of the digits
    sum_digits = sum(doubled_digits)

    # Return True if the sum is divisible by 10, False otherwise
    return sum_digits % 10 == 0

main()
