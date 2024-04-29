import matplotlib.pyplot as plt
import numpy as np
import math

n=np.arange(1,16)
log2n=np.log2(n)
nlog2n=n*np.log2(n)
n2=np.power(n,2)
n3=np.power(n,3)
n4=np.power(n,4)
twon=np.power(2,n)
fig,ax=plt.subplots()
ax.bar(n,log2n,label='log2n')
ax.bar(n, nlog2n,label='nlog2n')
ax.bar(n,n2,label='n^2')
ax.bar(n,n3,label='n^3')
ax.bar(n,n4,label='n^4')
ax.bar(n,twon,label='2^n')
ax.legend()
plt.show()