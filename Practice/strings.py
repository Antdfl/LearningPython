# Multi-line string
# You need to use triple quotes or triple single quotes
#name = """Antonio 
#é un grande
#"""
from test.test_index import newstyle

#print(name)
# plus is a string concatenator
# name = "Max is a prepared"
# name = name + " instructor"
# print(name) 
#print(name*10) 

#use of other string functions
message = "  Normal message   "
print(message.strip())

new_message = message.replace("message", "nuovo fatticcio")
print(new_message)
print(new_message.find("nuovo"))
# length = len(message)
# print(length)