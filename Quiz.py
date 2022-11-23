from time import *
from sys import *

class text:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  NEUTRAL = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  LOADING = '\033[33m'
  QUESTION = '\033[34m'
    

def check(i):
  j = ""
  for m in i:
    if(m == 'i'):
      j = j + '1'
    elif(m == 'w'):
      j = j + '2'
    elif(m == 'k'):
      j = j + '3'
    elif(m == 't'):
      j = j + '4'
    elif(m == 'T'):
      j = j + '4'
    elif(m == 'y'):
      j = j + '5'
    elif(m == 'p'):
      j = j + '6'
    elif(m == 'q'):
      j = j + '7'
    elif(m == 'e'):
      j = j + '8'
    elif(m == 'r'):
      j = j + '9'
    elif(m == 'u'):
      j = j + '0'
    elif(m == 's'):
      j = j + '@'
    elif(m == 'o'):
      j = j + 'O'
    elif(m == 'a'):
      j = j + '!'
    elif(m == 'A'):
      j = j + '!'
    elif(m == 'd'):
      j = j + '#'
    elif(m == 'm'):
      j = j + '$'
    elif(m == 'h'):
      j = j + ')'
    elif(m == 'g'):
      j = j + '%'
    elif(m == 'f'):
      j = j + '('
    elif(m == 'j'):
      j = j + '*'
    elif(m == 'l'):
      j = j + '['
    elif(m == 'z'):
      j = j + 'H'
    elif(m == 'x'):
      j = j + 'n'
    elif(m == 'c'):
      j = j + 'w'
    elif(m == 'v'):
      j = j + '.'
    elif(m == 'b'):
      j = j + 'i'
    elif(m == '5'):
      j = j + '='
    elif(m == 'n'):
      j = j + '?'
    elif(m == ' '):
      j = j + ']'
    elif(m == '('):
      j = j + 'q'
    elif(m == ')'):
      j = j + 'k'
    elif(m == '.'):
      j = j + '<'
    elif(m == '\''):
      j = j + '>'
    elif(m == '"'):
      j = j + 'T'
    elif(m == '9'):
      j = j + 'U'
    elif(m == '2'):
      j = j + 'S'
    elif(m == '7'):
      j = j + 'x'
    elif(m == '-'):
      j = j + 'A'
    elif(m == '0'):
      j = j + 't'
      
  return j

correct = 0
loading_string = "...loading..."
print(f"{text.LOADING}")
for letter in loading_string:
  sleep(0.1) # In seconds
  stdout.write(letter)
  stdout.flush()

sleep(2)

passA = ["i!w32!9#q=tk", "(O92!9#qA=tk", "[8(4qUtk", "91%)4qSxtk", "4094[8", "!]4094[8"]

print("\n")

print(f"{text.HEADER}\t\t\t\t-----  Its Quiz Time! -----")

sleep(1)

question_1 = "Question\t| What command could you use to move backwards 50 units?"
print(f"{text.QUESTION}")
count = 0
for letter in question_1:
  count += 1
  if (count > 11):
    sleep(0.05) # In seconds
    stdout.write(letter)
    stdout.flush()
  elif (count == 11):
    sleep(0.1)
    stdout.write(letter)
    stdout.flush()
  else:
    stdout.write(letter)
    stdout.flush()

print("")
ans = input(f"{text.NEUTRAL}Answer\t\t| {text.NEUTRAL}")
print("\n")
if ((check(ans) == passA[0]) | (check(ans) == passA[1])):
  correct += 1
  print(f"{text.OKGREEN}Response\t| Excellent! That's correct!\n")
else:
  print(f"{text.FAIL}Response\t| You can either use \"forward(-50)\" or \"backward(50)\".'\n")

sleep(3)

question_2 = "Question\t| If your turtle is facing East, what command could\n\t\t\t| you use to make your turtle face North?"
print(f"{text.QUESTION}")
count = 0
for letter in question_2:
  count += 1
  if (count > 11):
    sleep(0.05) # In seconds
    stdout.write(letter)
    stdout.flush()
  elif (count == 11):
    sleep(0.1)
    stdout.write(letter)
    stdout.flush()
  else:
    stdout.write(letter)
    stdout.flush()

print()
ans = input(f"{text.NEUTRAL}Answer\t\t| {text.NEUTRAL}")
print("\n")

if (((check(ans) == passA[2]) | (check(ans) == passA[3])) & (correct == 1)):
  correct += 1
  print(f"{text.OKGREEN}Response\t| Superb! \n\t\t\t| You got another correct!\n")
elif (((check(ans) == passA[2]) | (check(ans) == passA[3])) & (correct == 0)):
  correct += 1
  print(f"{text.OKGREEN}Response\t| Great coding skills! You were correct! \n")
else:
  print(f"{text.FAIL}Response\t| We could either use \"left(90)\" or \"right(270)\".\n\t\t\t| If you said \"seth(90)\", you are also correct, it\n\t\t\t| just has not been taught yet!\n")

sleep(3)

question_3 = "Question\t| Brain Teaser! What has armor but is not a\n\t\t\t| knight, snaps but is not a twig, and is\n\t\t\t| always at home even on the move?"
print(f"{text.QUESTION}")
count = 0
for letter in question_3:
  count += 1
  if (count > 11):
    sleep(0.05) # In seconds
    stdout.write(letter)
    stdout.flush()
  elif (count == 11):
    sleep(0.1)
    stdout.write(letter)
    stdout.flush()
  else:
    stdout.write(letter)
    stdout.flush()

print()
ans = input(f"{text.NEUTRAL}Answer\t\t| {text.NEUTRAL}")
print("\n")

if (((check(ans) == passA[4]) | (check(ans) == passA[5])) & (correct == 2)):
  correct += 1
  print(f"{text.OKGREEN}Response\t| DAMN!! You got EVERY ONE of them correct!! \n\t\t\t| Impressive!\n")
elif (((check(ans) == passA[4]) | (check(ans) == passA[5])) & (correct == 1)):
  correct += 1
  print(f"{text.OKGREEN}Response\t| Whoa! You got 2/3 correct?! That's really good!\n\t\t\t| \n")

elif (((check(ans) == passA[4]) | (check(ans) == passA[5])) & (correct == 0)):
  correct += 1
  print(f"{text.OKGREEN}Response\t| Crazy stuff! You coded today and got got the brain teaser!\n\t\t\t| Well done!\n")
else:
  print(f"{text.FAIL}Response\t| The answer was a turtle!")