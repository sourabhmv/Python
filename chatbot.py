import os
import subprocess
import pyttsx3
pyttsx3.speak("hi welcome")
while True:
	pyttsx3.speak("Please specify your requirements")
	print("Please specify your requirements: "  , end='')
	p = input()
	if("don't" in p) or ("donot" in p) or ("noneed" in p) or("no need" in p) or ("not open" in p) or("not run" in p) or ("not execute" in p):
		pyttsx3.speak("Ok then tell me what I need to open")
		print("Ok then tell me what I need to open")
	
	elif(("don't" in p) or ("donot" in p) or ("noneed" in p) or("no need" in p) or ("not close" in p) or("not terminate" in p) or ("not kill" in p)) :
		pyttsx3.speak("Ok I am not going to close")
		print("Ok I am not going to close")

	else: 
			if (("run" in p) or  ("execute" in p ) or ("open" in p) or ("launch" in p))  and ((("chrome" in p) or ("browser" in p)) and ("yahoo" in p)):
				pyttsx3.speak(" opening chrome")
				os.system("start chrome yahoo.com")

			elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("launch" in p))  and (("chrome" in p) or ("browser" in p)):
				pyttsx3.speak(" opening chrome")
				os.system(" start chrome")

			elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("launch" in p) or ("show"))  and (("time" in p) or ("clock" in p)):
				pyttsx3.speak(" opening clock")
				os.system("start time")		
			elif (("close" in p) or  ("kill" in p ) or ("terminate" in p))  and (("time" in p) or ("clock" in p)):
				pyttsx3.speak(" closing clock")
				os.system(" time")		

	
			elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("launch" in p) or ("show"))  and ("calculator" in p):
				pyttsx3.speak(" opening calculator")
				os.system(" start calc")



			elif (("close" in p) or  ("kill" in p ) or ("terminate" in p))  and (("chrome" in p) or ("browser" in p)):
				pyttsx3.speak(" closing chrome")
				os.system("taskkill /f /im chrome.exe")

			elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("launch" in p)) and  (("notepad" in p) or ("editor" in p) ) :
				pyttsx3.speak(" opening notepad")
				os.system(" start notepad")

			elif (("terminate" in p) or  ("kill" in p ) or ("close" in p)) and  (("notepad" in p) or ("editor" in p) ) :
				pyttsx3.speak(" closing notepad")
				os.system("taskkill /f /im notepad.exe")

			elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("launch" in p)) and ("player" in p) and (("video" in p) or ("vlc" in p) or ("media")):
				pyttsx3.speak(" opening vlc player")
				os.system("vlc player")

			elif (("kill" in p) or  ("terminate" in p ) or ("close" in p)) and ("player" in p) and (("video" in p) or ("media" in p)):
				pyttsx3.speak(" closing vlc")
				os.system("taskkil /f /im vlc.exe")


			elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("launch" in p)) and (("photo editor" in p) or ("photoshop" in p)):
				pyttsx3.speak(" opening photoshop")
				os.system("start photoshop")

			elif (("kill" in p) or  ("close" in p ) or ("terminate" in p)) and (("photo editor" in p) or ("photoshop" in p)):
				pyttsx3.speak(" closing photoshop")
				os.system("taskkill /f /im photoshop.exe")

			elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("launch" in p) or ("capture") or("take")) and (("camera" in p) or ("video record" in p) or("photo" in p) or("selfie" in p)):
				pyttsx3.speak(" opening camera")
				subprocess.run('start microsoft.windows.camera:', shell=True)

			elif (("close" in p) or  ("terminate" in p ) or ("kill" in p)) and (("camera" in p) or ("video record" in p) or(photo) or("selfie")):
				pyttsx3.speak(" closing camera")
				subprocess.run("taskkill /f /im WindowsCamera.exe", shell=True)
			elif ("exit" in p) or ("quit" in p) or ("stop" in p):
				pyttsx3.speak("Ok bye")
				print("Ok bye")
				break	
			
	
			else:
				pyttsx3.speak("dont support")
				print("dont support")
			


