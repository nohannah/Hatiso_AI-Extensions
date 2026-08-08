import importlib
import sys
import types
import unittest

fake_model_loader = types.ModuleType("model_loader")
fake_model_loader.tokenizer = None
fake_model_loader.model = None
sys.modules["model_loader"] = fake_model_loader

predictor = importlib.import_module("predictor")


class PredictorMappingTests(unittest.TestCase):
    def test_not_hate_label_maps_to_neither(self):
        self.assertEqual(predictor.map_label(0, "NOT-HATE"), "Neither")

    def test_hate_label_maps_to_hate_speech(self):
        self.assertEqual(predictor.map_label(1, "HATE"), "Hate Speech")

    def test_offensive_label_maps_to_offensive_language(self):
        self.assertEqual(predictor.map_label(0, "OFFENSIVE"), "Offensive Language")


if __name__ == "__main__":
    unittest.main()
