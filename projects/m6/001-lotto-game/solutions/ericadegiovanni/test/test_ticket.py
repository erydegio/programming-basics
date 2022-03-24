import unittest
from lotto.ticket import Ticket
from lotto.bet import Bet

class TestTicket(unittest.TestCase):

    def setUp(self):

        self.bet_type = Bet('ambo', 2.00)
        self.nums = [1, 66, 43, 9, 8]
        self.city = 'bari'

    def test_ticket(self):
        ticket = Ticket(self.bet_type, self.nums, self.city, 1)
        self.assertEqual(ticket.bet_type, 'ambo')
        self.assertTrue(type(ticket.nums) is list )
        self.assertEqual(ticket.city, 'bari')
        

       

    