fp = open('output.txt')
data = []
correctChunk = 0
foundCorrect = 0
FP = 0
FN = 0
f = fp.read()
fp.close() 
d =f.split('\n')
data = []
for i in d:
    data.append(i.split('\t'))
for i in data:
	try:
		if i[2] == i[3]:
			correctChunk += 1
		elif i[2] == 'O':
			FP += 1
		else:
			FN += 1
	except:
		pass
precision = 100.0*correctChunk/(correctChunk + FN)
recall = 100.0*correctChunk/(correctChunk + FP)
F = 2 * precision * recall/ (precision + recall)

print "precision:\t",precision
print "recall:\t",recall
print "F:\t",F
