import sys
input_file = sys.argv[1]

f = open(input_file)
lines = f.readlines()

def cmd_string2dict(cmd_string):
	output_dict = {}
	array_cmd_string = cmd_string.split('-')
	array_cmd_string.pop(0)
	for each_cmd in array_cmd_string:
		cmd_key = each_cmd.split(' ')[0]
		cmd_value = each_cmd.split(' ')[1]
		output_dict[cmd_key] = cmd_value
	return output_dict
			


class CMD():
	def __init__(self, tcl, type, sub_type, arguments = None):
		self.tcl = tcl
		self.type = type
		self.sub_type = sub_type
		self.arguments = arguments
CMDset = []
for line in lines:
	if line[0] == '#':
		pass
	else:
		cmd = line.split('\n')[0].split(' ')[0]
		subcmd = line.split('\n')[0].split(' ')[1]
		if cmd == 'setup':
			if subcmd == 'design':
				CMDset.append(CMD(line.split('\n')[0], 'setup', 'design'))
		elif cmd == 'perform':
			if subcmd == 'pwrcal':
				CMDset.append(CMD(line.split('\n')[0], 'perform', 'pwrcal'))
			elif subcmd == 'emcheck':
				arguments_str = line.split('\n')[0].split('perform emcheck ')[1]
				newCMD = CMD(line.split('\n')[0], 'perform','emcheck')
				newCMD.arguments = cmd_string2dict(arguments_str)
				CMDset.append(newCMD)
			else:
				print 'not meet:'+subcmd
			
for eachCMD in CMDset:
	print 'tcl:'
	print eachCMD.tcl
	print 'cmd:'
	print eachCMD.type
	print 'subcmd:'
	print eachCMD.sub_type
	print 'arguments:'
	print eachCMD.arguments
	print '\n'

