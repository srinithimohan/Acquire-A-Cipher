# IMPORTS
from termcolor import colored, cprint
import string

# FUNCTIONS FOR CIPHERS - MATCH FROM TEXT TO CIPHER
def morse_code(letter):
      if letter.upper() == "A":
          return "._"
    
      elif letter.upper() == "B":
          return "_..."
    
      elif letter.upper() == "C":
          return "_._."
    
      elif letter.upper() == "D":
          return "_.."
    
      elif letter.upper() == "E":
          return "."
    
      elif letter.upper() == "F":
          return ".._."
    
      elif letter.upper() == "G":
          return "__."
    
      elif letter.upper() == "H":
          return "...."
    
      elif letter.upper() == "I":
          return ".."
    
      elif letter.upper() == "J":
          return ".___"
    
      elif letter.upper() == "K":
          return "_._"
    
      elif letter.upper() == "L":
          return "._.."
    
      elif letter.upper() == "M":
          return "__"
    
      elif letter.upper() == "N":
          return "_."
    
      elif letter.upper() == "O":
          return "___"
    
      elif letter.upper() == "P":
          return ".__."
    
      elif letter.upper() == "Q":
          return "__._"
    
      elif letter.upper() == "R":
          return "._."
    
      elif letter.upper() == "S":
          return "..."
    
      elif letter.upper() == "T":
          return "_"
    
      elif letter.upper() == "U":
          return ".._"
    
      elif letter.upper() == "V":
          return "..._"
    
      elif letter.upper() == "W":
          return ".__"
    
      elif letter.upper() == "X":
          return "_.._"
    
      elif letter.upper() == "Y":
          return "_.__"
    
      elif letter.upper() == "Z":
          return "__.."
    
      elif letter == "1":
          return ".____"
    
      elif letter == "2":
          return "..___"
    
      elif letter == "3":
          return "...__"
    
      elif letter == "4":
          return "...._"
    
      elif letter == "5":
          return "....."
    
      elif letter == "6":
          return "_...."
    
      elif letter == "7":
          return "__..."
    
      elif letter == "8":
          return "___.."
    
      elif letter == "9":
          return "____."
    
      elif letter == "0":
          return "_____"
        
      elif letter == ".":
          return "._._._"
        
      elif letter == ",":
          return "__..__"
        
      elif letter == ":":
          return "___..."
        
      elif letter == "?":
          return "..__.."
        
      elif letter == "'":
          return ".___."
        
      elif letter == "-":
          return "_...._"
        
      elif letter == "/":
          return "_.._."

      elif letter == "(":
          return "_.__._"

      elif letter == ")":
          return "_.__._"

      elif letter == '"':
          return "*_**_*"
    
      elif letter == " ":
          return " "




def NATO_alphabet(letter):
  if letter.upper() == "A":
          return "Alfa"
    
  elif letter.upper() == "B":
      return "Bravo"

  elif letter.upper() == "C":
      return "Charlie"

  elif letter.upper() == "D":
      return "Delta"

  elif letter.upper() == "E":
      return "Echo"

  elif letter.upper() == "F":
      return "Foxtrot"

  elif letter.upper() == "G":
      return "Golf"

  elif letter.upper() == "H":
      return "Hotel"

  elif letter.upper() == "I":
      return "India"

  elif letter.upper() == "J":
      return "Juliett"

  elif letter.upper() == "K":
      return "Kilo"

  elif letter.upper() == "L":
      return "Lima"

  elif letter.upper() == "M":
      return "Mike"

  elif letter.upper() == "N":
      return "November"

  elif letter.upper() == "O":
      return "Oscar"

  elif letter.upper() == "P":
      return "Papa"

  elif letter.upper() == "Q":
      return "Quebec"

  elif letter.upper() == "R":
      return "Romeo"

  elif letter.upper() == "S":
      return "Sierra"

  elif letter.upper() == "T":
      return "Tango"

  elif letter.upper() == "U":
      return "Uniform"

  elif letter.upper() == "V":
      return "Victor"

  elif letter.upper() == "W":
      return "Whiskey"

  elif letter.upper() == "X":
      return "X-ray"

  elif letter.upper() == "Y":
      return "Yankee"

  elif letter.upper() == "Z":
      return "Zulu"

  elif letter == " ":
      return " "
  




