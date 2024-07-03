

#This python script has been created in order to generate cool band names for individuals based on their inputs

import re

run = True

def gen_func():
    global run

    # # town_name = input("What is the name of the town you grew up in ?")
    # # nick_name = input("What is your nickname ?")
    # #
    # final_town = re.sub('[0-9,.""]', "", town_name)
    # final_nick = re.sub('[0-9,.""]', "", nick_name)
    # #
    #  band_name = (final_town + " " + final_nick)
    # #
    # print("Your band name is : ", band_name)
    while run:
        town_name = input("What is the name of the town you grew up in ?")
        nick_name = input("What is your nickname ?")

        final_town = re.sub('[0-9,.""]', "", town_name)
        final_nick = re.sub('[0-9,.""]', "", nick_name)

        band_name = (final_town + " " + final_nick)

        print("Your band name is : ", band_name)

gen_func()