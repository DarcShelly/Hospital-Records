# implements operations on mysql tables
import mysql.connector as sqltr
from datetime import date

hostdata = open(r'./host_data.txt').readlines()
hostdata = [a.rstrip() for a in hostdata]
mycon = sqltr.connect(host = hostdata[0], user = hostdata[1], passwd = hostdata[2])
curs = mycon.cursor()

def init_tables():
    '''Creates a new databses if none exists. Opens the existing database otherwise.'''
    try:
        curs.execute("Create database project")      #Creates database required
        curs.execute("Use project")
        s1 = "CREATE TABLE staff(SID char(4) PRIMARY KEY, SName char(40) , Age char(2), Sex char(1), Address char(40), Contact varchar(15), DOJ date, Post char(30), Spec char(30), applicant char(1))"
        s2 = "CREATE TABLE patients(PID char(4) PRIMARY KEY, PName char(40), Age char(3), Sex char(1), DOA date, state char(20), relative char(40), attendant char(40) REFERENCES staff(SName), BedNo char(4), contact char(15) NOT NULL, address text NOT NULL)"
        curs.execute(s1)
        curs.execute(s2)
        i1 = "INSERT INTO staff values('1001', 'Dr. Pradeep Singh', '46', 'M', 'Almora', '7826452678', '2012-08-12', 'doctor', 'Neurology', 'N')"
        curs.execute(i1)
        mycon.commit()
    except:
        curs.execute("Use project")

class StaffImplement:
    '''(self, *arg) = (staff details).
       Initiate and saves new staff member details and/or make changes to them.'''
    
    def __init__(self,L=[0,0,0,0,0,0,0,0,0,'Y']):
        self.record = L
        self.col = [('SID', 'Staff Id'), ('SName', 'Name'), ('Age', 'Age'), ('Sex', 'Sex'), ('Address', 'Address'), ('Contact', 'Contact'), ('DOJ', 'DOJ(Date Of Join)'), ('Post', 'Post'), ('Spec', 'Specialisation of the doctor/surgeon')]
        self.a = 0
        self.b = 0

    def update(self, n, sid):
        self.a = self.col[n][0]
        self.b = self.record[n]
        query = query = "UPDATE staff SET {}='{}' WHERE SID='{}'".format(self.a, self.b, sid)
        curs.execute(query)
        mycon.commit()

    def doj(self):          # Use this function first for a new member so that the date gets filled up on its own
        if self.record[6] == 0 or self.record[6] == '0000-00-00':
            self.record[6] = date.today().strftime("%Y-%m-%d")
            
        else:
            self.record[6] = input('Enter date of join to : [Use format (YYYY-MM-DD):\n]')
            
    def sid(self):
        if self.record[0] == 0:
            newid = newpatid(table = 1)
            addid(newid, 1, 0)
            self.record[0] = newid
        else:
            while True:
                Idlist = newpatid(1, cond = True)
                newid = input('Enter new staff id of the member:\n')
                if len(newid)!=4:
                    print('Staff Id must be of 4 characters.')
                    print('Try Again.')
                    
                elif newid in Idlist:
                    print('Id already taken try again.')
                    print('Try Again.')
                    
                else:
                    break
                self.record[0] = newid
                addid(newid, 1, 1)
        
    def name(self):
        sname = self.record[1]
        while True:
            if sname:
                self.record[1] = input('Change name of the staff member to:\n').strip()
            else:
                self.record[1] = input('Enter your name:\n').strip()
            
            if len(self.record[1]) > 40 or len(self.record[1])<5:
               print('Name must be more than 5 and less than 40 characters.')
               print('Try Again.')
            else:               # This block checks wheter the name entered is valid ot not.
                r = True
                nparts = self.record[1].split()
                for i in nparts:
                    if not i.isalpha() and i != '.':
                        r = False
                if r:
                    break
                else:
                    print('Invalid Name.')
                    print('Try Again!')
                    
        if self.record[7] in ('doctor', 'surgeon'):         # To update the name of doctor in attendants file.
            attendant(False, self.record[1], sname)

    def age(self):
        while True:
            if self.record[2] == 0:
                age = input('Enter your age:\n')
                if not age.isnumeric():
                    print('Stop Kidding! Enter your correct age.')
                    print('Try Again.')
                else:
                    if int(age)>60:
                        print('Sorry! You are too old to apply for the job.')
                        return True
                    elif int(age)<18:
                        print('Sorry! You are too young to apply for the job.')
                        return True
                    else:
                        break
            else:
                age = input('Enter new age of the member:\n')
                if not age.isnumeric() or int(age)>50 or int(age)<18:
                    print('Invalid age!')
        self.record[2] = age

    def sex(self):
        gender = self.record[3]
        while True:
            if gender == 0:
                self.record[3] = input('Enter your gender:\n').upper()
                if self.record[3] not in ['M', 'F', 'T', 'O']:
                    print("How in Merlin's Beard do you not know your gender!")
                    print("Try Again!")
                else:
                    break
                
            else:
                self.record[3] = input('Change the gender of the member to:\n'+' ')[0].upper()
                if self.record[3] not in ['M', 'F', 'T', 'O']:
                    print('Invalid Gender!')
                    print('Try Again')
                else:
                    break
                

    def add(self):
        while True:
            if self.record[4] == 0:
                self.record[4] = input('Enter your primary address:\n')
            else:
                self.record[4] = input('Enter new address:\n')
                
            if len(self.record[4]) > 35:
                print('Address too long!')
                print('Try Again!')
            else:
                break

    def cont(self):
        while True:
            contact = input('Enter contact details\n')
            if (len(contact)==12 and contact[:2] == '91') or len(contact)==10:
                if contact.isnumeric() and contact[0] in ['7', '6', '8', '9']:
                    self.record[5] = contact
                    return
            print("Invalid Return.")
            print("Try Again.")

    def post(self):
            
            if self.record[7]==0:
                joblist = ['Hospital management', 'nurse', 'doctor', 'surgeon', 'intern']
                n = len(joblist)
                
                for i in range(len(joblist)):
                    print(i+1, '.', joblist[i], sep = '')

                while True:
                    ch = input("Want to apply for:\n").strip()
                    if ch.isnumeric() and int(ch) in range(n):
                        self.record[7] = joblist[int(ch)-1]
                        break
                    else:
                        print('Invalid choice. Try Again')
                        
            else:
                self.record[7] = input('Promote the member to position:\n')

    def spec(self):
        if 'doctor' in self.record[7] or 'surgeon' in self.record[7]:
            self.record[8] = input('Enter Speciality:\n')
        else:
            self.record[8] = 'NULL'

    def display(self):
        for a in range(len(self.col)):
            print(self.col[a][1], ':\t', self.record[a])

    def newrow(self):
        '''Saves new column into mysql database.'''
        record = self.record
        query = "INSERT INTO staff VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9])
        curs.execute(query)
        mycon.commit()