def reg_alphabet(letter):
  if letter.upper() == "ALFA":
          return "A"
    
  elif letter.upper() == "BRAVO":
      return "B"

  elif letter.upper() == "CHARLIE":
      return "C"

  elif letter.upper() == "DELTA":
      return "D"

  elif letter.upper() == "ECHO":
      return "E"

  elif letter.upper() == "FOXTROT":
      return "F"

  elif letter.upper() == "GOLF":
      return "G"

  elif letter.upper() == "HOTEL":
      return "H"

  elif letter.upper() == "INDIA":
      return "I"

  elif letter.upper() == "JULIETT":
      return "J"

  elif letter.upper() == "KILO":
      return "K"

  elif letter.upper() == "LIMA":
      return "L"

  elif letter.upper() == "MIKE":
      return "M"

  elif letter.upper() == "NOVEMBER":
      return "N"

  elif letter.upper() == "OSCAR":
      return "O"

  elif letter.upper() == "PAPA":
      return "P"

  elif letter.upper() == "QUEBEC":
      return "Q"

  elif letter.upper() == "ROMEO":
      return "R"

  elif letter.upper() == "SIERRA":
      return "S"

  elif letter.upper() == "TANGO":
      return "T"

  elif letter.upper() == "UNIFORM":
      return "U"

  elif letter.upper() == "VICTOR":
      return "V"

  elif letter.upper() == "WHISKEY":
      return "W"

  elif letter.upper() == "X-RAY":
      return "X"

  elif letter.upper() == "YANKEE":
      return "Y"

  elif letter.upper() == "ZULU":
      return "Z"

  elif letter == " ":
      return " "



def hill_affine_cipher(letter):
  if letter.upper() == "A":
          return 0
    
  elif letter.upper() == "B":
      return 1

  elif letter.upper() == "C":
      return 2

  elif letter.upper() == "D":
      return 3

  elif letter.upper() == "E":
      return 4

  elif letter.upper() == "F":
      return 5

  elif letter.upper() == "G":
      return 6

  elif letter.upper() == "H":
      return 7

  elif letter.upper() == "I":
      return 8

  elif letter.upper() == "J":
      return 9

  elif letter.upper() == "K":
      return 10

  elif letter.upper() == "L":
      return 11

  elif letter.upper() == "M":
      return 12

  elif letter.upper() == "N":
      return 13

  elif letter.upper() == "O":
      return 14

  elif letter.upper() == "P":
      return 15

  elif letter.upper() == "Q":
      return 16

  elif letter.upper() == "R":
      return 17

  elif letter.upper() == "S":
      return 18

  elif letter.upper() == "T":
      return 19

  elif letter.upper() == "U":
      return 20

  elif letter.upper() == "V":
      return 21

  elif letter.upper() == "W":
      return 22

  elif letter.upper() == "X":
      return 23

  elif letter.upper() == "Y":
      return 24

  elif letter.upper() == "Z":
      return 25
  



def other_hill_cipher(letter):
    if letter == 0:
          return "A"
      
    elif letter == 1:
        return "B"
  
    elif letter == 2:
        return "C"
  
    elif letter == 3:
        return "D"
  
    elif letter == 4:
        return "E"
  
    elif letter == 5:
        return "F"
  
    elif letter == 6:
        return "G"
  
    elif letter == 7:
        return "H"
  
    elif letter == 8:
        return "I"
  
    elif letter == 9:
        return "J"
  
    elif letter == 10:
        return "K"
  
    elif letter == 11:
        return "L"
  
    elif letter == 12:
        return "M"
  
    elif letter == 13:
        return "N"
  
    elif letter == 14:
        return "O"
  
    elif letter == 15:
        return "P"
  
    elif letter == 16:
        return "Q"
  
    elif letter == 17:
        return "R"
  
    elif letter == 18:
        return "S"
  
    elif letter == 19:
        return "T"
  
    elif letter == 20:
        return "U"
  
    elif letter == 21:
        return "V"
  
    elif letter == 22:
        return "W"
  
    elif letter == 23:
        return "X"
  
    elif letter == 24:
        return "Y"
  
    elif letter == 25:
        return "Z"


  

