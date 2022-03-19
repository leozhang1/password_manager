
from secrets import Secrets

from menu import create, find, find_accounts, menu

# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email

secret = Secrets.SECRET_KEY

passw = input('Please provide the master password to start using leomanager3000: ')

if passw == secret:
    print('You\'re in')

else:
    print('no luck')
    exit()

choice = menu()
while choice != 'Q' and choice != 'q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    else:
        choice = menu()
exit()
