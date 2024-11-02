# directory = 'D:\\Studies\\PycharmProjects\\DataAnalytics_Bhavani\\registration'
import registration_operations as ros
import os

global directory
def cust_registration(directory, name ,email , phnno):
    full_path = ros.get_current_filename(directory)
    ros.create_file_if_not_exists(full_path)
    details = ros.customer_details_verification(name, email, phnno)
    confirm =ros.write_to_the_file(full_path, details)
    return confirm, details







