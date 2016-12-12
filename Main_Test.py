import unittest
from main import *

class Test(unittest.TestCase):
    def test_1(self):
        expected = "fjvj"
        actual = main("fjvj")
        self.assertEqual(expected, actual, "Error")

    def test_2(self):
        expected = "Hello, world!"
        actual = main("Hello, world!")
        self.assertEqual(expected, actual, "Error")

    def test_3(self):
        expected = "This is long sentence to test if our function runs properly"
        actual = main("This is long sentence to test if our function runs properly")
        self.assertEqual(expected, actual, "Error")

    def test_4(self):
        expected = "Hello, world! Lalalalalalalal. It will be very long string. jfjvjgrvnjbgjbegueguhgwioghigwig   n3guohgu3huo   bfgu3hgu3hgu3goh" \
                   "begirbgughuoh3uoh hg3uohuo3h3uogh ugh3uoh3uogh3uoh hguo3h5uogh35uoh orgh3uoh5ug3uogh"
        actual = main("Hello, world! Lalalalalalalal. It will be very long string. jfjvjgrvnjbgjbegueguhgwioghigwig   n3guohgu3huo   bfgu3hgu3hgu3goh" \
                   "begirbgughuoh3uoh hg3uohuo3h3uogh ugh3uoh3uogh3uoh hguo3h5uogh35uoh orgh3uoh5ug3uogh")
        self.assertEqual(expected, actual, "Error")

    def test_5(self):
        expected = "9695984"
        actual = main("9695984")
        self.assertEqual(expected, actual, "Error")

    def test_6(self):
        expected = "959685 858869 9594040 05050600 50404003 05050400 5050040 05050506060786959404030394959 9595949"
        actual = main("959685 858869 9594040 05050600 50404003 05050400 5050040 05050506060786959404030394959 9595949")
        self.assertEqual(expected, actual, "Error")

    def test_7(self):
        expected = "-7-5-4 %^& @3"
        actual = main("-7-5-4 %^& @3")
        self.assertEqual(expected, actual, "Error")

    def test_8(self):
        expected = "&*$( $($ $ ### $$$$($*%*%*  )@(#($($)#*$*$)%)*$%*%)%*)#*$)%*%)##%#++#_%_+#%_#+_#%)#%(#)%*)*#%)*%*#  %*#%)*# %"
        actual = main( "&*$( $($ $ ### $$$$($*%*%*  )@(#($($)#*$*$)%)*$%*%)%*)#*$)%*%)##%#++#_%_+#%_#+_#%)#%(#)%*)*#%)*%*#  %*#%)*# %")
        self.assertEqual(expected, actual, "Error")

    def test_9(self):
        expected = "Hrjvfjjj 5595995gbjnfn#########                     JRJJCJJ))))$$$$$$$$JCNJ5995j"
        actual = main("Hrjvfjjj 5595995gbjnfn#########                     JRJJCJJ))))$$$$$$$$JCNJ5995j")
        self.assertEqual(expected, actual, "Error")

    def test_10(self):
        expected = "                   "
        actual = main( "                   ")
        self.assertEqual(expected, actual, "Error")

    def test_11(self):
        expected = "kfkgkkkkkkkkknikn56n677777777777777nlvknvNMMMMMMMMMMMMMMMMmmmmmmmmmmmmmmm050066))))))))))))))))))))))))))))))))))))))))##############)#)$KFKFFNnfino5in6odc"
        actual = main( "kfkgkkkkkkkkknikn56n677777777777777nlvknvNMMMMMMMMMMMMMMMMmmmmmmmmmmmmmmm050066))))))))))))))))))))))))))))))))))))))))##############)#)$KFKFFNnfino5in6odc")
        self.assertEqual(expected, actual, "Error")

    def test_12(self):
        expected = "            5hH/2#3Gg       "
        actual = main( "            5hH/2#3Gg       ")
        self.assertEqual(expected, actual, "Error")