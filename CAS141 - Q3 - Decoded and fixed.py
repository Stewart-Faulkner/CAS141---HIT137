#Looks like this is made to remove even numbers from a set.
#Could be useful for Q2 Chapter 2, but remove odds prior to ASCII

global_variable = 100
my_dict = {'key': 'value', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):
    #added numbers variable
    global global_variable 
    local_variable = 5
   
   #numbers list removed as prevents the use of my_set
 
    while local_variable > 0:
        if local_variable % 2 == 0:  
           numbers.remove(local_variable)
        local_variable -= 1 
    
    return numbers

my_set = {1, 2, 3, 4, 5} 
#removed mirrored numbers
result = process_numbers(my_set) 
#removed numbers equals

def modify_dict():
    local_variable = 10
 #spelling error
    my_dict['key14'] = local_variable

modify_dict()
#removed the 5 to elimate argument

def update_global():
    global global_variable 
    global_variable += 10

    for i in range(5):
        print(i)
 #removed the i increment/ there is a loop present 

#spelling error here, wrong brackets for function
    if my_set is not None and my_dict.get('key14') == 10:
        print("Condition met!")

    if 5 not in my_dict.values():
        #added values so it looks for 5 
        print("not found in the dictionary!") 
       
#add an update function here
update_global()

print(global_variable)
print(my_dict)
print(my_set)

#indents kinda a issue in a few places