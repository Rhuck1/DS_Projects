def create_dictionary(text_file):
   
    d = {}
    with open(text_file) as f:
        for line in f:
           (key, val) = line.split()
           d[int(key)] = val

    return d

def create_nums(dictionary):
   
   nums = [key for key in dictionary.keys()]

   return sorted(nums)

def create_staircase(nums):
    
  step = 1
  subsets = []
    
  while len(nums) != 0:
    
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    
    else:
      return False
      
  return subsets

def assemble_code(stairs, text_file):
   
   dictionary = create_dictionary(text_file)
   string = ""
   for lst in stairs:
      string = string + dictionary[lst[-1]] + " "

   return string.strip()  


def decode(message_file):

    dictionary = create_dictionary(message_file)

    nums = create_nums(dictionary)

    stairs = create_staircase(nums)

    if stairs is False:
       return "Your stairs are uneven"
    
    else:
       return assemble_code(stairs, message_file)
       


text = "coding_qual_input.txt"
uneven_text = "uneven_stairs_coding_qual_input.txt"



decode(uneven_text)
