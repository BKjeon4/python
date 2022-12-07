# 1. 코드의 실행 결과
a = [0,1,2,3,4]
print(a[:3], a[:-3])

# 2. 코드의 실행 결과
a = [0,1,2,3,4]
print(a[::-1])

# 3. 코드의 실행 결과
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]

order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]

del john[2]
john.extend([order[2][0:1]])
print(john)

# 4. 코드의 실행 결과
list_a = [3, 2, 1, 4]
list_b = list_a.sort() #(sorted(list_a)
print(list_a, list_b)

# 5. 코드의 실행 결과
fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])

# 6. 코드의 실행 결과
num = [1, 2, 3, 4]
print(num * 2)

# 7.
a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']
a.append('g')
b.append(6)
print('g' in b, len(b))

# 8.
list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
list_b = []
for i in range(len(list_a)):
    if i % 2 != 1:
        list_b.append(list_a[i])
print(list_b)

# 9. input 은 다 string
admission_year = input("입학 연도를 입력하세요: ")
print(type(admission_year))

# 10.
country = ["Korea", "Japan", "China"]
capital = ["Seoul", "Tokyo", "Beijing"]
index = [1, 2, 3]
country.append(capital)
country[3][1] = index[1:]
print(country)