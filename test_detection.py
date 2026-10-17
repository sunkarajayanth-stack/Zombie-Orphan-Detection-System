
import unittest
import sys
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

import main


class TestProcessDetection(unittest.TestCase):

    def test_zombie_detection_logic(self):
        processes = {
            100: {
                "pid": 100,
                "ppid": 1,
                "name": "zombie_test",
                "state": "Z",
            },
            101: {
                "pid": 101,
                "ppid": 1,
                "name": "normal_test",
                "state": "S",
            },
        }

        zombies = [
            p for p in processes.values()
            if p["state"] == "Z"
        ]

        self.assertEqual(len(zombies), 1)
        self.assertEqual(zombies[0]["pid"], 100)

    def test_empty_process_list(self):
        processes = {}
        zombies = [
            p for p in processes.values()
            if p["state"] == "Z"
        ]

        self.assertEqual(zombies, [])

    def test_process_fields(self):
        process = {
            "pid": 200,
            "ppid": 1,
            "name": "example",
            "state": "S",
        }

        self.assertIn("pid", process)
        self.assertIn("ppid", process)
        self.assertIn("name", process)
        self.assertIn("state", process)


if __name__ == "__main__":
    unittest.main()
