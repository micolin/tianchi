#coding=utf8
import sys,os
from collections import *
import logging

def seperateDataWithDate(data_file):
	dates_record = defaultdict(list)
	with open(data_file,'rb') as fin:
		skip = fin.readline()
		for line in fin.readlines():
			nline = line.strip().split(',')
			time = nline[5]
			date = time.split()[0]
			dates_record[date].append(line)
	
	for date,records in dates_record.items():
		outputfile = '../mid_data/userData_%s'%(date)
		with open(outputfile,'wb') as fin:
			for record in records:
				fin.write(record)

def get_train_data(date,days):
	'''
	@func:Used for get train data
	@params[in] date: 开始日期, format:'2015-11-14'
	@params[in] days: 向前推算的天数
	@return[out] user_item: dict, {uid:{item:cnt}}
	'''
	user_item = defaultdict(dict)
	for i in range(1,days+1):
		_day = int(date.split('-')[-1])-i
		if _day <= 0:
			_day = 30 + _day
			_date = '2014-11-%s'%(_day)
		else:
			if _day<10:
				_date = '2014-12-0%s'%(_day)
			else:
				_date = '2014-12-%s'%(_day)
		filepath = '../mid_data/userData_%s'%(_date)
		logging.info('Get train data from file:%s'%(filepath))
		with open(filepath,'rb') as fin:
			for line in fin.readlines():
				line = line.strip().split(',')
				uid = line[0]
				itemid = line[1]
				action_type = line[2]
				geo = line[3]
				item_cate = line[4]
				_time = line[5].split()
				_date = _time[0]
				_time = _time[1]

				#Add select options here
				if action_type == '4':
					try:
						user_item[uid][itemid]+=1
					except:
						user_item[uid][itemid]=1
				
	return user_item

def get_train_data_in_rate(date,days):
	'''
	@func:Used for get train data
	@params[in] date: 开始日期, format:'2015-11-14'
	@params[in] days: 向前推算的天数
	@return[out] user_item: dict, {uid:{item:rate}}
	'''
	pass

def get_resent_actions(date,days):
	user_view = defaultdict(dict)
	user_collection = defaultdict(dict)
	user_basket = defaultdict(dict)
	user_purchase = defaultdict(dict)
	actions = [user_view,user_collection,user_basket,user_purchase]
	for i in range(1,days+1):
		_day = int(date.split('-')[-1])-i
		if _day <= 0:
			_day = 30 + _day
			_date = '2014-11-%s'%(_day)
		else:
			if _day<10:
				_date = '2014-12-0%s'%(_day)
			else:	
				_date = '2014-12-%s'%(_day)
		filepath = '../mid_data/userData_%s'%(_date)
		logging.info('Get resent actions from file:%s'%(filepath))
		with open(filepath,'rb') as fin:
			for line in fin.readlines():
				line = line.strip().split(',')
				uid = line[0]
				itemid = line[1]
				action_type = line[2]
				try:
					actions[int(action_type)-1][uid][itemid]+=1
				except:
					actions[int(action_type)-1][uid][itemid]=1
	return user_view,user_collection,user_basket,user_purchase

def get_test_data(date):
	user_item = defaultdict(list)
	filepath = '../mid_data/userData_%s'%(date)
	logging.info('Get test data from file:%s'%(filepath))
	with open(filepath,'rb') as fin:
		for line in fin.readlines():
			line = line.strip().split(',')
			uid = line[0]
			itemid = line[1]
			action_type = line[2]
			if action_type == '4':
				user_item[uid].append(itemid)
	return user_item

def test():
	#get_resent_actions('2014-12-01',2)
	get_train_data('2014-12-18',2)
	get_test_data('2014-12-18')

if __name__=="__main__":
	logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(funcName)s %(lineno)d %(message)s')
	args = sys.argv
	test()
	#seperateDataWithDate('../data/tianchi_mobile_recommend_train_user.csv')
