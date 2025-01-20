import re

reString = "Shan ali mughal khan ha ksjk  is not important to tell any body that it " \
           "is not good so don't tell me what to do " \
           "0312041-9685" \
           "0312-5639631" \
           "03179350-107"

# com = re.compile(r'ali')
# com = re.compile(r'.ali')
# com = re.compile(r'^Shan ali')
# com = re.compile(r'07$')
# com = re.compile(r'1*2*')
# com = re.compile(r'12+')
# com = re.compile(r'an\b')
# com = re.compile(r'\d{7}-\d{4}')
# com = re.compile(r'\d{4}-\d{7}')
com = re.compile(r'\d{8}-\d{3}')

abc = com.finditer(reString)
for items in abc:
    print(items)
