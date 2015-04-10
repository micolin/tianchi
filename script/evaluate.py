#coding = utf8
import sys,os
import json
from databuilder import get_test_data
from collections import *

class Evaluator(object):
	def __init__(self,rec_result,test_result):
		self.rec_result = rec_result
		self.test_result = test_result
	
	def score(self):
		hit = 0
		predict_tot = 0
		recall_tot = 0
		for uid, predict_items in self.rec_result.iteritems():
			test_items = self.test_result[uid]
			hit += len(set(predict_items) & set(test_items))
			predict_tot += len(predict_items)
			recall_tot += len(test_items)
		
		precision = float(hit)/predict_tot
		recall = float(hit)/recall_tot
		if precision==0 and recall == 0:
			fscore = 0.0
		else:
			fscore = 2.0*(precision*recall)/(precision+recall)

		scores = {'precision':precision,'recall':recall,'f_score':fscore}
		return scores

def evaluate(prefile,test_date):
	rec_result = defaultdict(list)
	with open(prefile,'rb') as fin:
		for line in fin.readlines():
			line = line.strip().split('\t')
			uid = line[0]
			pre_items = line[1].split(',')
			rec_result[uid]=pre_items

	test_data = get_test_data(test_date)
	evaluator = Evaluator(rec_result,test_data)
	print evaluator.score()

if __name__=='__main__':
	evaluate('../rec_result/tianchi_mobile_recommendation_predict','2014-12-18')
			
