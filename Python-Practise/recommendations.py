import math

def sim_distance(prefs, p1, p2):
	#得到两人共同拥有的项目
	si = {}
	for item in prefs[p1]:
		if item in prefs[p2]:
			si[item] = 1

	if len(si) == 0:
		return 0

	sum_of_squares = sum([math.pow(prefs[p1][item]-prefs[p2][item], 2) for item in si])

	return 1/(1 + math.sqrt(sum_of_squares))

def sim_pearson(prefs, p1, p2):
	#得到两人共同拥有的项目
	si = {}
	for item in prefs[p1]:
		if item in prefs[p2]:
			si[item] = 1

	if len(si) == 0:
		return 0

	n = len(si)

	#对所有的偏好求和
	sum1 = sum([prefs[p1][item] for item in si])
	sum2 = sum([prefs[p2][item] for item in si])

	#对所有偏好求平方和
	sum1Sq = sum([pow(prefs[p1][item],2) for item in si])
	sum2Sq = sum([pow(prefs[p2][item],2) for item in si])

	#求乘积和
	pSum = sum([prefs[p1][item]*prefs[p2][item] for item in si])

	#计算皮尔逊相关度
	num = pSum - (sum1 * sum2/n)
	den = math.sqrt((sum1Sq-math.pow(sum1,2)/n) * (sum2Sq-math.pow(sum2,2)/n))
	if den == 0:
		return 0

	r = num/den

	return r



#从反映偏好的字典中返回最为匹配者
#返回结果的个数和相似度函数均为可选参数
def topMatches(prefs, person, n=5, similarity=sim_distance):
	scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

	scores.sort()
	scores.reverse()
	return scores[0:n]

#利用所有其他人评价值的加权平均，为某人提供建议
def getRecommendations(prefs, person, similarity=sim_distance):
	totals = {}
	simSums = {}

	for other in prefs:

		#不和自己作比较
		if other == person:
			continue

		sim = similarity(prefs, person, other)

		if sim < 0:
			continue

		for item in prefs[other]:
			#只对自己还未曾看过的影片进行评价推荐
			if item not in prefs[person] or prefs[person][item] == 0:
				totals.setdefault(item, 0)
				totals[item] += prefs[other][item]*sim
				simSums.setdefault(item, 0)
				simSums[item] += sim

	rankings = [(total/simSums[item], item) for item, total in totals.items()]

	rankings.sort()
	rankings.reverse()

	return rankings

def transformPrefs(prefs):
	result = {}

	for persons in prefs:
		for item in prefs[persons]:
			result.setdefault(item, {})
			result[item][persons] = prefs[persons][item]

	return result
