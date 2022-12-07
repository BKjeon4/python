# 1
list_1 = [0, 3, 1, 7, 5, 0, 5, 8, 0, 4]


def quiz_2(list_data):
    a = set(list_data)  # 중복값 x
    return list(a)[1:5]  # 자동정렬


print(quiz_2(list_1))


# 2
def delete_a_list_element(list_data, element_value):
    if element_value in list_data:
        list_data.remove(element_value)
        return list_data
    else:
        return "False"


list_data = ['a', 1, 'gachon', '2016.0']
element = float(2016)
result = delete_a_list_element(list_data, element)
print(result)

# 3
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)


def quiz_1(tuple_1, tuple_2):
    result = []
    for i in (tuple_1 + tuple_2):
        result.append(i)
    return result


print(quiz_1(tuple_1, tuple_2))


# 연습문제 1

def even_filter(ls):
    result = []
    for i in ls:
        if i % 2 == 0:
            result.append(i)
    return (result)


print(even_filter([1, 2, 4, 5, 8, 9, 10]))


# 연습문제 2
def is_prime_number(num):
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return "False"
    return "True"

print(is_prime_number(60))
print(is_prime_number(61))


# 연습문제 3
def count_vowel(words):
	vowel = ['a','e','i','o','u']
	count = 0
	for i in words:
		if i in vowel:
			count += 1
	return count

print(count_vowel("pythonian"))

def count_vowel2(words):
	vowel = ['a','e','i','o','u']
	cnt = 0
	for i in vowel:
		cnt += words.count(i)
	return cnt

print(count_vowel2("pythonian"))