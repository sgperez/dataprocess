import sys
import os
from random import random
from basicStats import BasicStats

MAX_OPTION = 4


def main_menu():

    stat_obj = BasicStats()
    main_list = []
    

    while True:
        os.system('cls')

        print "Basic Stats: \n1 - Generate random int array\n2 - Get mean\n3 - Get mediam\n4 - Get variance\n5 - Get Standar Derivation\n0 - Exit\n\n"

        if len(main_list) > 0:
            print "Your experimental list is:", main_list

        try:
            # print "Please choose an option: "
            # option = int(sys.stdin.read(1))
            option = int(raw_input("\nPlease choose an option: "))

            if option >=0 and option <= MAX_OPTION:
                if option == 0:
                    print "Goodbye!"
                    break
                elif option == 1:
                    main_list = stat_obj.creates_random_array()
                    print main_list

                elif option == 2:
                    mean = stat_obj.get_mean(main_list)
                    print "The mean value for you list is:", mean

                elif option == 3:
                    median = stat_obj.get_median(main_list)
                    print "The median value for you list is:", median

                raw_input("\nPress Enter to continue...")


            else:
                invalid_option()


        except ValueError:
            invalid_option()






def invalid_option():    
    print "\n**Valid options are 0 to %i" % MAX_OPTION
    raw_input("\nPress Enter to continue...")






if __name__ == '__main__':
  main_menu()
