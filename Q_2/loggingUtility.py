import logging

def Store_Log(write) :
	logging.basicConfig(filename='relation.log',filemode='w', datefmt='%d/%m/%Y %I:%M:%S %p', format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',level=logging.DEBUG)
	logging.info(write)
