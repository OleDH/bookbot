



def main():
   #print("ost")
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")

        print(count_strings(file_contents))
        print("\n")

        count_chars(file_contents)

        print("--- End report ---")

def count_strings(s):
    words = s.split()

    return f"{len(words)} words were found in the document" 



    




def count_chars(s):

    my_dict = {}

    clean_string = s.lower()

    sorted_list = []

    for char in clean_string:

        if char.isalpha():
            sorted_list.append(char)

    
    sorted_list.sort()

   # print(sorted_list)


    new_dict={}
    #print(clean_string)

    for char in sorted_list:
        
       

        if char not in my_dict:
            my_dict[char] = 1
        
        else:
            my_dict[char] += 1

    
         
    for key,value in my_dict.items():

        #print(value)

        print(f"'{key}' character was found {value} times")

        



    

    
       

        





main()





   