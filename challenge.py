import numpy as np
import sys
data = []
while True:
    inputs = input("Please enter your number (type exit to quit the program):\n")
    if inputs == 'exit':
        break
    try:
        data.append(float(inputs))
        #print (round(np.mean(data), 3), round(np.std(data), 3), round(np.median(data), 3))
        sys.stdout.write (str(round(np.mean(data), 3)) + " ")
        #sys.stdout.write ('')
        sys.stdout.write (str(round(np.std(data), 3)) + " ") 
        #sys.stdout.write ('')
        sys.stdout.write (str(round(np.median(data), 3)))
        sys.stdout.write ('\n')
    except ValueError:
        print ("The enterred value is not a number! Please enter a valid number:")

    
    

