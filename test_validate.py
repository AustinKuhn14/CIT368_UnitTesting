from validate import Validate    # The code to test
import unittest   # The test framework

class Test_TestValidate(unittest.TestCase):
    def test_zip_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.zip("17701"))

    def test_zip_bad(self):
        #ABUSE
        f = open("blns.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.zip(str(line)))

    def test_minor_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.minor(15))

    def test_minor_bad(self):
        #ABUSE
        minor_test_values = ['five', -14, 999, None, 11.5, ' ']
        for age in minor_test_values:
            self.assertFalse(Validate.minor(age))

    def test_email_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.email("random@gmail.com"))

    def test_email_bad(self):
        #ABUSE
        email_test_values = ['info@gmail', '', None, 'plainaddress']
        for value in email_test_values:
            self.assertFalse(Validate.email(value))

    def test_lat_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.is_lat(81.9))
    
    def test_lat_bad(self):
        #ABUSE
        lat_test_values = [-91, 91, 150, -100, 'north', 'east']
        for value in lat_test_values:
            self.assertFalse(Validate.is_lat(value))

    def test_lng_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.is_lng(81.9))
    
    def test_lng_bad(self):
        #ABUSE
        lng_test_values = [-181, 181, -360, 200, 'west', 'south']
        for value in lng_test_values:
            self.assertFalse(Validate.is_lng(value))

    def test_domain_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.is_domain('google.com'))
    
    def test_domain_bad(self):
        #ABUSE
        domain_test_values = ['example', 'my-domain', 'example!.com', 'example.c']
        for value in domain_test_values:
            self.assertFalse(Validate.is_domain(value))
    
    def test_url_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.is_url('https://www.google.com/'))

    def test_url_bad(self):
        #ABUSE
        url_test_values = ['www.example.com/path', 'ftp://example.com/abc', 'http://example.1a/path']
        for value in url_test_values:
            self.assertFalse(Validate.is_url(value))

    def test_grade_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.grade(100, 'A'))
        self.assertTrue(Validate.grade(74, 'C'))
    
    def test_grade_bad(self):
        #ABUSE
        grade_test_values = ['C', 'A', 1000, '', '-99']
        for value in grade_test_values:
            self.assertFalse(Validate.grade(value))

    def test_ip_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.ip('192.168.1.1'))

    def test_ip_bad(self):
        #ABUSE
        ip_test_values = ['192.168.1', '192.168.0.1.5', 'ip.address.here']
        for value in ip_test_values:
            self.assertFalse(Validate.ip(value))

    def test_mac_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.mac('00:1A:2B:3C:4D:5E'))

    def test_mac_bad(self):
        #ABUSE
        mac_test_values = ['00:1A:2B:3C:4D:5E:6F', '00:1A:2B:3C:4D', '00_1A_2B_3C_4D_5E', '001A2B3C4D5E']
        for value in mac_test_values:
            self.assertFalse(Validate.mac(value))
    
    def test_md5_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.md5('5d41402abc4b2a76b9719d911017c592'))
        self.assertTrue(Validate.md5('E99A18C428CB38D5F260853678922E03'))

    def test_md5_bad(self):
        #ABUSE
        md5_test_values = ['!d41402abc4b2a76b9719d911017c592', '', 'thisisnotamd5hashvalue00000000000']
        for value in md5_test_values:
            self.assertFalse(Validate.md5(value))

if __name__ == '__main__':
    unittest.main()
