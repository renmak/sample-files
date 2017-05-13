import logging
import time
import sys

keep_running = True
count = 0 

while keep_running:
	try:

		count += 1

		logging.basicConfig(filename='fake_logger.log', level=logging.INFO)

		logging.info(str(count) + ': Starting log generator program. To stop, hit ctrl + c')

		logging.debug(str(count) + ': This is a debug statement')

		logging.warning(str(count) + ': This is a debug statement')

		time.sleep(10)

	except KeyboardInterrupt:
		sys.exit(0)
	except:
		sys.exit(0)
	