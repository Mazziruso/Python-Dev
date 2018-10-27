import docclass
import recommendations

# c1 = docclass.classifier(docclass.getwords)
# docclass.sampletrain(c1)
#
# # c1.train('the quick brown fox jumps over the lazy dog', 'good')
# # c1.train('make quick money in the online casino', 'bad')
#
# print('the class \'good\' of feature \'quick\' has ', c1.fcount('quick', 'good'))
# print('the class \'bad\' of feature \'quick\' has ', c1.fcount('quick', 'bad'))

#涉及影评者及其对几部影片评分情况的字典
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, \
						 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0}, \
		   'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5,'Superman Returns': 5.0, \
							'You, Me and Dupree': 3.5, 'The Night Listener': 3.0}, \
		   'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, \
								'The Night Listener': 4.0}, \
		   'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 4.0, \
							'You, Me and Dupree': 2.5, 'The Night Listener': 4.5}, \
		   'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0,\
							'You, Me and Dupree': 2.0, 'The Night Listener': 3.0}, \
		   'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Superman Returns': 5.0, \
							 'You, Me and Dupree': 3.5, 'The Night Listener':3.0}, \
		   'Toby': {'Snakes on a Plane': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 1.0}}

list_of_recommendations = recommendations.topMatches(critics, 'Toby', n=3)
print('when algorithm of similarity is sim_distance:')
print(list_of_recommendations)

list_of_recommendations = recommendations.topMatches(critics, 'Toby', n=3, similarity=recommendations.sim_pearson)
print('when algorithm of similarity is sim_pearson:')
print(list_of_recommendations)


person_getRecommendations = recommendations.getRecommendations(critics, 'Toby')
print('when algorithm of similarity is sim_distance:')
print(person_getRecommendations)

person_getRecommendations = recommendations.getRecommendations(critics, 'Toby', similarity=recommendations.sim_pearson)
print('when algorithm of similarity is sim_pearson:')
print(person_getRecommendations)
print(end='\n')

movies = recommendations.transformPrefs(critics)
for item in movies:
	print(item, movies[item])
print(end='\n')

movie_recommendations = recommendations.topMatches(movies, 'Superman Returns')
print('when algorithm is sim_distance:\n', movie_recommendations)
movie_recommendations = recommendations.topMatches(movies, 'Superman Returns', similarity=recommendations.sim_pearson)
print('when algorithm is sim_pearson:\n', movie_recommendations)
