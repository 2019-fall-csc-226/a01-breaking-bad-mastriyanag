######################################################################
# Author: Vidya Mastriyana     TODO: Change this to your name
# Username: mastriyanag           TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
import time
user_input = input('Please type in the year when you were born to reveal your Chinese Zodiac sign!-->')

print('')

print('Your birth year is: ' + user_input +'')

print('')
# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples

if user_input == '2001':
    print("ssssssssay...you're a sssssssnake!")
if user_input == '2002':
    print("Get ready to ride 'til you can't no more to the Old Town Road, Horse!")
if user_input == '2003':
    print("Are YOU the Greatest Of All Time? 'Cause you're [a] GOAT.")
if user_input == '2004':
    print("  syntax error")
    time.sleep(3)
    print("")
    print("...Sorry, I was just MONKEYing around.")
if user_input == '2005':
    print("Rise and shine! You're a ROOSTER!")
if user_input == '2006':
    print("Like Dr. Heggen, you're a Dog, dawg! ")
    time.sleep(2)
    print("...which is kinda lame. No offense.")
if user_input == '2007':
    print("...ever heard of the Notorious P.I.G.?")
    time.sleep(1)
    print("--'cause that's you!")
if user_input == '2008':
    print("You're a RAT, and that is that.")
if user_input == '2009':
    print("You're an OX! Epic!")
if user_input == '2010':
    print("#DYK: A song has been made about one of your eyes...")
    time.sleep(1)
    print("That's right, you're a TIGER.")
if user_input == '2011':
    print("I heard that vaping's a real bad habit.")
    time.sleep(1)
    print("Oh and by the way--")
    time.sleep(1)
    print("you were born in the year of the RABBIT.")
if user_input == '2012':
    print("*ROAR!* You're a DRAGON!")
######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
print('')
friend_input = input("Type in a friend's birth year to reveal their Chinese Zodiac sign!-->")

print('')

print('Their birth year is: ' + friend_input +'')

print('')
if friend_input == '2001':
    print("ssssssssay...they're a sssssssnake! Be careful around them!")
if friend_input == '2002':
    print("Ignore the neigh-sayers, Horse!")
if friend_input == '2003':
    print("Is your friend the Greatest Of All Time? 'Cause they're a GOAT.")
if friend_input == '2004':
    print("ooh ooh! eee eee!")
    time.sleep(1)
    print("Your friend is a MONKEY!")
if friend_input == '2005':
    print("Rise and shine, ROOSTER!")
if friend_input == '2006':
    print("Like Dr. Heggen, you're a Dog, dawg! ")
    time.sleep(2)
    print("...which is kinda lame. No offense.")
if friend_input == '2007':
    print("...ever heard of the Notorious P.I.G.?")
    time.sleep(1)
    print("--'cause that's them!")
if friend_input == '2008':
    print("They're a RAT, and that is that.")
if friend_input == '2009':
    print("an OX! Epic!")
if friend_input == '2010':
    print("ROAR! a TIGER.")
if friend_input == '2011':
    print("I heard that vaping's a real bad habit.")
    time.sleep(1)
    print("Oh and by the way--")
    time.sleep(1)
    print("your friend was born in the year of the RABBIT.")
if friend_input == '2012':
    print("*Cinematic display of flames* ")
    print("Woah, a DRAGON!")
# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
