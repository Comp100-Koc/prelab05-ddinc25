def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    longest=''
    for start in range(len(s)):
        for end in range(start, len(s)):
            possible_pal= s[start:end+1]
            if len(possible_pal)>1:
                 if possible_pal==possible_pal[::-1]:
         
                     if len(possible_pal) > len(longest):
                         longest= possible_pal
            
    return longest              
 