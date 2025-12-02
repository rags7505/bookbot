from stats import get_num_words,get_char_count,sort_dict
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  print("============ BOOKBOT ============")
  file_path=sys.argv[1]
  print("Analyzing book found at {}...".format(file_path))
  book_text=get_book_text(file_path)
  print("----------- Word Count ----------")
  words_count=get_num_words(book_text)
  print(words_count)
  dict_char=get_char_count(book_text)
  print("--------- Character Count -------")
  sorted_dict=sort_dict(dict_char)
  for char_info in sorted_dict:
    if char_info["char"].isalpha():
      print("{}: {}".format(char_info["char"],char_info["count"]))
  print("============= END ===============")
  
  
if len(sys.argv)==1:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)
main()