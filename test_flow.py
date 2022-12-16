import datetime
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from main import Base
from config import case_test

class PagesTest(Base):
	def __init__(self, config_channel):
		super().__init__()
		self.config_channel = config_channel

	def check_open_page(self):
		return self.open_page(self.config_channel['domain'])

	def check_verify_open_page(self):
		for item in self.config_channel["step"]:
			if "name_case" in item:
				if item["locator"]["type"][0] == "XPATH":
					return self.verify_display(param_element = [(By.XPATH, item["locator"]["script"]),item["locator"]["type_get_element"]["type"],
											   item["locator"]["type_get_element"]["action"]],
											  action= item["locator"]["action"])

	def check_time_most_read_posts(self):
		for item in self.config_channel["step"]:
			if "locator_most_read_post" in item:
				if item["locator_most_read_post"]["type"][0] == "XPATH" :
					element_time = self.verify_display(param_element=[(By.XPATH,item["locator_most_read_post"]["script"]),item["locator_most_read_post"]["type_get_element"]["type"],
																	  item["locator_most_read_post"]["type_get_element"]["action"]],
													   action= item["locator_most_read_post"]["action"],
													   name_attribute = item["locator_most_read_post"]["name_attribute"])
					idx = 0
					time_now = datetime.datetime.now()
					time_satisfy = time_now - datetime.timedelta(days=2)
					print("=======time_satisfy===========", time_satisfy)
					for text_attribute in element_time[:5]:
						# text_time = text_attribute.split(" ")
						print("=======================text_attribute", text_attribute)
						time_check = datetime.datetime.strptime(text_attribute, "%d/%m/%Y %H:%M")
						idx += 1
						if time_satisfy < time_check:
							if idx == 5:
								print("-------thỏa mãn-----------")
								return True
							else:
								continue
						else:
							print("---------khong thoa mãn-----------")
							return False

	def click_on_post(self):
		"""
		thức hiện click vào bài viết đầu trang test comment
		:return:
		"""
		for item in self.config_channel["step"]:
			if "locator_on_post" in item:
				if item["locator_on_post"]["type"][0] == "XPATH":
					res = self.events_click(param_element= [(By.XPATH,item["locator_on_post"]["script"]),item["locator_on_post"]["type_get_element"]["type"]])
					return res

	def verify_box_cmt(self):
		for item in self.config_channel["step"]:
			if "locator_box_comment" in item:
				if item["locator_box_comment"]["type"][0] == "XPATH":
					element = self.events_get_element(locator=(By.XPATH, item["locator_box_comment"]["script"]),
					                                  action=item["locator_box_comment"]["type_get_element"]["type"],
					                                 )
					if element is None:
						return True
					else:
						return self.verify_display(param_element = [(By.XPATH, item["locator_box_comment"]["script"]),item["locator_box_comment"]["type_get_element"]["type"],
													   item["locator_box_comment"]["type_get_element"]["action"]],
													  action= item["locator_box_comment"]["action"])

	# check nục tìm kiếm bài trên trang
	def get_text_on_post(self):
		global text_zone, text_check
		for item in self.config_channel["step"]:
			if "locator_get_text" in item:
				if item["locator_get_text"]["type"][0] == "XPATH":
					element_check_text = self.events_get_element(locator = (By.XPATH, item["locator_get_text"]["script"]),
																 action= item["locator_get_text"]["type_get_element"]["type"],
																 _type=  item["locator_get_text"]["type_get_element"]["action"])

					if element_check_text is None:
						return False
					else:
						text_check = element_check_text.text
						list_text = text_check.split(" ")
						print("======text_check=======", text_check)
						text_zone = " ".join(list_text[:5])
						print("=======text_zone=======", text_zone)
						if text_zone is None:
							return False
						else:
							return True

	def input_text_check_find(self):
		for item in self.config_channel["step"]:
			if "locator_input_text" in item:
				if item["locator_input_text"]["type"][0] == "XPATH":
					res = self.events_send_keys(
						data=text_zone,
						param_element= [(By.XPATH,item["locator_input_text"]["script"]),item["locator_input_text"]["type_get_element"]["type"]]
					)
					time.sleep(1)
					return res

	def click_search_button(self):
		for item in self.config_channel["step"]:
			if "locator_search_button" in item:
				if item["locator_search_button"]["type"][0] == "XPATH":
					return self.events_click(param_element= [(By.XPATH,item["locator_search_button"]["script"]),
					                                         item["locator_search_button"]["type_get_element"]["type"]], action= "execute_script")

	def enter_find_text(self):
		for item in self.config_channel["step"]:
			if "locator_enter_find" in item:
				if item["locator_enter_find"]["type"][0] == "XPATH":
					return self.events_send_keys(Keys.ENTER,param_element= [(By.XPATH,item["locator_enter_find"]["script"])])

	def check_verify_post_find(self):
		for item in self.config_channel["step"]:
			if "locator_post_search" in item:
				if item["locator_post_search"]["type"][0] == "XPATH":
					element_zone = self.events_get_element(locator = (By.XPATH, item["locator_post_search"]["script"]),
																 action= item["locator_post_search"]["type_get_element"]["type"],
																 _type=  item["locator_post_search"]["type_get_element"]["action"])

					text_check_post = ''.join(char for char in text_check[:10] if char.isalnum())
					if element_zone is None:
						return False
					else:
						for post in element_zone:
							text_post = post.text
							text_post_compare = ''.join(char for char in text_post[:10] if char.isalnum())
							if text_check_post in text_post_compare:
								print("==============text_check_post", text_check_post)
								print("=============text_post_compare", text_post_compare)
								return True
							else:
								continue
						return False

	def open_link_check_video(self):
		for item in self.config_channel["step"]:
			if "link_check_video" in item:
				return self.open_page_continue_driver(item["link_check_video"])

	def click_find_button(self):
		for item in self.config_channel["step"]:
			if "locator_find_button" in item:
				if item["locator_find_button"]["type"][0] == "XPATH":
					return self.events_click(param_element=[(By.XPATH, item["locator_find_button"]["script"]),
					                                        item["locator_find_button"]["type_get_element"]["type"]])

	def move_mouse_check_play(self):
		for item in self.config_channel["step"]:
			if "locator_move_mouse" in item:
					for i in item["locator_move_mouse"]["script"]:
						if item["locator_move_mouse"]["type"][0] == "XPATH":
							res = self.events_move_mouse(item["locator_move_mouse"]["type_action"],
							                       _script=[(By.XPATH,i),item["locator_move_mouse"]["type_get_element"]["type"], item["locator_move_mouse"]["type_get_element"]["action"]])
							time.sleep(2)
							print("res==========", res)
							if res is None:
								return False
							else:
								continue
					return res

	def check_time_play_video(self):
		for item in self.config_channel["step"]:
			if "locator_start_video" in item:
				if item["locator_start_video"]["type"][0] == "XPATH":
					element_zone = self.events_get_element(locator = (By.XPATH, item["locator_start_video"]["script"]),
																	 action= item["locator_start_video"]["type_get_element"]["type"],
																	 _type=  item["locator_start_video"]["type_get_element"]["action"])
					if element_zone is None:
						return False
					else:
						text_element_zone = element_zone.text
						if text_element_zone is None:
							return False
						text_time_run_video = text_element_zone.split("\n")
						if len(text_time_run_video) == 2:
							print("=====text_time_run_video=======", text_time_run_video[1])
							if text_time_run_video[1] == "0:00":
								return False
							if text_time_run_video[1] is None:
								return False
							else:
								return True
						else:
							print("================text_time_video", text_element_zone)
							if text_element_zone == "0:00":
								return False
							if text_element_zone == "":
								return False
							else:
								return True

	# check ảnh load nhanh không lỗi
	def open_link_check_image(self):
		for item in self.config_channel["step"]:
			if "link_check_image" in item:
				return self.open_page_continue_driver(item["link_check_image"])

	def check_verify_image(self):
		for item in self.config_channel["step"]:
			if "locator_verify_image" in item:
				if item["locator_verify_image"]["type"][0] == "XPATH":
					res = self.verify_display(param_element = [(By.XPATH, item["locator_verify_image"]["script"]),item["locator_verify_image"]["type_get_element"]["type"],
												   item["locator_verify_image"]["type_get_element"]["action"]],
												  action= item["locator_verify_image"]["action"])
					return res

	# check truy cập bằng mobile
	def check_open_page_mobile(self):
		for item in self.config_channel["step"]:
			if "link_open_page_mobile" in item:
				return self.open_page_mb(item["link_open_page_mobile"])

	def check_verify_open_page_mobile(self):
		for item in self.config_channel["step"]:
			if "locator_verify_page_mobile" in item:
				if item["locator_verify_page_mobile"]["type"][0] == "XPATH":
					return self.verify_display(param_element = [(By.XPATH, item["locator_verify_page_mobile"]["script"]),item["locator_verify_page_mobile"]["type_get_element"]["type"],
												   item["locator_verify_page_mobile"]["type_get_element"]["action"]],
												  action= item["locator_verify_page_mobile"]["action"])

	# check video trên mobile
	def open_link_check_video_mobile(self):
		for item in self.config_channel["step"]:
			if "link_check_video_mobile" in item:
				return self.open_page_continue_driver(item["link_check_video_mobile"])

	def click_icon_pause_video_mobile(self):
		time.sleep(2)
		for item in self.config_channel["step"]:
			if "locator_click_pause_video_mobile" in item:
				if item["locator_click_pause_video_mobile"]["type"][0] == "XPATH":
					return self.events_click(param_element=[(By.XPATH, item["locator_click_pause_video_mobile"]["script"]),
					                                        item["locator_click_pause_video_mobile"]["type_get_element"]["type"]])
				else:
					return self.events_click(
						param_element=[(By.CSS_SELECTOR, item["locator_click_pause_video_mobile"]["script"]),
						               item["locator_click_pause_video_mobile"]["type_get_element"]["type"]])

	def click_play_video_mobile(self):
		for item in self.config_channel["step"]:
			if "locator_click_video_mobile" in item:
				if item["locator_click_video_mobile"]["type"][0] == "XPATH":
					res = self.events_click(param_element= [(By.XPATH,item["locator_click_video_mobile"]["script"]),item["locator_click_video_mobile"]["type_get_element"]["type"]])
					if res is None:
						return False
					return res

	def click_pass_advertisement_video(self):
		for item in self.config_channel["step"]:
			if "locator_pass_advertisement" in item:
				if item["locator_pass_advertisement"]["type"][0] == "XPATH":
					element = self.events_get_element(locator=(By.XPATH, item["locator_pass_advertisement"]["script"]),
					                                  action=item["locator_pass_advertisement"]["type_get_element"]["type"],
					                                  kwarg={"time_wait": 5})
					if element is None:
						print("not button advertisement")
						return self.events_click(param_element= [(By.XPATH,item["locator_pass_advertisement"]["script"]),item["locator_pass_advertisement"]["type_get_element"]["type"]])
					else:
						time.sleep(4)
						res=  self.events_click(param_element= [(By.XPATH,item["locator_pass_advertisement"]["script"]),item["locator_pass_advertisement"]["type_get_element"]["type"]])
						time.sleep(1)
						return res
	def move_mouse_check_play_mobile(self):
		for item in self.config_channel["step"]:
			if "locator_move_mouse_mobile" in item:
				for i in item["locator_move_mouse_mobile"]["script"]:
					if item["locator_move_mouse_mobile"]["type"][0] == "XPATH":
						try:
							self.events_move_mouse(item["locator_move_mouse_mobile"]["type_action"],
							                       _script=[(By.XPATH, i),
							                                item["locator_move_mouse_mobile"]["type_get_element"]["type"],
							                                item["locator_move_mouse_mobile"]["type_get_element"]["action"]])
							time.sleep(2)
						except:
							return False
				return True

	def check_time_play_video_mobile(self):
		time.sleep(2)
		for item in self.config_channel["step"]:
			if "locator_start_video_mobile" in item:
				if item["locator_start_video_mobile"]["type"][0] == "XPATH":
					element_zone = self.events_get_element(locator = (By.XPATH, item["locator_start_video_mobile"]["script"]),
																		 action= item["locator_start_video_mobile"]["type_get_element"]["type"],
																		 _type=  item["locator_start_video_mobile"]["type_get_element"]["action"])
					if element_zone is None:
						return False
					else:
						text_element_zone = element_zone.text
						text_time_run_video = text_element_zone.split("\n")
						if len(text_time_run_video) == 2:
							print("=====text_time_run_video=======", text_time_run_video[1])
							if text_time_run_video[1] == "0:00":
								print("text_time_run_video[1]==", text_time_run_video[1])
								return False

							if "0" not in text_time_run_video[1]:
								return False
							else:
								return True
						else:
							print("================text_time_video", text_element_zone)
							if text_element_zone == "0:00":
								return False
							elif text_element_zone is None:
								return False
							else:
								return True

	def open_link_check_image_mobile(self):
		for item in self.config_channel["step"]:
			if "link_check_image_mobile" in item:
				return self.open_page_continue_driver(item["link_check_image_mobile"])

	def verify_display_image_mobile(self):
		for item in self.config_channel["step"]:
			if "locator_verify_image_mobile" in item:
				if item["locator_verify_image_mobile"]["type"][0] == "XPATH":
					res = self.verify_display(param_element=[(By.XPATH, item["locator_verify_image_mobile"]["script"]),
					                                         item["locator_verify_image_mobile"]["type_get_element"]["type"],
					                                         item["locator_verify_image_mobile"]["type_get_element"][
						                                         "action"]],
					                          action=item["locator_verify_image_mobile"]["action"])
					return res

