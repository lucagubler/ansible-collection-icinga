#!/usr/bin/python
  

from ansible.module_utils.basic import AnsibleModule

def main():
	module = AnsibleModule(
		argument_spec = dict(
			state              = dict(default='present', choices=['present', 'absent']),
			name               = dict(required=True),
			order              = dict(default=10, type='int'),
			file               = dict(default='features-available/checker.conf', type='str'),
			template           = dict(default=False, type='bool'),
			imports            = dict(default=list(), type='list', elements='str'),
			check_command      = dict(type='str'),
			address            = dict(type='str'),
			address6           = dict(type='str'),
			check_interval     = dict(type='str'),
			retry_interval     = dict(type='str'),
			max_check_attempts = dict(type='int'),
			_vars              = dict(default=dict(), type='raw', aliases=['vars']),
		)
	)

	args = module.params
	name = args.pop('name')
	order = args.pop('order')
	state = args.pop('state')
	file = args.pop('file')
	template = args.pop('template')
	imports = args.pop('imports')
	del args['_vars']

	module.exit_json(changed=False, args=args, name=name, order=str(order), state=state, file=file, template=template, imports=imports)

if __name__ == '__main__':
	main()
