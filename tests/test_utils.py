import unittest

from utils import is_fingertip_on_tile


class FingertipCollisionTests(unittest.TestCase):
    def test_fingertip_inside_tile_hits(self):
        self.assertTrue(is_fingertip_on_tile([(105, 105)], 100, 100, 10))

    def test_fingertip_on_circle_boundary_hits(self):
        self.assertTrue(is_fingertip_on_tile([(110, 100)], 100, 100, 10))

    def test_fingertip_outside_circle_does_not_hit(self):
        # Inside the old square bounds, but outside the circular tile.
        self.assertFalse(is_fingertip_on_tile([(109, 109)], 100, 100, 10))

    def test_any_fingertip_can_hit(self):
        self.assertTrue(
            is_fingertip_on_tile([(0, 0), (100, 100)], 100, 100, 10)
        )

    def test_no_fingers_does_not_hit(self):
        self.assertFalse(is_fingertip_on_tile([], 100, 100, 10))


if __name__ == "__main__":
    unittest.main()
