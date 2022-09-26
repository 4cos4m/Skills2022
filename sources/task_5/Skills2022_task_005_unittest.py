import unittest

def factors(n):
    p = 2
    f = list()
    while n >= p*p :
        if n % p == 0:
            f.append(p)
            n = int(n / p)
        else:
            p = p + 1
    f.append(n)
    return f

def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    else:
        return True

def vowels(text):
    v = list()
    for i in text:
        if i in 'aeiouAEIOU':
            v.append(i)
    return v

# https://habr.com/ru/company/otus/blog/481806/
class tests(unittest.TestCase):

    def test_factors(self):
        self.assertEqual(factors(19), [19])
        self.assertEqual(factors(12), [2, 2, 3])
        self.assertEqual(factors(54), [2, 2, 3])

    def test_is_prime(self):
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(4))

    def test_vowels(self):
        self.assertEqual(vowels("Gravity"), ['a','i'])

    def test_len(self):
        self.assertEqual(len([34,54,21,76,5]), 5)

if __name__ == '__main__':
    unittest.main()