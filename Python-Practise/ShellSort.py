#希尔排序
#使用Shell推荐的增量序列

def InsertIndex(Arr,start,Increment,end,K) :

	#Search inset index of k in list Arr
	bias = start #组里第一个元素下标的偏移值
	while start <= end : #等号避免当end缩小时与start相同但是start值却未变，导致下标没有按照预设输出

		middle_index = ((start // Increment + end // Increment) // 2 ) * Increment + bias
		middle_data = Arr[middle_index]

		if middle_data >= K : #等号避免start跳出数组范围
			end = middle_index - Increment
		else :
			start = middle_index + Increment

	return start

def InsertSort(Arr) :

	#Insert sort algorithm by insert index

	# if len(Arr) == 0 :
	# 	print('The list Arr is NULL')
	# 	break

	Increment = len(Arr) // 2

	while Increment > 0 :

		for i in range(Increment,len(Arr)) :

			temp = Arr[i]

			index = InsertIndex(Arr,(i % Increment),Increment,i,Arr[i])


			for j in range((i-Increment),(index-Increment),-Increment) :
				Arr[j+Increment] = Arr[j]

			Arr[index] = temp

		Increment //= 2

	#插入排序结束

	#输出排序后的序列
	Arr_output = str(Arr).split(',') #用字符串来输出

	print('Sort List: '.ljust(10))

	for k in range(0,len(Arr_output)) :

		if k == 0 :
			print(end='')
		elif k % 10 == 0 :
			print(end='\n')

		print(Arr_output[k].rjust(8),end=' ')

	print(end='\n')





while True:

	# list_input1 = input('Please enter a list here: ')

	#文件读取，输出的是字符串
	f = open('testData.txt','r')
	list_input1 = f.read()

	if len(list_input1) == 0 :
		print('Please input list again: ')
	
	if list_input1 == 'quit' :
		break

	#将字符串进行分割，取出空格分隔出的字符并转化为列表
	list_input = list_input1.split(' ')

	#将列表中的每一个字符元素转化为int
	for i in range(0,len(list_input)) :
		list_input[i] = int(list_input[i])


	InsertSort(list_input)

	break

else : 
	print('You quit the sort now')

print('Done!')
