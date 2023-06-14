# import random
# from retrying import retry

# @retry
# def do_something_unreliable():
#     if random.randint(0, 10) > 1:
#         raise IOError("Broken sauce, everything is hosed!!!111one")
#     else:
#         return "Awesome sauce!"

# print(do_something_unreliable())