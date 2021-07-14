from array import array
import random as r 
import plotly_express as p
import plotly.figure_factory as pf



#print('the numbers are ' + str(num1) + ' and ' + str(num2))

res = []
#count = []

for i in range (0,100):
    num1 = r.randint(1,6)
    num2 = r.randint(1,6)


    res.append(num1 + num2)
  #  count.append(i)

fig = pf.create_distplot([res],['Result'])
fig.show()



