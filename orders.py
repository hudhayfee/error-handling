# we are using open()- a built in functionality to open files.

def open_and_print(file_to_open):
    try:  # tries to run the block of code
        file = open(file_to_open, 'r')
        file_line_list = file.readlines()

        for line in file_line_list:
            print(line.rstrip('\n'))

        file.close()  # if you don't close it you can cause a lock in the file - similar to trying to send a file via email which is already open

    except FileNotFoundError as errmsg:  # if it fails it runs this block of code
        print('File could not be open, please see below')
        print(errmsg)  # captured error message in line 5
    # raise  # sends the default error and stops the code: line 9 will not run

open_and_print('order.txt')