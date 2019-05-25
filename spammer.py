
import requests, time, sys, getopt

import request, bcolors
    
def usage():
    print(bcolors.colors.OKBLUE + '## HELP ##' + bcolors.colors.ENDC)
    # Help section
    print(bcolors.colors.OKGREEN + '1. Help ' + bcolors.colors.ENDC)
    print(bcolors.colors.OKGREEN + '     ' + sys.argv[0] + ' -h' + bcolors.colors.ENDC)
    # Spam form section
    print(bcolors.colors.OKGREEN + '2. Spam a Form ' + bcolors.colors.ENDC)
    print(bcolors.colors.OKGREEN + ' Spams a webform x times. Define the x using the -t parameter' + bcolors.colors.ENDC)
    print(bcolors.colors.OKGREEN + '     ' + sys.argv[0] + ' -f [url] -t [times]' + bcolors.colors.ENDC)

def main(argv):
    EXEC_TYPE_FORM = 'exec_form'

    exec_type = ''
    exec_param = ''
    exec_times = 1

    try: 
        opts, args = getopt.getopt(argv, 'f:t:h', [])
    except getopt.GetoptError as err:
        print(bcolors.colors.FAIL + str(err) + bcolors.colors.ENDC)
        usage()
        sys.exit(2)

    for (opt, arg) in opts:
        if opt == '-h':
            usage()
        elif opt == '-f':
            exec_type = EXEC_TYPE_FORM
            exec_param = arg
        elif opt == '-t':
            exec_times = arg
        else:
            print(bcolors.colors.FAIL + 'Missing parameters.' + bcolors.colors.ENDC)
            usage()

    if exec_type == EXEC_TYPE_FORM:
        spam_form(exec_param, exec_times)
        
    else:
        print(bcolors.colors.FAIL + 'Missing parameters.' + bcolors.colors.ENDC)
        usage()

def spam_form(url, times):
    r = request.Request()

    try:
        r.call(url, times)
    except Exception as err:
        print(bcolors.colors.FAIL + str(err) + bcolors.colors.ENDC)
        usage()
        sys.exit(2)


if __name__ == "__main__": 
    main(sys.argv[1:])