# USER INTRODUCTION
def atbash(letter):
  if letter.upper() == "A":
      return "Z"

  elif letter.upper() == "B":
      return "Y"

  elif letter.upper() == "C":
      return "X"

  elif letter.upper() == "D":
      return "W"

  elif letter.upper() == "E":
      return "V"

  elif letter.upper() == "F":
      return "U"

  elif letter.upper() == "G":
      return "T"

  elif letter.upper() == "H":
      return "S"

  elif letter.upper() == "I":
      return "R"

  elif letter.upper() == "J":
      return "Q"

  elif letter.upper() == "K":
      return "P"

  elif letter.upper() == "L":
      return "O"

  elif letter.upper() == "M":
      return "N"

  elif letter.upper() == "N":
      return "M"

  elif letter.upper() == "O":
      return "L"

  elif letter.upper() == "P":
      return "K"

  elif letter.upper() == "Q":
      return "J"

  elif letter.upper() == "R":
      return "I"

  elif letter.upper() == "S":
      return "H"

  elif letter.upper() == "T":
      return "G"

  elif letter.upper() == "U":
      return "F"

  elif letter.upper() == "V":
      return "E"

  elif letter.upper() == "W":
      return "D"

  elif letter.upper() == "X":
      return "C"

  elif letter.upper() == "Y":
      return "B"

  elif letter.upper() == "Z":
      return "A"
    
  elif letter == ".":
      return "."
    
  elif letter == ",":
      return ","
    
  elif letter == ":":
      return ":"
    
  elif letter == "?":
      return "?"
    
  elif letter == "'":
      return "'"
    
  elif letter == "-":
      return "-"
    
  elif letter == "/":
      return "/"

  elif letter == "(":
      return "("

  elif letter == ")":
      return ")"

  elif letter == '"':
      return '"'

  elif letter == " ":
      return " "




# Beginning Page - Gives user options
print(colored("Welome to Acquire A Cipher, a program that encodes messages with historial ciphers and teaches others about cryptography! ","magenta"))

print(colored("\nLearn about cybersecutiy and encryption:", "blue"))
print("\t0 - What is encryption and decryption, and cryptography?\n")

print(colored("Which cipher would you like to encode your message in?","blue"))
print("\t1 - Caesar Cipher\n"
     "\t2 - Morse Code\n"
     "\t3 - International Phonetic Alphabet\n"
     "\t4 - Hill Cipher\n"
     "\t5 - Affine Cipher\n"
     "\t6 - Vigenere Cipher\n"
    "\t7 - Atbash Cipher"
     )

print(colored("\nOr, enter the number corresponding with the option you would like to learn about:" ,"blue"))
print("\t8 - How does cryptography defend against cyber threats?\n"
     "\t9 - What are some women in cryptography, and why is diversity important?\n"
     "\t10 - What are jobs in cryptography?\n"
     )

# User input for if else statements
cipherNum = input("\nEnter the number corresponding with the option you would like: ")

# Explanation to those who may not know about about cryptography, or simply want a more in depth knowledge
if cipherNum == "0":
  print(colored("Cryptoraphy has specific words related to the field. Read on to learn more!","green"))

  print("\nCryptography - the art of writing or solving codes.")
  print("\nEncryption - the method by which information is converted into secret code that hides the information's true meaning.")
  print("\nDecryption - process that transforms encrypted information into its original format.")
  print("\nCiphers - an algorithm for performing encryption or decryption; a code.")
  print("\nCybersecurity - art of protecting networks, devices, and data from unauthorized access or criminal use.")
  print("\nCyber Threat - the possibility of a malicious attempt to damage or disrupt a computer network or system.")

  print("\n\nThank you for interacting with Acquire A Cipher! I hoped you learned more about cybersecurity and cryptography!")

