import json
import difflib

data = json.load(open("Data.json"))

def Translate(userInput):
    userInput = userInput.lower() 
    closeMatch = difflib.get_close_matches(userInput,data.keys())[0]
    if userInput in data:
        result = data[userInput]
        return result
    elif userInput.capitalize() in data:
        return data[userInput.capitalize()]
    elif userInput.upper() in data:
        return  data[userInput.upper()]      
    elif  closeMatch != " ": 
        #return "Do you mean "+closeMatch+" instead. Please double check it." 
        userEntry = input("Do you mean "+closeMatch+" instead? Enter Y if Yes or N if No: ")
        if userEntry.upper() == 'Y':
            return data[closeMatch]
        elif userEntry.upper() == 'N':
            return  "The word doesn't exists. Please double check it."    
        else:
            return "We didn't understand your entry." 
    else:
        return "The word doesn't exists.Please double check it." 

while True:
    a = ['q','quit']
    userInput = input("Enter word:")
    if userInput.lower() not in a:
        output = Translate(userInput)
        if isinstance(output,list):
            for item in output:
                print(item)
        else:
            print(output)    
    else:
        break    