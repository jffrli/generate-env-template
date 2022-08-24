import sys, re

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 generate_env_template.py [source].py")
		return

	filename = sys.argv[1]
	if filename[-3:] != ".py":
		print("Usage: python3 generate_env_template.py [source].py")
		return

	lines = []
	try:
		with open(filename,"r") as f:
			lines = f.read().splitlines()

	except OSError as e:
		print(e)
		return

	'''
	Possibilities:
		env("x")
		
		[CASTS]
		env.str("x")
		env.bool("x")
		env.int("x")
		env.float("x")
		env.decimal("x")
		env.list("x")
		env.dict("x")
		env.json("x")
		env.datetime("x")
		env.date("x")
		env.time("x")
		env.timedelta("x")
		env.url("x")
		env.uuid("x")
		env.log_level("x")
		env.path("x")
		env.enum("x")
	
		[PREFIX]
		with env.prefixed("pre"):
			x = env("x")
	'''
	#prefix 
	prefix_regex = r"^(\s*)with env.prefixed\(\"([a-zA-Z0-9_\-]*)\"\):"

	for i in range(len(lines)):
		l = lines[i]

		prefix_match = re.search(prefix_regex, l)
		if (prefix_match):
			indentation = prefix_match.group(1)
			greater_indent = r''


if __name__ == '__main__':
	main()