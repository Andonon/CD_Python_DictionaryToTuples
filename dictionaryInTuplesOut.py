''' -Assignment: Dictionary in, tuples out
Write a function that takes in a dictionary and returns a list
of tuples where the first tuple item is the key and the second is the value.
'''
#pylint: disable=C0103
def function():
''' This function takes a dictionary and outputs tuples of the data. 
'''

    # function input
    my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
    }

    listoftuples = []
    for eachperson, phonenumber in my_dict.iteritems():
        #print eachperson, phonenumber
        listoftuples.append(tuple([eachperson, phonenumber]))
    print listoftuples
function()




'''
#function output expected
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
'''

