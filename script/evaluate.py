#coding = utf8
import sys,os
import json

class Evaluator(object):
	def __init__(self):
		self.rec_result = {}
		self.test_result = {}
	
	def score(self):
		hit = 0
		predict_tot = 0
		recall_tot = 0
		for uid, predict_songs in self.rec_result.iteritems():
			test_songs = self.test_set[uid]
			hit += len(set(predict_songs) & set(test_songs))
			predict_tot += len(predict_songs)
			recall_tot += len(test_songs)
		
		precision = float(hit)/predict_tot
		recall = float(hit)/recall_tot
		if precision==0 and recall == 0:
			fscore = 0.0
		else:
			fscore = 2.0*(precision*recall)/(precision+recall)

		scores = {'precision':precision,'recall':recall,'f_score':fscore}
		return scores
		