# Ciphers and Information
if cipherNum == "1": # Red
  # Info about cipher
  print(colored("\nYou have chosen Caesar Cipher!\n","red"))
  print("\nFun Fact: The Caesar Cipher is one of the earliest known ciphers, developed around 100 BC. Julius Caesar used it to send secret messages to his generals in the field.")

  # Code to solve encryption
  initialPosition = 0
  shiftedPosition = 0
  shiftedMessage = ""
  lettersLower = string.ascii_lowercase
  lettersUpper = string.ascii_uppercase
  numbers = string.digits
  symbols = string.punctuation
  possibleCharacters = lettersLower + lettersUpper + numbers + symbols
  def encrypt():
    global shiftedPosition
    shiftedPosition = initialPosition + key

  def wraparound():
    global shiftedPosition
    if shiftedPosition >= len(possibleCharacters):
        shiftedPosition -= len(possibleCharacters)
    elif shiftedPosition < 0:
      shiftedPosition += len(possibleCharacters)

    # Give user instructions for encryption
  initialMessage = input("\n\nEnter the message want to convert to Caesar Cipher\nOnly use letters (uppercase or lowercase), numbers, spaces, and these special character: \"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\n")
  
  key = int(input("\nWhat is your key? Choose a number from 0 to 93. "))

  for character in initialMessage:
    if character in possibleCharacters:
      initialPosition = possibleCharacters.find(character)
      encrypt()
      wraparound()
  
      shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
  
    else:
      shiftedMessage += character

  # Print out encryption
  print()
  print("Here is your encrypted Caesar Cipher message!:\n")
  cprint(shiftedMessage.lower(),"red")

  print("\n\nThank you for interacting with Acquire A Cipher!")

if cipherNum == "2":
  # Output information to user about cipher
  print(colored("\nYou have chosen Morse Code!\n","green"))
  print("\nFun Fact: The Morse Code System was invented in the United States by inventor Samule F.B Morse in the 1830s to transmit messages through electrical teleraphy.")
  
  user_input = input("\nEnter the message want to convert to Morse Code\nOnly use letters (uppercase or lowercase), numbers, spaces, and these special character: .,:?'-/\"()\n\n")

  # Solve cipher
  sentence = []
  
  for character in user_input:
    sentence.append(morse_code(character))

  # Print out cipher
  print()
  print("Here is your encrypted Morse Code message!:")
  print(colored(" ".join(sentence),"green"))

  print("\n\nThank you for interacting with Acquire A Cipher!")

 
if cipherNum == "3": 
  # Give information about cipher
  print(colored("\nYou have chosen International Phonetic Alphabet!\n","yellow"))
  print("\nFun Fact: A phonetic alphabet is used as a set of words used instead of letters in oral communication. This program uses the NATO Phonetic Alphabet, which is the most common.")

  user_input = input("\nEnter the message you want to convert to NATO Phonetic Alphabet\nOnly use letters (uppercase or lowercase) and spaces: ")

  # Solve for cipher
  sentence = []
  
  for character in user_input:
    sentence.append(NATO_alphabet(character))

  # Print out cipher
  print()
  print("Here is your translated message in NATO Phonetic Alphabet!:\n")
  print(colored(" ".join(sentence),"yellow"))

  print("\n\nThank you for interacting with Acquire A Cipher!")

 
