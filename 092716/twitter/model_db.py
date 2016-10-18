# import Json
#List of the tabel in the Database
# Users - username, password, userProfile, tweet_id, followers, following, picture_id, location
#
# Tweets - tweet_id, tweet_text, timestamp, RT_list(Null if no text attach), Like_list, reply_list_of_id,
# DM -
# Like -
# Favorite -
# RT with Quote as a property when a text is added to the RT
# Reply

db = {}

def create_tables(key,value):
       db[key]= value


# def read():


# def update():


# def delete():



def read_file(fn1):
    file = open(fn1, "r")
    text = file.read()
    file.close()
    return text

def write_file(fn1):
    newfile = open(fn1, "w")
    newfile.write(text)
    newfile.close()

def backup(fn1):
    text = read_file(fn1)

    newfile = open("backups/"+fn1+".bak", "wb")
    newfile.write(text)
    newfile.close()

if __name__ == '__main__':
    # twitter = Database(Users="SuperUser")

    # var = "Tweets"
    # twitter.create_tables(var, {var:1,
    #                               "sure":"here"})

    # twitter.create_tables("Rt", "ahdklfhlahfjafladf ajdnflafd")

    print(db)