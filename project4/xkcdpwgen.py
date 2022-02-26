#!/usr/bin/env python3
import argparse, logging, random

# Generate a randomized password given the command line arguments
def main(args, loglevel):
  logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
  numWords = int(args.words)
  numCaps = int(args.caps)
  numNums = int(args.numbers)
  numSymbs = int(args.symbols)

  # must pass at least one word
  if numWords <= 0:
    logging.error("must provide at least one word")

  # there can only be as many capitals as words
  if numCaps > numWords:
    numCaps = numWords

  words = []

  # select numWords random words from the word list
  lines = open('words.txt').read().splitlines()
  for n in range(numWords):
    line =random.choice(lines)
    words.append(line)

  # print(words)

  # capitalize numCaps words
  for n in range(numCaps):
    words[n] = words[n].capitalize()
  
  randomizedOutput = []

  # add them to a new array in random order
  for n in range(numWords):
    randIndex = random.randint(0, len(words) - 1)
    randomizedOutput.append(words[randIndex])
    words.pop(randIndex)

  # add numbers in random places
  for n in range(numNums):
    randDigit = str(random.randint(0, 9))
    randIndex = random.randint(0, len(randomizedOutput))
    randomizedOutput.insert(randIndex, randDigit)

  symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]

  # add symbols in random places
  for n in range(numSymbs):
    randSymbolIndex = symbols[random.randint(0, len(symbols)-1)]
    randIndex = random.randint(0, len(randomizedOutput))
    randomizedOutput.insert(randIndex, randSymbolIndex)  

  result = ''
  for s in randomizedOutput:
    result = result + s
  
  print(result)
 
# to call the main() function
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Generate a secure, memorable password using the XKCD method.')
  parser.add_argument(
                      "-w",
                      "--words",
                      metavar="WORDS",
                      default=4,
                      help="include WORDS words in the password (default=4)")
  parser.add_argument(
                      "-c",
                      "--caps",
                      metavar="CAPS",
                      default=0,
                      help="capitalize the first letter of CAPS random words (default=0)")
  parser.add_argument(
                      "-n",
                      "--numbers",
                      metavar="NUMBERS",
                      default=0,
                      help="insert NUMBERS random numbers in the password (default=0)")
  parser.add_argument(
                      "-s",
                      "--symbols",
                      metavar="SYMBOLS",
                      default=0,
                      help="insert SYMBOLS random symbols in the password (default=0)")
  args = parser.parse_args()
  
  loglevel = logging.INFO
  
  main(args, loglevel)