# UTILS
import sys
import random

# FUNCTION DICTIONARY EXIST DATA
def exist_data(data_dictionary, data_find):
    if data_find in data_dictionary:
        print_log('CONTAINS - DATA_DICTIONARY: {}'.format(data_find))
    else:
        print_log('NOT CONTAINS DATA IN THE DICTIONARY.')


# FUNCTION LIST EXIST DATA
def exist_data(data_list, data_find):
    return (data_find.upper in data_list)


# FUNCTION RANDOM NUMBER
def get_random_number(end_seed, start_seed=0):
    try:
        random_number = random.randrange(start_seed, end_seed)
    except:
        random_number = -1
        print_log('get_random_number')
    return random_number


# FUNCTION RANDOM QUESTION
# -*- coding: utf-8 -*-
def get_random_question(file_name, cod_index):
    try:
        questions_file = []
        data_file = open(file_name, 'r')
        rows_file = data_file.readlines()
        for row in rows_file:
            questions_file.append(row + '\n')
        data_file.close
        random_question = questions_file[cod_index].strip()
    except:
        random_question = '-'
        print_log('get_random_question')
    return random_question


# FUNCTION PRINT_ERROR
def print_error(name_method):
    print('Unexpected error in the method: ' + name_method, sys.exc_info()[0])


# FUNCTION PRINT_LOG
def print_log(name_method):
    print('Log-data write in the method: ' + name_method, sys.exc_info()[0])