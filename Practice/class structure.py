#Banking system
# Make a class with three methods-- add user, get details, make messages
#import library datetime

import datetime
#add user-- first name capital, rest must be lowered, enter the amount of cash
#store the user detail in a dict-- user detail--> amount & name
# store today's date in the dictionary as well
#if user has entered the detail then add it to the dictionary as well
#Append the dictionary in the user_details an empty list initially

#get details--- this should simply return the user_details list in the class

class Message_user:

    user_details = []
    messages = []
    def _init_(self):
        print("Constructor has been called")

    def add_user(self,name,amount,email = None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" % (amount)
        detail = {
            "name" : name,
            "amount" : amount
        }

        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text

        if email != None:
            detail["Email"] = email

        self.user_details.append(detail)
    
    def send_deets(self):
        print (self.user_details)
        return self.user_details

    
obj = Message_user()
obj.add_user("Molly", 2345, "habe@123.com")
obj.add_user("Eman", 758)
obj.add_user("MM", 1900)
obj.add_user("NN", 400)
obj.send_deets()











