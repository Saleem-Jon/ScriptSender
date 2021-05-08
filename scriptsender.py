import pyautogui as pt
from time import sleep

sleep(3)


#Opening the file
word = "x"   

    


def send_message():
          
    global word
    with open('PutYourScriptHere.txt', 'r') as f:
        try:
            for line in f:
       
            # reading each word        
                for word in line.split():
                     pt.typewrite(word)
                     pt.typewrite("\n")
                    
           

       

        
        except:
            print("cant find")
        # if postion == True:
       
        
    #     pt.typewrite("in")
    #pt.typewrite("\n")

send_message()
