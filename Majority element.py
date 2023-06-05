def findMajorityElement(arr, n):
	d = {}
	for i in range(n):
		d[arr[i]] = d.get(arr[i], 0) + 1
	for key in d:
		if(d[key] > n//2):
			return key
	return -1