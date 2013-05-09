#Initialize parts of the program

User_Card_Inserted = 'No'
User_Auth = 'Not Authed'

def Open_Iris_Doors():
    print 'Opening Iris Scanning Booth doors...'

def Open_LHC_Doors():
    

print 'Welcome to the user authorization area.'
print 'Please enter your card.

 User_Card_Inserted == 'No':
    print 'Please enter your user card...'
    User_Card_Inserted = raw_input()
else:
    print 'Checking user auth... Please wait.'
    if User_Auth == 'Granted':
        print 'User Auth granted.'
        print 'Please continue to the Iris scanning booth..'
        print 'Ejecting user card...'
    else:
        print 'User Auth not granted.'
        print 'Ejecting user card...'
    User_Card_Inserted = 'No'
