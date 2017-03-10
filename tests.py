import unittest

import party



class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        party.app.config['TESTING'] = True
        self.client = party.app.test_client()


    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("I'm having a party", result.data)

    def test_no_rsvp_yet(self):
        # FIXME: Add a test to show we haven't RSVP'd yet
        result = self.client.get("/")
        # if session.get("rsvp") is None:
        #     print session
        self.assertIn("Please RSVP", result.data)
        self.assertNotIn("Party Details", result.data)
        print "FIXME"

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={'name': "Jane", 'email': "jane@jane.com"},
                                  follow_redirects=True)
        # FIXME: check that once we log in we see party details--but not the form!
        self.assertNotIn("Please RSVP", result.data)
        self.assertIn("Party Details", result.data)
        print "FIXME"

    def test_rsvp_mel(self):
        # FIXME: write a test that mel can't invite himself
        result = self.client.post("/rsvp",
                                  data={'name': "Mel Melitpolski", 'email': "mel@ubermelon.com"},
                                  follow_redirects=True)
        self.assertIn("Sorry, Mel. This is kind of awkward.", result.data)
        print "FIXME"


if __name__ == "__main__":
    unittest.main()