if cipherNum == "4": 
  # Output information about cipher
  print(colored("\nYou have chosen Hill Cipher!\n","blue"))
  print("\nFun Fact: The Hill Cipher was developed in 1929 by Lester S. Hill, an American mathematician, and uses linear algebra!")

  user_input = input('\nWhat is your keyword? Let it be a 4-letter word, examples being "hill" or "blue": ')

  # Solve for cipher
  sentence = []
  
  for character in user_input:
    sentence.append(hill_affine_cipher(character))

  user_input_sentence = input('\nWhat message would you like to encrypt? Only use letters and spaces: ')

  phrase = []
  
  for character in user_input_sentence:
    if character == " ":
      pass
    else:
      phrase.append(hill_affine_cipher(character))

  shortList = []
  chunk_size = 2
  
  for i in range(0, len(phrase), chunk_size):
      shortList.append(phrase[i:i+chunk_size])

  # Math to encrypt message
  finalList = []
  for item in shortList:
    if len(item) == 2:
      firstNum = (sentence[0] * item[0]) + (sentence[1] * item[1])
      finalList.append(firstNum%26)
      secondNum = (sentence[2] * item[0]) + (sentence[3] * item[1])
      finalList.append(secondNum%26)
    
    elif len(item) == 1:
      aNum = (sentence[0] * item[0]) + (sentence[0] * item[0]) 
      finalList.append(aNum%26)

  letterList = []
  
  for item in finalList:
    letterList.append(other_hill_cipher(item))

  # Output encryption
  print()
  print("Here is your encrypted Hill's Cipher message!:")
  print(colored("".join(letterList),"blue"))
    
  print("\n\nThank you for interacting with Acquire A Cipher!")
    

    
   
if cipherNum == "5": 
  # Give information about cipher
  print(colored("\nYou have chosen Affine Cipher!\n","red"))
  print("\nFun Fact: The Affine Cipher is an example of a Monoalphabetic Substituiton cipher, meaning that a text symbol is replaced with a cipher text symbol.\n\n")

  key = input("Enter a number that'll be used for your key: ")
  key2 = input("Enter a second number that'll be used for your key: ")

  user_input_sentence = input('\nWhat message would you like to encrypt? Only use letters (uppercase or lowercase) and spaces: ')

  # Solve for cipher
  sentence = []
  
  for character in user_input_sentence:
    if character == " ":
      pass
    else:
      sentence.append(hill_affine_cipher(character))

  # Math to encrypt cipher
  encryptedList = []
  for item in sentence:
    total = ((int(key)*item) + int(key2))%26
    encryptedList.append(total)

  letterList = []

  for item in encryptedList:
    letterList.append(other_hill_cipher(item))

  # Output encryption
  print()
  print("Here is your encrypted Affine Cipher message!:")
  print(colored("".join(letterList),"red"))

  print("\n\nThank you for interacting with Acquire A Cipher!")
 
if cipherNum == "6":
  # Give information about cipher
  print(colored("\nYou have chosen Vignere Cipher!\n","green"))
  print("\nFun Fact: The Vignere Cipher was created in 1553, by Giovan Battista Bellaso, an Italian cryptogropher.\n\n")

  # Recieve user keyword 
  key = input("Enter a keyword to encrypt your message. It is a keyword, so only enter one word!: ")

  sentence = []
    
  for character in key:
    sentence.append(hill_affine_cipher(character))

  # Recieve user message
  user_input_sentence = input('\nWhat message would you like to encrypt? Only use letters (uppercase or lowercase) and spaces: ')

  user_sentence = []

  # Take out spaces
  for character in user_input_sentence:
    if character == " ":
      pass
    else:
      user_sentence.append(hill_affine_cipher(character))

  if len(user_sentence)%len(sentence) == 0:
    x = len(user_sentence)/len(sentence)
    total_sentence = sentence*int(x)
    
  else:
    remainder = len(user_sentence)%len(sentence)
    x = len(user_sentence)/len(sentence)
    total_sentence = sentence*int(x+1)
    total_num = len(total_sentence) - len(user_sentence)
    for num in range(total_num):
      total_sentence.pop()
  
  added_list = [sum(i) for i in zip(total_sentence, user_sentence)] 
  
  encryption = []
  
  for num in added_list:
    if num > 25:
      num = num%26  
      encryption.append(other_hill_cipher(num))
    else:
      encryption.append(other_hill_cipher(num))

  # Output cipher
  print()
  print("Here is your encrypted Vignere message!:")
  print(colored("".join(encryption),"green"))

  print("\n\nThank you for interacting with Acquire A Cipher!")
  

