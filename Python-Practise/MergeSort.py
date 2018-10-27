#归并排序
#分治策略
#递归结构

#合并两个已排序好的数组成一个大数组
#q是排序好的左右数组的分界下标，这个下标所对应的值属于L
def Merge_func(A,p,q,r) :

	nl = q-p+1
	nr = r-q

	L = A[p:(p + nl)] #排序好的左数组
	R = A[(q + 1):(r+1)]  #排序好的右数组


	i = 0 #左数组的下标
	j = 0 #右数组的下标

	#将划分出来的数组存在原来数组的位置
	for k in range(p,r+1) :

		if i == nl :
			A[k] = R[j]
			j += 1
		elif j == nr :
			A[k] = L[i]
			i += 1
		elif L[i] > R[j] :
			A[k] = R[j]
			j += 1
		else :
			A[k] = L[i]
			i += 1
	#合并结束
#函数结束

#递归实现，对原数组进行拆分，并调用Merge_func函数
#A为输入数组，p是A最左边的下标，r是A最右边的下标
def Msort(A, p, r) :

	if p < r :

		q = (p + r) //2

		Msort(A,p,q)
		Msort(A,q+1,r)

		Merge_func(A,p,q,r)
	#合并结束
#函数结束

while True:

	# list_input_str = input('Please enter a list here: ')

	#文件读取，输出的是字符串
	f = open('testData.txt','r')
	list_input_str = f.read()

	if len(list_input_str) == 0 :
		print('Please input list again: ')
	
	if list_input_str == 'quit' :
		break

	#将字符串进行分割，取出空格分隔出的字符并转化为列表
	list_input = list_input_str.split(' ')

	#将列表中的每一个字符元素转化为int
	for i in range(0,len(list_input)) :
		list_input[i] = int(list_input[i])


	Msort(list_input,0,(len(list_input)-1))

	#输出排序后的序列
	Arr_output = str(list_input).split(',') #用字符串来输出

	print('Sort List: '.ljust(10))

	for k in range(0,len(Arr_output)) :

		if k == 0 :
			print(end='')
		elif k % 10 == 0 :
			print(end='\n')

		print(Arr_output[k].rjust(8),end=' ')

	print(end='\n')

	break

else : 
	print('You quit the sort now')

print('Done!')
