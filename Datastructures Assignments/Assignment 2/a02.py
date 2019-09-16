class Address: 

    def __init__(self, house_no = 0,street = 0, city= "" , country=""):
        self.house_no = house_no
        self.street = street
        self.city = city
        self.country = country


    def get_full_address(self):
         
        return  "H. No."+ " " + str(self.house_no) +  ", " +"Street "+ str(self.street)+ ", " + str(self.city) + " "+str(self.country)
    # "H. No. 2, Street 3, Peshawar Pakistan"
    
    def __str__(self):
        return self.get_full_address()

    

class Employee: 
    def __init__(self, id = 1, name = None):
        self.name = name
        self.id = id
        self.current_address = None
        self.permanent_address = None

    def set_current_address(self,house_no,street,city,country):
        self.current_address = Address(house_no,street,city,country)
        #return self.current_address

    def set_permanent_address(self,house_no,street,city,country):
        self.permanent_address = Address(house_no,street,city,country)
        # self.get_current_address == None

        #return self.permanent_address

    def get_current_address(self):
        # pass
        return  "H. No."+ " " + str(self.current_address.house_no) +  ", " +"Street "+ str(self.current_address.street)+ ", " + str(self.current_address.city) + " "+str(self.current_address.country)
        

    def get_permanent_address(self):
        # pass
        # return self.permenant_address

        ## check if peremenatn address is None
            ## if yes then return None
        if self.permanent_address == None:
            #pass
            return None

        return  "H. No."+ " " + str(self.permanent_address.house_no) +  ", " +"Street "+ str(self.permanent_address.street)+ ", " + str(self.permanent_address.city) + " "+str(self.permanent_address.country)

    def __str__(self):
        
        # print("This is the current Address")
        # return str(self.id) + " " + self.name + " H. No." + str(self.current_address.house_no) + ", " + "Street "+ str(self.current_address.street) + ", " + str(self.current_address.city) + " "+ str(self.current_address.country)
        #11 Ali H. No. 1, Street 2, Cape Town South Africa

        #print("This is the permenant Address")
        #return str(self.id) +  " " + self.name + " H. No." + str(self.get_permenant_address.house_no) + ", " + "Street "+ str(self.permenant_address.street) + ", " + str(self.permenant_address.city) + " "+ str(self.permenant_address.country)
        return str(self.id) + " " + str(self.name) + " " + str(self.permanent_address.get_full_address())
        


class Lecturer(Employee): 
    def __init__(self):
        super().__init__(1,"Mr. Bigshot")

    def __str__(self):
        return "Lecturer:"+ " " + str(self.id) + " " + str(self.name) + " " + str(self.permanent_address.get_full_address())
    

if __name__ == "__main__": 
    # Uncomment these to test out your code before run.py local 

    
    # a = Address() 
    # a.house_no = 2 
    # a.street = 3 
    # a.city = "Peshawar"
    # a.country = "Pakistan"

    # print(a.get_full_address())
    # print(a)


    e = Employee() 
    e.set_current_address(1, 2, "Cape Town", "South Africa")
    print(e.get_current_address()) 

    e.set_permanent_address(4, 19, "Cape Town", "South Africa")
    print(e.get_permanent_address())

    print(e)

    # l = Lecturer() 
    # l.set_permanent_address(44, 24, "KL", "Malaysia")
    # print(l.get_permanent_address())
    # print(l)