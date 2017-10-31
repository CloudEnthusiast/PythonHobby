#!/usr/bin/python
print ('5 < N < 101\n15 < M < 303\n')

N=input('Enter rows(N):')
M=input('Enter columns(M):')

for i in range(1,N,2):
    print('{0:-^{m}}'.format('.|.'*i, m=M))

print('{0:-^{m}}'.format('WELCOME',m=M))

for i in range(N-2,0,-2):
    print('{0:-^{m}}'.format('.|.'*i, m=M))
