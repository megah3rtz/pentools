import sys

print "Prints all flags or variables passed to the script"

#print everything in sys.argv, from 0 upwards
print sys.argv[0:]

#loop through all the variables in sys.argv and print them
for var in sys.argv:
    print var
