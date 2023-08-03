import random
import string

def passwordGenerator(pwdSize, uppercase=False, lowercase=False, numbers=False, specialChar=False, ambiguity=False):
    if uppercase and lowercase:
        pwdSize -= 2
        if not ambiguity:
            pwd = random.choice("abcdefghijkmnpqrtuvwxyz") + random.choice("ACDEFGHJKLMNPQRTUVWXYZ")
        else:
            pwd = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)
    else:
        pwd = ""

    characters = ""
    if uppercase:
        if not ambiguity:
            characters += "ACDEFGHJKLMNPQRTUVWXYZ"
        else:
            characters += string.ascii_uppercase
    if lowercase:
        if not ambiguity:
            characters += "abcdefghijkmnpqrtuvwxyz"
        else:
            characters += string.ascii_lowercase
    if numbers:
        if not ambiguity:
            allowedNumbers = "234679"
            characters += allowedNumbers
            pwdSize -= 1
            pwd += random.choice(allowedNumbers) 
        else:
            characters += string.digits
            pwdSize -= 1
            pwd += random.choice(string.digits)
    if specialChar:
        pwdSize -= 1
        allowedChars = "!@#$%&^()[]{}<>/*+=-_;:,."
        characters += allowedChars
        pwd += random.choice(allowedChars)

    pwd += ''.join(random.choice(characters) for _ in range(pwdSize))

    return pwd


def getValidInput(message, validInputs):
    while True:
        userInput = input(message).upper()
        if userInput == 'Q':
            return None
        if userInput in validInputs:
            return userInput
        if userInput not in validInputs:
            try:
                if int(userInput) in validInputs:
                    return int(userInput)
                else:
                    print('Invalid input. Try again.')
            except ValueError:
                print('Invalid input. Try again.')


def main():
    print('Password Generator')
    
    pwdSize = getValidInput('Enter the password length (between 8 and 20). Enter q to quit: ', list(range(8,21)))
    if not pwdSize:
        return

    case = getValidInput('Include uppercase, lowercase, or both? (1 to uppercase, 2 to lowercase, 3 to both). Enter 0 to quit: ', ['1', '2', '3'])
    if not case:
        return

    uppercase = case == '1' or case == '3'
    lowercase = case == '2' or case == '3'

    numbersInput = getValidInput('Include numbers? (Y/N). Enter 0 to quit: ', ['Y', 'N'])
    if not numbersInput:
        return
    numbers = numbersInput == 'Y'

    specialCharInput = getValidInput('Include special characters? (Y/N). Enter 0 to quit: ', ['Y', 'N'])
    if not specialCharInput:
        return
    specialChar = specialCharInput == 'Y'

    ambiguityInput = getValidInput('Allow character ambiguity? (Y/N). Enter 0 to quit: ', ['Y', 'N'])
    if not ambiguityInput:
        return
    ambiguity = ambiguityInput == 'Y'

    pwd = passwordGenerator(pwdSize, uppercase, lowercase, numbers, specialChar, ambiguity)
    print('Password generated:', pwd)


if __name__ == "__main__":
    main()
