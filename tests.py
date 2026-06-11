class TestGetLedsOn(unittest.TestCase):

    def test_full_time_all_leds(self):
        self.assertEqual(get_leds_on(25 * 60, 25 * 60), 25)

    def test_half_time_half_leds(self):
        self.assertEqual(get_leds_on(25 * 30, 25 * 60), 12)

    def test_no_time_no_leds(self):
        self.assertEqual(get_leds_on(0, 25 * 60), 0)


class TestGetTimeLeft(unittest.TestCase):

    def test_25_minutes(self):
        self.assertEqual(get_time_left(25), 1500)

    def test_5_minutes(self):
        self.assertEqual(get_time_left(5), 300)

    def test_zero_minutes(self):
        self.assertEqual(get_time_left(0), 0)


class TestIsSessionOver(unittest.TestCase):

    def test_time_remaining(self):
        self.assertFalse(is_session_over(60))

    def test_exactly_zero(self):
        self.assertTrue(is_session_over(0))

    def test_negative(self):
        self.assertTrue(is_session_over(-1))


class TestGetNextSession(unittest.TestCase):

    def test_moves_to_next(self):
        self.assertEqual(get_next_session(0, [25, 5, 25, 5]), 1)

    def test_last_session_returns_none(self):
        self.assertIsNone(get_next_session(3, [25, 5, 25, 5]))

    def test_middle_session(self):
        self.assertEqual(get_next_session(2, [25, 5, 25, 5]), 3)


if __name__ == '__main__':
    unittest.main()