import time

yes = ['Y', 'YE', 'YES', 'YA', 'YEAH', 'YEY']
no = ['N', 'NO', '', 'NOPE', 'NONE', 'NAY']

def cosym():
    '''Gets symptoms from the patient and provides a score for them'''
    score = 0
    
    print("Enter y for yes and n for no\n")
    
    a = input("Are you suffering from fever?\n").upper()
    if a in yes:
        score += 2

    a = input("Having dry cough or sore throat?\n").upper()
    if a in yes:
        score += 2

    a = input("Feeling tired or lethargic or having pains and aches without any physical exertion?\n").upper()
    if a in yes:
        score += 2

    a = input("Headache, diarrhoea, conjuctiveness or loss of smell/taste?\n").upper()
    if a in yes:
        score += 3

    a = input("Having difficulty in breathing or shortness of breath?\n").upper()
    if a in yes:
        score+= 5

    a = input("Chest pain or shortness of breath?\n").upper()
    if a in yes:
        score += 5

    a = input("Loss of speech or movement?\n").upper()
    if a in yes:
        score += 5

    print()        # Breathing space between texts

    return score


def suggest(score = 0):
    '''Gives the condition of the patient'''
    if score<=2:
        print("Good News! You don't have much symptoms to suggest COVID infection.")
        return

    if score <= 4:
        print("You have minor symptoms suggesting COVID infection.\nWe recommend maintaining self quarintine until your report arrives.")
        return report(2)
        
    text = "You have symptoms suggesting COVID infection.\nYou will have to to stay under controlled quarintine conditions until your report arrives.\n\nWaiting for the report...         # The program is not lagging. The delay is just for realism."
    
    if score <= 8:
        print(text)
        return report(3)

    if score >8:
        print(text)
        return report(5)

def tell(cond):
    '''Prints the result.'''
    
    print()
    time.sleep(5)
    if cond == 'negative':
        print("Great news! You have been tested corona negative. \n*Sigh* I was worried about you. You are good to go.\n*Behind your Back* \nI just didn't want to have to treat that guy. Didn't like his/her looks if you know what I mean.")
        return

    text = "We are very sorry to inform you.\nYou are tested to be corona positve with '{}' state.\nYou are to be admitted and assigned to special beds ASAP.\nPlease fill up your details. Common guys bring this guy/gal in".format(cond)
    print(text)
    return

def report(score):
    '''Randomly assigns a condition to the patient based on previous responses.'''
    import random
    opt = ['negative', 'mild', 'normal', 'severe', "HOW AREN'T YOU DEAD!!", 'negative', 'negative', 'negative', 'negative']
    L = opt[:score] + opt[(2*score)+1:]
    if score==5:
        L.remove('mild')
    n = random.randint(0, len(L)-1)
    cond = L[n]
    tell(cond)
    return cond


def getch():
    '''Prints the main menu and reads a response from user.'''
    print ("Are you a patient here? Enter 1.")
    print("Are you a staff member or have applied for a job? Enter 2.")
    print("Want to apply for a job? Enter 3.")
    print("Not sure who you are, where you are or what you are doing? Enter \"help\" or \"?\".")
    print("Admin? Enter password.")
    print("Any other value to EXIT.")
    ch = input("").strip()
    print()
    return ch
