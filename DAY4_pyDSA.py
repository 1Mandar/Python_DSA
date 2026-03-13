# list=[1,2,3,4,5]
# list.append(10)
# print(list)
# list.insert(1,20)
# print(list)
# list.remove(3)
# print(list)


list=[1,2,2,2,3,4,5]
list.reverse()
print(list)
print(list.count(2))
list2=["a","b","c"]
print("index of b is ",list2.index("b"))


# #remove duplicates from list
# number=[1,2,2,3,4,4,5]
# rem=[]
# for i in number:
#     if i not in rem:
#         rem.append(i)
# print("actual list is ",number)
# print("list after removing duplicates is ",rem)

num=[45,23,67,12,89]
maximum=second_largest =float('-inf')
for i in num:
    if i>maximum:
        second_largest=maximum
        maximum=i
    elif i>second_largest and i!=maximum:
        second_largest=i
print("maximum is ",maximum)
print("second largest is ",second_largest)


# find all pairs in a list whose sum eql to target
num=[2,4,3,5,7,8,9]
target=10
rem=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]+num[j]==target):
            rem.append((num[i],num[j]))
print("pair is ",rem)            


# count how many times each element appears in list
num=[1,2,2,3,3,3,4,4,5,5,5,5]
dict={} 
for i in num:
    dict[i]=dict.get(i,0)+1
print(dict)  
# 2nd approch
dict2={}
for i in num:
    if i in dict2:
        dict2[i]+=1
    else:
        dict2[i]=1
print(dict2)            


# find frequency of each element in list
num=[1,2,2,3,3,3,4,4,5,5,5,5]
dict3={}    
for i in num:
    dict3[i]=dict3.get(i,0)+1
for key,value in dict3.items():
    print(f"{key} appears {value} times")

# list functions
data=["hello","python","java"]
print(data)
data.append("C++")
print(data)
data.insert(1,"php")
print(data)
data.remove("hello")
print(data)
data.reverse()
print(data) 



# list tuple set dictionary
# list [] tuple () {set} {key:value}
list=[1,2,3,4,5,10.67,"hello",'A']
print(type(list))
print(list)

tuple=(1,2,3,5,'A',"python","java")
print(tuple)
print(type(tuple))

set1={1,2,3,4,5}
print(set1)
print(type(set1))

dict={"name":"Mandar","age":19}
print(dict)
print(type(dict))

# list functions
marks=[10,20,60,40,89,43]
marks.sort()
print(marks)
marks.reverse()
print(marks)

# find second largset
num=[12,45,78,56,34,89]
maximum=second_max=float('-inf')
for i in num:
    if i>maximum:
        second_max=maximum
        maximum=i
    elif i>second_max and i!=maximum:
        second_max=i
print("second largest number:",second_max)

#    find all pairs sum is equal to target
num=[2,4,3,5,7,8,9]
target=10
rem=[]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==target:
            rem.append((num[i],num[j]))
print("pairs are ",rem)


# tasK

# find missing number in sequence
# 1 2  4 5 ==> 3
num=[1,2,4,5]
n=len(num)+1
total_sum=n*(n+1)//2
actual_sum=sum(num)
missing_number=total_sum-actual_sum
print("missing number is ",missing_number)

# through list separate even odd  numbere
num=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers are ",even)
print("odd numbers are ",odd)

# find common elements between two lists
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print("common elements are ",common)


# reverse list without using reverse function
list=[1,2,3,4,5]
reversed_list=[]
for i in range(len(list)-1,-1,-1):
    reversed_list.append(list[i])
print("reversed list is ",reversed_list)

# find longest word in list
words=["hello","python","java","programming"]
longest_word=""
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print("longest word is ",longest_word)


# list=["hello","python","c","c++","FullstackJava"]
print("original list is ",list)
list.sort(key=len)
print("sorted list is ",list)

