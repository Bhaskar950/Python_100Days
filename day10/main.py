def format_name(f_name,l_name):
    print(f_name.title())
    print(l_name.title())

format_name("bhaSkAR","kOilada")



def format_name1(f_name,l_name):  
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    print(f"My name is {formatted_f_name} {formatted_l_name}")
format_name1("bhaSkAR","kOilada")



def format_name3(f_name,l_name):
    if f_name == "" or l_name == "":
       return "you didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return (f"My name is {formatted_f_name} {formatted_l_name}")

print(format_name3(input("What is your first name?\n "),input("What is your last name?\n")))