class PatientImplement:
    '''(self, *arg') = (patient details)
        Initiates and saves patient details and/or makes changes to them.'''

    def __init__(self, L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
        '''Initialise values for the class.'''
        self.record = L
        self.col = [('PID', 'Patient ID'), ('PName', 'Name of the patient'), ('Age', 'Age'), ('Sex', 'Gender'), ('DOA', 'Date of Admittance'), ('state', 'state'), ('relative', 'relative staying with the patient'), ('attendant', 'Doctor/Nurse attending to the patient'), ('BedNo', 'Bed Number of patient'), ('contact', 'Contact'), ('address', 'Address')]
        self.a = 0
        self.b = 0

    def update(self, n, pid):
        self.a = self.col[n][0]
        self.b = self.record[n]
        query = "UPDATE patients SET {}='{}' WHERE PID='{}'".format(self.a, self.b, pid)
        curs.execute(query)
        mycon.commit()

    def doa(self):
        if self.record[4]==0:
            self.record[4] = date.today().strftime("%Y-%m-%d")
        else:
            self.record[4] = input('Change the date of admittance to: [YYYY-MM-DD]\n').strip()
                
            

    def PID(self):    
        if self.record[0]==0:
            newid = newpatid(0)
            self.record[0] = newid
            addid(newid, 0, 0)
        else:
            Idlist = newpatid(0, cond = True)
            
            while True:            # Checks if the id is valid or not
                newid = input('Enter new patient id of the patient:\n').strip()
                if len(newid)==4:
                    if newid not in Idlist:
                        break
                    else:
                        print('This Id already exists. Try Again.')
                else:
                    print('Id must be of 4 characters')
                    print('Example: \'1211\'')
                    
            self.record[0] = newid
            addid(newid, 0, 1)

    def PName(self):
        while True:
            name = input('Enter name of the patient:\n')
            if len(name) <= 40 and len(name)>5:
                self.record[1] = name
                break
            print('Name too long')

    def Age(self):
        while True:
            self.record[2] = input('Enter age of the patient:\n')
            if len(self.record[2])<=3 and self.record[2].isnumeric():
                break
            print('Stop kidding! Enter the correct age.')

    def sex(self):
        while True:
            self.record[3] = input('Enter gender of the patient:\n').strip()[0].upper()
            if self.record[3] in ['M', 'F', 'O', 'T']:
                break
            print('How the hell do you not know your gender! Try Again')
            

    def state(self):
        while True:
            self.record[5] = input("The patient's state have detiorated/improved to:\n").lower()
            if self.record[5] in ['mild', 'normal', 'severe']:
                break
            print("Invalid state! Choose from:")
            print("mild     normal      severe")
            
    def relative(self):
        if self.record[6]==0:
            query = 'The name of the relative staying with you:\n'
        else:
            query = 'Change the name of the relative staying with you to:\n'

        while True:
            self.record[6] = input(query)
            if len(self.record[6])<=40:
                break
            print("Name too long!")

    def attendant(self):
        if self.record[7] == 0:
            self.record[7] = attendant()        # choses a doctor from doctor list itself
        else:
            while True:
                self.record[7] = input('New doctor/nurse to attend to the patient:\n')
                doc_list = attendant(check = True)              # gets the list of doctors
                if self.record[7] not in doc_list:
                    print('No doctor found with the given name.')
                    print('Choose from the given doctors')
                    for a in doc_list:
                        print(a, end = '    ')
                    print()
                

    def bed(self):
        if self.record[8]==0:
            self.record[8] = newpatid(table = 0, bed = True)

        else:
            while True:
                bedno = input("Change the bed alloted to patient to bed number:   [Enter new bed number.]\n")
                bedlist = newpatid(table = 0, cond = True, bed = True)
                
                if len(bedno)<4 and bedno not in bedlist:
                    if bedno.isnumeric():
                        self.record[8] = bedno
                        break
                    else:
                        print('Bed number must be a number.')
                else:
                    print('Bed not available.Try entering another number')
        addid(Id = self.record[8], table = 0, t = False, bed = True)

    def contact(self):
        while True:
            contact = input('Enter your contact number:\n').strip()
            if (len(contact)==12 and contact[:2] == '91') or len(contact)==10:
                if contact.isnumeric() and contact[0] in ['7', '6', '8', '9']:
                    self.record[9] = contact
                    break
            print("Invalid contact number.")

    def address(self):
        self.record[10] = input("Enter the patient's adress:\n")

    def display(self):
        for a in range(len(self.col)):
            print(self.col[a][1], ':\t', self.record[a])
        print()
    
    def newrow(self):
        '''Saves new column into mysql database.'''
        record = self.record
        query = "INSERT INTO patients VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10])
        curs.execute(query)
        mycon.commit()

def newpatid(table, cond = False, bed = False):
    '''Creates a new patid which does not already exist in the file.'''
    with open('./project.txt', 'r') as fh:           # Opening the file consisting already existing ids
        if table:
            fh.readline()
            fh.readline()
        if bed:
            for a in range(4):
                fh.readline()
        Idlist = fh.readline().split()
        if not bed:
            custidlist = fh.readline().split()          # fetching id-list and custom-id-list.

    if cond:
        result = []
        result.extend(Idlist)            # returns Id list if asked for it.
        if not bed:
            result.extend(custidlist)
        return result
    
    n = len(Idlist) - 1
    Id = Idlist[n]
    newid = str(int(Id )+1)

    if bed:
        return newid
    
    while newid in custidlist:
        a = str(int(newid)+1)
        newid = a           # Changes the patient id until it is different from all the custom made ids
            
    return newid


def addid(Id, table=0, t = False, bed = False):
    '''Adds newly created id to the id file.'''
    with open('./project.txt', 'r') as fh:
        file = fh.readlines()       # Retrieving file data as list.
    
    n = 0
    if table:
        n+=2
    if t:
        n+=1
    if bed:
        n+=4

    actlist = file[n].strip()               # "actlist" is a string containing all the ids seperated by whitespaces
    newlist = actlist + ' ' + Id + ' \n'          # The slicing is to re
    file[n] = newlist                     # writes the new list back in file data

    with open('./project.txt', 'w') as fh:
        fh.writelines(file)

    return
    
def attendant(check = False, newname = '', oldname = ''):
    ''' Assigns the doctor with the least patients with a new patient.'''

    fh = open('./attendants.txt', 'r')
    doc_list = fh.readline().strip().split('  ')
    patnumlist = fh.readline().strip().split()
    fh.close()

    fh = open('./attendants.txt', 'w')

    if check:
        fh.close()
        return doc_list

    if oldname:             # updates name of doctor
        index = doc_list.index(oldname)
        doc_list[index] = newname
        doc = '  '.join(doc_list)
        patnum = ' '.join(patnumlist)
        fh.write(doc +'\n'+ patnum)
        fh.close()
        return
    
    index = patnumlist.index(min(patnumlist))
    doctor = doc_list[index]
    patnumlist[index] = str(int(patnumlist[index])+1)
    doc = '  '.join(doc_list)
    patnum = ' '.join(patnumlist)
    
    fh.write(doc +'\n'+ patnum)
        
    return doctor.strip()


def applicant(a):
    '''Creates a new class instance of StaffImplement and gathers the required info.'''
    s1 = StaffImplement([0, 0, 0, 0, 0, 0, 0, 0, 0, a])
    s1.doj()
    s1.name()
    if s1.age():
        return
    s1.sid()
    s1.sex()
    s1.add()
    s1.cont()
    s1.post()
    s1.spec()
    s1.newrow()
    return

def getrow(tab, Id=0):
    '''Fetches the row of the specified patient/staff.'''
    L = (['patient', 'staff'], ['patient', 'staff member'])
    identity = (['PID', 'SID'], ['PName', 'SName'])
    table = ('patients', 'staff')
    table = table[tab]
    if Id==0:
        Id = input("Enter name or {} ID of the {}:\n".format(L[0][tab], L[1][tab]))
    a = identity[0][tab]
    b = Id
    if len(b)>4:
        a = identity[1][tab]

    query = "SELECT * FROM {} WHERE {} = \'{}\'".format(table, a, b)

    curs.execute(query)
    row = curs.fetchone()
    
    if not row:
        return(row, a, b)
    return (list(row), a, b)

def getadminrows(tab):
    field = [('PID', 'PName', 'Age', 'Gender', 'Date of admittance', 'State', 'Relative', 'Attendant', 'Bedno', 'Contact', 'Address'), ('SID', 'SName', 'Age', 'Gender', 'Address', 'Contact', 'Date of Join', 'Post', 'Specialisation')]

    query = "SELECT * FROM patients"
    if tab:
        query = "SELECT * FROM staff WHERE applicant = 'N'"
        
    curs.execute(query)
    data = curs.fetchall()
    print(field[tab])
    idlist = []
    
    for a in data:
        print(a)
        idlist.append(a[0])
    print()
    i = input('Enter id of the record which is to be modified:\n')
    if i in idlist:
        return list(data[idlist.index(i)])

    else:
        return

def display(table = 0):
    
    tab = ('patient', 'staff')
        
    row, a, Id = getrow(table)
    
    if not row:
        print('There is no record with the following {} ID/name.'.format(tab[table]))
        print()
        return

    if table == 0:
        p1 = PatientImplement(row)
        print()
        p1.display()
        return row

    s1 = StaffImplement(row)
    s1.display()
    print()
    return row
    
def newpatrow(state):
    '''Initialises an instant of patient data.'''
    p1 = PatientImplement([0, 0, 0, 0, 0, state, 0, 0, 0, 0, 0])
    p1.doa()
    p1.PID()
    p1.PName()
    p1.Age()
    p1.sex()
    p1.relative()
    p1.attendant()
    p1.bed()
    p1.contact()
    p1.address()
    p1.newrow()
    

def uppat(row, admin = False):
    '''Updates the patient information.'''
    p1 = PatientImplement(row)
    pid = row[0]
    print('Choose what you want to modify:')
    print('1.Name')
    print('2.Age')
    print('3.Gender')
    print('4.Relative')
    print('5.Contact No.')
    print('6.Address')
    if admin:
        print('7.PID')
        print('8.Date of Admittance')
        print('9.State')
        print('10.Bedno')
        
    print('Anything else to EXIT.')
    print()
    
    while True:
        ch = input('Enter your choice:\n').strip()
        print()
        if ch == '1':
            p1.PName()
            n = 1
        elif ch == '2':
            p1.Age()
            n = 2
        elif ch == '3':
            p1.sex()
            n = 3
        elif ch == '4':
            p1.relative()
            n = 6
        elif ch == '5':
            p1.contact()
            n = 9
        elif ch == '6':
            p1.address()
            n = 10
        elif admin:
            if ch == '7':
                p1.pid()
                n = 0
            elif ch == '8':
                p1.doa()
                n = 4
            elif ch == '9':
                p1.state()
                n = 5
            elif ch == '10':
                p1.bed()
                n = 8
            else:
                break
            
        else:
            break
        p1.update(n, pid)
        print('Record modified successfully.')

        
def upstaff(row, admin = False):
    '''Updates the staff information.'''
    s1 = StaffImplement(row)
    sid = row[0]
    print("Choose what you want to modify:")
    print('1.Address')
    print('2.Contact')
    if admin:
        print('3.SID')
        print('4.Name')
        print('5.Age')
        print('6.Date of Join')
        print('7.Post')
        print('8.Specialisation')
    print('Anything else to EXIT')
    print()
    while True:
        ch = input('Enter your choice:\n').strip()
        print()
        if ch == '1':
            s1.add()
            n = 4
        elif ch == '2':
            s1.cont()
            n = 5
            
        elif admin:
            if ch == '3':
                s1.sid()
                n = 0
            elif ch == '4':
                s1.name()
                n = 1
            elif ch == '5':
                s1.age()
                n = 2
            elif ch == '6':
                s1.doj()
                n = 6
            elif ch == '7':
                s1.post()
                n = 7
            elif ch == '8':
                s1.spec()
                n = 8
            else:
                break
            
        else:
            break
        s1.update(n, sid)
        print('Record modified successfully.')

def showpats(row):
    ch = input('Want to know names of patients assigned to you?  [y for yes]:\n').strip().upper()
    if ch[0] == 'Y':
        query = "SELECT PID, PName, BedNo FROM patients WHERE attendant = '{}'".format(row[1])
        curs.execute(query)
        data = curs.fetchall()
        count = curs.rowcount
        print('Total number of patients: ', count)
        print('[Patient Id, Name, Bed Number]')
        for pat in data:
            print(pat)

def addattend(name):
    '''Adds another staff member into the hospital records.'''
    with open('./attendants.txt', 'r') as fh:
        doc = fh.readline().strip()
        patnum = fh.readline().strip()

    doc = doc + '  ' + name
    patnum = patnum + ' 0'
    
    with open('./attendants.txt', 'w') as fh:
        fh.write(doc + '\n' + patnum)
    

def appoint():
    '''Appoint a doctor to a patient.'''
    query = "SELECT SID, SName, Age, Sex, Address, Post FROM staff WHERE applicant = 'Y'"
    curs.execute(query)
    data = curs.fetchall()
    count = curs.rowcount
    
    print('The number of applicants is', count)
    print('[SID, SName, Age, Gender, Adress, applied for]')
    
    sidlist = []
    for row in data:
        sidlist.append(row[0])
        print(row)
        
    while True:
        print()
        sid = input('Enter sid of the patient you want to appoint: [blank to exit]\n').strip()
        query = "UPDATE staff SET applicant = 'N' WHERE SID = '{}'".format(sid)

        if not sid:
            return
        
        elif sid not in sidlist:
            print('No such SID exists.')
            
        else:
            curs.execute(query)
            mycon.commit()
            print('Applicant appointed.')
            print()
            index = sidlist.index(sid)
            if 'doctor' in data[index][5] or 'surgeon' in data[index][5]:
                addattend(data[index][1])
            return
            
        

if __name__ == '__main__':
    print(attendant())
