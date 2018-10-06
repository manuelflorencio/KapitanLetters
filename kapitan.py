#Import the libraries
import numpy as np
import sys
import getopt

def usage():
  print "KapitanLetter - by Manuel Florencio"
  print "------------------------------------"
  print "A tool designed to create a dictionary list based on a single word"
  print "You can obtain all possible combinations of upper and lower case letters"
  print "and mix certain vocals with numbers"
  print "------------------------------------"
  print
  print "Usage: python Kapitan.py -w word_to_modify"
  print "-h --help      - help options"
  print "-w --word      - write here the word to modify"
  print "-n --notshow   - do not show the words in command line"
  print "-s --save      - specify a path/name to save the output in a file"
  print "-a             - change all a for 4"
  print "-e             - change all e for 5"
  print "-i             - change all i for 1"
  print "-o             - change all o for 0"
  print
  print "Examples: "
  print "python Kapitan.py -w test -n -s pass.txt"
  print "python Kapitan.py --word test -e"
  print "python Kapitan.py -h"
  sys.exit(0)
  
def main():
  global word_w
  global show
  global path
  global output
  global mayus_a
  global mayus_e
  global mayus_i
  global mayus_o

  show = True
  output = False
  mayus_a = False
  mayus_e = False
  mayus_i = False
  mayus_o = False

  if not len(sys.argv[1:]):
    usage()  
  
  # read the commandline options
  try:
    opts, args = getopt.getopt(sys.argv[1:],'hw:ns:aeio',['help','word=','notshow','save','a','e','i','o'])
  except getopt.GetoptError as err:
    print str(err)
    usage()  
  
  for o,a in opts:
    if o in ('-h','--help'):
      usage()
    elif o in ('-w','--word'):
      word_w = str(a)
    elif o in ('-n','--notshow'):
      show = False
    elif o in ('-s','--save'):
      output = True
      path = str(a)
      #Filename definition
      filename = "%s" %path
      #File opening
      g = open (filename, "w")
    elif o in ('-a'):
      mayus_a = True
    elif o in ('-e'):
      mayus_e = True
    elif o in ('-i'):
      mayus_i = True
    elif o in ('-o'):
      mayus_o = True
    else:
      usage()
  
  word_ch = str(word_w)
  
  #Calculate the sizes
  lon = len(word_ch)
  lines = 2**lon  
  
  #Vector for the ASCII numbers of the word
  word_as = []
  for i in range(0,lon):
    #Filter that the word is in lower-case letter, if so, it is agregated to the vector in ASCII code
    if (ord(word_ch[i]) > 96 and ord(word_ch[i]) < 123):
      word_as.append(ord(word_ch[i]))
    else:
      print 'Error! Please, instert only lower-case letters.'
      sys.exit(0) 
  
aux_vec_init = []
for i in range(0,lon):
  aux_vec_init.append(0)
  
  #We now go for each line
  for x in range(0, lines):
    #Take the corresponding binary number
    num_bin = bin(x)
    aux_vec = aux_vec_init
    for y in range(2,len(num_bin)):
      #Put the number in a clear vector
      aux_vec[y-2] = int(num_bin[len(num_bin)-y+1]) * (-32)
      word_charact = []
    for k in range(0,len(aux_vec)):
      #Add the corresponding character in function of the corresponding number
      aux_vec[k] = aux_vec[k] + word_as[k]
      #Check if a change is required
      if (aux_vec[k] == 65 or aux_vec[k] == 97) and mayus_a == True:
        aux_vec[k] = 52
      if (aux_vec[k] == 69 or aux_vec[k] == 101) and mayus_e == True:
        aux_vec[k] = 53
      if (aux_vec[k] == 73 or aux_vec[k] == 105) and mayus_i == True:
        aux_vec[k] = 49
      if (aux_vec[k] == 79 or aux_vec[k] == 111) and mayus_o == True:
        aux_vec[k] = 48
      word_charact.append(chr(aux_vec[k]))
    word_to_save = ''.join(word_charact)
    #Print the wordlist
    if show == True:
      print word_to_save
    #Save the wordlist in a file    
    if output == True:
      g.write(word_to_save)
      g.write("\n")      
  
  #Close the file (if opened)
  if output == True:
    g.close()
main()