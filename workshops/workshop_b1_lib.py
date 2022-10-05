def rating_sol_f1():
	test = f1('hello', 4)
	asst = 'hello\nhello\nhello\nhello'
	c = test == asst
	if c:
		print('Test: Pass')
	else:
		print('Test: Not Pass')
	return 0

