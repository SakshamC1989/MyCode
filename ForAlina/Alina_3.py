# Create a variable to store the given string "You can have data without information, but you cannot have information without data."
# Convert the given string to lowercase
# Create a list containing every lowercase letter of the English alphabet
#
# for every letter in the alphabet list:
#     Create a variable to store the frequency of each letter in the string and assign it an initial value of zero
#     for every letter in the given string:
#         if the letter in the string is the same as the letter in the alphabet list
#             increase the value of the frequency variable by one.
#     if the value of the frequency variable does not equal zero:
#         print the letter in the alphabet list followed by a colon and the value of the frequency variable

my_string = "You can have data without information, but you cannot have information without data."
my_string = str.lower(my_string)
a_z = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for l1 in a_z:
    var = 0
    for l2 in my_string:
        if l1==l2:
            var+=1
    if var>0:
        print(l1 + ':' + str(var))





