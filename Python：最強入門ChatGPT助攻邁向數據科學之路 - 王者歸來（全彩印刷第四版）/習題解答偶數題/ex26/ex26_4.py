# ex26_4.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
states = {'state':['北美', '南美', '歐洲',
                   '非洲', '亞洲'],
          '人口數':[3.8, 6.2, 7.4, 12.28, 45.45]}
statedf = pd.DataFrame(states, columns=['人口數'],
                      index=states['state'])
cum = statedf['人口數'].cumsum()
statedf['累加'] = cum
print(statedf)











