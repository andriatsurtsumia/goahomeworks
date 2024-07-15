# def is_anagram(test, original):
#     if len(test) != len(original):
#         return False
    
#     test = test.lower()
#     original = original.lower()
    
#     for char in test:
#         if test.count(char) != original.count(char):
#             return False
    
#     return True


# def is_anagram(test, original):
#     if len(test) != len(original):
#         return False
    
#     joined = (test + original).lower()
    
#     for char in joined:
#         if joined.count(char) % 2 != 0:
#             return False
    
#     return True