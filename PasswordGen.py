# Motivation: Create a random password generator that is able to create passwords that contain lower cases, 
# upper cases, and special characters, or any combination of the above
import random

class Password:
    
    SPECIAL_CHARACTERS = '!@#$%^&*()'
    LOWER_CASES = 'abcdefghijklmnopqrstuvwxyz'
    UPPER_CASES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    @classmethod
    def constantChange(cls, constant, sequence):
        if constant in cls.__dict__:
            setattr(cls,constant,sequence)

    def __init__(self):
        self.initial = True
        self.minimum_length = None
        self.maximum_lenth = None
        self.special_character = None
        self.upper_case = None
    
    def requirements(self):
        if self.initial == False:
            choice = input("Are you sure you want to override current requirements? [Y/N]: ").upper()
            while choice != 'N' and choice != 'Y':
                choice = input("Override current Requirements? [Y/N]: ").upper()
            if choice == 'Y':
                self.initial = True
                
        if self.initial == True:
            try:
                self.minimum_length = int(input("Set the min Length: "))
                self.maximum_lenth = int(input(f"Set the max Length, it must be greater than {self.minimum_length}: "))
                while self.maximum_lenth <= self.minimum_length:
                    self.maximum_lenth = int(input(f"Invalid length, please enter a length greater than {self.minimum_length}: "))
            except:
                print('Incorrect Values, try again')
                return self.requirements()

            self.special_character = input("Are special characters required? [Y]/[N]: ").upper()
            while self.special_character != 'N' and self.special_character != 'Y':
                self.special_character = input("Incorrect input, are special characters required? [Y]/[N]: ").upper()

            self.upper_case = input("Are upper cases required? [Y]/[N]: ").upper()
            while self.upper_case != 'N' and self.upper_case != 'Y':
                self.upper_case = input("Incorrect input, are special characters required? [Y]/[N]: ").upper()
            self.initial = False
    
    def status(self):
        print(f"Minimum Length:{self.minimum_length}, Maximum Length:{self.maximum_lenth}")
        print(f"Special Character Requirement:{self.special_character}, Upper Case Requirement:{self.upper_case}")
    
    def createPass(self):
        if self.initial == True:
            print("Use the requirements method to create the requirements")
            return
        
        passwordBucket = []
        passwordBucket.append(self.LOWER_CASES)
        if self.upper_case == 'Y':
            passwordBucket.append(self.UPPER_CASES)
        if self.special_character == 'Y':
            passwordBucket.append(self.SPECIAL_CHARACTERS)
        
        elements = 0
        for i in passwordBucket:
            elements += len(i)
            
        password = ''
        s = 0 ; f = 0
        nodes = {}
        for i in range(0,len(passwordBucket)):
            f += len(passwordBucket[i])
            nodes[i] = [s,f, passwordBucket[i]]
            s = f
        while len(password) < self.maximum_lenth:
            pick = random.randint(0,elements-1)
            for i in nodes:
                if pick in range(nodes[i][0],nodes[i][1]):
                    password += passwordBucket[i][random.randint(0,len(passwordBucket[i])-1)]  


            if len(password) == self.maximum_lenth:
                count = 0
                for buckets in passwordBucket:
                    for letters in password:
                        if letters in buckets:
                            count +=1
                            break
                if count != len(passwordBucket):
                    password = ''

                    
        return password

newPass = Password()
newPass.requirements()
print('\n')
print(f'Your new password is: {newPass.createPass()}\n')
txt = ''
while txt != 'Y':
    txt = input('Exit the program? [Y]/[N]').upper()