import random
r = random.randint(0, 100)
while True:
	g = input('在0~100之间猜猜看是哪个数字？: ')
	g = int(g)
	if r == g:
		print('恭喜你猜对了！')
		break
	elif r > g:
		print('你输入的值比正确答案小哦！')
	elif r < g:
		print('你输入的值比正确答案大哦！')



