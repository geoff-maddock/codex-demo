import unittest
from boardgame_art.app import compose_prompt


class TestPrompt(unittest.TestCase):
    def test_compose_prompt_all_fields(self):
        result = compose_prompt(
            base_idea="fantasy board",
            style="watercolor",
            color_scheme="vibrant",
        )
        self.assertIn("fantasy board", result)
        self.assertIn("watercolor", result)
        self.assertIn("vibrant", result)

    def test_compose_prompt_minimal(self):
        result = compose_prompt(base_idea="spaceship")
        self.assertEqual(result, "spaceship")


if __name__ == "__main__":
    unittest.main()
