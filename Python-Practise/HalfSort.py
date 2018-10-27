
#二分法排序

def InsertIndex(Arr,start,end,K) :

	#Search inset index of k in list Arr
	while start < end :

		middle_index = int((start + end)/2)
		middle_data = Arr[middle_index]

		if middle_data > K :
			end = middle_index - 1
		else :
			start = middle_index + 1

	return start

def InsertSort(Arr) :

	#Insert sort algorithm by insert index

	# if len(Arr) == 0 :
	# 	print('The list Arr is NULL')
	# 	break

	for i in range(1,len(Arr)) :

		temp = Arr[i]

		index = InsertIndex(Arr,0,i,Arr[i])


		for j in range(i-1,index-1,-1) :
			Arr[j+1] = Arr[j]

		Arr[index] = temp

	print('Sort List: '.ljust(10))

	for k in range(0,len(Arr)) :
		if k % 10 == 0 :
			print(end='\n')

		print(Arr[k],end=' ')

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
