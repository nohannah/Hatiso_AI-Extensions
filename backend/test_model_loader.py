import os
import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

import model_loader


class ModelLoaderPathTests(unittest.TestCase):
    def test_model_path_exists(self):
        self.assertTrue(os.path.isdir(model_loader.MODEL_PATH))
        self.assertTrue(os.path.exists(os.path.join(model_loader.MODEL_PATH, "config.json")))


if __name__ == "__main__":
    unittest.main()
