import pyautogui as pg
import time
import keyboard
import cv2


def find_template_offset(main_image_path, template_image_path, threshold=0.8):
	# 读取图像
	main_image = cv2.imread(main_image_path)
	template = cv2.imread(template_image_path)

	if main_image is None or template is None:
		return None

	result = cv2.matchTemplate(main_image, template, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

	if max_val >= threshold:
		max_loc[0] += 10
		max_loc[1] += 10
		return max_loc
	else:
		return [0, 0]

def is_black_pixel_in_region(x, y, width, height):
	black_count = 0
	for i in range(x, x + width):
		for j in range(y, y + height):
			color = pg.pixel(i, j)
			if color[0] < 50 and color[1] < 50 and color[2] < 50:
				black_count += 1
				if black_count > 0:
					return True
	return False


def auto_pass():
	query_pos = find_template_offset("file/full_screen.png", "file/query.png")
	count = 0
	while True:
		pg.moveTo(1780, 485, duration=0.1)
		pg.click(button='left')
		time.sleep(0.3)
		pg.moveTo(1180, 250, duration=0.1)
		pg.click(button='left')

		pg.moveTo(680, 360, duration=0.1)
		pg.click(button='left')
		count += 1

		wait_time = 1
		while wait_time > 0:
			if keyboard.is_pressed("a"):  # a键暂停，s键继续，d键退出
				keyboard.wait("s")
			elif keyboard.is_pressed("d"):
				return
			time.sleep(0.1)
			wait_time -= 0.1

		if count % 5 == 0:
			pg.moveTo(query_pos[0], query_pos[1], duration=0.1)
			pg.click(button='left')
			time.sleep(1)

			if not is_black_pixel_in_region(245, 485, 5, 5):
				while True:
					pg.moveTo(1760, 350, duration=0.1)
					pg.click(button='left')

					wait_time = 2
					while wait_time > 0:
						if keyboard.is_pressed("a"):  # a键暂停，s键继续，d键退出
							keyboard.wait("s")
						elif keyboard.is_pressed("d"):
							return
						time.sleep(0.1)
						wait_time -= 0.1

					if is_black_pixel_in_region(245, 485, 5, 5):
						break


if __name__ == "__main__":
	auto_pass()