# check bài đặc biệt cho page to quoc
	def open_link_post_special(self):
		for item in self.config_channel["step"]:
			if "link_post_special" in item:
				return self.open_page_continue_driver(item["link_post_special"])

	def verify_time_line_post_special(self):
		for item in self.config_channel["step"]:
			if "loacator_special" in item:
				if item["loacator_special"]["type"][0] == "XPATH":
					return self.verify_display(param_element = [(By.XPATH, item["loacator_special"]["script"]),item["loacator_special"]["type_get_element"]["type"],
													   item["loacator_special"]["type_get_element"]["action"]],
													  action= item["loacator_special"]["action"])

	def check_time_load_page(self):
		self.refresh_page()
		return self.verify_time_line_post_special()

	def load_verify_time_line(self):
		for i in range(9):
			self.refresh_page()
			time.sleep(2)
			self.verify_time_line_post_special()
			if self.verify_time_line_post_special == False:
				return False
		return True
# check hoạt động của tag
	def click_tag_post(self):
		for item in self.config_channel["step"]:
			if "locator_tag_post" in item:
				if item["locator_tag_post"]["type"][0] == "XPATH":
					element = self.events_get_element(locator = (By.XPATH, item["locator_tag_post"]["script"]),
																	 action= item["locator_tag_post"]["type_get_element"]["type"], kwarg= {"time_wait": 4})
					if element is not None:
						return self.events_click(param_element= [(By.XPATH,item["locator_tag_post"]["script"]),item["locator_tag_post"]["type_get_element"]["type"]])
					else:
						print('not tag post')
						return True

	def verify_tag_post(self):
		for item in self.config_channel["step"]:
			if "locator_verify_tag" in item:
				print("=======text_check=======", text_check)
				text_check_post = ''.join(char for char in text_check[:10] if char.isalnum())
				if item["locator_verify_tag"]["type"][0] == "XPATH":
					element_list_post = self.events_get_element(locator = (By.XPATH, item["locator_verify_tag"]["script"]),
																	 action= item["locator_verify_tag"]["type_get_element"]["type"],
																	 _type=  item["locator_verify_tag"]["type_get_element"]["action"],
						                                            kwarg= {"time_wait": 4})
					if element_list_post is None:
						print("post not tag element")
						return True
					i = 0
					for post in element_list_post:
						i += 1
						text_post = post.text
						text_post_compare = ''.join(char for char in text_post[:10] if char.isalnum())
						if text_check_post in text_post_compare:
							return True
						else:
							print("======text_list_post=======", text_post)
							if i == 6:
								return False
						# continue

	def open_link_check_search(self):
		for item in self.config_channel["step"]:
			if "link_check_search" in item:
				return self.open_page_continue_driver(item["link_check_search"])







