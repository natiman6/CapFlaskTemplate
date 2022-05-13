# The purpose of this file is to hold sensitive information that you don't want to 
# post publicly to GitHub.  This file is excluded from being sent to github by .gitignore

def getSecrets():
    secrets = {
        'MAIL_PASSWORD':'00413289',
        'MAIL_USERNAME':'s_nathan.negose@ousd.org',
        'MONGO_HOST':'mongodb+srv://nathannegose:Natiman6.com@cluster0.l1d7y.mongodb.net/capstone?retryWrites=true&w=majority',
        'MONGO_DB_NAME':'capstone'
        }
    return secrets