# Renaming Bulk Files

import os

def main():
    i = 0
    path = "" # input the path where the archives are (change \ to / and add a last / in the end)
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()



