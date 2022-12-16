from Screenshot import Screenshot
from selenium import webdriver
import sys
import os
import time
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, Firefox, ActionChains
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as OptionFireFox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import requests


class Base:
	def __init__(self):
		self.time_wait = 30
		self.flag_error = False


	def choose_type_driver(self, type_driver):
		if type_driver == "chrome":
			opts_chrome = OptionsChrome()
			opts_chrome.add_argument("--start-maximized")
			opts_chrome.add_argument('--ignore-certificate-errors')
			opts_chrome.add_argument('--ignore-ssl-errors')
			opts_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])
			# opts_chrome.add_argument('--headless')  # run background
			self._driver = Chrome(options=opts_chrome,service=Service(ChromeDriverManager().install()))
			res = self._driver
			return res

		elif type_driver == "chrome_mobile":
			mobile_emulation = {"deviceName": "iPhone 12 Pro"}
			opts_chrome = OptionsChrome()
			opts_chrome.add_experimental_option("mobileEmulation", mobile_emulation)
			# opts_chrome.add_argument('--headless')
			opts_chrome.add_argument("--start-maximized")
			opts_chrome.add_argument('--ignore-ssl-errors')
			opts_chrome.add_argument('--ignore-certificate-errors')
			opts_chrome.add_argument('--ignore-ssl-errors')
			# opts_chrome.binary_location = "src/tool/static"
			opts_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])
			self._driver = Chrome(
				options=opts_chrome,
				service=Service(ChromeDriverManager().install())
			)
			res = self._driver
			return res
		else:
			opts_firefox = OptionFireFox()
			opts_firefox.headless = True
			self._driver = Firefox(options=opts_firefox)

	# self._driver.implicitly_wait(10)
	def reopen_page(self, type_driver):
		if type_driver == 'chrome':
			opts_chrome = OptionsChrome()
			opts_chrome.add_argument("--start-maximized")
			opts_chrome.add_argument('--ignore-certificate-errors')
			opts_chrome.add_argument('--ignore-ssl-errors')
			# opts_chrome.binary_location = "src/tool/static"
			opts_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])
			# opts_chrome.headless = True
			self._driver = Chrome(
				options=opts_chrome,
				service=Service(ChromeDriverManager().install())
			)
		else:
			opts_firefox = OptionFireFox()
			opts_firefox.headless = True
			self._driver = Firefox(options=opts_firefox)

	def open_page_by_incognito(self, type_driver):
		if  type_driver == 'chrome':
			opts_chrome = OptionsChrome()
			opts_chrome.add_argument("--start-maximized")
			opts_chrome.add_argument('--ignore-certificate-errors')
			opts_chrome.add_argument('--ignore-ssl-errors')
			opts_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])
			opts_chrome.add_argument("incognito")

			# opts_chrome.headless = True
			self._driver = Chrome(
				service=Service(ChromeDriverManager().install()),
				options=opts_chrome
			)
		else:
			opts_firefox = OptionFireFox()
			opts_firefox.headless = True
			self._driver = Firefox(options=opts_firefox)

	def open_page(self, url):
		try:
			self.choose_type_driver("chrome")
			self._driver.get(url)
			return True
		except:
			return

	def open_page_continue_driver(self, url):
		try:
			self._driver.get(url)
			return  True
		except:
			return

	def open_page_mb(self, url):
		try:
			self.choose_type_driver("chrome_mobile")
			self._driver.get(url)
			return True
		except:
			return False
	def parent_window_handle(self):
		return self._driver.switch_to.window(self._driver.window_handles[0])

	def browser_tab_window(self):
		return self._driver.window_handles[1]

	def screenshot(self):
		path_dir = os.path.dirname(os.path.dirname(os.getcwd()))
		path_file_image = os.path.join(path_dir, '/tool/')
		try:
			os.mkdir(path_file_image)
			print(path_file_image)
		except:
			print("muc da dc tao")
		try:
			self._driver.save_screenshot(os.path.join(path_file_image, "image.png"))
			# self.ob.full_Screenshot(os.path.join(path_file_image, "image.png"))
			ob = Screenshot.Screenshot()
			ob.full_Screenshot(self._driver, save_path = os.path.join(path_file_image),image_name= "screenshot.png")
		except:
			print("screenshot==========", traceback.format_exc())

	def switch_tab(self, element, new_tab = True):
		action = ActionChains(self._driver)
		action.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
		parent_window = self._driver.window_handles[0]
		browser_tab = self._driver.window_handles[1]
		if new_tab:
			self._driver.switch_to.window(browser_tab)
		else:
			self._driver.switch_to.window(parent_window)

	def switch_to_driver_auto_new_tab(self, idx_tab):
		browser_tab = self._driver.window_handles[idx_tab]
		self._driver.switch_to.window(browser_tab)

	def driver_switch_to(self, action, **kwargs):
		if action  == "new_tab":
			browser_tab = self._driver.window_handles[1]
			self._driver.switch_to.window(browser_tab)
		elif action == "old_tab":
			parent_window = self._driver.window_handles[0]
			self._driver.switch_to.window(parent_window)
		elif action == "frame":
			if "locator" not in kwargs:
				return False
			element = self.events_get_element(kwargs["locator"], "wait", "singular_visibility")
			if element is None:
				return element
			self._driver.switch_to.frame(element)
		else:
			self._driver.switch_to.default_content()
		return True

	def close_driver(self):
		self._driver.close()

	def quit_driver(self):
		self._driver.quit()

	def refresh_page(self):
		self._driver.refresh()

	def new_tab(self, url):
		self._driver.execute_script("window.open('{}','_blank')".format(url))

	# def events_execute_script(self, action, **kwargs):
	# 	if action == "script_open":
	# 		self._driver.execute_script("window.open('{}','_blank')".format(kwargs["url"]))
	# 	elif action == "script_click":


	def events_get_element(self, locator, action="find", _type="clickable", **kwargs):
		"""
		Get element in page
		:param action: wait/find
		wait: get element by time wait load js display element
		find: find element in page
		:param locator:
		:param _type:
		:param kwargs:
		:return:
		"""
		try:
			# print("events_get_element>>>>>>:", locator, action, _type, kwargs)
			if action == "wait":
				wait = WebDriverWait(self._driver, kwargs["time_wait"] if "time_wait" in kwargs else self.time_wait)
				# wait = WebDriverWait(self._driver, 1)
				if _type == 'plural_presence':
					element = wait.until(EC.presence_of_all_elements_located(locator))
				elif _type == 'singular_presence':
					element = wait.until(EC.presence_of_element_located(locator))
				elif _type == 'singular_invisibility':
					element = wait.until(EC.invisibility_of_element_located(locator))
				elif _type == "visibility_of":
					element = wait.until(EC.visibility_of(locator))
				elif _type == 'singular_visibility':
					element = wait.until(EC.visibility_of_element_located(locator))
				elif _type == 'any_visibility':
					element = wait.until(EC.visibility_of_any_elements_located(locator))
				elif _type == 'plural_visibility':
					element = wait.until(EC.visibility_of_all_elements_located(locator))
				else:
					element = wait.until(EC.element_to_be_clickable(locator))
			else:
				if _type == 'plural':
					element = self._driver.find_elements(locator[0], locator[1])
				else:
					element = self._driver.find_element(locator[0], locator[1])
			return element
		except:
			print('ERROR =>>>>>>> events_get_element===============', locator)
			print(traceback.format_exc())
			print('END-ERROR =>>>>>>> events_get_element===============')
			return

	def events_loading_page_expire(self, locator):
		print('------------events_loading_page_expire------------')
		flag_change = False
		while 1:
			try:
				if flag_change:
					element = self._driver.find_element(locator[0], locator[1])
				else:
					wait = WebDriverWait(self._driver, 10)
					element = wait.until(EC.visibility_of_element_located(locator))
				if element:
					flag_change = True
					time.sleep(1)
					continue
			except:
				break
		time.sleep(3)
		return True

	def events_click(self, param_element, action="default", **kwargs):
		try:
			element = kwargs["element"] if "element" in kwargs else self.events_get_element(*param_element)
			if element is None:
				return element
			if action == 'execute_script':
				self._driver.execute_script("$(arguments[0]).click();", element)
			elif action == 'switch_tab':
				self.switch_tab(element)
			else:
				element.click()
			if 'response' in kwargs:
				return element
			return True
		except:
			print("======events click======>>>>>>>>", traceback.format_exc())
			return

	# def events_send_keys(self, _script, data, action=None, response=False, **kwargs):
	def events_send_keys(self, data, param_element, action="default", **kwargs):
		try:
			element = self.events_get_element(*param_element)
			if element is None:
				return element

			if action == 'execute_script':
				self._driver.execute_script("arguments[0].setAttribute('value', '{}')".format(data), element)
			else:
				if "click" in kwargs:
					element.click()
				element.send_keys(data)
			if "response" in kwargs:
				return element
			return True
		except:
			print('====', traceback.format_exc())
			self.flag_error = True
			return

	def events_scroll(self, locator, **kwargs):
		try:
			if "element" in kwargs:
				element = kwargs["element"]
			else:
				element = self.events_get_element(locator, "wait", "singular_presence")
				if element is None:
					return element
			self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
			return True
		except:
			return

	def events_move(self, action="default", **kwargs):
		try:
			ac = ActionChains(self._driver)
			if action == 'drag_drop_js':
				self.drag_and_drop_by_js(kwargs['text_command'], conf_js=kwargs['config_js'], action=kwargs['_action'])
			else:
				for item in kwargs["locators"]:
					if "locator" in item:
						element = self.events_get_element(*item["locator"])
					elif "key" in item:
						element = item["key"]
					elif "data" in item:
						element = item["data"]
					else:
						element = ''
					run_actions = getattr(ac, item['action'])
					run_actions(element)
				ac.perform()
			return True
		except:
			print('events_move_mouse===========', traceback.format_exc())
			return

	def events_move_mouse(self, action, **kwargs):
		try:
			self.flag_error = False
			ac = ActionChains(self._driver)
			if action == 'move_element':
				element = self.events_get_element(*kwargs['_script'])
				if element is None:
					return False
				else:
					ac.move_to_element(element)
			elif action == 'drag_drop':
				source_element = self.events_get_element(kwargs['script_source'], time_wait=False)
				target_element = self.events_get_element(kwargs['script_target'], time_wait=False)
				ac.drag_and_drop(source_element, target_element)
			elif action == 'drag_drop_js':
				self.drag_and_drop_by_js(kwargs['text_command'], conf_js=kwargs['config_js'], action=kwargs['_action'])
			elif action == "hold_move":
				source_element = self.events_get_element(kwargs['script_source'], time_wait=False)
				target_element = self.events_get_element(kwargs['script_target'], time_wait=False)
				ac.click_and_hold(source_element).move_to_element(target_element).release(target_element)
			elif action == "move_click":
				source_element = self.events_get_element(*kwargs['script_source'])
				target_element = self.events_get_element(*kwargs['script_target'])
				ac.move_to_element(source_element).click(target_element)
			elif action == "move_send_keys":
				source_element = self.events_get_element(*kwargs['script_source'])
				ac.click(source_element).send_keys(kwargs["data"]).send_keys(Keys.ENTER)
			elif action == "double_click":
				element = self.events_get_element(kwargs['_script'])
				ac.double_click(element)

			elif action == "click_and_hold":
				element = self.events_get_element(kwargs['_script'])
				ac.click_and_hold(element)

			else:
				for item in kwargs['scripts']:
					element = self.events_get_element(*item['script'])
					run_actions = getattr(ac, item['action'])
					run_actions(element)
			ac.perform()
			return True
		except:
			print('events_move_mouse===========', traceback.format_exc())
			return

	def clear_operation(self, _script, steps=None):
		"""
		Xóa hành động cũ
		:param _script: Tuple
		:param steps: Tuple
		:return:
		"""
		if steps:
			element_steps = self.events_get_element(_script)
			element_steps.click()
		element = self.events_get_element(_script)
		element.click()

	def reset_data(self, action, scripts, steps=None, html=None, **kwargs):
		try:
			self.flag_error = False
			if not isinstance(scripts, list):
				scripts = [scripts]
			if action == 'action_chains':
				self.events_move_mouse(action, scripts=scripts)
				if steps:
					if steps['action'] == 'click':
						self.events_click(steps['script'])
			elif action == 'clear_by_click':
				for item in scripts:
					self.events_click(item)
					time.sleep(kwargs['time_sleep'] if 'time_sleep' in kwargs else 1)
			elif action == 'clear_operation':
				for item in scripts:
					element = self.events_get_element(item)
					element.click()
			elif action == 'clear_input':
				for item in scripts:
					element = self.events_get_element(item)
					element.send_keys(Keys.CONTROL + "a")
					element.send_keys(Keys.DELETE)
			elif action == 'clear_textarea':
				for item in scripts:
					element = self.events_get_element(item, action='clickable')
					element.click()
					element.clear()
					element.send_keys('')
			elif action == 'set_default':
				for item in scripts:
					element = self.events_get_element(item)
					element.send_keys(Keys.CONTROL + "a")
					element.send_keys('')
			elif action == 'execute_script':
				if html:
					self._driver.execute_script(html)
				else:
					for item in scripts:
						self.events_click(item, action="execute_script")
					# time.sleep(kwargs['time_sleep'] if 'time_sleep' in kwargs else 1)
			elif action == 'clear_position':
				self.events_move_mouse(**kwargs)
			else:
				pass
		except:
			self.flag_error = True
		# print('========reset_data======', traceback.format_exc())

	def check_condition_and_action(self, action, _script, **kwargs):
		try:
			element = self.events_get_element(_script, kwargs['type_script'])
			if not element:
				return
			for item in element:
				if action == 'attribute_and_click':
					val = item.get_attribute(kwargs['name_attribute']).strip()
					if val.upper() == kwargs['val_check']:
						self.events_click('', element=item)
						if 'response' in kwargs and kwargs['response']:
							return item.text
						break
			return
		except:
			print("--------check_condition_and_action---------", traceback.format_exc())
			return

	# @staticmethod
	def verify_display(self, param_element, action="default", **kwargs):
		"""
		Get value, check exists element, length element ...
		:param action: String - Loại hành động thục hiện
		:param param_element: list param, get element
		:return:
		"""
		try:
			element = self.events_get_element(*param_element)
			if element is None:
				return False

			if action == 'bool':
				res = True if element else False
			elif action == 'attribute':
				if 'name_attribute' not in kwargs and not kwargs['name_attribute']:
					return False
				if isinstance(element, list):
					res = [item.get_attribute(kwargs['name_attribute']).strip() for item in element]
				else:
					res = element.get_attribute(kwargs['name_attribute']).strip()
			elif action == 'length_element':
				res = len(element)
			else:
				res = [item.text for item in element] if isinstance(element, list) else element.text
			return res
		except:
			print('=========verify_display==========', traceback.format_exc())
			return False


	def __load_jquery(self, jquery_load_helper, jquery_url):
		"""
		:param jquery_load_helper: STRING, path file js
		:param jquery_url: STRING, url from which to import jq
		:return: None
		"""
		with open(jquery_load_helper) as f:
			load_jquery_js = f.read()
		# If JQ is already imported on the page, this wont overwrite it
		self._driver.execute_async_script(load_jquery_js, jquery_url)

	def drag_and_drop_by_js(self, txt_command, **kwargs):
		"""
		:param txt_command: STRING
		:return: None
		"""

		config_js = kwargs['conf_js']
		self.__load_jquery(config_js['JQUERY_LOAD_HELPER'], config_js['JQUERY_URL'])
		with open(config_js['DRAG_AND_DROP_HELPER']) as f:
			drag_and_drop_js = f.read()
		drag_and_drop_final = drag_and_drop_js % (kwargs['action'], txt_command)
		self._driver.execute_script(drag_and_drop_final)

	def send_msg_telegram(self,text):
		token = "5779670285:AAEvXmhNGPB4d6q9rvYgb7iGv0uhX2b9aZU"
		# chat_id = "-621570045"
		chat_id = "-864720815"
		url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
		results = requests.get(url_req)
		print(results.json())
		return results.json()

	def send_img_telegram(self):
		file = {'photo': open(os.getcwd()  + r'\screenshot.png', 'rb')}
		res = requests.post(
			'https://api.telegram.org/bot5779670285:AAEvXmhNGPB4d6q9rvYgb7iGv0uhX2b9aZU/sendPhoto?chat_id=-864720815', files = file)
		print(res.status_code)
		return res



