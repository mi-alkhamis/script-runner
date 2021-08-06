#!/usr/bin/python

from os import environ
from subprocess import run
from sys import stderr,stdout 
from time import sleep



def input_check():
    """
    This function check input variables
    """ 
    DWS_TESTER_COMMAND = environ.get('DWS_TESTER_COMMAND', 'None')
    DWS_TESTER_THRESHOLD = environ.get('DWS_TESTER_THRESHOLD', 1)
    DWS_TESTER_INTERVAL = environ.get('DWS_TESTER_INTERVAL', 0)

    if str(DWS_TESTER_COMMAND).endswith("py"):
        print(f"command file is \"{DWS_TESTER_COMMAND}\" ")
    else:
        print("please input a python file to app to execute\n")
        return 1
    
    if str(DWS_TESTER_THRESHOLD).isnumeric():
        DWS_TESTER_THRESHOLD = int(DWS_TESTER_THRESHOLD)
        
    else:

        print("Please input a number for DWS_TESTER_THRESHOLD \n")
        return 1
    
    if str(DWS_TESTER_INTERVAL).isnumeric():
        DWS_TESTER_INTERVAL = int(DWS_TESTER_INTERVAL)
        
    else:

        print("Please input a number for DWS_TESTER_INTERVAL \n")
        return 1
    
    return (DWS_TESTER_COMMAND,DWS_TESTER_THRESHOLD,DWS_TESTER_INTERVAL)


def cmd_tester(args):

    command,threshold,interval = args
    while threshold  > 0 :
        run_code = run(["python" , command], stdout = stdout, stderr = stderr)
        threshold = threshold - 1
        if run_code.returncode == 0 :
            print ("code run successfully")
            return 1
        else:
            if threshold == 0:
                return 1
            else:
                sleep(interval)
            
    return 1
        
if __name__ == '__main__':
    check_result = input_check()
    if check_result == 1:
        print("please check your inputs and try agian")
        exit(1)
    else:
        cmd_result =  cmd_tester(check_result)
        # print(f"status code: {status}")
        if cmd_result == 0:
            print("Program runs successfully")
            exit(0)
        else:
            print("Program failed", file = stderr)
            exit(1)
    
