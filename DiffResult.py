import re

class DiffResult:
	
	def __init__(self):
		self.files = []
		self.regions = 0
		self.lines_added = 0
		self.lines_deleted = 0
		self.function_calls = {}

	def add_to_list_of_files(self, file):
		self.files.append(file)

	def parse(self, line):
		if self.is_region(line):
			self.regions += 1
		elif self.is_file(line):
			files = line.split(" ")
			# Always diff --git between 2 files, so we can just do this?
			self.files.append(files[2].strip())
			self.files.append(files[3].strip())
		elif self.is_from_to_header(line):
			if (line.startswith("+++")):
				#assert self.files[-1] == line.split(" ")[1].strip()
				pass
			else:
				#assert self.files[-2] == line.split(" ")[1].strip()
				pass
		elif self.is_added_line(line):
			self.lines_added += 1
		elif self.is_deleted_line(line):
			self.lines_deleted += 1


	def is_region(self, line):
		return re.match(r"^@@ -(\d)+,(\d)+ \+(\d)+,(\d)+ @@(.*)?", line)

	def is_file(self, line):
		return re.match(r"^diff --git (.*)?", line)

	def is_from_to_header(self, line):
		return re.match(r"^(\+\+\+|\-\-\-)(.*)?", line)

	# Not robust yet
	def is_added_line(self, line):
		return re.match(r"^\+([^\+])", line)

	# Not robust yet
	def is_deleted_line(self, line):
		return re.match(r"^\-([^\-])", line)

	def __str__(self):
		contents = str({
			"Num regions": self.regions,
			"Num lines added": self.lines_added,
			"Num lines deleted": self.lines_deleted,
			"Num files in diffs": len(self.files)})
		return contents
