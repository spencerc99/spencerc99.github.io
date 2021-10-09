import unittest
import re
from find_linked_articles import ABSOLUTE_URL_REGEX, INTERNAL_ARTICLE_REGEX

class TestLinkedArticlesScript(unittest.TestCase):
    def test_regexes(self):
        line1 = '*This is the **64th** installment in my experiment of publishing raw, lightly edited mini-essays every day towards achieving 100 public pieces. Check out the rationale and the full list [here](/experiments/100posts/)*.'
        line2 = '*This is the **64th** installment in my experiment of publishing raw, lightly edited mini-essays every day towards achieving 100 public pieces. Check out the rationale and the full list [here](https://www.spencerchang.me/experiments/100posts/)*. [here](https://www.spencerchang.me/posts/100posts/)*.'
        line3 = '[here](/posts/100). anad something [blah](/experiments/100posts)'

        # relative article
        self.assertSequenceEqual(re.findall(INTERNAL_ARTICLE_REGEX, line1),
                        ['/experiments/100posts/'])
        self.assertSequenceEqual(re.findall(INTERNAL_ARTICLE_REGEX, line2),[])
        self.assertSequenceEqual(re.findall(INTERNAL_ARTICLE_REGEX, line3), [
            '/posts/100', '/experiments/100posts'])

        # absolute one
        self.assertSequenceEqual(re.findall(ABSOLUTE_URL_REGEX, line1),
                                 [])
        self.assertSequenceEqual(re.findall(ABSOLUTE_URL_REGEX, line2), [('[here](https://www.spencerchang.me/experiments/100posts/)', '/experiments/100posts/'), ('[here](https://www.spencerchang.me/posts/100posts/)', '/posts/100posts/')])
        self.assertSequenceEqual(re.findall(ABSOLUTE_URL_REGEX, line3), [])

if __name__ == '__main__':
    unittest.main()
