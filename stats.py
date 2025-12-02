def get_num_words(text):
  num_words=text.split()
  return "Found {} total words".format(len(num_words))

def get_char_count(text):
  text=text.lower()
  dict_char={}
  for char in text:
    if char in dict_char:
      dict_char[char]+=1
    else:
      dict_char[char]=1
      
  return dict_char

def sort_on(items):
  return items["count"]

def sort_dict(input_dict):
  l=[]
  for char,count in input_dict.items():
    dic={"char":char,"count":count}
    l.append(dic)
    
  l.sort(reverse=True,key=sort_on)
  return l
