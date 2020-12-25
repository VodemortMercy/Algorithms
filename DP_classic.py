def canSum(tarSum, fromList):# true false table
	dp_table = [False for i in range(tarSum)]
	dp_table[0] = True
	for idx in range(len(dp_table)):
		for each in fromList:
			if dp_table[idx] and each+idx<len(dp_table):
				dp_table[each+idx] = True
	return dp_table

def howSum(tarSum, fromList):# possible situation table
	dp_table = [None for _ in range(tarSum+1)]
	dp_table[0] = []
	for idx in range(len(dp_table)+1):
		for each in fromList:
			if idx + each >= tarSum+1:
				continue
			if dp_table[idx] != None:
				tmp_list = [] + dp_table[idx]
				tmp_list.append(each)
				dp_table[idx+each] = tmp_list
	return dp_table

def bestSum(tarSum, fromList):# max-min possible situation table
	dp_table = [None for i in range(tarSum+1)]
	dp_table[0] = []
	for idx in range(tarSum+1):
		for each in fromList:
			if idx+each>=tarSum+1:
				continue
			if dp_table[idx] != None and dp_table[idx+each]!=None:
				cur_path = dp_table[idx+each]
				new_path = [] + dp_table[idx]
				new_path.append(each)
				min_path = (new_path, cur_path)[1 if len(new_path)>len(cur_path) else 0]
				dp_table[each+idx] = min_path
			if dp_table[idx] != None and dp_table[idx+each] == None:
				tmp_path = [] + dp_table[idx]
				tmp_path.append(each)
				dp_table[idx+each] = tmp_path
	return dp_table

print(canSum(7, [3,4,5]))
print(howSum(300, [7,14]))
print(bestSum(300, [7,14]))