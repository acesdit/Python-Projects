# ð¤ VIRTUAL-ASSISTANT ð¤

>### This Project is the Virtual Assistant that's been created by using Libraries and end-to-end Customization

### ***`"Olivia"`*** is the name of my Assistant and does whatever you ask her to do!!

<br>

## â IMPLEMENTATION â

Once the program is run, the microphone gets activated to listen to the voice commands.
The assistant gets activated only when the name assigned to her is called, otherwise it doesnât respond.
Once the assistant is activated a number of tasks can be performed by her all with youâre voice like,

### As every Assistant out there it does the following :
ð Date, time and day can be asked.\
ð Search the web.\
ð Open various apps, sites.\
â° Sets a Reminder.\
ð Open Word and write in it all with your voice.\
ð° Read out the latest news from NDTV without even opening it.\
ð¼ Change the assistant's voice as per wish.\
ð Crack some jokes.

<br>

## â¡ ALGORITHM â¡

***1ï¸â£    &nbsp; &nbsp; &nbsp; START***\
***2ï¸â£    &nbsp; &nbsp; &nbsp; Use get_audio() function to take audio input from the microphone.***\
***3ï¸â£    &nbsp; &nbsp; &nbsp; If "Olivia" in the input: Reply/Greet the user.***\
***ï¸4ï¸â£    &nbsp; &nbsp; &nbsp; Else: Ask the user to call the assistant's name in the input.***\
***5ï¸â£    &nbsp; &nbsp; &nbsp; Expect voice input/commands from the user.***\
***6ï¸â£    &nbsp; &nbsp; &nbsp; User asks to set a reminder.***\
***7ï¸â£    &nbsp; &nbsp; &nbsp; Call the reminder_seconds() function.***\
***8ï¸â£    &nbsp; &nbsp; &nbsp; Takes input as description/reason of reminder and time.***\
***9ï¸â£    &nbsp; &nbsp; &nbsp; Reminds you of your given description at a given time.***\
***1ï¸â£0ï¸â£  &nbsp;   And also notifies you using the Windows System Notification with the reason.***\
ï¸***1ï¸â£1ï¸â£  &nbsp;   User asks to open a word document.***\
***1ï¸â£2ï¸â£  &nbsp;   Calls write_content() function which Opens a word document.***\
***1ï¸â£3ï¸â£  &nbsp;   Takes live audio input for specified time.***\
***1ï¸â£4ï¸â£  &nbsp;   Audio input is converted to a string.***\
***1ï¸â£5ï¸â£  &nbsp;   This string is printed on the Word Document.***\
***1ï¸â£6ï¸â£  &nbsp;   This function includes features like using Left, right, centre align, bold, underline and italics.*** <br> 
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  ***All this is excluded from the text to be typed on the word  document.***\
***1ï¸â£7ï¸â£  &nbsp;   User asks to do a google search (search Elon Musk).***\
***1ï¸â£8ï¸â£  &nbsp;   Here the keyword is search and the rest is searched on Bing.***\
***1ï¸â£9ï¸â£  &nbsp;   Opens a browser and searches results and gives output.***\
***2ï¸â£0ï¸â£  &nbsp;   User asks for a date/time.***\
***2ï¸â£1ï¸â£  Displays day, date, time accordingly.***\
***2ï¸â£2ï¸â£  Other possible inputs.***\
&nbsp; &nbsp; &nbsp;   ***ð§¨    Runs its respective program/ calls function.***\
&nbsp; &nbsp; &nbsp;   ***ð§¨    Displays error on not recognizing input.***\
&nbsp; &nbsp; &nbsp;   ***ð§¨    Asks for the input again.***\
***2ï¸â£3ï¸â£ Input to terminate the program.***\
***2ï¸â£4ï¸â£ STOP***

<br>

## ð§ WORKING ð§

### When the program executes the mic is enabled and is waiting for the userâs input for the name of the assistant to activate it. There are three possible outcomes:
***âï¸  If no input, assistant asks politely for input***
\
***âï¸ If the input is wrong, assistant reminds the user to call out itâs name***
\
***âï¸ If the input is correct the assistant is activated*** 

<br>

### ð¡ Now when the assistant is activated there is a list of functions available for use.  For Ex. : 


 ### ***ð When the user asks for date, day or time :*** 
   Assistant replies to the user accordingly getting real time values with hardcoded name of days.


 ### ***ð When the user asks for a reminder to be set :***
   Assistant asks what to remind and will remind the user at the specified time with the specified reason. Assistant also uses a system notification sent for reminding.


### ***ð When the user asks to use a word :***
   Assistant opens a word file and does real time typing while the user is talking excluding the words like bold, italics, underline, centre. left, right align while providing    functions for the same.


### ***ð When the user asks for latest news updates :***
   Assistant web scraps NDTV.com in the background for the latest news and prints it on the output panel of the IDE with a link provided for the same.


### ***ð When the user asks for a web search :***
   Assistant searches the web for the same and opens the browser for us.


### ***ð When the user asks for help in python :***
   Assistant gives the user a choice of three websites commonly used for programming related doubts. According to the userâs wish the assistant opens the chosen website.


### ***ð When the user asks for some jokes :***
   Assistant gets jokes from a dataset of more than 60,000 jokes and speaks it out and after every joke accesses a .mp3 file in the computer directory for a crowd laughing effect.


### ***ð When the user asks to change the voice :***
   Assistant changes its voice to male and asks the user if would like to be kept and do so accordingly. If the user doesnât like that voice it changes to another voice and again asks the user for acceptance, and do so accordingly.


### ***ð When the user asks to open any application :***
   Assistant opens the computer applications. These applications can be stored in a file with the applications shortcuts and this file path can be saved in the environment variables so that it can be accessed anywhere in the computer.
