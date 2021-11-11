def nextStep(steps, maxDistance, oldList):
	if len(steps) == 0 and oldList[0][1] == '':
		return 'IMPOSSIBLE'
	if len(steps) == 0:
		return oldList[0][1]

	step = steps[0]
	newList = [(1001, '')]*(maxDistance+1)
	
	for k in range(len(oldList)):
		if oldList[k][1] == '':
			continue

		down = k - step
		up = k + step
		
		if down >= 0:
			newOption = (oldList[k][0], oldList[k][1] + 'D')
			if newOption[0] < newList[down][0]:
				newList[down] = newOption
		
		if up < maxDistance:

			maxHeight = oldList[k][0]
			if up > maxHeight:
				maxHeight = up 

			if  maxHeight < newList[up][0]:
				newList[up] = (maxHeight, oldList[k][1] + 'U')

	return(nextStep(steps[1:], maxDistance, newList))



n = int(input())

for k in range(n):
	m = input()
	steps = list(map(int, input().split()))

	maxDistance = 0
	for num in steps:
		maxDistance += num

	myList = [(1001, '')]*(maxDistance+1)
	firstStep = steps[0]
	myList[firstStep] = (firstStep, 'U')
	print(nextStep(steps[1:], maxDistance, myList))