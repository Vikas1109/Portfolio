# print("HELLO WORLD")

# # def sum(n):
# #     d1 = []
# #     d2 = []
# #     for i in range(n):
# #         x = [int(i) for i in input().split()]
# #         d1.append(x[0])
# #         d2.append(x[1])
# #     d3 = list(zip(d1,d2))
    
# #     d4 = {}

# #     for i in range(len(d3)):
# #         for j in range(2):
# #             if d3[i][0] in d4 and d3[i][1] > d4.values():
                
# # n = int(input())

# # print(sum(n))



# def passing(arr):
#     d = []
#     for i in range(3):
#         if(arr[-1]>=arr[0]and arr[-2]>= arr[1]and arr[-3]>=arr[2] and (arr[-1]+arr[-2]+arr[-3] >= arr[3])):
            

#             d.append(True)
#         else:
#             d.append(False)
#     if all(d) == True:

#         return("YES")
#     else:
#         return("NO")
# T = int(input())
# for i in range(T):
#     arr = [int[i] for i in input().split()]
#     print(passing(arr))
# your code goes here


def pairs(n1,a):

    c = [(a[i]+a[i+1])**2 for i in range(n1-1)]
    
    m = []

    for i in c:
        if i not in m:
            m.append(i)
    print(sum(m))
   


t = int(input())

for i in range(t):
	n1 = int(input())
	a = [int(i) for i in input().split()]
	
	
	
	(pairs(n1,a))
