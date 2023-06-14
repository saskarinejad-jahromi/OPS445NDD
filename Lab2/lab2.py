import sys

def print_arguments():
    script_name = sys.argv[0]
    variables = ' '.join(sys.argv[1:])
    print("Script name:", script_name)
    print("Script name with variables:", script_name, variables)

print_arguments()
