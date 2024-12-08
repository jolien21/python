import re

def main():
  #variables
  tekst = input("Tekst: ")
  
  word_count = len(tekst.split())
  letter_count = len(re.findall(r'\w', tekst))
  sentences_count = len(re.findall(r'[.!?](?:\s|$)', tekst))

  #calculate cole_liau_index 
  grade = Coleman_liau_index(letter_count, sentences_count, word_count)

  #print message
  message(grade)




def Coleman_liau_index(letters, sentences, words):
  l = (letters/words)*100
  s = (sentences/words)*100

  index = (0.0588 * l) - (0.296 * s) - 15.8

  return round(index)




def message(number):
  if number < 1:
    print("Before Grade 1")
  elif number >= 16:
    print("Grade 16+")
  else:
    print("Grade", number)




main()
