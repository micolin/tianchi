#coding=utf8
import sys,os
import json
import logging
from collections import *
from databuilder import *

def popularity():
	user_view,user_collection,user_basket,user_purchase=get_resent_actions('2014-12-18',10)
	user_itemRate = defaultdict(dict)
	view_rate = 0.2
	collection_rate = 0.5
	basket_rate = 0.8
	purchase_rate = 1.0
	for uid,items in user_view.items():
		for item,cnt in items.items():
			try:
				user_itemRate[uid][item] += cnt*view_rate
			except:
				user_itemRate[uid][item] = cnt*view_rate
		break
	print user_itemRate
	return user_itemRate


if __name__=="__main__":
	logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(funcName)s %(lineno)d %(message)s')
	popularity()
