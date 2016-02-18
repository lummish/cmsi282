#threepartition.py

def three_partition(numbers, target_sum_is_set=False, target_sum=0):

	if len(numbers) == 0:
		return True

	if len(numbers) == 3:
		if target_sum_is_set:

			if sum(numbers) == target_sum:
				return True
		else:
			return True

	if len(numbers) % 3 != 0:
		return False

	total = sum(numbers)
	n = len(numbers) / 3

	if total % n != 0: #if sum of numbers is not divisible by n, not partitionable
		return False

	if not target_sum_is_set:
		target_sum = total / n #stores target sum for each partition
		target_sum_is_set = True
	
	for i in range(1, len(numbers) - 1):
		for j in range(2, len(numbers)):
				if numbers[0] + numbers[i] + numbers[j] == target_sum:
					return three_partition(numbers[1:i] + numbers[i+1:j] + numbers[j+1:],
										   True,
										   target_sum)

	return False


	

