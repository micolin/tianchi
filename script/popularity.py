#coding=utf8
import sys,os
import json
import logging
from collections import *
from databuilder import *

def popularity():
	r_days = 10
	user_view,user_collection,user_basket,user_purchase=get_resent_actions('2014-12-18',r_days)
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

	for uid,items in user_collection.items():
		for item,cnt in items.items():
			try:
				user_itemRate[uid][item] += cnt*collection_rate
			except:
				user_itemRate[uid][item] = cnt*collection_rate
	
	for uid,items in user_basket.items():
		for item,cnt in items.items():
			try:
				user_itemRate[uid][item] += cnt*basket_rate
			except:
				user_itemRate[uid][item] = cnt*basket_rate
	
	user_buy_cnt = defaultdict(int)
	for uid,items in user_purchase.items():
		user_buy_cnt[uid] += len(items.keys())
		for item,cnt in items.items():
			try:
				user_itemRate[uid][item] += cnt*purchase_rate
			except:
				user_itemRate[uid][item] = cnt*purchase_rate

	for uid,items in user_itemRate.items():
		sort_items = sorted(items.items(),key=lambda x:x[1],reverse=True)
		rec_num = user_buy_cnt[uid]/r_days
		if rec_num == 0:
			rec_num = 2

		rec_items = [item[0] for item in sort_items[:rec_num]]
		print "%s\t%s"%(uid,','.join(rec_items))
	return user_itemRate

if __name__=="__main__":
	logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(funcName)s %(lineno)d %(message)s')
	popularity()
