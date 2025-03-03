from stats import count_strings,count_chars
import sys


def main():
   #print("ost")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(str(sys.argv[1])) as f:
        
        

        file_contents = f.read()
        #print(file_contents)
        print("Analyzing book found at books/frankenstein.txt...")
        print("============ BOOKBOT ============")

        print("--- Begin report of books/frankenstein.txt ---")
        #print(count_strings(file_contents))
        print("----------- Word Count ----------")
        count_strings(file_contents)
        
        #print("\n")
        print("--------- Character Count -------")
        count_chars(file_contents)
        print("============= END ===============")


main()





   