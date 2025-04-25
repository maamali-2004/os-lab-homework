# def climb(n):
#     if n < 0 :
#         return 0 
#     if n == 0 :
#         return 1
#     if n > 0:
#         return climb(n-1) + climb(n-2)
# print(climb(10))

# def climb(n):
#     if n < 0 :
#         return 0
#     if n == 0 :
#         return 1
#     if n > 0:
#         stair = [0] * (n+1)
#         stair[0] = stair[1] = 1
#         for i in range(2, n+1):
#             stair[i] = stair[i-1] + stair[i-2]
#         return stair[n]
# print(climb(10))
