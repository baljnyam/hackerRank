#ABCDCDC
#CDC

def count_substring(string, sub_string):
       b = [i for i in range(0, len(string)) if sub_string == string[i:i+len(sub_string)]]
       return len(b)

count_substring("ABCDCDC", "CDC")
'''
count = 0
       for i in range(0, len(string)):
              if sub_string == string[i:i+len(sub_string)]:
                     count = count + 1
       return count
       '''
