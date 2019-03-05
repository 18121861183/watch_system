from django.test import TestCase

# Create your tests here.


_str = 'safe,online,'

print(_str.endswith(','), _str[:len(_str)-1])
