import os
import PySimpleGUI as sg
import customer_registration as reg_info
import customer_operations as ros
import search_details as cus
sg.theme('DarkAmber')
custo_detail = ''
filename = ''
search_again = True
while(search_again):
     layout = [[sg.Text("\t\t\t\nWELCOME TO INFO SEARCH.....\n ",font=('Constantia',15))],
              [sg.Text("\n\nwhat do you want to do?....\n\n", font=('Georgia', 15))],
              [sg.Text('Select here...\n', font=('MV Boli', 13))],
              [sg.Button(button_text='Register', size=(15, 1), pad=(5, (1, 0))),
              sg.Button(button_text='Search Details', size=(15, 1), pad=((75, 1), (0, 2)))],
              [sg.Button(button_text='Exit', size=(10, 1), pad=((600, 1), (10, 1)))]]
     window = sg.Window('--Info Search--',  layout, size=(700, 400))
     events, values = window.read()
     if events in (sg.WIN_CLOSED, 'Exit'):
        exit()
     elif 'Register' in events:
           layout1 = [[sg.Text("\n\n\t\t\t******** Customer registration application ********\n\n", font=('Bahnschrift SemiBold',10))],
                      [sg.Text("Enter your name       :", font=('Constantia', 12)),
                      sg.InputText(text_color='black', size=(40, 0),key='-IN-', font=('Calisto MT', 11))],
                      [sg.Text('Enter your EmailID    :', font=('Constantia', 12)),
                      sg.InputText(text_color='black', size=(40, 0),key='--IN--', font=('Calisto MT', 11))],
                      [sg.Text('Enter your Phone.No :', font=('Constantia', 12)),
                      sg.InputText(text_color='black', size=(40, 0),key='---IN---', font=('Calisto MT', 11))],
                      [sg.Text()],
                      [sg.Button(button_text='save', font=('Dubai Medium', 11))],
                      [sg.Button('EXIT'),
                       sg.Button('Back<<')]]
           window = sg.Window('--Customer Registration--', layout1, size=(700, 500))
           events1, values1 = window.read()
           cus_name = values1['-IN-']
           cus_email = values1['--IN--']
           cus_no = values1['---IN---']
           location = 'C:\\Users\\ELCOT\\PycharmProjects\\InfoSearch\\registration'
           registration = reg_info.cust_registration(location, cus_name, cus_email, cus_no)
           if 'save' in events1:
               layout2 = [[sg.Text(text=f'You entered valid details are.....{registration}\n\n', text_color='black')],
                          [sg.Text('\n\n\n\n\t\t\t******** Customer registration Successfull ********\n\n',  font=('Bahnschrift SemiBold', 10))],
                          [sg.Button('Exit'), sg.Button('Back<<')]]
               window = sg.Window('-- Registration Confirmation-- ', layout2, size=(600,700))
               events2 , values2 = window.read()
           if 'Exit'in events2:
                exit()
           if 'Back<<' in events2:
               search_again = True
     elif 'Search Details' in events:
           all_files = os.listdir("C:\\Users\\ELCOT\\PycharmProjects\\infosearch\\registration")
           layout1 = [[sg.Text('\t\t\t********To Search Customer Details********\n\n\n')],
                       [sg.Text('what basis you want to search: ')],
                       [sg.Listbox(['Name', 'Email', 'Phone.No'], key='in', font=('Bahnschrift Semibold', 11),size=(20,3),pad=(5,100))],
                       [sg.Text('Do you know registration date')],
                       [sg.Button('Yes>>', pad=((10, 1), (1, 0))), sg.Button('No>>', pad=((400, 1), (0, 2)))]]
           window = sg.Window('--Search Customer Details--', layout1, size=(600, 700))
           events1, values1 = window.read()
           detail_basis = values1['in']
           if 'Yes>>' in events1:
               layout2 = [[sg.Text('Choose  file name :\n(search and select filename based on your registration date)')],
                          [sg.Listbox(all_files, font='arialblack', size=(30,6),pad=(5,10))],
                          [sg.Text('Enter the choosen filename:'), sg.InputText('',key='choosen', size=(30,1))],
                          [sg.Text(f'\nEnter your {detail_basis}:'), sg.InputText(key='entered', size=(30, 1))],
                          [sg.Button('Search>>', pad=((400,1),(10,5)))]]
               window = sg.Window('--Search Cutsomer Details--', layout2, size=(600, 500))
               events2, values2 = window.read()
               filename= values2['choosen']
               custo_detail = values2['entered']
               if 'Search>>' in events2:
                   value = cus.searching_with_user_confirmation(user_known_file_name=filename, detail=custo_detail, basis=detail_basis)
                   layout3 = [[sg.Text(f'\n\n\t{value[0]}\n\t{value[1]}')],
                              [sg.Button('<<Back'),sg.Button('Exit')]]
                   window = sg.Window('--Search Customer Details--', layout3, size=(500, 600))
                   events3, values3 = window.read()
                   if '<<Back' in events3:
                       search_again = True
                   if 'Exit' in events3:
                       exit()
           if 'No>>' in events1:
               layout2 = [[sg.Text(f'\n   Enter your {detail_basis}'),sg.InputText('',key='IN', size=(30, 1))],
                          [sg.Button('Search>>', pad=((400,1),(10,5))),sg.Button('Exit', pad=((400,1),5))]]
               window = sg.Window('--Search Customer Details--', layout2, size=(700,400))
               events2, values2 = window.read()
               if 'Exit' in events2:
                   exit()
               if 'Search>>' in events2:
                   value = cus.searching_with_unknown_file(files_name=all_files, detail=custo_detail, basis=detail_basis)
                   layout3 = [[sg.Text(f'\n\n\t{value[0]}\n\t{value[1]}')],
                              [sg.Button('<<Back'), sg.Button('Exit')]]
                   window = sg.Window('--Searched Details--', layout3, size=(700,400))
                   events3 , values3 = window.read()
                   if '<<Back' in events3:
                       search_again = True
                   if 'Exit' in events3:
                       exit()
     window.close()



# window['welcometext'].update(visible=Tru
#            window['name_qn'].update(visible=True)
#            window['mail_qn'].update(visible=True)
#            window['phnno_qn'].update(visible=True)
#            window['-IN-'].update(visible=True)
#            window['--IN--'].update(visible=True)
#            window['---IN---'].update(visible=True)
#            window['ok'].update(visible=False)
#            window['confirmation'].update(visible=True)
#window['-OUT-'].update(visible=True)
#[sg.Text('In what basis you want to search details:(name,email,phnnum):',font=('arial black',12)),sg.Input(size=(15,1))],



