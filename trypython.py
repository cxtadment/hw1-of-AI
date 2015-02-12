from collections import OrderedDict
o = OrderedDict()
o[2.2] = 1
o['first'] = 123
o['second'] = 234


first_item = o.popitem(last=False)
print type(first_item[0])