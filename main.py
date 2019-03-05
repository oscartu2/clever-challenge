import time
import os
from DiffResult import DiffResult

DIRECTORY = "./diffs/"
DIFF_EXTENSION = ".diff"

def main():
	#track_time()
	#print(compute_diff)
	print(compute_diff())

def compute_diff():
	dr = DiffResult()
	for file_name in os.listdir(DIRECTORY):
		if file_name.endswith(DIFF_EXTENSION):
			# dr.add_to_list_of_files(file_name)
			with open(DIRECTORY + str(file_name), 'r') as f:
				for line in f:
					dr.parse(line)
	return dr



if __name__ == '__main__':
	main()