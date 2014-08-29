"""
python requirements:
pyexecjs

other requirements:
node

"""


import execjs


print(execjs.eval('[1, 2, 4].indexOf(4)'))
print(execjs.eval('[1, 2, 4].indexOf(3)'))
