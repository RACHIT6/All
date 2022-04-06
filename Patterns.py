n = int(input("Enter the number of rows: "))

# *
# **
# ***
# ****
# *****
# for i in range(n):
#     for j in range(0, i + 1):
#         print("*", end = "")
#     print()

# 1
# 12
# 123
# 1234
# 12345
# for i in range(0, n):
#     for j in range(1, i + 2):
#         print(j, end = "")
#     print()

#     *     *
#    **    **
#   ***   ***
#  ****  ****
# ***** *****
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end = "")
#     for z in range(0, i + 1):
#         print("*", end = "")
#     for j in range(n - i):
#         print(" ", end = "")
#     for z in range(0, i + 1):
#         print("*", end = "")
#     print()

# *****
# ****
# ***
# **
# *
# for i in range(n):
#     for j in range(n - i):
#         print("*", end= "")
#     print()

# 1
# 23
# 456
# 7891
# 23456
# sum = 1
# for i in range(n):
#     for j in range(0, i + 1):
#         if sum > 9:
#             sum = 1
#         print(sum, end = "")
#         sum += 1
#     print()

# *****
# *   *
# *   *
# *****
# for i in range(1, n):
#     for j in range(0, n):
#         if i == 1 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end = "")
#         else:
#             print(" ", end= "")
#     print()

#     *
#    **
#   ***
#  ****
# *****
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end= "")
#     for z in range(i + 1):
#         print("*", end= "")
#     print()

# A
# BC
# DEF
# GHIJ
# KLMNO
# alp = 65
# for i in range(n):
#     for j in range(i + 1):
#         if alp > 90:
#             alp = 65
#         print(chr(alp), end= "")
#         alp += 1
#     print()

#     *  
#    * *
#   * * *
#  * * * *
# * * * * *
# k = n - 1
# for i in range(n):
#     for j in range(0, k):
#         print(end= " ")
    
#     k -= 1

#     for z in range(0, i + 1):
#         print("* ", end= "")
#     print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# for i in range(n):
#     for j in range(n - i):
#         print(" ", end= "")
#     for j in range(i + 1):
#         print("*", end = " ")
#     print()

# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end= "")
#     print(end = " ")
#     for j in range(n - i - 1):
#         print("*", end=" ")
#     print()

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
# for i in range(n):
#     for j in range(n - i):
#         print(" ", end= "")
#     for j in range(i + 1):
#         print("*", end = " ")
#     print()

# *****
#  ****
#   ***
#    **
#     *
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n - i):
#         print("*", end= "")
#     print()