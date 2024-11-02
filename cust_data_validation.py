def email_valiadation(emailID):
    splitted = emailID.split("@")
    if len(splitted[0]) >= 8 and (len(splitted[0])) < 20:
        splitted = emailID.split("@")
        if len(splitted[0]) > 2:
            print()
            splitted = emailID.split("@")
            if emailID.startswith(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')):
                #print("Congrats...!The entered email id is valid...!")
                return True
            else:
                msg = 'Should not start with numbers'
                #print("The entered email id " + emailID + " is Invalid due to the reason : " + msg)
                return False
        else:
            msg = ' Should contain at least 2 characters before the symbol @ '
            #print("The entered email id " + emailID + " is Invalid due to the reason : " + msg)
            return False
    else:
        msg = ' Email Id length should be greater than 8 and less than 20 '
        #print("The entered email id " + emailID + " is invalid due to the reason : " + msg)
        return False
