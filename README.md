# Jarvis
Virtual Assistant
This is a Python script for a voice assistant called "Jarvis". The script uses various modules such as pyttsx3, speech_recognition, wikipedia, webbrowser, os, and smtplib to enable various functionalities such as sending emails, opening applications, searching Wikipedia, and opening websites.

The script starts by initializing the pyttsx3 engine and setting the voice property. The greet() function is used to greet the user and ask for their query. The command() function is used to recognize the user's speech using the speech_recognition module.

The send_email() function is used to send an email using the smtplib module. It prompts the user for the email recipient, subject, and body and then sends the email using the SMTP protocol.

The rest of the script contains various if-else statements that perform specific tasks based on the user's query. For example, if the user says "open calculator", the script will attempt to open the calculator application using the os module. Similarly, if the user says "search Wikipedia for Albert Einstein", the script will use the wikipedia module to search for Albert Einstein and then speak the first two sentences of the corresponding Wikipedia page.

The script also contains an exit condition that exits the program if the user says "exit", "thanks", or "thank you".

Overall, this script serves as a basic implementation of a voice assistant using Python and various modules.
