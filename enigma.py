import sys
from mediator import create_code_book
'''
module for comunication with user
first argument tells about desired functionality (count of arguments):
    -book - create code book (0:3)
    -build - build machine (0:3)
    -load - build machine from code (2)
    -enc - encrypt message ( )
    -encf - encrypt file ( )
'''

def execute():
    arg_len = len(sys.argv) 
    if arg_len < 2:
        print('provide action sigature and arguments')
        return -1
    function_choice = sys.argv[1]
    argument_list = sys.argv[2:] + [None]*(5-arg_len+1) # max argument count: 
    # print(argument_list)

    if function_choice == '-c':
        # def create_code_book(no=100, seed=None, filename=None):
        no = int(argument_list[0]) if argument_list[0] else 100
        filename = argument_list[1] if argument_list[1] else 'codebook'
        seed = argument_list[2] if argument_list[2] else 123

        print(no, filename, seed)
        create_code_book(no, filename, seed)









# class NotEnouchArg(Exception):
#     def __init__(self):
#         print('provide action sigature and arguments')

if __name__=="__main__":
    execute()
