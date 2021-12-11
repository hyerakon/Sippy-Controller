import os

from sippycontroller.command_logger import THIS_FOLDER
#THIS_FOLDER = os.getcwd()
THIS_FOLDER = os.path.dirname(os.path.realpath(__file__))

token_file = os.path.join(THIS_FOLDER, 'tokens.txt')

def getTokens(integer):
    with open(token_file, 'r') as file:
        for l in file:  
            token,chadID = l.strip().split('---')
            if integer == 0:
                return token
            else:
                return chadID


