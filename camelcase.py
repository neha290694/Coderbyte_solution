import re  # importing regular exoression

class Solution:
   def CamelCase(self, str):
      s = "".join(word[0].upper() + word[1:].lower() for word in str)
      return s[0].lower() + s[1:]

   def main():
      ob = Solution()
      string = input("Input:")
      words = re.sub("[^0-9a-zA-Z']+", ' ', string)
      str = words.split(' ')
      
      print("Output:",ob.CamelCase(str))
      
Solution.main()
