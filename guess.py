import random
i = 1
start = input('请输入范围的初始值: ')
if start.isdigit():
	end = input('请输入范围的结束值: ')
	if end.isdigit():
		start = int(start)
		end = int(end)
		r = random.randint(start, end)
		while True:
			g = input('猜猜看是哪个数字？: ')
			g = int(g)
			if r == g:
				print('恭喜你猜对了！ 你一共猜了', i, '次')
				break
			elif r > g:
				print('你输入的值比正确答案小哦！')
			elif r < g:
				print('你输入的值比正确答案大哦！')
			i = i + 1
	else:
		print('请输入整数')
else:
	print('请输入整数')
	


