# majority_elem.py

def majority_element(numbers):
	mid = len(numbers) / 2
	first_half = numbers[:mid + 1]
	last_half = numbers[mid + 1:]

	if (len(numbers) > 1):
		first_majority = majority_element(first_half)
		last_majority = majority_element(last_half)
	else:
		if len(numbers) == 1:
			return numbers[0]
		elif numbers[0] == numbers[1]:
			return numbers[0]
		else:
			return None
	if not first_majority and not last_majority:
			return None
	if len(first_half) == len(last_half):
		if first_majority and not last_majority:
			return first_majority
		elif last_majority and not first_majority:
			return last_majority
		elif first_majority == last_majority:
			return first_majority
		elif first_majority != last_majority:
			first_count = numbers.count(first_majority)
			last_count = numbers.count(last_majority)
			if first_count > len(numbers) / 2:
				return first_majority
			elif lst_count > len(numbers) / 2:
				return last_majority
			else:
				return None
	else:
		if not last_majority:
			return first_majority
		else:
			return last_majority


print(majority_element([1,2,3,4,2, 2, 2, 2, 2, 5]))
