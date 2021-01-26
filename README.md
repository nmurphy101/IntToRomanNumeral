# Converter
Takes an input and converts it to any number of potential options.

Current Options:
 - Integer to Roman Numeral

 # Setup
 If on windows run:
    
    $ python3 -m venv venv
    $ .\venv\Scripts\activate
    $ pip3 install -r ./requirements.txt

 If on linux run:

    $ make init

 If the make file doesn't work manually run the commands:
    
    $ python3 -m venv venv
    
    $ . ./venv/bin/activate  
       or  
    $ source venv/bin/activate
    
    $ pip3 install -r requirements.txt

# Running
On Windows/Linux run:
    
    $ make run
      or
    $ python converter.py


# Testing
On Windows/Linux run:
    
    $ make test
      or
    $ pytest
