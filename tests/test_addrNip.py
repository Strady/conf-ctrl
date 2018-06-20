import unittest
import sys
sys.path.append('G:\\python\\conf&ctrl')
import addrNip


class TestCalc(unittest.TestCase):

    def test_calcAddr(self):
        result = addrNip.calcAddr('a18', 'a5', 'a1')
        self.assertEqual(result, '2:18:101:5:1:0')
        result = addrNip.calcAddr('a18', 'a10', 'a2')
        self.assertEqual(result, '2:18:102:10:2:0')
        result = addrNip.calcAddr('a19', 'a16', 'a3')
        self.assertEqual(result, '2:19:103:16:3:0')
        result = addrNip.calcAddr('a20', 'a21', 'a4')
        self.assertEqual(result, '2:20:104:21:4:0')

    def test_calcIP(self):
        self.assertEqual(addrNip.calcIP('a18', 'a5', 'a1'), ('10.71.118.1', '10.72.118.1'))
        self.assertEqual(addrNip.calcIP('a18', 'a10', 'a2'), ('10.71.118.22', '10.72.118.22'))
        self.assertEqual(addrNip.calcIP('a19', 'a16', 'a3'), ('10.71.119.61', '10.72.119.61'))
        self.assertEqual(addrNip.calcIP('a20', 'a21', 'a4'), ('10.71.120.82', '10.72.120.82'))

if __name__ == '__main__':
    unittest.main()