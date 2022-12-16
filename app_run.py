import json
import os
import time
# from datetime import datetime
from config import case_test
from test_spec import Process_test

import installer_requiments

if __name__ == '__main__':
	# try:
	print("==========toquoc========")
	installer_requiments.installer()
	data_json = open("data.json")
	file_data = json.load(data_json)
	data_json.close()
	list_time = []
	lastmodified = os.stat(r'data.json').st_mtime
	idx_page = 0
	list_time.append(lastmodified)

	with open('config.json', 'r') as f:
		domain = json.load(f)['domain']
		k = 0
		for idx in domain:
			print("idx", idx)
	# 	print(domain)
	# while True:
	# if file_data[domain] == False:
			Process_test(file_data[idx]).run_by_page()
			if k == 0:
				Process_test(file_data[idx]).create_result()
			else:
				Process_test(file_data[idx]).add_result(idx)
			k += 1
			# time.sleep(file_data[domain]["scan"])
			# lastmodified_check = os.stat(r'C:\Users\DELL\Desktop\new_project\test_pages\data.json').st_mtime
			# if lastmodified_check in list_time:
			# 	pass
			# else:
			# 	data_json = open("data.json")
			# 	file_data = json.load(data_json)
			# 	data_json.close()
			# 	print("đã load lại")
			# 	list_time.clear()
			# 	list_time.append(lastmodified_check)
	# except Exception as e:
	# 	print(e)
		# time.sleep(10)

	# Process_test(case_test["vtv"]).run_by_page()

	# for item in case_test:
	# 	Process_test(case_test[item]).run_by_page()

