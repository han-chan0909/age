driving = input('請問你有沒有開過車')
if driving != '有' or driving != '沒有':
	print ('只能輸入有或沒有')
	raise SystemExit
	
age = input('請問你的年齡')
age = int(age)
if driving == '有':
	if age >= 18:
		print ('你通過測驗了')
	else:
		print('奇怪,你怎麼會開過車')
elif driving == '沒有':
	if age >= 18:
		print('那可以去考駕照啦')
	else:
		print('很好,很快就可以靠駕照了')



