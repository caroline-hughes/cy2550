#!/usr/bin/env python3

from email.policy import default
import sys, argparse, logging

# Gather our code in a main() function
def main(args, loglevel):
  logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
  
  numWords = 4


  
  # TODO Replace this with your actual code.
  print("Hello there.")
  logging.info("You passed an argument.")
  logging.debug("Your Argument: %s" % args.argument)
 

 
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Generate a secure, memorable password using the XKCD method.')
  # parser = argparse.ArgumentParser( 
  #                                   description = "Does a thing to some stuff.",
  #                                   epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
  #                                   fromfile_prefix_chars = '@' )
  # TODO Specify your real parameters here.
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
  
  # Setup logging
  # if args.verbose:
  #   loglevel = logging.DEBUG
  # else:
  loglevel = logging.INFO
  
  main(args, loglevel)