# Background
I have been looking for a open-source test management tool for my whole life.
Once i setup a Test-link for my project but it's way too much for me.
So i decide to make one for my own.

This project is started at August 2016, and still a empty framework.
I hope i can finish this and achive my blueprint totally.


# Quick Guide
## Setup Environment
1. git clone https://github.com/evinoca/TeSonic.git
2. cd TeSonic
3. virtualenv PyEnv
4. source PyEnv/bin/activate
5. pip install -r dependence.txt
6. cd TeSonic
7. python manager.py db init
8. python manager.py db migrate -m "install"
9. python manager.py db upgrade
10. python manager.py runserver

## Prepare to meet overwhelming bugs...