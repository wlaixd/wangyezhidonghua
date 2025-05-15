import pyautogui as pg
import time
import keyboard

pg.scroll(50)

def check():
	pg.moveTo(1710, 440, duration=0.1)
	pg.click(button='left')
	time.sleep(0.5)

	pg.moveTo(1800, 1015, duration=0.1)
	pg.click(button='left')
	time.sleep(0.1)

	pg.moveTo(900, 510, duration=0.1)
	pg.click(button='left')

def main():
	count = 0
	while count < 100:
		check()
		temp = 0.5
		while temp > 0:
			if keyboard.is_pressed("s"):
				keyboard.wait("a")
				check()
			elif keyboard.is_pressed("d"):
				print(f"本次共审核{count}例样本")
				return
			time.sleep(0.1)
			temp -= 0.1

		# keyboard.wait("a")
		pg.moveTo(1170, 965, duration=0.1)
		pg.click(button='left')
		time.sleep(0.5)
		count += 1





if __name__ == "__main__":
	main()