if cipherNum == "7":
  # Give information on cipher
  print(colored("\nYou have chosen Atbash Cipher!\n","cyan"))
  print("\nFun Fact: The Atbash Cipher dates back as far as anciant Israel, and originally developed for use with the Hebrew Alphabet.")

  user_input = input("\nEnter the message you want to convert to Atbash Cipher\nOnly use letters (uppercase or lowercase) and these special character: .,:?'-/()\: ")

  # Solve cipher
  sentence = []
  
  for character in user_input:
    sentence.append(atbash(character))

  # Print out cipher
  print()
  print("Here is your encrypted Atbash Cipher message!:\n")
  print(colored("".join(sentence),"cyan"))

  print("\n\nThank you for interacting with Acquire A Cipher!")

if cipherNum == "8":
  # Give basic info first
  print("\n Cryptography secures the integrity and protection of information by encrypting data, allowing the receiver to be assured that the data has not been tampered with or intercepted during transmission and that if it were, would still ensure that the interceptor would not be able to use the data.")

  # User data - want to learn more or not
  datab = input(colored('\n\nWould you like to learn about how cryptography defends against data breaches? Enter "yes" or "no": ',"cyan"))

  # If user says yes
  if datab == "yes":
    print("\nData breaches are a type of cybersecurity risk where information is accessed and stolen without the knowledge of the systems’ owners. Most attacks are attributed to malware or hacking.")

    print("It can be devestating when a data breach occurs- personal information of users can be exploited. In March of 2021, Facebook had a data breach where 533 million of their users had their personal data leaked online, an event that could have affected anyone you know with a Facebook account.")

    print("\nThis is where cryptography comes in - it can defend against data breaches by creating a system that keep unauthorized users from gaining access to sensitive information. Modern cryptography uses encryption types such as hashing, symmetric encryption, and asymmetric encryption to create a secure network.")

        # Ask user which option to learn more about- solutions or prevention
    userDataBreach = int(input(colored("\n\nWould you like to learn how to defend against data breaches(1) or how to take action if you are apart of a data breach?(2) Enter the number correlating to the option you want: ","cyan")))

    # Output if prevention
    if userDataBreach == 1:
      print("\nHere are some tips and tricks on how YOU can defend against data breaches:")
      print("\t- Update software available. Companies will have important updates on security measured and fixing bugs.")
      print("\t- Create complex and different passwords for accounts. Ciphers are a great way to create one! ;)")
      print("\t- Have data backed up in case of a server crash or data loss.")

      print("\n\nThank you for interacting with Acquire A Cipher!")

    # Output if solution
    if userDataBreach == 2: 
      print("\nIf you do fall victim to a data breach, here are actions you can take: ")
      print("\t- Secure your accounts by updating passwords and PINs involved with the breach.")
      print("\t- Freeze your credit account so unauthorized persons will not be able to use it.")

      print("\n\nThank you for interacting with Acquire A Cipher!")

  if datab == "no":
    print("\n\nThank you for interacting with Acquire A Cipher!")

