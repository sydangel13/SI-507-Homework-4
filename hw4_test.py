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

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        card = cards.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")

    def test_2_clubs(self):
        card = cards.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")

    def test_3_str_method(self):
        card = cards.Card(suit = 3, rank = 13)
        self.assertEqual(card.__str__(), "King of Spades")

    def test_4_deck(self):
        deck = cards.Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_5_deal(self):
        deck = cards.Deck()
        card_inst = deck.deal_card()
        self.assertIsInstance(card_inst, cards.Card)

    def test_6_fewer(self):
        deck = cards.Deck()
        len_cards = len(deck.cards)
        deck.deal_card()
        # deck.deal_card()
        self.assertEqual(len(deck.cards), (len_cards-1))

    def test_7_plus(self):
        deck = cards.Deck()
        len_cards = len(deck.cards)
        deck1 = deck.deal_card()
        deck.replace_card(deck1)
        self.assertEqual(len(deck.cards), len_cards)
    
    def test_8_not(self):
        deck = cards.Deck()
        len_cards = len(deck.cards)
        # for c in range(len(deck)):
        deck.replace_card(cards.Card())
        self.assertEqual(len(deck.cards), len_cards)
            




    




############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
