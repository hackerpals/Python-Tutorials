#!/usr/bin/python

'''
Given a message, convert it into 1337
'''

TEST_MESSAGE = "Hello World!"
##TEST_SUBSTITUTIONS = ['e','3']
SUBSTITUTIONS = [['a','4'],['e','3'],['1','1'],['o','0'],['t','7']]

### Function Section
def encode_message(message, substitutions):
    for s in substitutions:
        old = s[0]
        new = s[1]
        message = message.replaace(old,new)
        print("converted text = " + message)
    print("Leaving encode_message")
    return message


#### Testing Section
message = input("Type the message to be encoded here: ")
converted_text = encode_message(message, SUBSTITUTIONS)
print("started with "+message)
print("Converted to "+converted_text)
