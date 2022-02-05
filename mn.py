# with open("photo.jfif", 'ab') as f:
#     f.write(b"Dark Army")

 
# with open("photo.jfif", 'rb') as f:
#      content = f.read()
#      offset = content.index(bytes.fromhex('FFD9'))

#      f.seek(offset + 2)
#      print(f.read().decode('utf-8'))


# def compute_hcf(x, y):
    
# # choose the smaller number
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if((x % i == 0) and (y % i == 0)):
#             hcf = i 
#     return hcf

# num1 = 450
# num2 = 1080

# print("The H.C.F. is", compute_hcf(num1, num2))

# s=0
# c=0
# for i in range(2,72):
#      # s=s+i**2
#      # c=c+1
#      if 72%i==0:
#           s=s+i
#           c=c+1

# print(s/c)

# print(c)


# n=int(input())
# s=0
# for i in range(2,n+1):
#      s = s + n//i

# print(s)
n=int(input())
st = input()
k=int(input())
s=0

v=['a', 'e', 'i', 'o', 'u']
for i in range(0, n):
     if st[i] not in v:
          s = s + 1
sr = 0
for i in range(0, n):
     if st[i] in v:
          sr = sr + 1
print(s, sr)
if s==0 or sr==0:
     print(0)
elif sr>s:
     print(s+k)
else:
     print(sr+k)












