class phonebook:
    def __init__(self,name,number):
        self.name = name
        self.number = number
    
    def write(self):
        f = open("phonebook.txt","a")
        f.write(self.name)
        f.write("\t")
        f.write(self.number)
        f.write("\n")
        f.close()
    
    def read_data(self):
        f = open("phonebook.txt","r")
        file = f.read()
        f.close()
        print(file)
        
name = input("enter Name  : ")
number= input("enter phone number : ")
user1 = phonebook(name,number)
user1.write()
user1.read_data()










