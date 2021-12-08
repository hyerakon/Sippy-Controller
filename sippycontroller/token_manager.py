import os
THIS_FOLDER = '.'
token_file = os.path.join(THIS_FOLDER, 'tokens.txt')

def getTokens(integer):
    with open(token_file, 'r') as file:
        for l in file:  
            token,chadID = l.strip().split('---')
            if integer == 0:
                return token
            else:
                return chadID


