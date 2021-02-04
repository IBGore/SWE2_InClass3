import unittest
import calculator as c


class TestCase(unittest.TestCase):
    #Addition Tests
    def test_add(self):
        self.assertEqual(c.add(2, 1),3)

    def test_add2(self):
        self.assertEqual(c.add(1.1, 0),1.1)

    def test_add3(self):
        self.assertEqual(c.add(-1, 1),0)

    def test_add4(self):
        self.assertEqual(c.add(-10, -3),-13)

    #Subtraction Tests
    def test_sub(self):
        self.assertEqual(c.subtract(10, 9),1)

    def test_sub2(self):
        self.assertEqual(c.subtract(10, 2.5),7.5)

    def test_sub3(self):
        self.assertEqual(c.subtract(3, 5),-2)

    def test_sub4(self):
        self.assertEqual(c.subtract(2, -1),3)

    #Multiplication
    def test_mun(self):
        self.assertEqual(c.multiply(2, 1),2)

    def test_mul2(self):
        self.assertEqual(c.multiply(200, 0),0)

    def test_mul3(self):
        self.assertEqual(c.multiply(0, -3),0)

    def test_mul4(self):
        self.assertEqual(c.multiply(1.5, -1),-1.5)

    #division
    def test_div(self):
        self.assertEqual(c.divide(200, 1),200)

    def test_div2(self):
        self.assertEqual(c.divide(2, -2),-1)

    def test_div3(self):
        self.assertEqual(c.divide(5, 2),2.5)

    def test_div4(self):
        with self.assertRaises(ZeroDivisionError):
            c.divide(10,0)
        

    


if __name__ == '__main__':
    unittest.main(verbosity=2)