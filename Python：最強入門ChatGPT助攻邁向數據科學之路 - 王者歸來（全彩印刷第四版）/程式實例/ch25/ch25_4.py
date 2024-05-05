# ch25_4.py
import numpy as np

x = np.arange(16).reshape(4,4)
np.savetxt('out25_4_1.txt',x,delimiter=',',header='out25_4_1.txt',
           footer='bye',fmt="%d")
np.savetxt('out25_4_2.txt',x,delimiter=',',header='out25_4_2.txt',
           footer='bye',fmt="%4.2f")













