# import tkinter
# window=tkinter.Tk()
# # add widgets here
#
# window.title('Customers Details')
# window.geometry("300x200+10+20")
# window.mainloop()
import os
import customer_registration as reg_info
global direction
def searching_with_user_confirmation(user_known_file_name,detail,basis):
    direction = 'C:\\Users\\ELCOT\\PycharmProjects\\infosearch\\registration'
    user_known_file_path = (f'{direction}\\{user_known_file_name}')
    open_file = open(user_known_file_path, 'r')
    reading_file = open_file.readlines()
    flag = 0
    index = 0
    for line in reading_file:
        index += 1
        if detail in line:
            flag = 1
            if flag == 0:
                pass
            elif flag > 0 and detail in line:
                 confirmation = f'The given name {detail}found in line {index} in {user_known_file_name}'
                 line= f'{index} line : {line}'
                 break
            else:
                 confirmation= f'The given {basis} is not in {user_known_file_name} file'
                 line = ''
    open_file.close()
    return confirmation, line

def searching_with_unknown_file(files_name,detail,basis):
    for file1 in files_name:
        direct_path = 'C:\\Users\\ELCOT\\PycharmProjects\\InfoSearch\\registration'
        file_path = (f'{direct_path}\\{file1}')
        file_opening = open(file_path, 'r')
        reading_lines = file_opening.readlines()
        flag = 0
        index = 0
        for line in reading_lines:
            index += 1
            if detail in line:
                flag=1
                if flag == 0:
                    pass
                elif flag > 0 and detail in line:
                     confirmation = f'Given {basis}=  {detail} Found In line {index}  in {file1}  file'
                     line= f'{index} line: {line}'
                     break
                else:
                     confirmation=f'Given {basis}={detail} is not registered'
        file_opening.close()
        return confirmation , line

