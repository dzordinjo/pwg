# PWG
**PWG** is a simple and secure CLI (Command Line Interface) tool for generating passwords of your choice. It provides the ability to create strong, random passwords using a combination of upper and lower case letters, numbers and punctuation.

## Features
- Random password generation
- Selection of password length
- Option to include: uppercase and lowercase letters, uppercase or lowercase letters only, numbers, punctuation marks
- Nice ASCII banner with the name of the program
- Colors in the terminal for better readability

## Installation
1. Clone the repository or download the ZIP: git clone https://github.com/dzordinjo/pwg.git
2. Install the package locally using pip:
   > cd pwg
   > pip install ./.pwg
3. Verify that the installation was successful
   > pwg

## Usage
1. Run PWG:
   > pwg
2. Follow the instuctions in the terminal
   - Select the length of the password
   - Select whether you want letters, numbers, and/or punctuation
3. PWG generates a colored password and prints it to the screen

## Technical information
- Python 3.10+
- Libaries used: random and string (standard libary), pyfiglet (ASCII banner), colorama (colors in terminal)

## Safety
- Passwords are generated locally, they are never sent to the server
- The randomness is based on Python's random.choices, which ensures good quality for everyday passwords, although we are currently working on implementing the 'secrets' module from the Python standard library to enhance security even more

## Author
**dzordinjo** - **dzordinjo@proton.me**
GitHub: https://github.com/dzordinjo/pwg

## License
This project is licensed under the MIT License. Feel free to use, modify and share it.
