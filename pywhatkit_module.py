#pip install pywhatkit

# importing the module 
import pywhatkit

#1. Send Whatsapp Messages:
pywhatkit.sendwhatmsg("+12035437486", "Hello!! This is pywhatkit.", 12, 49) 
#Syntax: pywhatkit.sendmsg(“receiver mobile number”,”message”,hours,minutes)
#Parameters:
#Receiver mobile number: The Receiver’s mobile number must be in string format and the country code must be mentioned before the mobile number.
#Message: Message to be sent(Must be in string format).
#Hours: This module follows the 24 hrs time format.
#Minutes: Mention minutes of the scheduled time for the message(00-59).

#2. Play a YouTube video: 
# video of GeeksforGeeks 
pywhatkit.playonyt("https://youtu.be/gNN5HDgx370")
#Syntax: pywhatkit.playonyt(“url/topic name”)
#Parameters: 
#URL/Topic Name: Mention the topic name or URL of the YouTube video

#3. Perform Google Search: 
# it will perform the Google search 
pywhatkit.search("Python")
#Syntax: pywhatkit.search(“Keyword”)
#Parameters: 
#Keyword: It open your browser and performs search operation.

#4. Get information on  particular topic: 
# it will perform google search 
pywhatkit.info("Google", lines = 4) 
#Syntax: pywhatkit.info(“topic”,lines=x)
#Parameters: 
#Topic: Gives the output on the topic mentioned.
#lines: It prints the searched topic in the specified number of lines.