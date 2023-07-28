import sys

#changed_files = sys.argv[1:]
changed_files = sys.argv[1:]


for filename in changed_files:
    print(filename)
    
def process_list(list):
    for element in list:
        
        try:
            if isinstance(element, int):
                
                print(f"It is integer: {element}")
            else:
                raise ValueError(f"It's a string: {element}")
        except ValueError as e:
            print(f"Error: {e}. Skipping to the next element.")
            continue


mixed_list = [1, 'hello', 2, 'world', 3]

process_list(mixed_list)
