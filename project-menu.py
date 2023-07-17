from addit import *
from staff import *

password = 'DDpt'

init_tables()

if __name__ == "__main__":
    
    print("WELCOME TO VAIBHAV HOSPITAL")
    print("Check for covid symptoms? [y for yes]")
    
    ch = input().strip()
    print()
    
    if ch.upper() in yes:
        
        score = cosym()      # Checks for symptoms and returns condition of patient
        cond = suggest(score)
        if cond=='negative':
            pass
        else:
            if cond == "HOW ARE YOU ALIVE!!":
                cond = 'severe'
            newpatrow(cond)
            print('\nYour details have been saved in the database.\nPlease follow the nurse to your assigned bed.')
            
    else:
        while True:
            ch = getch()        # Asks user for choice to progress in the program.
            
            if ch == '1' or ch == '2':             # User is a patient.
                ch = int(ch)
                row = display(ch-1)
                
                if row:
                    choice = input("Make changes in your details? [Enter y for yes]:\n").strip().upper()
                    
                    if choice in yes:
                        if ch == 1:
                            uppat(row, admin = False)
                        else:
                            upstaff(row, admin = False)
                    
                    
                    elif row[9] == 'N' and ('doctor' in row[7] or 'surgeon' in row[7]):
                        print()
                        showpats(row)
                        
                    break
                        
                    print('\n')

            elif ch == '3':
                print("Enter your details below:")
                applicant('Y')
                break
                
            elif ch == password:
                while True:
                    print('Choose from the menu.')
                    print('1.Appoint staff members from applicants.')
                    print('2.Modify staff member table.')
                    print('3.Modify patient table.')
                    print('Anything else to EXIT.')
                    ch = input('Enter your choice:\n').strip()
                    
                    if ch =='1':
                        appoint()
                    
                    elif ch == '2':
                        while True:
                            row = getadminrows(tab = 1)
                            if row:
                                upstaff(row, admin = True)
                                break
                            
                    elif ch == '3':
                        while True:
                            row = getadminrows(tab = 0)
                            if row:
                                uppat(row, admin = True)
                                break
                    
                        
                    else:
                        break
                    
                break

            else:
                break
            
