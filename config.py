import os
from datetime import datetime
import json

case_test = {
		"toquoc": {
			"name_page": "toquoc",
			"domain": "https://toquoc.vn/",
			"name_case": "check page toquoc.vn",
			"scan": 10,
			"step": [
				{
					"name_func": "check_open_page",
					"name_time": "start_time_1",
				},
				{
					"name_func": "check_verify_open_page",
					"name_case": "verify display in pc",
					"locator": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@id='container']",
							"type_get_element": {
												"type": "wait",
												"action": "singular_visibility"
												},
							"action": "bool",
							},

					"name_time": "end_time_1",
					"time_check": 5,
				},
				{
					"name_func": "check_time_most_read_posts",
					"name_case": "check the display of the most read posts",
					"locator_most_read_post": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@class='time need-get-timeago']",
							"type_get_element": {
												"type": "wait",
												"action": "plural_visibility"
												},
							"action": "attribute",
							"name_attribute": "title"
							},
				},
				{
					"name_func": "click_on_post",
					"locator_on_post": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@id='container']/div[9]/div/div[1]/div[2]/div[1]/h3/a",
							"type_get_element": {"type": "wait"},
					"name_time": "start_time_2"},
				},

				{
					"name_func": "verify_box_cmt",
					"name_case": "verify box comment",
					"locator_box_comment": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@id='comments']",
							"type_get_element": {
								"type": "wait",
								"action": "singular_visibility"
							},
							"action": "bool",
							},

					"name_time": "end_time_2",
					"time_check": 5,
				},
				{
					"name_func": "get_text_on_post",
					"name_case": "get text post check search",
					"locator_get_text": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@class='entry-title']",
							"type_get_element": {
								"type": "wait",
								"action": "singular_presence"
							},
							},
				},
				{
					"name_func": "click_search_button",
					"name_case": "click button search",
					"locator_search_button": {
							"type": ["XPATH", "SELECTOR"],
							"script": "//*[@class='sup-menu']/li[16]/a/i",
							"type_get_element": {"type": "wait"},
							},
				},

				{
					"name_func": "input_text_check_find",
					"name_case": "input text find",
					"locator_input_text": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@class='sup-menu']/li[16]/input",
							"type_get_element": {
								"type": "wait",
								"action": "singular_visibility"
							}
							},
				},
				{
					"name_func": "enter_find_text",
					"name_case": "enter find text",
					"locator_enter_find": {
						"type": ["XPATH", "SELECTOR"],
						"script": "//*[@class='sup-menu']/li[16]/input",
						"type_get_element": {"type": "wait"},
					},
				},
				{
					"name_func": "check_verify_post_find",
					"name_case": "verify post find",
					"locator_post_search": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@class='qitem']",
							"type_get_element": {
								"type": "wait",
								"action": "plural_presence"
							},
							},

				},
				{
					"name_func": "open_link_check_video",
					"name_case": "open link check video",
					"link_check_video": "http://ttvn.toquoc.vn/videos.htm",
					"name_time": "start_time_3",
				},

				{
					"name_func": "move_mouse_check_play",
					"name_case": "move_mouse_check_play",
					"locator_move_mouse": {
							"type": ["XPATH", "SELECTOR"],
							"script" : ["//*[@class='ToQuocPlayer-area-control']/div/div[3]","//*[@class='ToQuocPlayer-area-control']/div/div[4]"],
							"type_action": "move_element",
							"type_get_element": {
								"type": "wait",
								"action": "singular_presence"
							},
							},
				},

				{
					"name_func": "check_time_play_video",
					"name_case": "verify time play video",
					"locator_start_video": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
							"type_get_element": {
								"type": "wait",
								"action": "singular_presence"
							},
							},
					"name_time": "end_time_4",
					"time_check": 5,
				},
				{
					"name_func": "open_link_check_image",
					"name_case": "open link post check image",
					"link_check_image": "https://toquoc.vn/nhung-hinh-anh-an-tuong-trong-le-khai-giang-truc-tiep-nam-hoc-moi-2022-2023-sau-dai-dich-covid-19-20220905115404895.htm",
					"name_time": "start_time_4",
				},
				{
					"name_func": "check_verify_image",
					"name_case": "verify image in mobile",
					"locator_verify_image": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@class='entry-body']/figure[1]/div/a/img",
							"type_get_element": {
												"type": "wait",
												"action": "singular_visibility"
												},
							"action": "bool"
							},

					"name_time": "end_time_4",
					"time_check": 3,
				},
				{
					"name_func": "check_open_page_mobile",
					"name_case": "check open page in mobile",
					"link_open_page_mobile": "https://toquoc.vn/",
					"name_time": "start_time_1",
					'mobile': True,
				},
				{
					"name_func": "check_verify_open_page_mobile",
					"name_case": "verify open page in mobile",
					"locator_verify_page_mobile": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@id='container']",
							"type_get_element": {
												"type": "wait",
												"action": "singular_visibility"
												},
					"action": "bool"
							},
					"name_time": "end_time_1",
					"time_check": 5,
					'mobile': True,
				},
				{
					"name_func": "open_link_check_video_mobile",
					"name_case": "open link video in mobile",
					"link_check_video_mobile": "http://ttvn.toquoc.vn/video/xe-buyt-chu-dong-chan-gio-cho-nguoi-di-xe-buyt-tren-cau-vinh-tuy-trong-con-mua-lon-hoi-dau-thang-7-video-hoang-quan-99252587.htm",
					"name_time": "start_time_1",
					'mobile': True,
				},
				{
					"name_func": "click_play_video_mobile",
					"name_case": "click play video",
					"locator_click_video_mobile": {
											"type": ["XPATH", "SELECTOR"],
											"script": "//*[@id='context-stats']/div[3]/div[2]/div",
											"type_get_element": {"type": "wait"},
											},
					'mobile': True,
				},
				{
					"name_func": "check_time_play_video_mobile",
					"name_case":"check action video in mobile",
					"locator_start_video_mobile": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
							"type_get_element": {
								"type": "wait",
								"action": "singular_presence"
							},
							},
					'mobile': True,
					"name_time": "end_time_4",
					"time_check": 5,
				},
				{
					"name_func": "open_link_check_image_mobile",
					"name_case": "open link image in mobile",
					"link_check_image_mobile": "https://toquoc.vn/nhung-hinh-anh-an-tuong-trong-le-khai-giang-truc-tiep-nam-hoc-moi-2022-2023-sau-dai-dich-covid-19-20220905115404895.htm",
					"name_time": "start_time_1",
					'mobile': True,
				},
				{
					"name_func": "verify_display_image_mobile",
					"name_case": "verify image in mobile",
					"locator_verify_image_mobile":{
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@id='img_491101523500568576']",
							"type_get_element": {
												"type": "wait",
												"action": "singular_visibility"
												},
							"action": "bool"
							},
					"name_time": "end_time_1",
					"time_check": 5,
					'mobile': True,
				},

			]
		},

		"kenh14": {
				"name_page": "kenh14",
				"domain": "https://kenh14.vn/",
				"name_case": "check page kenh14.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='admWrapsite']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='bindRegionNews']/div[1]/div[1]",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},

					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class = 'kbwc-title']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "click_tag_post",
						"name_case": "th???c hi???n click v??o b??i vi???t",
						"locator_tag_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='knt-list']/li",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "verify_tag_post",
						"name_case": "check tag b??i vi???t ???? hi???n th??? b??i ????ng ch??a",
						"locator_verify_tag": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='knswli need-get-value-facebook clearfix']",
								"type_get_element": {
													"type": "wait",
													"action": "plural_presence"
													},
								"action": "bool",
								},

					},
					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='searchinput']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "enter_find_text",
						"name_case": "enter find text",
						"locator_enter_find": {
							"type": ["XPATH", "SELECTOR"],
							"script": "//*[@id='searchinput']",
							"type_get_element": {"type": "wait"},
						},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='knsw-list']/li[1]/div[2]/h3/a",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},

					},
					{
						"name_func": "open_link_check_video",
						"name_case": "open link check video",
						"link_check_video": "https://video.kenh14.vn/",
						"name_time": "start_time_3",
					},

					{
						"name_func": "move_mouse_check_play",
						"name_case": "move_mouse_check_play",
						"locator_move_mouse": {
								"type": ["XPATH", "SELECTOR"],
								"script" : ["//*[@id='admWrapsite']/div[1]/div[2]/div/div[1]","//*[@id='admWrapsite']/div[1]/div[2]/div/div[1]/div"],
								"type_action": "move_element",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "check_time_play_video",
						"name_case": "verify time play video",
						"locator_start_video": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://kenh14.vn/song-gio-cua-jennie-kim-20220907225510007.chn",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='img_492144292705054720']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},

				{
					"name_func": "open_link_post_special",
					"name_case": "Truy c???p link b??i ?????c bi???t",
					"link_post_special": "https://kenh14.vn/truc-tiep-u19-indonesia-vs-u19-viet-nam-thuoc-thu-lieu-cao-o-tran-ra-quan-20220702194305016.chn",
				},
				{
					"name_func": "verify_time_line_post_special",
					"name_case": "check hi???n th??? th???i gian trong b??i ?????c bi???t",
					"loacator_special": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='entry-info']/div[1]",
								"type_get_element": {
													"type": "wait",
													"action": "plural_visibility"
													},
								"action": "bool"
								},

					"name_time": "start_time_1",
				},

				{
					"name_func": "check_time_load_page",
					"name_case": "ki???m tra th???i gian load_pgae",
					"name_time": "end_time_4",
					"time_check": 5,
				},

				{
					"name_func": "load_verify_time_line",
					"name_case": "ki???m tra load page 10 l???n",
				},

					{
						"name_func": "check_open_page_mobile",
						"name_case": "check open page in mobile",
						"link_open_page_mobile": "https://kenh14.vn/",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "check_verify_open_page_mobile",
						"name_case": "verify open page in mobile",
						"locator_verify_page_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='admwrapper']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
						"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

					{
						"name_func": "open_link_check_image_mobile",
						"name_case": "open link image in mobile",
						"link_check_image_mobile": "https://kenh14.vn/song-gio-cua-jennie-kim-20220907225510007.chn",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "verify_display_image_mobile",
						"name_case": "verify image in mobile",
						"locator_verify_image_mobile":{
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='img_492144292705054720']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

				]
			},

		"cafef": {
				"name_page": "cafef",
				"domain": "https://cafef.vn/",
				"name_case": "check page cafef.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='streamItem']/div[1]",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='top_noibat_row2 mgt20']/ul/li[1]/h2/a",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},

					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='left_cate totalcontentdetail']/h1",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},
					{
						"name_func": "open_link_check_search",
						"name_case": "open link check button search",
						"link_check_search": "https://cafef.vn/search/doanh-nghiep-o-at-mua-lai-trai-phieu-truoc-han.chn",
						"name_time": "start_time_3",
					},

					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='txtKeyword']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "click_search_button",
						"name_case": "click button search",
						"locator_search_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@class='btSearch']",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='titlehidden']",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},

					},
					{
						"name_func": "open_link_check_video",
						"name_case": "open link check video",
						"link_check_video": "https://cafef.vn/videos.chn",
						"name_time": "start_time_3",
					},

					{
						"name_func": "move_mouse_check_play",
						"name_case": "move_mouse_check_play",
						"locator_move_mouse": {
								"type": ["XPATH", "SELECTOR"],
								"script" : ["//*[@id='video-embeb']","//*[@id='video-embeb']/div"],
								"type_action": "move_element",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "check_time_play_video",
						"name_case": "verify time play video",
						"locator_start_video": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='current-time-display']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://cafef.vn/chung-khoan-viet-nam-thuong-bien-dong-ra-sao-sau-nhung-lan-dow-jones-lao-doc-20220914043608923.chn",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='media']/img",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},

					{
						"name_func": "open_link_post_special",
						"name_case": "Truy c???p link b??i ?????c bi???t",
						"link_post_special": "https://cafef.vn//chuyen-khoi-nghiep-cua-mot-giang-vien-dai-hoc-bach-khoa-voi-von-30-trieu-dong-den-tham-vong-cong-ty-cong-nghe-doanh-thu-ngan-ty-20201110112721428.chn",
					},
					{
						"name_func": "verify_time_line_post_special",
						"name_case": "check hi???n th??? th???i gian trong b??i ?????c bi???t",
						"loacator_special": {
									"type": ["XPATH", "SELECTOR"],
									"script" : "//*[@class='info']",
									"type_get_element": {
														"type": "wait",
														"action": "plural_visibility"
														},
									"action": "bool"
									},

						"name_time": "start_time_1",
					},

					{
						"name_func": "check_time_load_page",
						"name_case": "ki???m tra th???i gian load_pgae",
						"name_time": "end_time_4",
						"time_check": 5,
					},

					{
						"name_func": "load_verify_time_line",
						"name_case": "ki???m tra load page 10 l???n",
					},

					{
						"name_func": "check_open_page_mobile",
						"name_case": "check open page in mobile",
						"link_open_page_mobile": "https://cafef.vn/",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "check_verify_open_page_mobile",
						"name_case": "verify open page in mobile",
						"locator_verify_page_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='admwrapper']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
						"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},
					{
						"name_func": "open_link_check_video_mobile",
						"name_case": "open link video in mobile",
						"link_check_video_mobile": "https://m.cafef.vn/videos/18196-nong-bat-1-doi-tuong-tinh-nghi-trong-vu-cuop-ngan-hang-o-dong-nai-bao-nguoi-lao-dong.chn",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "click_play_video_mobile",
						"name_case": "click play video",
						"locator_click_video_mobile": {
												"type": ["XPATH", "SELECTOR"],
												"script": "//*[@class='CafefPlayer-loading-vid-icon']",
												"type_get_element": {"type": "wait"},
												},
						'mobile': True,
					},
					{
						"name_func": "check_time_play_video_mobile",
						"name_case":"check action video in mobile",
						"locator_start_video_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[3]/div[2]/div/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						'mobile': True,
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image_mobile",
						"name_case": "open link image in mobile",
						"link_check_image_mobile": "https://cafef.vn/chung-khoan-viet-nam-thuong-bien-dong-ra-sao-sau-nhung-lan-dow-jones-lao-doc-20220914043608923.chn",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "verify_display_image_mobile",
						"name_case": "verify image in mobile",
						"locator_verify_image_mobile":{
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='ovh detail_avatar']/img",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

			]
		},

		"tuoitre": {
				"name_page": "tuoitre",
				"domain": "https://tuoitre.vn/",
				"name_case": "check page tuoitre.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='content']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='focus-first']",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},
					{
						"name_func": "verify_box_cmt",
						"name_case": "verify box comment",
						"locator_box_comment": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='tagandnetwork']/div[5]/section/div[1]",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								},
								"action": "bool",
								},

						"name_time": "end_time_2",
						"time_check": 5,
					},
					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='article-title']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='search-frm']/input",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "click_search_button",
						"name_case": "click button search",
						"locator_search_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@id='search-frm']/a",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='news-item']",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},
					},
					{
						"name_func": "open_link_check_video",
						"name_case": "open link check video",
						"link_check_video": "https://tv.tuoitre.vn/",
						"name_time": "start_time_3",
					},

					{
						"name_func": "move_mouse_check_play",
						"name_case": "move_mouse_check_play",
						"locator_move_mouse": {
								"type": ["XPATH", "SELECTOR"],
								"script" : ["//*[@class='video-display fl']/div","//*[@class='video-display fl']/div/div"],
								"type_action": "move_element",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "check_time_play_video",
						"name_case": "verify time play video",
						"locator_start_video": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='customSkin-currenttime']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://tuoitre.vn/29-thang-chap-moi-nghi-tet-la-qua-muon-nguoi-lao-dong-mong-duoc-nghi-som-hon-20220914143546606.htm",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='main-detail-body']/div[1]/div[1]/a/img",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},

					{
						"name_func": "open_link_post_special",
						"name_case": "Truy c???p link b??i ?????c bi???t",
						"link_post_special": "https://tuoitre.vn/do-merlo-doai-cong-chuoc-toi-sai-gon-fc-song-lai-hi-vong-tru-hang-2022082719183668.htm",
					},
					{
						"name_func": "verify_time_line_post_special",
						"name_case": "check hi???n th??? th???i gian trong b??i ?????c bi???t",
						"loacator_special": {
									"type": ["XPATH", "SELECTOR"],
									"script" : "//*[@class='minute']",
									"type_get_element": {
														"type": "wait",
														"action": "plural_visibility"
														},
									"action": "bool"
									},

						"name_time": "start_time_1",
					},

					{
						"name_func": "check_time_load_page",
						"name_case": "ki???m tra th???i gian load_pgae",
						"name_time": "end_time_4",
						"time_check": 5,
					},

					{
						"name_func": "load_verify_time_line",
						"name_case": "ki???m tra load page 10 l???n",
					},

					{
						"name_func": "check_open_page_mobile",
						"name_case": "check open page in mobile",
						"link_open_page_mobile": "https://tuoitre.vn/",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "check_verify_open_page_mobile",
						"name_case": "verify open page in mobile",
						"locator_verify_page_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='content']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
						"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},
					{
						"name_func": "open_link_check_video_mobile",
						"name_case": "open link video in mobile",
						"link_check_video_mobile": "https://tv.tuoitre.vn/video-nguoi-dan-vay-bat-nghi-pham-cuop-giat-2-soi-day-chuyen-tai-tiem-vang-132110.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "click_pass_advertisement_video",
						"name_case": "click advertisement video",
						"locator_pass_advertisement": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@id='video_132110-ad-container']/div[1]/button",
								"type_get_element": {"type": "wait"},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "check_time_play_video_mobile",
						"name_case":"check action video in mobile",
						"locator_start_video_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[3]/div[2]",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						'mobile': True,
					},
					{
						"name_func": "open_link_check_image_mobile",
						"name_case": "open link image in mobile",
						"link_check_image_mobile": "https://tuoitre.vn/29-thang-chap-moi-nghi-tet-la-qua-muon-nguoi-lao-dong-mong-duoc-nghi-som-hon-20220914143546606.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "verify_display_image_mobile",
						"name_case": "verify image in mobile",
						"locator_verify_image_mobile":{
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='divfirst']/div/div/img",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

				]
			},

		"baochinhphu": {
				"name_page": "baochinhphu",
				"domain": "https://baochinhphu.vn/",
				"name_case": "check page baochinhphu.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='admwrapper']/div[3]",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='home__focus-flex']/div[1]/div/div/div/div/h2/a",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},

					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='detail-title']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},


					{
						"name_func": "click_find_button",
						"name_case": "click n??t hi???n tr?????ng t??m ki???m",
						"locator_find_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@class='header__search-layout']/a[2]",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='btn-search']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "click_search_button",
						"name_case": "click button search",
						"locator_search_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@class='submit-search']",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='box-stream-item']",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},

					},
					{
						"name_func": "open_link_check_video",
						"name_case": "open link check video",
						"link_check_video": "https://media.chinhphu.vn/video.htm",
						"name_time": "start_time_3",
					},

					{
						"name_func": "move_mouse_check_play",
						"name_case": "move_mouse_check_play",
						"locator_move_mouse": {
								"type": ["XPATH", "SELECTOR"],
								"script" : ["//*[@class='overlay-pause']","//*[@class=' control-bar']/div[5]"],
								"type_action": "move_element",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "check_time_play_video",
						"name_case": "verify time play video",
						"locator_start_video": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='current-time-display']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://baochinhphu.vn/thu-tuong-pham-minh-chinh-chu-tri-hoi-nghi-toan-quoc-ve-cai-cach-tthc-phuc-vu-nguoi-dan-doanh-nghiep-102220915084109046.htm",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='img_494684030960619520']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},

					{
						"name_func": "open_link_post_special",
						"name_case": "Truy c???p link b??i ?????c bi???t",
						"link_post_special": "https://baochinhphu.vn/tong-thuat-thu-tuong-chu-tri-hop-ban-ve-cac-giai-phap-on-dinh-kinh-te-vi-mo-kiem-soat-lam-phat-va-thuc-day-tang-truong-102220912132107304.htm",
					},
					{
						"name_func": "verify_time_line_post_special",
						"name_case": "check hi???n th??? th???i gian trong b??i ?????c bi???t",
						"loacator_special": {
									"type": ["XPATH", "SELECTOR"],
									"script" : "//*[@class='livenews-item detail-tab-item']",
									"type_get_element": {
														"type": "wait",
														"action": "plural_visibility"
														},
									"action": "bool"
									},

						"name_time": "start_time_1",
					},

					{
						"name_func": "check_time_load_page",
						"name_case": "ki???m tra th???i gian load_pgae",
						"name_time": "end_time_4",
						"time_check": 5,
					},

					{
						"name_func": "load_verify_time_line",
						"name_case": "ki???m tra load page 10 l???n",
					},

					{
						"name_func": "check_open_page_mobile",
						"name_case": "check open page in mobile",
						"link_open_page_mobile": "https://baochinhphu.vn/",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "check_verify_open_page_mobile",
						"name_case": "verify open page in mobile",
						"locator_verify_page_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='admwrapper']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
						"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},
					{
						"name_func": "open_link_check_video_mobile",
						"name_case": "open link video in mobile",
						"link_check_video_mobile": "https://media.chinhphu.vn/video/khang-dinh-tam-quan-trong-cua-quan-he-viet-nam-trung-quoc-16838.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "click_play_video_mobile",
						"name_case": "click play video",
						"locator_click_video_mobile": {
												"type": ["XPATH", "SELECTOR"],
												"script": "//*[@id='context-stats']/div[3]/div[2]",
												"type_get_element": {"type": "wait"},
												},
						'mobile': True,
					},
					{
						"name_func": "click_icon_pause_video_mobile",
						"name_case": "click d???ng video sau 2s ch???y",
						"locator_click_pause_video_mobile": {
							"type": ["XPATH", "SELECTOR"],
							"script": "//*[@class=' control-bar']/button[1]",
							"type_get_element": {"type": "wait"},
						},
						'mobile': True,
					},
					{
						"name_func": "check_time_play_video_mobile",
						"name_case":"check action video in mobile",
						"locator_start_video_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						'mobile': True,
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image_mobile",
						"name_case": "open link image in mobile",
						"link_check_image_mobile": "https://baochinhphu.vn/thu-tuong-pham-minh-chinh-chu-tri-hoi-nghi-toan-quoc-ve-cai-cach-tthc-phuc-vu-nguoi-dan-doanh-nghiep-102220915084109046.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "verify_display_image_mobile",
						"name_case": "verify image in mobile",
						"locator_verify_image_mobile":{
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='img_494684030960619520']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

				]
			},

		"afamily": {
				"name_page": "afamily",
				"domain": "https://afamily.vn/",
				"name_case": "check page afamily.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='admWrapsite']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='af_section-top']/div/div[1]/article/div",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},

					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='contentforhdna fl']/div/article/h1",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "click_tag_post",
						"name_case": "th???c hi???n click v??o b??i vi???t",
						"locator_tag_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='afcbcbst-ul']/li[1]",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "verify_tag_post",
						"name_case": "check tag post",
						"locator_verify_tag": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='afwblul-info']",
								"type_get_element": {
													"type": "wait",
													"action": "plural_presence"
													},
								"action": "bool",
								},
					},

					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='txt-search-on-header']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "enter_find_text",
						"name_case": "enter find text",
						"locator_enter_find": {
							"type": ["XPATH", "SELECTOR"],
							"script": "//*[@id='txt-search-on-header']",
							"type_get_element": {"type": "wait"},
						},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='afwbl-ul']/li[1]/div/h2/a",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},

					},
					{
						"name_func": "open_link_check_video",
						"name_case": "open link check video",
						"link_check_video": "https://video.afamily.vn/",
						"name_time": "start_time_4",
					},

					{
						"name_func": "move_mouse_check_play",
						"name_case": "move_mouse_check_play",
						"locator_move_mouse": {
								"type": ["XPATH", "SELECTOR"],
								"script" : ["//*[@id='context-stats']/div[4]/div[2]/div/div","//*[@id='customSkin-checkclass-progess']"],
								"type_action": "move_element",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},
					{
						"name_func": "check_time_play_video",
						"name_case": "verify time play video",
						"locator_start_video": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[4]/div[2]/div/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://afamily.vn/5-mon-thoi-trang-giup-xay-dung-phong-cach-toi-gian-cho-nang-cong-so-20220914174029986.chn",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='kbwc-cover ']/img",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},

					{
						"name_func": "check_open_page_mobile",
						"name_case": "check open page in mobile",
						"link_open_page_mobile": "https://afamily.vn/",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "check_verify_open_page_mobile",
						"name_case": "verify open page in mobile",
						"locator_verify_page_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='wrapper_ct']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
						"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},
					{
						"name_func": "open_link_check_video_mobile",
						"name_case": "open link video in mobile",
						"link_check_video_mobile": "https://video.afamily.vn/",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "click_play_video_mobile",
						"name_case": "click play video",
						"locator_click_video_mobile": {
												"type": ["XPATH", "SELECTOR"],
												"script": "//*[@class='video-item featured-video-item']/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[2]",
												"type_get_element": {"type": "wait"},
												},
						'mobile': True,
					},
					{
						"name_func": "click_icon_pause_video_mobile",
						"name_case": "click d???ng video sau 2s ch???y",
						"locator_click_pause_video_mobile": {
												"type": ["XPATH", "SELECTOR"],
												"script": "//*[@class='video-item featured-video-item']/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[1]",
												"type_get_element": {"type": "wait"},
												},
						'mobile': True,
					},

					{
						"name_func": "check_time_play_video_mobile",
						"name_case":"check action video in mobile",
						"locator_start_video_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[3]/div[2]/div/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						'mobile': True,
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image_mobile",
						"name_case": "open link image in mobile",
						"link_check_image_mobile": "https://baochinhphu.vn/thu-tuong-pham-minh-chinh-chu-tri-hoi-nghi-toan-quoc-ve-cai-cach-tthc-phuc-vu-nguoi-dan-doanh-nghiep-102220915084109046.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "verify_display_image_mobile",
						"name_case": "verify image in mobile",
						"locator_verify_image_mobile":{
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='img_494684030960619520']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

				]
			},

		"phunuvietnam": {
				"name_page": "phunuvietnam",
				"domain": "https://phunuvietnam.vn/",
				"name_case": "check page phunuvietnam.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='wrapper']/div[1]",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='left']/div[1]/a[3]",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},
					{
						"name_func": "verify_box_cmt",
						"name_case": "verify box comment",
						"locator_box_comment": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='ykcb']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								},
								"action": "bool",
								},

						"name_time": "end_time_2",
						"time_check": 5,
					},
					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='wrapper']/div[3]/div[1]/div[1]/h1",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "click_tag_post",
						"name_case": "th???c hi???n click v??o b??i vi???t",
						"locator_tag_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='tag']/a[1]",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "verify_tag_post",
						"name_case": "check tag b??i vi???t ???? hi???n th??? b??i ????ng ch??a",
						"locator_verify_tag": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='box']",
								"type_get_element": {
													"type": "wait",
													"action": "plural_presence"
													},
								"action": "bool",
								},
					},
					{
						"name_func": "open_link_check_search",
						"name_case": "truy c???p link t??m ki???m",
						"link_check_search": "https://phunuvietnam.vn/tim-kiem.htm?keywords=6%20tr%E1%BA%BB%20t%E1%BB%AD%20vong,%20h%C6%A1n%20400%20ca",
						"name_time": "start_time_3",
					},
					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='txtSearchPage']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "click_search_button",
						"name_case": "click button search",
						"locator_search_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@id='btnSearchPage']",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='list-news-timeline']",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},

					},
					{
						"name_func": "open_link_check_video",
						"name_case": "open link check video",
						"link_check_video": "https://phunuvietnam.vn/video/khat-vong-phu-sa-563.htm",
						"name_time": "start_time_3",
					},

					{
						"name_func": "move_mouse_check_play",
						"name_case": "move_mouse_check_play",
						"locator_move_mouse": {
								"type": ["XPATH", "SELECTOR"],
								"script" : ["//*[@id='context-stats']/div[3]/div[2]","//*[@class='overlay-ad']"],
								"type_action": "move_element",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},
					{
						"name_func": "check_time_play_video",
						"name_case": "verify time play video",
						"locator_start_video": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://phunuvietnam.vn/6-tre-tu-vong-hon-400-ca-mac-virus-adeno-bv-nhi-trung-uong-canh-bao-cac-dau-hieu-tre-nhiem-benh-20220915160953048.htm",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='avatar-normal']/div/a/img",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},



					{
						"name_func": "check_open_page_mobile",
						"name_case": "check open page in mobile",
						"link_open_page_mobile": "https://phunuvietnam.vn/",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "check_verify_open_page_mobile",
						"name_case": "verify open page in mobile",
						"locator_verify_page_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='admWrapsite']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
						"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},
					{
						"name_func": "open_link_check_video_mobile",
						"name_case": "open link video in mobile",
						"link_check_video_mobile": "https://phunuvietnam.vn/video/khat-vong-phu-sa-563.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "click_play_video_mobile",
						"name_case": "click play video",
						"locator_click_video_mobile": {
												"type": ["XPATH", "SELECTOR"],
												"script": "//*[@id='context-stats']/div[3]/div[2]",
												"type_get_element": {"type": "wait"},
												},
						'mobile': True,
					},
					{
						"name_func": "click_icon_pause_video_mobile",
						"name_case": "click d???ng video sau 2s ch???y",
						"locator_click_pause_video_mobile": {
												"type": ["XPATH", "SELECTOR"],
												"script": "//*[@id='context-stats']/div[3]/button[1]",
												"type_get_element": {"type": "wait"},
												},
						'mobile': True,
					},

					{
						"name_func": "check_time_play_video_mobile",
						"name_case":"check action video in mobile",
						"locator_start_video_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						'mobile': True,
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image_mobile",
						"name_case": "open link image in mobile",
						"link_check_image_mobile": "https://phunuvietnam.vn/6-tre-tu-vong-hon-400-ca-mac-virus-adeno-bv-nhi-trung-uong-canh-bao-cac-dau-hieu-tre-nhiem-benh-20220915160953048.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "verify_display_image_mobile",
						"name_case": "verify image in mobile",
						"locator_verify_image_mobile":{
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='avatar-normal']/div/a/img",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

				]
			},

		"danviet": {
				"name_page": "danviet",
				"domain": "https://danviet.vn/",
				"name_case": "check page phunuvietnam.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='auto-loadhome']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='homehl-bot']/li[1]/a",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},
					{
						"name_func": "verify_box_cmt",
						"name_case": "verify box comment",
						"locator_box_comment": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='box-cmt']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								},
								"action": "bool",
								},

						"name_time": "end_time_2",
						"time_check": 5,
					},
					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='detail-main']/div/h1/span",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "click_tag_post",
						"name_case": "th???c hi???n click v??o b??i vi???t",
						"locator_tag_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='tags']/ul/li[1]",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "verify_tag_post",
						"name_case": "check tag b??i vi???t ???? hi???n th??? b??i ????ng ch??a",
						"locator_verify_tag": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='title-box']",
								"type_get_element": {
													"type": "wait",
													"action": "plural_presence"
													},
								"action": "bool",
								},
					},

					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='search']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "click_search_button",
						"name_case": "click button search",
						"locator_search_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@id='search-form']/button/i",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='title-box']/h3/a",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},

					},
					{
						"name_func": "open_link_check_video",
						"name_case": "open link check video",
						"link_check_video": "https://tv.danviet.vn/hien-truong-ngoi-nha-tro-noi-vo-chong-tre-chet-chay-o-khanh-hoa-20220915134915969.htm",
						"name_time": "start_time_3",
					},

					{
						"name_func": "move_mouse_check_play",
						"name_case": "move_mouse_check_play",
						"locator_move_mouse": {
								"type": ["XPATH", "SELECTOR"],
								"script" : ["//*[@id='context-stats']/div[3]/div[2]","//*[@class='overlay-shadow']"],
								"type_action": "move_element",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},
					{
						"name_func": "check_time_play_video",
						"name_case": "verify time play video",
						"locator_start_video": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://danviet.vn/chu-tich-tinh-gia-lai-vo-ngoc-thanh-bi-cach-chuc-va-xoa-tu-cach-20220915172328642.htm",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='img_494814822975746048']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},
					{
						"name_func": "open_link_post_special",
						"name_case": "Truy c???p link b??i ?????c bi???t",
						"link_post_special": "https://danviet.vn/tong-thuat-thu-tuong-doi-thoai-voi-nong-dan-nam-2022-20220529013108203.htm",
					},
					{
						"name_func": "verify_time_line_post_special",
						"name_case": "check hi???n th??? th???i gian trong b??i ?????c bi???t",
						"loacator_special": {
									"type": ["XPATH", "SELECTOR"],
									"script" : "//*[@class='item-date']",
									"type_get_element": {
														"type": "wait",
														"action": "plural_visibility"
														},
									"action": "bool"
									},

						"name_time": "start_time_1",
					},
					{
						"name_func": "check_time_load_page",
						"name_case": "ki???m tra th???i gian load_pgae",
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "load_verify_time_line",
						"name_case": "ki???m tra load page 10 l???n",
					},

					{
						"name_func": "check_open_page_mobile",
						"name_case": "check open page in mobile",
						"link_open_page_mobile": "https://danviet.vn/",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "check_verify_open_page_mobile",
						"name_case": "verify open page in mobile",
						"locator_verify_page_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='main-wrapper']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
						"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},
					{
						"name_func": "open_link_check_video_mobile",
						"name_case": "open link video in mobile",
						"link_check_video_mobile": "https://tv.danviet.vn/hien-truong-ngoi-nha-tro-noi-vo-chong-tre-chet-chay-o-khanh-hoa-20220915134915969.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "click_play_video_mobile",
						"name_case": "click play video",
						"locator_click_video_mobile": {
												"type": ["XPATH", "SELECTOR"],
												"script": "//*[@id='context-stats']/div[3]/div[2]",
												"type_get_element": {"type": "wait"},
												},
						'mobile': True,
					},
					{
						"name_func": "click_icon_pause_video_mobile",
						"name_case": "click d???ng video sau 2s ch???y",
						"locator_click_pause_video_mobile": {
												"type": ["XPATH", "SELECTOR"],
												"script": "//*[@id='context-stats']/div[3]/button[1]",
												"type_get_element": {"type": "wait"},
												},
						'mobile': True,
					},

					{
						"name_func": "check_time_play_video_mobile",
						"name_case":"check action video in mobile",
						"locator_start_video_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						'mobile': True,
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image_mobile",
						"name_case": "open link image in mobile",
						"link_check_image_mobile": "https://danviet.vn/chu-tich-tinh-gia-lai-vo-ngoc-thanh-bi-cach-chuc-va-xoa-tu-cach-20220915172328642.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "verify_display_image_mobile",
						"name_case": "verify image in mobile",
						"locator_verify_image_mobile":{
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='img_494814822975746048']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

				]
			},

		"vtv": {
				"name_page": "vtv",
				"domain": "https://vtv.vn/",
				"name_case": "check page vtv.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='admWrapsite']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='homefocusslider']/ul/li[1]/a",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},
					{
						"name_func": "verify_box_cmt",
						"name_case": "verify box comment",
						"locator_box_comment": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='detail_comment clearfix fl']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								},
								"action": "bool",
								},

						"name_time": "end_time_2",
						"time_check": 5,
					},
					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='title_detail']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},
					{
						"name_func": "click_tag_post",
						"name_case": "th???c hi???n click v??o b??i vi???t",
						"locator_tag_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class ='news_keyword']/a[1]",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "verify_tag_post",
						"name_case": "check tag post",
						"locator_verify_tag": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class ='dsk-focus clearfix']/div/h2/a",
								"type_get_element": {
													"type": "wait",
													"action": "plural_presence"
													},
								"action": "bool",
								},
					},
					{
						"name_func": "click_find_button",
						"name_case": "click n??t hi???n tr?????ng t??m ki???m",
						"locator_find_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@id='btnSearch']",
								"type_get_element": {"type": "wait"},
								},
					},

					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='txtSearch']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "enter_find_text",
						"name_case": "enter find text",
						"locator_enter_find": {
							"type": ["XPATH", "SELECTOR"],
							"script": "//*[@id='txtSearch']",
							"type_get_element": {"type": "wait"},
						},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='tlitem']",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},
					},
					{
						"name_func": "open_link_check_video",
						"name_case": "open link check video",
						"link_check_video": "https://vtv.vn/video/imf-danh-gia-cao-cac-chinh-sach-dieu-hanh-kinh-te-cua-vn-586688.htm",
						"name_time": "start_time_4",
					},

					{
						"name_func": "move_mouse_check_play",
						"name_case": "move_mouse_check_play",
						"locator_move_mouse": {
								"type": ["XPATH", "SELECTOR"],
								"script" : ["//*[@class='VTVNewsPlayer-area-control']","//*[@class='btn_toggle_skin2']"],
								"type_action": "move_element",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},
					{
						"name_func": "check_time_play_video",
						"name_case": "verify time play video",
						"locator_start_video": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='customSkin-currenttime']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://vtv.vn/kinh-te/chinh-phu-ban-hanh-nghi-quyet-thuc-day-giai-ngan-von-dau-tu-cong-nhung-thang-cuoi-nam-20220916062638982.htm",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='news-avatar']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},

					{
						"name_func": "open_link_post_special",
						"name_case": "Truy c???p link b??i ?????c bi???t",
						"link_post_special": "https://vtv.vn/bong-da-trong-nuoc/kt-topenland-binh-dinh-0-0-clb-hai-phong-chia-diem-kich-tinh-20220914172621559.htm",
					},
					{
						"name_func": "verify_time_line_post_special",
						"name_case": "check hi???n th??? th???i gian trong b??i ?????c bi???t",
						"loacator_special": {
									"type": ["XPATH", "SELECTOR"],
									"script" : "//*[@class='time']",
									"type_get_element": {
														"type": "wait",
														"action": "plural_visibility"
														},
									"action": "bool"
									},

						"name_time": "start_time_1",
					},

					{
						"name_func": "check_time_load_page",
						"name_case": "ki???m tra th???i gian load_pgae",
						"name_time": "end_time_4",
						"time_check": 5,
					},

					{
						"name_func": "load_verify_time_line",
						"name_case": "ki???m tra load page 10 l???n",
					},

					{
						"name_func": "check_open_page_mobile",
						"name_case": "check open page in mobile",
						"link_open_page_mobile": "https://vtv.vn/",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "check_verify_open_page_mobile",
						"name_case": "verify open page in mobile",
						"locator_verify_page_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='admwrapper']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
						"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},
					{
						"name_func": "open_link_check_video_mobile",
						"name_case": "open link video in mobile",
						"link_check_video_mobile": "https://vtv.vn/video/imf-danh-gia-cao-cac-chinh-sach-dieu-hanh-kinh-te-cua-vn-586688.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "click_pass_advertisement_video",
						"name_case": "click advertisement video",
						"locator_pass_advertisement": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@id='player-init-ad-container']/div[1]/button",
								"type_get_element": {"type": "wait"},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "check_time_play_video_mobile",
						"name_case":"check action video in mobile",
						"locator_start_video_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='customSkin-currenttime']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						'mobile': True,
					},

					{
						"name_func": "open_link_check_image_mobile",
						"name_case": "open link image in mobile",
						"link_check_image_mobile": "https://vtv.vn/chinh-tri/giai-cuu-hang-tram-cong-dan-viet-lao-dong-bat-hop-phap-tai-campuchia-20221020184834609.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "verify_display_image_mobile",
						"name_case": "verify image in mobile",
						"locator_verify_image_mobile":{
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='cover-dtl']/img",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

				]
			},

		"suckhoevadoisong": {
				"name_page": "suckhoavadoisong",
				"domain": "https://suckhoedoisong.vn/",
				"name_case": "check page vtv.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='admwrapper']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='home-box-focus-big']/div/h2",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},
					{
						"name_func": "verify_box_cmt",
						"name_case": "verify box comment",
						"locator_box_comment": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='ykcb']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								},
								"action": "bool",
								},

						"name_time": "end_time_2",
						"time_check": 5,
					},
					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='detail-title']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "click_find_button",
						"name_case": "click n??t hi???n tr?????ng t??m ki???m",
						"locator_find_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@class='header__search']",
								"type_get_element": {"type": "wait"},
								},
					},

					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='header__searhc-form']/div/input",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "click_search_button",
						"name_case": "click button search",
						"locator_search_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@class='header__searhc-form']/button",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='box-category-item ']",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},

					},
					{
						"name_func": "open_link_check_video",
						"name_case": "open link check video",
						"link_check_video": "https://suckhoedoisong.vn/nguoi-dan-ong-110kg-va-quyet-tam-thay-doi-chua-bao-gio-la-muon-169220915174555174.htm",
						"name_time": "start_time_3",
					},

					{
						"name_func": "move_mouse_check_play",
						"name_case": "move_mouse_check_play",
						"locator_move_mouse": {
								"type": ["XPATH", "SELECTOR"],
								"script" : ["//*[@class='overlay-ad']","//*[@id='context-stats']/div[4]/div[2]"],
								"type_action": "move_element",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},
					{
						"name_func": "check_time_play_video",
						"name_case": "verify time play video",
						"locator_start_video": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://suckhoedoisong.vn/cuoc-thi-toi-khoe-dep-hon-khong-chi-la-dong-luc-de-toi-giam-can-ma-con-khoe-dep-va-ngua-benh-tat-169220912123336782.htm",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='VCSortableInPreviewMode']/div/a",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},

				{
					"name_func": "open_link_post_special",
					"name_case": "Truy c???p link b??i ?????c bi???t",
					"link_post_special": "https://suckhoedoisong.vn/live-hoi-nghi-truc-tuyen-nang-cao-cong-tac-cham-soc-suc-khoe-nhan-dan-16922082106534952.htm",
				},
				{
					"name_func": "verify_time_line_post_special",
					"name_case": "check hi???n th??? th???i gian trong b??i ?????c bi???t",
					"loacator_special": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='time']",
								"type_get_element": {
													"type": "wait",
													"action": "plural_visibility"
													},
								"action": "bool"
								},

					"name_time": "start_time_1",
				},

				{
					"name_func": "check_time_load_page",
					"name_case": "ki???m tra th???i gian load_pgae",
					"name_time": "end_time_4",
					"time_check": 5,
				},

				{
					"name_func": "load_verify_time_line",
					"name_case": "ki???m tra load page 10 l???n",
				},

				{
					"name_func": "check_open_page_mobile",
					"name_case": "check open page in mobile",
					"link_open_page_mobile": "https://suckhoedoisong.vn/",
					"name_time": "start_time_1",
					'mobile': True,
				},
				{
					"name_func": "check_verify_open_page_mobile",
					"name_case": "verify open page in mobile",
					"locator_verify_page_mobile": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@class='main']",
							"type_get_element": {
												"type": "wait",
												"action": "singular_visibility"
												},
					"action": "bool"
							},
					"name_time": "end_time_1",
					"time_check": 5,
					'mobile': True,
				},
				{
					"name_func": "open_link_check_video_mobile",
					"name_case": "open link video in mobile",
					"link_check_video_mobile": "https://suckhoedoisong.vn/nguoi-dan-ong-110kg-va-quyet-tam-thay-doi-chua-bao-gio-la-muon-169220915174555174.htm",
					"name_time": "start_time_1",
					'mobile': True,
				},
				{
					"name_func": "click_play_video_mobile",
					"name_case": "click play video",
					"locator_click_video_mobile": {
											"type": ["XPATH", "SELECTOR"],
											"script": "//*[@class='TruyenhinhVovPlayer-loading-vid-icon']",
											"type_get_element": {"type": "wait"},
											},
					'mobile': True,
				},
				{
					"name_func": "click_icon_pause_video_mobile",
					"name_case": "click d???ng video sau 2s ch???y",
					"locator_click_pause_video_mobile": {
											"type": ["XPATH", "SELECTOR"],
											"script": "//*[@class=' control-bar']/button[1]",
											"type_get_element": {"type": "wait"},
											},
					'mobile': True,
				},

				{
					"name_func": "check_time_play_video_mobile",
					"name_case":"check action video in mobile",
					"locator_start_video_mobile": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
							"type_get_element": {
								"type": "wait",
								"action": "singular_presence"
							},
							},
					'mobile': True,
					"name_time": "end_time_4",
					"time_check": 5,
				},
				{
					"name_func": "open_link_check_image_mobile",
					"name_case": "open link image in mobile",
					"link_check_image_mobile": "https://suckhoedoisong.vn/cuoc-thi-toi-khoe-dep-hon-khong-chi-la-dong-luc-de-toi-giam-can-ma-con-khoe-dep-va-ngua-benh-tat-169220912123336782.htm",
					"name_time": "start_time_1",
					'mobile': True,
				},
				{
					"name_func": "verify_display_image_mobile",
					"name_case": "verify image in mobile",
					"locator_verify_image_mobile":{
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@class='VCSortableInPreviewMode']/div/a",
							"type_get_element": {
												"type": "wait",
												"action": "singular_visibility"
												},
							"action": "bool"
							},
					"name_time": "end_time_1",
					"time_check": 5,
					'mobile': True,
				},

				]
			},

		"autopro": {
				"name_page": "autopro",
				"domain": "https://autopro.com.vn/",
				"name_case": "check page autopro.com.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='mainsection']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='bignews1']/h2/a",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},

					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class = 'news-details']/h1",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},
					{
						"name_func": "click_search_button",
						"name_case": "click n??t hi???n tr?????ng t??m ki???m",
						"locator_find_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@class = 'icon-search sprite']",
								"type_get_element": {"type": "wait"},
								},
					},

					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='search_keyword']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "click_search_button",
						"name_case": "click button search",
						"locator_search_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@class = 'icon-search sprite']",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class = 'lstnews']",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},

					},
					{
						"name_func": "open_link_check_video",
						"name_case": "open link check video",
						"link_check_video": "https://autopro.com.vn/video.chn",
						"name_time": "start_time_3",
					},

					{
						"name_func": "move_mouse_check_play",
						"name_case": "move_mouse_check_play",
						"locator_move_mouse": {
								"type": ["XPATH", "SELECTOR"],
								"script" : ["//*[@id='context-stats']/div[3]/div[2]/div","//*[@id='timelinevod']/li[2]/div/div[1]"],
								"type_action": "move_element",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},
					{
						"name_func": "check_time_play_video",
						"name_case": "verify time play video",
						"locator_start_video": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
						"name_time": "end_time_4",
						"time_check": 5,
					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://autopro.com.vn/dang-sau-gia-pin-suzuki-ertiga-hybrid-chi-299-trieu-dong-tai-viet-nam-re-bang-1-3-tren-corolla-cross-177221019150142111.chn",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='append_box_thread']/figure[1]/div/a/img",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},

				{
					"name_func": "check_open_page_mobile",
					"name_case": "check open page in mobile",
					"link_open_page_mobile": "https://autopro.com.vn/",
					"name_time": "start_time_1",
					'mobile': True,
				},
				{
					"name_func": "check_verify_open_page_mobile",
					"name_case": "verify open page in mobile",
					"locator_verify_page_mobile": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@class = 'w-full']",
							"type_get_element": {
												"type": "wait",
												"action": "singular_visibility"
												},
					"action": "bool"
							},
					"name_time": "end_time_1",
					"time_check": 5,
					'mobile': True,
				},
				{
					"name_func": "open_link_check_video_mobile",
					"name_case": "open link video in mobile",
					"link_check_video_mobile": "https://m.autopro.com.vn/video/bo-suu-tap-xe-duoc-dat-trong-mot-khong-gian-kha-giong-phong-cach-cua-nhung-ngoi-nha-lon-o-nuoc-y-video-at-dadocesaroinstagram-v20218.chn",
					"name_time": "start_time_1",
					'mobile': True,
				},
				{
					"name_func": "click_play_video_mobile",
					"name_case": "click play video",
					"locator_click_video_mobile": {
											"type": ["XPATH", "SELECTOR"],
											"script": "//*[@id='context-stats']/div[3]/div[2]",
											"type_get_element": {"type": "wait"},
											},
					'mobile': True,
				},
				{
					"name_func": "click_icon_pause_video_mobile",
					"name_case": "click d???ng video sau 2s ch???y",
					"locator_click_pause_video_mobile": {
											"type": ["XPATH", "SELECTOR"],
											"script": "//*[@id='context-stats']/div[3]/div[2]/div",
											"type_get_element": {"type": "wait"},
											},
					'mobile': True,
				},

				{
					"name_func": "check_time_play_video_mobile",
					"name_case":"check action video in mobile",
					"locator_start_video_mobile": {
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
							"type_get_element": {
								"type": "wait",
								"action": "singular_presence"
							},
							},
					'mobile': True,
					"name_time": "end_time_4",
					"time_check": 5,
				},
				{
					"name_func": "open_link_check_image_mobile",
					"name_case": "open link image in mobile",
					"link_check_image_mobile": "https://m.autopro.com.vn/hyundai-santa-fe-2023-dan-lo-dien-ro-net-bom-tan-tham-vong-danh-bai-sorento-ra-mat-nam-sau-177221021080747543.chn",
					"name_time": "start_time_1",
					'mobile': True,
				},
				{
					"name_func": "verify_display_image_mobile",
					"name_case": "verify image in mobile",
					"locator_verify_image_mobile":{
							"type": ["XPATH", "SELECTOR"],
							"script" : "//*[@id='content']/div[5]/div[5]/figure[1]/div/a/img",
							"type_get_element": {
												"type": "wait",
												"action": "singular_visibility"
												},
							"action": "bool"
							},
					"name_time": "end_time_1",
					"time_check": 5,
					'mobile': True,
				},

				]
			},

		"gamek": {
						"name_page": "gamek",
						"domain": "https://gamek.vn/",
						"name_case": "check page gamek.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admWrapsite']/div[1]",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='contentleft']/div[1]/div[1]/a/img",
										"type_get_element": {"type": "wait"},
										},
								"name_time": "start_time_2",
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class = 'topdetail']/h1",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='searchinput']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='admWrapsite']/div[1]/div[1]/div/div[2]/ul/li[8]/a",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class = 'contentleft']",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://gamek.vn/tran-cong-thanh-chien-kinh-dien-bac-nhat-15-nam-vo-lam-vua-moi-dien-ra-thang-thua-chi-dinh-doat-bang-giay-20220302202840277.chn",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@class='GamekPlayer-loading-vid-icon']", "//*[@id='context-stats']/div[4]/div[2]/div/div"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[2]/div/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://gamek.vn/ba-game-di-dong-moi-hay-nhat-tuan-2-thang-10-co-mot-tro-choi-la-doi-trong-thuc-su-cua-diablo-immortal-178221020165418511.chn",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class = 'VCSortableInPreviewMode noCaption']/div/a/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

						{
							"name_func": "check_open_page_mobile",
							"name_case": "check open page in mobile",
							"link_open_page_mobile": "https://gamek.vn/",
							"name_time": "start_time_1",
							'mobile': True,
						},
						{
							"name_func": "check_verify_open_page_mobile",
							"name_case": "verify open page in mobile",
							"locator_verify_page_mobile": {
									"type": ["XPATH", "SELECTOR"],
									"script" : "//*[@id='hot_new']",
									"type_get_element": {
														"type": "wait",
														"action": "singular_visibility"
														},
							"action": "bool"
									},
							"name_time": "end_time_1",
							"time_check": 5,
							'mobile': True,
						},

						{
							"name_func": "open_link_check_image_mobile",
							"name_case": "open link image in mobile",
							"link_check_image_mobile": "https://gamek.vn/ba-game-di-dong-moi-hay-nhat-tuan-2-thang-10-co-mot-tro-choi-la-doi-trong-thuc-su-cua-diablo-immortal-178221020165418511.chn",
							"name_time": "start_time_1",
							'mobile': True,
						},
						{
							"name_func": "verify_display_image_mobile",
							"name_case": "verify image in mobile",
							"locator_verify_image_mobile":{
									"type": ["XPATH", "SELECTOR"],
									"script" : "//*[@class = 'VCSortableInPreviewMode noCaption']/div/a/img",
									"type_get_element": {
														"type": "wait",
														"action": "singular_visibility"
														},
									"action": "bool"
									},
							"name_time": "end_time_1",
							"time_check": 5,
							'mobile': True,
						},

						]
					},

		"cafebiz": {
						"name_page": "cafebiz",
						"domain": "https://cafebiz.vn/",
						"name_case": "check page cafebiz.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='form1']/div[4]/div/div[1]/div",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='cfbiz_bigright-left']/div/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='mainDetail']/h1",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "click_tag_post",
								"name_case": "event click on post",
								"locator_tag_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='tags-item']/a[1]",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "verify_tag_post",
								"name_case": "check tag display post",
								"locator_verify_tag": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='load_listnews']/div",
										"type_get_element": {
															"type": "wait",
															"action": "plural_presence"
															},
										"action": "bool",
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='imgSearch']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='CafeF_Biz_Search']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='CafeF_Biz_Search']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='infodsthome']/h3/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://cafebiz.vn/videos.chn",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[3]/div[2]","//*[@id='context-stats']/div[3]/div[1]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[2]/div/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://cafebiz.vn/ai-dung-sau-thuong-hieu-mixue-chuyen-ban-kem-va-tra-sua-gia-binh-dan-mo-ram-ro-600-cua-hang-khap-viet-nam-176221021141503367.chn",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='mainDetail']/div[5]/center/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

						{
							"name_func": "check_open_page_mobile",
							"name_case": "check open page in mobile",
							"link_open_page_mobile": "https://cafebiz.vn/",
							"name_time": "start_time_1",
							'mobile': True,
						},
						{
							"name_func": "check_verify_open_page_mobile",
							"name_case": "verify open page in mobile",
							"locator_verify_page_mobile": {
									"type": ["XPATH", "SELECTOR"],
									"script" : "//*[@id='admwrapper']",
									"type_get_element": {
														"type": "wait",
														"action": "singular_visibility"
														},
							"action": "bool"
									},
							"name_time": "end_time_1",
							"time_check": 5,
							'mobile': True,
						},
						# {
						# 	"name_func": "open_link_check_video_mobile",
						# 	"name_case": "open link video in mobile",
						# 	"link_check_video_mobile": "https://m.cafebiz.vn/video/ville-de-mont-moutain-resort-giac-mong-phu-hoa-giua-rung-thong-tram-tuoi-20234.chn",
						# 	"name_time": "start_time_1",
						# 	'mobile': True,
						# },
						# {
						# 	"name_func": "click_play_video_mobile",
						# 	"name_case": "click play video",
						# 	"locator_click_video_mobile": {
						# 							"type": ["XPATH", "SELECTOR"],
						# 							"script": "//*[@id='context-stats']/div[3]/div[2]",
						# 							"type_get_element": {"type": "wait"},
						# 							},
						# 	'mobile': True,
						# },
						# {
						# 	"name_func": "click_icon_pause_video_mobile",
						# 	"name_case": "click d???ng video sau 2s ch???y",
						# 	"locator_click_pause_video_mobile": {
						# 							"type": ["XPATH", "SELECTOR"],
						# 							"script": "//*[@id='context-stats']/div[3]/div[2]",
						# 							"type_get_element": {"type": "wait"},
						# 							},
						# 	'mobile': True,
						# },
						#
						# {
						# 	"name_func": "check_time_play_video_mobile",
						# 	"name_case":"check action video in mobile",
						# 	"locator_start_video_mobile": {
						# 			"type": ["XPATH", "SELECTOR"],
						# 			"script" : "",
						# 			"type_get_element": {
						# 				"type": "wait",
						# 				"action": "singular_presence"
						# 			},
						# 			},
						# 	'mobile': True,
						# 	"name_time": "end_time_4",
						# 	"time_check": 5,
						# },
						{
							"name_func": "open_link_check_image_mobile",
							"name_case": "open link image in mobile",
							"link_check_image_mobile": "https://m.cafebiz.vn/ai-dung-sau-thuong-hieu-mixue-chuyen-ban-kem-va-tra-sua-gia-binh-dan-mo-ram-ro-600-cua-hang-khap-viet-nam-176221021141503367.chn",
							"name_time": "start_time_1",
							'mobile': True,
						},
						{
							"name_func": "verify_display_image_mobile",
							"name_case": "verify image in mobile",
							"locator_verify_image_mobile":{
									"type": ["XPATH", "SELECTOR"],
									"script" : "//*[@id='wrapper']/div[3]/center/img",
									"type_get_element": {
														"type": "wait",
														"action": "singular_visibility"
														},
									"action": "bool"
									},
							"name_time": "end_time_1",
							"time_check": 5,
							'mobile': True,
						},

					]
				},

		"genk": {
						"name_page": "genk",
						"domain": "https://genk.vn/",
						"name_case": "check page genk.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admWrapsite']/div/div[2]/div[1]",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class = 'gk_bigright-left']/div/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='kbwc-title clearfix']/span",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='btnSearch']",
										"type_get_element": {"type": "wait"},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='searchinput']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='btnSearch']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='list-news-other nob clearfix']",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://genk.vn/video/tai-sao-trung-quoc-duoc-menh-danh-la-than-den-trong-viec-di-chuyen-cac-toa-nha-hang-nghin-tan-36423.chn",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[4]/div[2]/div/div"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[2]/div/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://genk.vn/redmi-a1-smartphone-gia-2-trieu-co-mat-lung-gia-da-pin-5000mah-20221021154412029.chn",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_507392528659787776']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},


						{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://genk.vn/",
								"name_time": "start_time_1",
								'mobile': True,
						},
						{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='content']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
							},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
						},
						{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://m.genk.vn/video/tai-sao-trung-quoc-duoc-menh-danh-la-than-den-trong-viec-di-chuyen-cac-toa-nha-hang-nghin-tan-36423.chn",
								"name_time": "start_time_1",
								'mobile': True,
						},

							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
									"type": ["XPATH", "SELECTOR"],
									"script": "//*[@id='context-stats']/div[3]/div[2]",
									"type_get_element": {"type": "wait"},
								},
								'mobile': True,
							},
						{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
						},
						{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://genk.vn/redmi-a1-smartphone-gia-2-trieu-co-mat-lung-gia-da-pin-5000mah-20221021154412029.chn",
								"name_time": "start_time_1",
								'mobile': True,
						},
						{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_507392528659787776']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
						},

					]
					},

		"sport5": {
						"name_page": "sport5",
						"domain": "https://sport5.vn/",
						"name_case": "check page sport5.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admWrapsite']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class = 'itemright clearfix']/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='maincontentdetail']/h1",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
									"type": ["XPATH", "SELECTOR"],
									"script": "//*[@id='btnSearch']/span",
									"type_get_element": {"type": "wait"},
								},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='searchinput']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='btnSearch']/span",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='knswli clearfix']",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://sport5.vn/video/highlights-psg-4-0-nantes-sieu-cup-phap-19653.htm",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[4]/button[1]", "//*[@id='context-stats']/div[4]/div[1]/div"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://sport5.vn/nhan-dinh-bong-da-chelsea-vs-man-utd-vong-13-ngoai-hang-anh-20221022072811979.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='VCSortableInPreviewMode']/div/a",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},



							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://sport5.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='wrapper_ct']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://sport5.vn/video/highlights-psg-4-0-nantes-sieu-cup-phap-19653.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},
							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://sport5.vn/cau-thu-duy-nhat-len-tieng-ung-ho-ronaldo-den-luc-nay-20221022081506006.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='divfirst']/figure/div/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"nld": {
						"name_page": "nld",
						"domain": "https://nld.com.vn/",
						"name_case": "check page nld.com.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='form1']/section[2]/div[1]",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='top1-focus']/div/h3",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='comment-container']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='title-content']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "click_tag_post",
								"name_case": "th???c hi???n click v??o b??i vi???t",
								"locator_tag_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='listtags']//li[1]/a",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "verify_tag_post",
								"name_case": "check tag b??i vi???t ???? hi???n th??? b??i ????ng ch??a",
								"locator_verify_tag": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='list-news clearfix']/li",
										"type_get_element": {
															"type": "wait",
															"action": "plural_presence"
															},
										"action": "bool",
										},
							},

							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
									"type": ["XPATH", "SELECTOR"],
									"script": "//*[@id='MenuTopPage']/ul/li[18]/a",
									"type_get_element": {"type": "wait"},
								},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='MenuTopPage']/ul/li[18]/input",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='MenuTopPage']/ul/li[18]/a",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='gs-title']/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://tv.nld.com.vn/",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@class = 'NLDPlayer-loading-vid-icon']", "//*[@class = 'btn_toggle_skin2']"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='customSkin-currenttime']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://nld.com.vn/thoi-su/chu-tich-ubnd-tp-hcm-phan-van-mai-neu-van-de-lien-quan-ngan-hang-scb-xang-dau-20221022093949374.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508104904991076352']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

						# {
						# 	"name_func": "open_link_post_special",
						# 	"name_case": "Truy c???p link b??i ?????c bi???t",
						# 	"link_post_special": "",
						# },
						# {
						# 	"name_func": "verify_time_line_post_special",
						# 	"name_case": "check hi???n th??? th???i gian trong b??i ?????c bi???t",
						# 	"loacator_special": {
						# 				"type": ["XPATH", "SELECTOR"],
						# 				"script" : "//*[@class='time']",
						# 				"type_get_element": {
						# 									"type": "wait",
						# 									"action": "plural_visibility"
						# 									},
						# 				"action": "bool"
						# 				},
						#
						# 	"name_time": "start_time_1",
						# },
						#
						# {
						# 	"name_func": "check_time_load_page",
						# 	"name_case": "ki???m tra th???i gian load_pgae",
						# 	"name_time": "end_time_4",
						# 	"time_check": 5,
						# },
						#
						# {
						# 	"name_func": "load_verify_time_line",
						# 	"name_case": "ki???m tra load page 10 l???n",
						# },

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://nld.com.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='wrapper']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://nld.com.vn/thoi-su/chu-tich-ubnd-tp-hcm-phan-van-mai-neu-van-de-lien-quan-ngan-hang-scb-xang-dau-20221022093949374.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508104904991076352']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"ttvn": {
						"name_page": "nld",
						"domain": "https://ttvn.toquoc.vn/",
						"name_case": "check page nld.com.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='top_noibat clearfix']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='top_noibat_row2 mgt20']/ul/li[1]/a/img",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='detail-small']/div[2]/h1",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='textSearch']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='btnSearchTop']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='item last']",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://ttvn.toquoc.vn/videos.htm",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[3]/div[2]", "//*[@id='context-stats']/div[4]/div[1]/div"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://ttvn.toquoc.vn/7-thuc-pham-co-hai-cho-nao-bo-ma-ban-van-tieu-thu-hang-ngay-20221022102015436.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508114975255306240']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://ttvn.toquoc.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='wrapper_ct']/div",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://ttvn.toquoc.vn/video/xe-buyt-chu-dong-chan-gio-cho-nguoi-di-xe-buyt-tren-cau-vinh-tuy-trong-con-mua-lon-hoi-dau-thang-7-video-hoang-quan-99252587.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},
							# {
							# 	"name_func": "click_icon_pause_video_mobile",
							# 	"name_case": "click d???ng video sau 2s ch???y",
							# 	"locator_click_pause_video_mobile": {
							# 							"type": ["XPATH", "SELECTOR"],
							# 							"script": "//*[@class=' control-bar']/button[1]",
							# 							"type_get_element": {"type": "wait"},
							# 							},
							# 	'mobile': True,
							# },

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://ttvn.toquoc.vn/my-nhan-viet-gap-su-co-voi-trang-phuc-dan-toc-thuy-tien-thien-an-xu-ly-khon-kheo-khanh-van-toa-sang-trong-kho-khan-20221022082423834.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508076549604114432']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"nhipsongkinhte": {
						"name_page": "nhapsongkinhte",
						"domain": "http://nhipsongkinhte.toquoc.vn/",
						"name_case": "check page nhipsongkinhte.toquoc.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='col740 fl']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='content-sub pkg']/li[1]/h3",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='col650 fr ']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='searchinput']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text box find",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='searchinput']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='pkg']",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "http://nhipsongkinhte.toquoc.vn/camera-vu-xe-khach-cho-cong-nhan-gap-nan-18-nguoi-bi-thuong-2022100614101787.htm",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[3]/div[2]","//*[@id='context-stats']/div[4]/button[1]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "http://nhipsongkinhte.toquoc.vn/vu-chay-quan-bar-gan-cho-ben-thanh-phong-toa-ban-kinh-200m-quanh-hien-truong-de-dap-lua-2022101712135598.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_506331743994470400']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "http://nhipsongkinhte.toquoc.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='sb-site']/div[2]/div/div[2]/div[1]",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "http://nhipsongkinhte.toquoc.vn/camera-vu-xe-khach-cho-cong-nhan-gap-nan-18-nguoi-bi-thuong-2022100614101787.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},


							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "http://nhipsongkinhte.toquoc.vn/la-quoc-gia-asean-thu-hai-cong-bo-ket-qua-kinh-te-quy-3-2022-tang-truong-gdp-cua-singapore-cao-hay-thap-so-voi-viet-nam-20221021172253682.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class = 'avatar']/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"ETime": {
						"name_page": "vtv",
						"domain": "http://ETime.danviet.vn",
						"name_case": "check page vtv.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admWrapsite']/div[1]/div[2]/div[1]",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='sidebar sidebar-small']/div/ul/li[1]/a[1]",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='dt-title']/h1/span",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "click_tag_post",
								"name_case": "th???c hi???n click v??o b??i vi???t",
								"locator_tag_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='tags']/ul/li[1]",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "verify_tag_post",
								"name_case": "check tag b??i vi???t ???? hi???n th??? b??i ????ng ch??a",
								"locator_verify_tag": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='content-box']/h3[1]/a",
										"type_get_element": {
															"type": "wait",
															"action": "plural_presence"
															},
										"action": "bool",
										},
							},


							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='search']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='search-form']/button/i",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='content-box']",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://danviet.vn/gia-xang-dau-hom-nay-14-10-dau-co-kha-nang-tang-vot-vi-rui-ro-nay-20221014083452925.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_505187387893489664']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "http://ETime.danviet.vn",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='container']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://etime.danviet.vn/quang-ngainam-trong-top-10-tinh-giai-ngan-von-dau-tu-cong-cao-nhat-nuoc-20221024093149587.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508828819178389504']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"langcuoi": {
						"name_page": "langcuoi",
						"domain": "https://langcuoi.danviet.vn/",
						"name_case": "check page langcuoi.danviet.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='mainHtml']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='homehl-small']/li[1]",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-cmt']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='dt-title']/h1/span",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='search']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='search-form']/button",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='list-news']",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://langcuoi.danviet.vn/1001-cach-ma-sep-ep-ban-phai-tang-ca-20191009175428196.htm",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[3]/div[2]","//*[@id='context-stats']/div[4]/button[1]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://langcuoi.danviet.vn/1001-cach-ma-sep-ep-ban-phai-tang-ca-20191009175428196.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='image-avatar']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://langcuoi.danviet.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='container']/div",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://langcuoi.danviet.vn/1001-cach-ma-sep-ep-ban-phai-tang-ca-20191009175428196.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://langcuoi.danviet.vn/quan-ly-duc-phuc-len-tieng-sau-khi-nam-ca-si-bi-to-vo-on-20191009173012509.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='image-avatar']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
				},

		"trangtraiviet": {
						"name_page": "trangtraiviet",
						"domain": "https://trangtraiviet.danviet.vn/",
						"name_case": "check page trangtraiviet.danviet.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='block-wrapper']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='review-posts-list']/li[1]/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-cmt']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='single-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "click_tag_post",
								"name_case": "th???c hi???n click v??o b??i vi???t",
								"locator_tag_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='meta-tags pull-left']/ul/li[2]",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "verify_tag_post",
								"name_case": "check tag b??i vi???t ???? hi???n th??? b??i ????ng ch??a",
								"locator_verify_tag": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='col-md-9 col-sm-8']",
										"type_get_element": {
															"type": "wait",
															"action": "plural_presence"
															},
										"action": "bool",
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='txtSearchKeyword']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='search-submit']/i",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='col-md-9 col-sm-8']/h4/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://trangtraiviet.danviet.vn/nong-dan-hoa-binh-tiet-lo-bi-quyet-bien-trau-gay-thanh-trau-beo-20221024091858213.htm",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[3]/div[2]", "//*[@id='context-stats']/div[4]/button[1]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://trangtraiviet.danviet.vn/xuat-khau-chuoi-vao-nhat-ban-dung-quan-tam-den-gia-20221024102229314.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='VCSortableInPreviewMode']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://trangtraiviet.danviet.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='mainbody']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://trangtraiviet.danviet.vn/nong-dan-hoa-binh-tiet-lo-bi-quyet-bien-trau-gay-thanh-trau-beo-20221024091858213.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://trangtraiviet.danviet.vn/nong-dan-hoa-binh-tiet-lo-bi-quyet-bien-trau-gay-thanh-trau-beo-20221024091858213.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='VCSortableInPreviewMode']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
				},

		"suckhoehangngay": {
						"name_page": "suckhoehangngay",
						"domain": "https://suckhoehangngay.vn/",
						"name_case": "check page https://suckhoehangngay.vn/",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='section section-1']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='homepage']/div/div[1]/section[1]/div[2]/div/div[2]/div/div[2]/a/img",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='single__title']/h1",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='auto_search_head']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@class='fa fa-search']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='list-item div_load_post']/div/div/h3/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://suckhoehangngay.vn/7-nguyen-tac-cham-soc-ban-chan-tai-nha-cho-nguoi-benh-dai-thao-duong-co-video-minh-hoa-20211221235517384.htm",
								"name_time": "start_time_3",
							},
							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[3]/div[2]", "//*[@id='context-stats']/div[4]/button[1]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://suckhoehangngay.vn/cam-lanh-co-gay-viem-phoi-o-tre-em-khong-20221020225213147.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='post-header']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://suckhoehangngay.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='wrapper']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://suckhoehangngay.vn/7-nguyen-tac-cham-soc-ban-chan-tai-nha-cho-nguoi-benh-dai-thao-duong-co-video-minh-hoa-20211221235517384.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://suckhoehangngay.vn/7-nguyen-tac-cham-soc-ban-chan-tai-nha-cho-nguoi-benh-dai-thao-duong-co-video-minh-hoa-20211221235517384.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='image-main-header']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
				},

		"doanhnghieptiepthi": {
						"name_page": "doanhnghieptiepthi",
						"domain": "https://doanhnghieptiepthi.vn/",
						"name_case": "check page doanhnghieptiepthi.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='home__news-sticky']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='home__news-item-sub-sticky']/div[1]/h3/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='ykcb']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail__title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "click_tag_post",
								"name_case": "event click on post",
								"locator_tag_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail__tag']/a[1]",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "verify_tag_post",
								"name_case": "check tag display post",
								"locator_verify_tag": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box__ir-content']/h3/a",
										"type_get_element": {
															"type": "wait",
															"action": "plural_presence"
															},
										"action": "bool",
										},
							},

							{
								"name_func": "click_find_button",
								"name_case": "click n??t hi???n tr?????ng t??m ki???m",
								"locator_find_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='headerSearchSubmit']",
										"type_get_element": {"type": "wait"},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='headerSearch']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='headerSearchSubmit']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box__ir-content']/h3",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://doanhnghieptiepthi.vn/video/ky-niem-5-nam-thanh-lap-van-phong-dai-dien-hau-giang-tap-chi-doanh-nghiep-va-tiep-thi-43888.htm",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@class='overlay-ad']","//*[@id='context-stats']/div[4]/div[2]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[1]",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://doanhnghieptiepthi.vn/bat-dong-san-thuoc-do-tai-san-dang-cap-song-cua-gioi-thuong-luu-161221024141924007.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='VCSortableInPreviewMode']/div/a",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://doanhnghieptiepthi.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='wrapper has-tab-bar']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://doanhnghieptiepthi.vn/video/ky-niem-5-nam-thanh-lap-van-phong-dai-dien-hau-giang-tap-chi-doanh-nghiep-va-tiep-thi-43888.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@class='DoanhNghiepTiepThiPlayer-loading-vid-icon']",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://doanhnghieptiepthi.vn/bat-dong-san-thuoc-do-tai-san-dang-cap-song-cua-gioi-thuong-luu-161221024141924007.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='VCSortableInPreviewMode']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"ictvietnam": {
						"name_page": "ictvietnam",
						"domain": "https://ictvietnam.vn/",
						"name_case": "check page ictvietnam.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='main']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='ktobarR']/div[1]/h3/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='ex_detail_title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "click_find_button",
								"name_case": "click n??t hi???n tr?????ng t??m ki???m",
								"locator_find_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='search-form']/button",
										"type_get_element": {"type": "wait"},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='search']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='search-form']/button",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-title']/h3/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},
							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://ictvietnam.vn/cong-nghe-thuc-te-ao-tao-buoc-ngoat-tren-cac-giang-duong-2021060811170363.htm",
								"name_time": "start_time_3",
							},
							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[3]/div[2]","//*[@id='context-stats']/div[4]/button[1]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://ictvietnam.vn/gapowork-chinh-thuc-trien-khai-dich-vu-cho-ngan-hang-bidv-2022102414382741.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail-thumb-image']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://ictvietnam.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admWrapsite']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://ictvietnam.vn/cong-nghe-thuc-te-ao-tao-buoc-ngoat-tren-cac-giang-duong-2021060811170363.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-category-item box-category-item-first']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"phapluat": {
						"name_page": "phapluat.suckhoedoisong",
						"domain": "https://phapluat.suckhoedoisong.vn/",
						"name_case": "check page ictvietnam.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='layout__content']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='layout__sticky-bitem']/div/a[1]",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "/html/body/div[2]/div/div[1]/div[1]/h1",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "click_tag_post",
								"name_case": "event click on post",
								"locator_tag_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail__tag']/a[1]",
										"type_get_element": {"type": "wait",
										                     "action": "plural_presence"},
										},
							},
							{
								"name_func": "verify_tag_post",
								"name_case": "check tag display post",
								"locator_verify_tag": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='loadListData']/div/div/h3/a",
										"type_get_element": {
															"type": "wait",
															"action": "plural_presence"
															},
										"action": "bool",
										},
							},
							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
									"type": ["XPATH", "SELECTOR"],
									"script": ["//*[@id='Capa_1']"],
									"type_action": "move_element",
									"type_get_element": {
										"type": "wait",
										"action": "singular_presence"
									},
								},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='headerSearch']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='headerSearchSubmit']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='content']/h3/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://phapluat.suckhoedoisong.vn/ta-hoa-khi-biet-co-rang-moc-trong-hoc-mui-sau-khi-di-kham-162221019152553474.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='VCSortableInPreviewMode']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://phapluat.suckhoedoisong.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='wrapper has-tab-bar']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://phapluat.suckhoedoisong.vn/nhung-bieu-hien-canh-bao-benh-nguy-hiem-o-phu-nu-tuoi-trung-nien-162221023080933682.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://phapluat.suckhoedoisong.vn/gia-han-giay-dang-ky-luu-hanh-cho-55-loai-thuoc-va-nguyen-lieu-lam-thuoc-162221024095753934.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508836643367579648']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"truyenhinhvov": {
						"name_page": "truyenhinhvov",
						"domain": "https://truyenhinhvov.vn/",
						"name_case": "check page truyenhinhvov.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-focus-bg']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-focus-sticky']/div/div/div[1]/h3",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='ykcb']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "click_tag_post",
								"name_case": "th???c hi???n click v??o b??i vi???t",
								"locator_tag_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail-tag-list']/li[1]",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "verify_tag_post",
								"name_case": "check tag b??i vi???t ???? hi???n th??? b??i ????ng ch??a",
								"locator_verify_tag": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-list-focus-content']/h2/a",
										"type_get_element": {
															"type": "wait",
															"action": "plural_presence"
															},
										"action": "bool",
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='headerSearch']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='headerSearchSubmit']/span",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-list-focus-content']/h2/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://truyenhinhvov.vn/video/man-nhan-chung-kien-ca-voi-xanh-san-moi-o-vung-bien-de-gi-binh-dinh-42855.htm",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[4]/div[1]/div"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://truyenhinhvov.vn/thai-lan-siet-chat-kiem-soat-su-dung-cay-can-sa-va-gai-dau-trong-thuc-pham-164221024150208901.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508912989417431040']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://truyenhinhvov.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admwrapper']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://truyenhinhvov.vn/video/man-nhan-chung-kien-ca-voi-xanh-san-moi-o-vung-bien-de-gi-binh-dinh-42855.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://truyenhinhvov.vn/thai-lan-siet-chat-kiem-soat-su-dung-cay-can-sa-va-gai-dau-trong-thuc-pham-164221024150208901.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='VCSortableInPreviewMode']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"sotttt": {
						"name_page": "sotttt",
						"domain": "https://sotttt.hanoi.gov.vn/",
						"name_case": "check page sotttt.hanoi.gov.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='main-content']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box_hot_news']/div[2]/a",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='_2_WAR_portalcmsappportlet_keywords']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='_2_WAR_portalcmsappportlet_search']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='news-list4 ']/div/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://sotttt.hanoi.gov.vn/tin-tuc-su-kien/-/view_content/4452944-dang-uy-co-quan-so-thong-tin-va-truyen-thong-trao-huy-hieu-30-nam-tuoi-dang-cho-2-dang-vien.html",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='_101_4452944']/div[2]/p[1]/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://sotttt.hanoi.gov.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='main-content']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://sotttt.hanoi.gov.vn/tin-tuc-su-kien/-/view_content/4452944-dang-uy-co-quan-so-thong-tin-va-truyen-thong-trao-huy-hieu-30-nam-tuoi-dang-cho-2-dang-vien.html",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='_101_4452944']/div[2]/p[1]/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"nhandaovtv": {
				"name_page": "nhandaovtv",
				"domain": "https://nhandaovtv.vn/",
				"name_case": "check page nhandaovtv.vn",
				"scan": 10,
				"step": [
					{
						"name_func": "check_open_page",
						"name_time": "start_time_1",
					},
					{
						"name_func": "check_verify_open_page",
						"name_case": "verify display in pc",
						"locator": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='main video-page ']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool",
								},

						"name_time": "end_time_1",
						"time_check": 5,
					},

					{
						"name_func": "click_on_post",
						"locator_on_post": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='home__fv-scroll']/div[1]/div/a",
								"type_get_element": {"type": "wait"},
								},

						"name_time": "start_time_2",
					},
					{
						"name_func": "verify_box_cmt",
						"name_case": "verify box comment",
						"locator_box_comment": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='fb-comments fb_iframe_widget fb_iframe_widget_fluid_desktop']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								},
								"action": "bool",
								},

						"name_time": "end_time_2",
						"time_check": 5,
					},
					{
						"name_func": "get_text_on_post",
						"name_case": "get text post check search",
						"locator_get_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='detail-title']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_presence"
								},
								},
					},

					{
						"name_func": "input_text_check_find",
						"name_case": "input text find",
						"locator_input_text": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='headerSearch']",
								"type_get_element": {
									"type": "wait",
									"action": "singular_visibility"
								}
								},
					},
					{
						"name_func": "click_search_button",
						"name_case": "click button search",
						"locator_search_button": {
								"type": ["XPATH", "SELECTOR"],
								"script": "//*[@id='headerSearchSubmit']",
								"type_get_element": {"type": "wait"},
								},
					},
					{
						"name_func": "check_verify_post_find",
						"name_case": "verify post find",
						"locator_post_search": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@id='loadDataItem']/div/div/a",
								"type_get_element": {
									"type": "wait",
									"action": "plural_presence"
								},
								},

					},
					{
						"name_func": "open_link_check_image",
						"name_case": "open link post check image",
						"link_check_image": "https://nhandaovtv.vn/thu-tuong-pham-minh-chinh-chung-tay-vi-nguoi-ngheo-bang-ca-trai-tim-va-su-thau-hieu-168221018155956301.htm",
						"name_time": "start_time_4",
					},
					{
						"name_func": "check_verify_image",
						"name_case": "verify image in mobile",
						"locator_verify_image": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class ='VCSortableInPreviewMode noCaption']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},

						"name_time": "end_time_4",
						"time_check": 3,
					},

					{
						"name_func": "check_open_page_mobile",
						"name_case": "check open page in mobile",
						"link_open_page_mobile": "https://nhandaovtv.vn/",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "check_verify_open_page_mobile",
						"name_case": "verify open page in mobile",
						"locator_verify_page_mobile": {
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class='main video-page ']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
						"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

					{
						"name_func": "open_link_check_image_mobile",
						"name_case": "open link image in mobile",
						"link_check_image_mobile": "https://nhandaovtv.vn/doan-dai-bieu-nguoi-co-cong-tinh-bac-lieu-tham-bo-lao-dong-thuong-binh-va-xa-hoi-168221017135515091.htm",
						"name_time": "start_time_1",
						'mobile': True,
					},
					{
						"name_func": "verify_display_image_mobile",
						"name_case": "verify image in mobile",
						"locator_verify_image_mobile":{
								"type": ["XPATH", "SELECTOR"],
								"script" : "//*[@class = 'VCSortableInPreviewMode noCaption']",
								"type_get_element": {
													"type": "wait",
													"action": "singular_visibility"
													},
								"action": "bool"
								},
						"name_time": "end_time_1",
						"time_check": 5,
						'mobile': True,
					},

				]
			},

		"hoadatviet": {
						"name_page": "hoadatviet",
						"domain": "https://hoadatviet.phunuvietnam.vn/",
						"name_case": "check page hoadatviet.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-home-focus']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-home-focus']/div/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='ykcb']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='header__search-layout']/input",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@class ='header__search-layout']/a",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='box-stream-item']/h2/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://hoadatviet.phunuvietnam.vn/ba-me-tre-cho-2-con-gai-di-giut-co-hon-vui-la-chinh-20220813142637865.htm",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[3]/div[2]","//*[@id='context-stats']/div[4]/button[1]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[4]/div[1]",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://hoadatviet.phunuvietnam.vn/kon-tum-tang-qua-cho-phu-nu-ngheo-bien-gioi-20221020152305118.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='media']/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://hoadatviet.phunuvietnam.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class= 'box-home-focus']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://hoadatviet.phunuvietnam.vn/ba-me-tre-cho-2-con-gai-di-giut-co-hon-vui-la-chinh-20220813142637865.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},

							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
									"type": ["XPATH", "SELECTOR"],
									"script": "//*[@id='context-stats']/div[3]/div[2]",
									"type_get_element": {"type": "wait"},
								},
								'mobile': True,
							},
							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]/div",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
						},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://hoadatviet.phunuvietnam.vn/de-nghi-bo-sung-che-do-dai-ngo-nhan-luc-y-te-vung-dong-bao-dan-toc-thieu-so-mien-nui-20221024113148176.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : " //*[@class='media']/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"kenhvtc9": {
						"name_page": "kenhvtc9",
						"domain": "https://kenhvtc9.vn/",
						"name_case": "check page kenhvtc9.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box top-content']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='text-30 text-white bold']",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='ykcb']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class = 'header-info-category-search']/input",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@class = 'header-info-category-search']/a/i",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class = 'text-30 text-white bold']",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://kenhvtc9.vn/dau-bep-nguyen-thanh-nam-ke-cau-chuyen-mon-an-qua-lang-kinh-nhiep-anh-170220921171328911.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='VCSortableInPreviewMode']/div/a",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://kenhvtc9.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='app']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://kenhvtc9.vn/dau-bep-nguyen-thanh-nam-ke-cau-chuyen-mon-an-qua-lang-kinh-nhiep-anh-170220921171328911.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_496986010748256256']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"thegioitiepthi": {
						"name_page": "thegioitiepthi",
						"domain": "https://thegioitiepthi.danviet.vn/",
						"name_case": "check page thegioitiepthi.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='body home-page']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='app']/section/div[2]/div[1]/div/div/div[1]/div/div[1]/div/h2/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='ykcb']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='app']/header/div/div[2]/input",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='app']/header/div/div[2]/input",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-category-middle']/div/div/h3/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://tv.danviet.vn/quang-ngai-lien-tuc-phat-canh-bao-ve-dot-mua-lon-lien-tiep-noi-duoi-nhau-20221012155751177.htm",
								"name_time": "start_time_3",
							},
							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
									"type": ["XPATH", "SELECTOR"],
									"script": ["//*[@id='context-stats']/div[3]/div[2]", "//*[@id='context-stats']/div[4]/button[1]"],
									"type_action": "move_element",
									"type_get_element": {
										"type": "wait",
										"action": "singular_presence"
									},
								},
							},

							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://kenhvtc9.vn/dau-bep-nguyen-thanh-nam-ke-cau-chuyen-mon-an-qua-lang-kinh-nhiep-anh-170220921171328911.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='VCSortableInPreviewMode']/div/a",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://thegioitiepthi.danviet.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box top-content']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://tv.danviet.vn/quang-ngai-lien-tuc-phat-canh-bao-ve-dot-mua-lon-lien-tiep-noi-duoi-nhau-20221012155751177.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},
							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='context-stats']/div[3]/div[1]",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://thegioitiepthi.danviet.vn/nguoi-chan-nuoi-can-trong-tai-dan-phuc-vu-tet-20221024185719625.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='divfirst']/figure/div/a/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"covid19": {
						"name_page": "check page covid19",
						"domain": "https://covid19.gov.vn/",
						"name_case": "check page covid19.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admwrapper']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='home__focus-flex']/div/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='detail-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
									"type": ["XPATH", "SELECTOR"],
									"script": ["//*[@class='form-search']"],
									"type_action": "move_element",
									"type_get_element": {
										"type": "wait",
										"action": "singular_presence"
									},
								},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='input-search input-search-text']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@class='input-search input-search-text']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-stream-content']/h2/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},
							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://covid19.gov.vn/phong-chong-dich-covid-19-tai-cho-sieu-thi-trung-tam-thuong-mai-171220427160149408.htm",
								"name_time": "start_time_3",
							},
							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[3]/div[2]","//*[@id='context-stats']/div[3]/div[1]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://covid19.gov.vn/thu-tuong-trao-quyet-dinh-bo-nhiem-bo-truong-bo-y-te-dao-hong-lan-171221022203641659.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508273119160709120']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://covid19.gov.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='home__focus-flex']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://covid19.gov.vn/phong-chong-dich-covid-19-tai-cho-sieu-thi-trung-tam-thuong-mai-171220427160149408.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://covid19.gov.vn/thu-tuong-trao-quyet-dinh-bo-nhiem-bo-truong-bo-y-te-dao-hong-lan-171221022203641659.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508273119160709120']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"giadinh": {
						"name_page": "check page giadinh",
						"domain": "https://giadinh.suckhoedoisong.vn/",
						"name_case": "check page giadinh.suckhoedoisong.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admWrapsite']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='home-box-scroll']/div[1]/h2/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='detail-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='ykcb']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},
							{
								"name_func": "click_tag_post",
								"name_case": "click on tag",
								"locator_tag_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail-tag-list']/li[1]/a",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "verify_tag_post",
								"name_case": "check tag b??i vi???t ???? hi???n th??? b??i ????ng ch??a",
								"locator_verify_tag": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-category-item box-category-item-first']/h3/a",
										"type_get_element": {
															"type": "wait",
															"action": "plural_presence"
															},
										"action": "bool",
										},
							},
							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='header__search header-search']/input",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@class='header__search header-search']/input",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-category-content']/h3/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},
							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://giadinh.suckhoedoisong.vn/chuyen-gia-huong-dan-cac-bac-phu-huynh-cach-cham-soc-mat-cho-tre-mac-tat-khuc-xa-tai-nha-17222102317322179.htm",
								"name_time": "start_time_3",
							},
							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@class ='GiaDinhNetPlayer-loading-vid-icon']", "//*[@class ='btn_toggle_skin2']"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://giadinh.suckhoedoisong.vn/bac-ninh-mau-thuan-tinh-ai-nam-thanh-nien-chem-ban-gai-cu-va-tinh-dich-guc-tai-quan-cat-toc-172221024235126019.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_509045541880262656']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://giadinh.suckhoedoisong.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='main']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://giadinh.suckhoedoisong.vn/chuyen-gia-huong-dan-cac-bac-phu-huynh-cach-cham-soc-mat-cho-tre-mac-tat-khuc-xa-tai-nha-17222102317322179.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://giadinh.suckhoedoisong.vn/chuyen-gia-huong-dan-cac-bac-phu-huynh-cach-cham-soc-mat-cho-tre-mac-tat-khuc-xa-tai-nha-17222102317322179.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='media VCSortableInPreviewMode ']/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"bvhttdl": {
						"name_page": "check page bvhttdl",
						"domain": "https://bvhttdl.gov.vn/",
						"name_case": "check page bvhttdl.gov.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='wrapper']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='slideshow-1']/div/a/span[2]/span[2]",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "//*[@class='title']",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='_searchInput']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='_searchInput']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='content-right left']/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},
							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://bvhttdl.gov.vn/video.htm",
								"name_time": "start_time_3",
							},
							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[4]/button[1]","//*[@id='context-stats']/div[4]/div[5]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://bvhttdl.gov.vn/to-chuc-hoi-nghi-hoi-thao-pho-bien-cac-quy-dinh-phap-luat-ve-quyen-tac-gia-quyen-lien-quan-tren-moi-truong-so-20221024161741868.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508931529471254528']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://giadinh.suckhoedoisong.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='home__top-focus']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://bvhttdl.gov.vn/video.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://bvhttdl.gov.vn/cung-co-viec-thuc-thi-quyen-so-huu-tri-tue-trong-linh-vuc-van-hoa-va-sang-tao-o-viet-nam-20221024214028027.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508922874235912192']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"cungcau": {
						"name_page": "check page giadinh",
						"domain": "https://cungcau.vn/",
						"name_case": "check page cungcau.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admWrapsite']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='contain__first--box2__left--news']/div[1]/h3/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail__title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admWrapsite']/div[2]/div[2]/div/div[2]/div[1]/input",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='admWrapsite']/div[2]/div[2]/div/div[2]/div[1]/input",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='search__item']/div/h2/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},
							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://cungcau.vn/video/4-cay-cau-thu-thiem-bac-qua-song-sai-gon-hien-gio-ra-sao-43901.htm",
								"name_time": "start_time_3",
							},
							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@class='qltnscungcau-loading-vid-icon']", "//*[@class='btn_toggle_skin2']"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://cungcau.vn/giam-doc-iea-the-gioi-dang-o-trong-cuoc-khung-hoang-nang-luong-thuc-su-dau-tien-174221025122218186.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_509234204416159744']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://cungcau.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admWrapsite']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://cungcau.vn/video/4-cay-cau-thu-thiem-bac-qua-song-sai-gon-hien-gio-ra-sao-43901.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@class='qltnscungcau-loading-vid-icon']",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://cungcau.vn/giam-doc-iea-the-gioi-dang-o-trong-cuoc-khung-hoang-nang-luong-thuc-su-dau-tien-174221025122218186.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_509234204416159744']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"congdankhuyenhoc": {
						"name_page": "check page congdankhuyenhoc",
						"domain": "https://congdankhuyenhoc.vn/",
						"name_case": "check page congdankhuyenhoc.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='main']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='box-category-item-first ']/a/img",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='detail-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "click_tag_post",
								"name_case": "th???c hi???n click v??o b??i vi???t",
								"locator_tag_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='detail__tab-list']/a",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "verify_tag_post",
								"name_case": "check tag b??i vi???t ???? hi???n th??? b??i ????ng ch??a",
								"locator_verify_tag": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='box-category-content']/h3/a",
										"type_get_element": {
															"type": "wait",
															"action": "plural_presence"
															},
										"action": "bool",
										},
							},
							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='btn-input txt-search']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@class ='btn-input txt-search']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class ='box-category-item ']/div/h3/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},
							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://congdankhuyenhoc.vn/media.htm",
								"name_time": "start_time_3",
							},
							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@id='context-stats']/div[3]/div[2]", "//*[@id='context-stats']/div[4]/div[1]"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://congdankhuyenhoc.vn/tong-bi-thu-nguyen-phu-trong-se-tham-chinh-thuc-cong-hoa-nhan-dan-trung-hoa-tu-ngay-30-10-2-11-2022-179221025100302217.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_509197144885096448']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},
							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://congdankhuyenhoc.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='home__focus']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://congdankhuyenhoc.vn/media.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://congdankhuyenhoc.vn/tong-bi-thu-nguyen-phu-trong-se-tham-chinh-thuc-cong-hoa-nhan-dan-trung-hoa-tu-ngay-30-10-2-11-2022-179221025100302217.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_509197144885096448']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
							},

		"podcast_tuoitre": {
						"name_page": "check page podcast",
						"domain": "https://podcast.tuoitre.vn/",
						"name_case": "check page podcast.tuoitre.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='content']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='podCastFocusTop']/div/a",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='podCastFocusTop']/div/div/h3/a",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='txt-search']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@class='txt-search']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-category-link-title']",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},
							},
							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://podcast.tuoitre.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='content']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='lstDataItem']/div[1]/div[1]/a/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"cuoituoitre": {
						"name_page": "cuoi.tuoitre",
						"domain": "https://cuoi.tuoitre.vn/",
						"name_case": "check page cuoi.tuoitre.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='admWrapsite']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='section border-bottom-red']/div/div[2]/article[1]/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='top-art']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "click_find_button",
								"name_case": "click n??t hi???n tr?????ng t??m ki???m",
								"locator_find_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@class='icon icon-search-black']",
										"type_get_element": {"type": "wait"},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='txt-search']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@class='txt-search']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='art-right art-7 news-item']/div/h3/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://cuoi.tuoitre.vn/video.htm",
								"name_time": "start_time_3",
							},

							{
								"name_func": "move_mouse_check_play",
								"name_case": "move_mouse_check_play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@class='TuoiTrePlayer-loading-vid-icon']","//*[@class='btn_toggle_skin2']"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "check_time_play_video",
								"name_case": "verify time play video",
								"locator_start_video": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='customSkin-currenttime']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://cuoi.tuoitre.vn/co-dat-cung-an-kieng-20221024171303402.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_a401e710-5384-11ed-aa4f-cb3eec60e752']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},
							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://cuoi.tuoitre.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='content']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://cuoi.tuoitre.vn/video.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@class='TuoiTrePlayer-loading-vid-icon']",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},

							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='customSkin-currenttime']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},

							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://cuoi.tuoitre.vn/co-dat-cung-an-kieng-20221024171303402.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_a401e710-5384-11ed-aa4f-cb3eec60e752']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"cuoituan": {
						"name_page": "cuoituan.tuoitre",
						"domain": "https://cuoituan.tuoitre.vn/",
						"name_case": "check page cuoituan.tuoitre.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='app']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='h1']/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='fck-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "click_find_button",
								"name_case": "click n??t hi???n tr?????ng t??m ki???m",
								"locator_find_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='app']/div[1]/div[1]/div[1]/div/ul/li/a/span",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='txtSearch']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "enter_find_text",
								"name_case": "enter find text",
								"locator_enter_find": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='txtSearch']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='art-right-one news-item']/div[2]/div/a",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://cuoituan.tuoitre.vn/am-nhac-phan-chien-khi-tre-em-chet-chung-co-lon-nua-dau-1634134.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='fr-img-wrap']/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},
							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://cuoituan.tuoitre.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='content']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://cuoituan.tuoitre.vn/am-nhac-phan-chien-khi-tre-em-chet-chung-co-lon-nua-dau-1634134.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='fr-img-wrap']/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"truyenhinhthanhhoa": {
						"name_page": "truyenhinhthanhhoa",
						"domain": "https://truyenhinhthanhhoa.vn/",
						"name_case": "check page truyenhinhthanhhoa.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='headerSticky']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='section__home-focus']/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "open_link_check_video",
								"name_case": "open link check video",
								"link_check_video": "https://truyenhinhthanhhoa.vn/thach-thanh-vinh-loc-som-hoan-thanh-viec-ho-tro-dong-bao-sinh-song-tren-song-len-bo-180221024204435219.htm",
								"name_time": "start_time_3",
							},
							{
								"name_func": "move_mouse_check_play",
								"name_case": "move mouse check play",
								"locator_move_mouse": {
										"type": ["XPATH", "SELECTOR"],
										"script" : ["//*[@class='qltnstruyenhinhthanhhoa-loading-vid-icon']","//*[@class='btn_toggle_skin2']"],
										"type_action": "move_element",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "open_link_check_image",
								"name_case": "open link post check image",
								"link_check_image": "https://truyenhinhthanhhoa.vn/thach-thanh-vinh-loc-som-hoan-thanh-viec-ho-tro-dong-bao-sinh-song-tren-song-len-bo-180221024204435219.htm",
								"name_time": "start_time_4",
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508999623165870080']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},
							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://truyenhinhthanhhoa.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='main']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "open_link_check_video_mobile",
								"name_case": "open link video in mobile",
								"link_check_video_mobile": "https://truyenhinhthanhhoa.vn/dai-bieu-quoc-hoi-thanh-hoa-thao-luan-tai-hoi-truong-va-o-to-180221024192140532.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "click_play_video_mobile",
								"name_case": "click play video",
								"locator_click_video_mobile": {
														"type": ["XPATH", "SELECTOR"],
														"script": "//*[@id='context-stats']/div[3]/div[2]",
														"type_get_element": {"type": "wait"},
														},
								'mobile': True,
							},
							{
								"name_func": "check_time_play_video_mobile",
								"name_case":"check action video in mobile",
								"locator_start_video_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='current-time-display']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
								'mobile': True,
								"name_time": "end_time_4",
								"time_check": 5,
							},
							{
								"name_func": "open_link_check_image_mobile",
								"name_case": "open link image in mobile",
								"link_check_image_mobile": "https://truyenhinhthanhhoa.vn/ky-ket-quy-che-phoi-hop-trong-cong-tac-phong-chong-tham-nhung-tieu-cuc-180221024192922668.htm",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='img_508979780358594560']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"podcast_nld": {
						"name_page": "danviet",
						"domain": "https://podcast.nld.com.vn/",
						"name_case": "check page podcast.nld.com.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='main']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='main']/div[2]/div/div/div/div[2]/div[1]/a/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='title-flex']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='navSearch']/span",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='search-text']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@id='navSearch']/span",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='navSearch']/span",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},

							},
							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://podcast.nld.com.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='main']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='home__box-new']/div/div/div[2]/div[1]/a/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"chamsocnguoicaotuoi": {
						"name_page": "chamsocnguoicaotuoi",
						"domain": "https://chamsocnguoicaotuoi.vn/",
						"name_case": "check page chamsocnguoicaotuoi.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='outer-wrap']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='post-758']/div/div[1]/a/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},
							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='post-758']/div/header/h2",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='comments']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='single-post-title entry-title']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://chamsocnguoicaotuoi.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='wrap']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@id='post-758']/div/div[1]/a/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

		"tapchigiaothong": {
						"name_page": "tapchigiaothong",
						"domain": "https://tapchigiaothong.vn/",
						"name_case": "check page tapchigiaothong.vn",
						"scan": 10,
						"step": [
							{
								"name_func": "check_open_page",
								"name_time": "start_time_1",
							},
							{
								"name_func": "check_verify_open_page",
								"name_case": "verify display in pc",
								"locator": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='body home']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool",
										},

								"name_time": "end_time_1",
								"time_check": 5,
							},
							{
								"name_func": "check_verify_image",
								"name_case": "verify image in mobile",
								"locator_verify_image": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box flex']/a/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},

								"name_time": "end_time_4",
								"time_check": 3,
							},

							{
								"name_func": "click_on_post",
								"locator_on_post": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/h2/a",
										"type_get_element": {"type": "wait"},
										},

								"name_time": "start_time_2",
							},
							{
								"name_func": "verify_box_cmt",
								"name_case": "verify box comment",
								"locator_box_comment": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-comment']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										},
										"action": "bool",
										},

								"name_time": "end_time_2",
								"time_check": 5,
							},
							{
								"name_func": "get_text_on_post",
								"name_case": "get text post check search",
								"locator_get_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='detail-title title-1']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_presence"
										},
										},
							},

							{
								"name_func": "input_text_check_find",
								"name_case": "input text find",
								"locator_input_text": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='txt-search']",
										"type_get_element": {
											"type": "wait",
											"action": "singular_visibility"
										}
										},
							},
							{
								"name_func": "click_search_button",
								"name_case": "click button search",
								"locator_search_button": {
										"type": ["XPATH", "SELECTOR"],
										"script": "//*[@class='absolute btn-search']",
										"type_get_element": {"type": "wait"},
										},
							},
							{
								"name_func": "check_verify_post_find",
								"name_case": "verify post find",
								"locator_post_search": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='title-3']",
										"type_get_element": {
											"type": "wait",
											"action": "plural_presence"
										},
										},
							},
							{
								"name_func": "check_open_page_mobile",
								"name_case": "check open page in mobile",
								"link_open_page_mobile": "https://tapchigiaothong.vn/",
								"name_time": "start_time_1",
								'mobile': True,
							},
							{
								"name_func": "check_verify_open_page_mobile",
								"name_case": "verify open page in mobile",
								"locator_verify_page_mobile": {
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='body home']",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
								"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},
							{
								"name_func": "verify_display_image_mobile",
								"name_case": "verify image in mobile",
								"locator_verify_image_mobile":{
										"type": ["XPATH", "SELECTOR"],
										"script" : "//*[@class='box-link-title relative']/a/img",
										"type_get_element": {
															"type": "wait",
															"action": "singular_visibility"
															},
										"action": "bool"
										},
								"name_time": "end_time_1",
								"time_check": 5,
								'mobile': True,
							},

						]
					},

}

# data = json.dumps(case_test, indent= 4)
# print(data)













