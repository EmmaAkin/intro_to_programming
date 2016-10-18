from model_db import Database
import user

db = Database()


class Timeline():

    def __init__(self, user):
        self.user = user

    def timeline(self, limit=10):
        self.limit = limit

    def get_bio (self):
        print ("FirstName:     %s" %self.firstname)
        print ("LastName:      %s" %self.lastname)
        print ("Website:       %s" %self.website)
        print ("Date of Birth: %s" %self.dob)
        print ("Address:       %s" %self.address)


    def get_timeline(self, username):
        self.username = username
        return "Done"

   def display(self):




if __name__ == '__main__':
    database.

    print(emma.create_bio("Emma", "Awokoya","emma.com","12/21/22", "MEST"))
    print(emma.get_username())
    print(charlse.get_username())
    print(emma.get_bio())