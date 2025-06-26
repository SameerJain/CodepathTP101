"""
A pangram is a sentence that contains every letter of the English alphabet at least once, regardless of case. Write a function to determine if a given sentence is a pangram.
"""

def is_pangram(sentence):
   sentence = sentence[:].lower().replace(' ','')
   freqs = {}
   print(sentence)
   for char in sentence:
      if char != ' ':
         freqs[char] = freqs.get(char,0) + 1
   
   if len(freqs.keys()) < 26:
      return False

   return True


"""
Input: sentence = "The quick brown fox jumps over the lazy dog"
Output: True
"""
sentence = "The quick brow fox jumps over the lazy dog"
print(is_pangram(sentence))

"""
Given a string s containing words separated by spaces, reverse the order of the words. Remove extra spaces and ensure that words are separated by a single space in the output.
"""
def reverse_string(myStr):
	reversed_str = ''
	for char in myStr:
		reversed_str = char + reversed_str
	return reversed_str
   
def reverse_words(s):
   new_str = s.split()
   result = []

   for word in new_str[::-1]:
      result.append(word)
   return ' '.join(result)

"""
Input: s = "  the sky is  blue  "
Output: "blue is sky the"
"""
s = "  the sky is  blue  "
print(reverse_string(s))