def majorityElementII(arr):
	d = {}
	n = len(arr)
	for i in range(n):
		d[arr[i]] = d.get(arr[i], 0) + 1
	res = []
	for key in d:
		if d[key] > n//3:
			res.append(key)
	
	return res