import os
from datetime import datetime
import random

BASE_PATH = os.getcwd()
LOGS_FILE_NAME = 'logs.txt'

full_path = os.path.join(BASE_PATH, LOGS_FILE_NAME)

def make_logs(old_func):
	def range_func(*args, **kwargs):
		results = f'{old_func(*args, **kwargs)}'
		print('Лог записан')
		return results

	return range_func

@make_logs
def log_func(file_path, results):
	with open(file_path, 'a') as file:
		result = f'{datetime.now()} | {log_func.__name__} | {results} "\n"'
		file.write(result)

for i in range(10):
	log_func(full_path, random.randint(1,10))



def parametrized_logs(parameter):
	def make_logs(old_func):
		def range_func(*args, **kwargs):
			results = old_func(*args, **kwargs)
			print('Лог также записан')
			return results

		return range_func

	return make_logs

@parametrized_logs(parameter=full_path)
def log_func(file_path, results):
	with open(file_path, 'a') as file:
		result = f'{datetime.now()} | {log_func.__name__} | {results} "\n"'
		file.write(result)

for i in range(10):
	log_func(full_path, random.randint(1,10))
	# Куда необходимо добавить parameter? Потому что, если добавить в качестве аргумента в log_func, то он не видит и выходит ошибка
