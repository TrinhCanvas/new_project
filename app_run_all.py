import json
import os
import time
import  installer_requiments
from test_spec import Process_test


if __name__ == '__main__':
	try:
		data_json = open("data.json")
		installer_requiments.installer()
		file_data = json.load(data_json)
		data_json.close()
		list_time = []
		# lastmodified = os.stat(r'C:\Users\DELL\Desktop\new_project\test_pages\data.json').st_mtime
		# list_time.append(lastmodified)
		# counter = 0
		k=0
		for key, val in file_data.items():
				# if file_data[key]["status"] in file_data. items:
				# 	if file_data[key]["status"] == False:
				# 		continue
				# if counter % (val['scan']*60) == 0:
			Process_test(file_data[key]).run_by_page()
			if k == 0:
				Process_test(file_data[key]).create_result()
			else:
				Process_test(file_data[key]).add_result(key)
			k += 1
			# counter += 1
			# time.sleep(1)
			# if counter > 10000:
			# 	counter = 0
			#
			# lastmodified_check = os.stat(r'/test_pages/data.json').st_mtime
			# if lastmodified_check in list_time:
			# 	continue
			# else:
			# 	data_json = open("data.json")
			# 	file_data = json.load(data_json)
			# 	data_json.close()
			# 	print("đã load lại")
			# 	list_time.clear()
			# 	list_time.append(lastmodified_check)

	except Exception as e:
		print(e)
		time.sleep(10)

