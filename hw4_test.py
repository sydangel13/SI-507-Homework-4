import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments


class EC1(unittest.TestCase):
    # Add methods below to test Extra Credit 1
    pass


class EC2(unittest.TestCase):
    # Add methods below to test Extra Credit 2
    pass

############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
