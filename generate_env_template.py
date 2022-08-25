import sys, re, os

def find_var_name(l):
	env_regex = r"env(\.(str|bool|int|float|decimal|list|dict|json|datetime|date|time|timedelta|url|uuid|log_level|path|enum))?\(\"([a-zA-Z0-9_\-]*)\"\)"
	matches = re.findall(env_regex,l)

	var_names = []
	for match in matches:
		var_names.append(match[2] + "=\n")
		
	return var_names

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 generate_env_template.py [source].py")
		return

	filename = sys.argv[1]
	if filename[-3:] != ".py":
		print("Usage: python3 generate_env_template.py [source].py")
		return

	path = os.path.split(filename)[0]

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
				#print("prefix search: " + lines[i])
				var_names = find_var_name(lines[i])
				for var_name in var_names:
					env_variables.append(prefix_match.group(2) + var_name)
				i += 1
			continue #to avoid incrementing twice
		else:
			var_names = find_var_name(l)
			env_variables.extend(var_names)
		i += 1

	#remove duplicates
	unique_envs = []
	[unique_envs.append(x) for x in env_variables if x not in unique_envs] #method 2 of https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/

	with open(os.path.join(path,"env.template"), "w") as f:
		f.writelines(unique_envs)

if __name__ == '__main__':
	main()