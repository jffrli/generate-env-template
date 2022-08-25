import sys, re

def find_var_name(l):
	env_regex = r"=\s*env(\.(str|bool|int|float|decimal|list|dict|json|datetime|date|time|timedelta|url|uuid|log_level|path|enum))?\(\"([a-zA-Z0-9_\-]*)\"\)"
	match = re.search(env_regex,l)
	if not match:
		return None
	return match.group(3)

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

	#prefix 
	prefix_regex = r"^(\s*)with env.prefixed\(\"([a-zA-Z0-9_\-]*)\"\):"

	env_variables = []

	i = 0
	while i < len(lines):
		l = lines[i]

		prefix_match = re.search(prefix_regex, l)
		if (prefix_match):
			#print(prefix_match.group(1))
			#print(prefix_match.group(2))

			indentation = prefix_match.group(1)

			greater_indent = r"^"+ indentation+r"\s"
			i += 1
			while (re.search(greater_indent, lines[i])):
				var_name = find_var_name(lines[i])
	
				if var_name:
					env_variables.append(prefix_match.group(2) + var_name)
				i += 1	
		else:
			var_name = find_var_name(l)
			if var_name:
				env_variables.append(var_name)
		i += 1

	env_variables = [s + "=\n" for s in env_variables]

	with open("env.template", "w") as f:
		f.writelines(env_variables)

if __name__ == '__main__':
	main()