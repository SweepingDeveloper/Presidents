presidents = ['George Washington','John Adams','Thomas Jefferson','James Madison','James Monroe','John Quincy Adams','Andrew Jackson','Martin VanBuren','William Henry Harrison','John Tyler','James K. Polk','Zachary Taylor','Millard Filmore','Franklin Pierce','James Buchannan','Abraham Lincoln','Andrew Johnson','Ulysses S. Grant','Rutherford B. Hayes','James Garfield','Chester A. Arthur','Grover Cleveland','Benjamin Harrison','Grover Cleveland','William McKinley','Theodore Roosevelt','William Howard Taft','Woodrow Wilson','Warren G. Harding','Calvin Coolidge','Herbert Hoover','Franklin D. Roosevelt','Harry S. Truman','Dwight D. Eisenhower','John F. Kennedy','Lyndon Johnson','Richard Nixon','Gerald Ford','Jimmy Carter','Ronald Reagan','George H. W. Bush','Bill Clinton','George W. Bush','Barack Obama','Donald Trump']

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .*"

def findLastName(string):
    spaceFound = False
    counter = -1
    upperLetter = ""
    while not spaceFound:
        if string[counter] == " ":
            spaceFound = True
        counter -= 1
    counter += 2
    return string[counter:]

def findFirstName(string):
    lastName = findLastName(string)
    tempText = string[:len(string) - len(lastName) - 1]
    return tempText

def putNamesTogether(string):
    lastName = ""
    firstName = ""
    mode = "lastName"

    for a in string:
        if (a == "*"):
            mode = "firstName"
        elif (mode == "lastName"):
            lastName += a
        else:
            firstName += a

    return firstName + " " + lastName
                
def easySort(array):
    tempArray = []
    finalArray = []
    for a in array:
        tempString = findLastName(a) + "*" + findFirstName(a)
        tempArray.append(tempString)

    tempArray.sort()

    return tempArray
    
presidents = easySort(presidents)

for a in presidents:
    print (putNamesTogether(a))

    

    
