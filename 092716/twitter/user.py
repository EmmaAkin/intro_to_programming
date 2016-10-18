import model_db
import like

db = model_db.db


class User():

    def __init__(self, username, password, email, phonenumber=" ", User="User",signin = True):
        self.users = User
        self.username = username.lower()
        self.password =  password
        self.email = email
        self.phonenumber = phonenumber
        self.signin = True
        self.tweet = {} #This refer to an Identifier in the Tweet Table
        self.followers = {} #This is a list of users handle and the last tweet time username:tweet_id or sorted according to tweet id
        self.following = {}
        self.pictures = {} #contains the location of picture in the system. Filename
        # def signin(self, username, password):
        self.like = {}


       db[self.users].create_tables(self.users, {username,password})

    def signin(self,username, password):
        if databse[self.username.lower()][1]==password:
            self.signin = True


    def signout():
        self.signin = False



    def create_bio (self, firstname, lastname, website, dob, address):
        self.firstname  =  firstname.title()
        self.lastname   =  lastname.title()
        self.website     =  website
        self.dob          =   dob
        self.address    = address
        # self.profile = {"FirstName": self.firstname),
        #                     "LastName:" %self.lastname)}
        # print ("Website:       %s" %self.website)
        # print ("Date of Birth: %s" %self.dob)
        # print ("Address:       %s" %self.address)}


    def get_bio (self):
        print ("FirstName:     %s" %self.firstname)
        print ("LastName:      %s" %self.lastname)
        print ("Website:       %s" %self.website)
        print ("Date of Birth: %s" %self.dob)
        print ("Address:       %s" %self.address)


    def set_username(self, username):
            self.username = username
            return "Done"

    def get_username(self):
        return self.username

    def change_password(self, oldpassword, password):
        if oldpassword == self.password:
            self.password = password
            return "Done"
        else:
            return "Enter a wrong former password"


    def tweet(self, tweet):
        self.tweet =
        # Add the information of the new tweet to the dabase with the information of the user making the tweet


    def retweet(self, tweet):
        #Check if the tweet is part of the timeline

        pass

    def like(self, tweet):

        # calls the LIKE class and increase the number of likes, create a timestamp for the like and also record the like
        self.like.append("tweet")
        return


if __name__ == '__main__':



    emma =   User("emma",  "asdf", "ahdfjkhadflaf@kjfaldf")


    charlse = User("charlse","jfkadlhfadf@jfhlhdad", "jdfkhaldf")

    print(db)