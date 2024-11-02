import datetime
import os

import cust_data_validation as validation



def create_file_if_not_exists(location):
    if os.path.exists(location):
        pass#print(f'File {location} is already existing. So not creating newly.')
    else:
        created_file = open(location, 'x')
        created_file.close()
        #print(f'File {location} is not existing. So creating newly.')


def get_current_filename(location):
    filename = datetime.datetime.now().date()
    full_path = f'{location}\\{filename}.txt'
    return full_path

def customer_details_verification(Name, Email, Phnno):
    #repeat_name = False
    #name = input('Enter your name : ')
    # x = name.isalpha()
    # if x == True:
    #     print('')
    # else:
    #     print('Your should have only alphabet characters..So..Please enter valid name!!')
    #repeat_name = False
    repeat_name = False
    while repeat_name:
        name_validiy = name.isalpha()
        if name_validiy== True:
            pass
        else:
            repeat_name = False
    repeat_email = True
    while repeat_email:
        validity = validation.email_valiadation(Email)
        if validity:
            repeat_email = False
        else:
            repeat_email = True
    reg_tim = datetime.datetime.now().time()
    cust_details = f'{Name},\n{Email},\n{Phnno}\nTime:{reg_tim}'
    return cust_details

def write_to_the_file(filename, details):
    file_to_write = open(filename, 'a')
    file_to_write.write(details)
    file_to_write.close()
    confirm = 'values are stored'
    return confirm

