#
#
#
#   Author: Serhat Yıldırm
#   Date: 14/08/2020
#
#
#

from sys import argv
from function import control_with_name
    
if __name__ == "__main__":
    if(len(argv) == 2):
        a = control_with_name(argv[1])
        print(a)