if cipherNum == "9":
  # Give user options what woman to learn about
  print(colored("\nThere have been many incredible women who have revolutionized cryptography. Enter the number of the woman you would like to learn about: ","red"))
  print("\t1 - Agnes Meyer Driscoll\t2 - Barbara McNamara")
  print("\t3 - The Female Code Breakers\t4 - Genevieve Grotjan")
  print("\t5 - Importance of Diversity in Cybersecurity and Cryptography")
  
  # Take user input
  the_amazing_woman = int(input("\nEnter number here: "))

  # Output based on user input
  if the_amazing_woman == 1:
    print(colored("\n\nAgnes Meyer Driscoll","yellow"))
    print("\t- Driscoll earned her bachelor degree in mathematics and physics in 1911, and was proficient in English, French, German, Latin, and Japanese.")
    print("\n\t- She joined the Navy in 1918 and was assigned to the Code and Signal Section throughout World War II, and her work was vital for giving American commanders knowledge on Japan’s naval aviation and maneuvers.")
    print("\n\t- Driscoll helped to design the Navy’s Cipher Machine, setting the foundation for cryptanalysis in WWII and beyond.")
    
    print("\n\nThank you for interacting with Acquire A Cipher!")

  
  if the_amazing_woman == 2:
    print(colored("\n\nBarbara McNamara","green"))
    print("\t- Barabara McNamara has had several positions in the National Security Agency (NSA)  and became the first women to be the Agency’s Deputy Director of Operations.")
    print("\n\t- Her achievements in senior positions have had a long lasting impact in improving NSA’s operations, making the United States more secure.")
    print("\n\t- Ms. McNamara has received several awards for her work, and was the 2020 Inductee of the NSA/CSS Hall of Honor.")

    print("\n\nThank you for interacting with Acquire A Cipher!")

  if the_amazing_woman == 3:
    print(colored("\n\nThe Female Code Breakers","cyan"))
    print("\t- During World War II, the Navy and Army recruited more than 10,000 women as cryptanalysts to decipher enemy codes.")
    print("\n\t- These women were sent to Washnington, D.C., and where behind some of the most significant cod-breaking achievements of the war. They ran office machines converted to code-breaking purposes, built libraries, and worked as translators.")
    print("\n\t- Arlington Hall was a secret African-American unit that made up of mostly females, tackled commercial codes and kept track of businesses involved with Hilter or Mitsubishi.")
    print("\n\t- Thanks to these women, the war was able to shorten as it aided to the success of the defeat in Japan and penetration of the Nazi Enigma cipher.")

    print("\n\nThank you for interacting with Acquire A Cipher!")

  if the_amazing_woman == 4:
    print(colored("\n\nGenevieve Grotjan","red"))
    print('\t- Grotjan was hired by the US Army Signals Intelligence Service (SIS), a team of codebreakers formed to break the most Japan’s most challenging code to date, named by cryptologists as "Purple."')
    print('\n\t- 18 months later, the code was still unbroken. Finally, in September 1940, Grotjan was the first one to find the key to breaking "Purple," a breakthrough that allows SIS to build a machine to decrypt Japanese diplomatic messages throughout WWII. Her contribution to the Allied victory saved thousands, if not millions, of lives.')

    print("\n\nThank you for interacting with Acquire A Cipher!")

  if the_amazing_woman == 5:
    print("\n\nDiversity in fields such as cybersecurity and cryptography can help develop a variety of solutions to properly defend against attacks such as data breaches, ransomware, and phishing. Incorporating people from minority groups will also ensure that marginalized people will still receive the same level of protections and security as any other, because we all deserve to know that our technology and privacy is safe.")

    print("\n\nThank you for interacting with Acquire A Cipher!")

if cipherNum == "10":
  # Gives user options of jobs to learn about
  print("\nThere are several jobs in cybersecurity that specialize in codes and ciphers. Enter the number correlating to the job you would like to learn about!: ")
  print("\t1 - Cryptanalyst\t2 - Cryptographer")

  # Takes user input
  job = int(input("\nEnter number here: "))

  # Output based on user input
  if job == 1:
    print(colored("\nCryptanalysts are employed by law enforcement and government agencies to decrypt ciphers and gain access to information from law breakers. They are code breakers.","cyan"))
    print('\t- Cryptanalysts earn a salary of an average of $131,619')
    print('\n\t- Cryptanalysts need a knack of mathematics and solving puzzles, and need a foundation in cybersecurity')
    print('\n\t- This job requires a bachelor’s degree in a technical or math-related field, such as computer science.')
    print('\n\t-  The US Bureau of Labor Statistics sees a job growth of 35% between 2021 and 2031 in information security occupations.')

    print("\n\nThank you for interacting with Acquire A Cipher!")

  if job == 2:
    print(colored("\nCryptographers help ensure computer and networking security by safeguarding data through encryption. They are code makers.","red"))
    print('\t- Cybercrime Magazine projects that 3.5 million job openings from 2021-2025 will appear!')
    print('\n\t- Cryptographers will need logical and problem-solving skills, have strong competency with mathematics, as well as experience in coding with programming languages.')
    print('\n\t- That national salary in the U.S. for cryptographers range from around $109,500 - $197,500.')
    print('\n\t-  Many employers will require a bachelor degree in computer science, mathematics, or a related field. After, many pursue a master’s or doctorate degree.')

    print("\n\nThank you for interacting with Acquire A Cipher!")
