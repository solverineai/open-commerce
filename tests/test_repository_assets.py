import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryAssetsTest(unittest.TestCase):
    def test_required_directories_exist(self):
        for directory in [
            "skills",
            "datasets",
            "schemas",
            "prompts",
            "examples",
            "docs",
            "governance",
            ".github",
        ]:
            self.assertTrue((ROOT / directory).is_dir(), directory)

    def test_schema_json_files_load(self):
        schema_paths = sorted((ROOT / "schemas").glob("*.schema.json"))
        self.assertEqual(len(schema_paths), 7)
        for path in schema_paths:
            with self.subTest(path=path):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertIn("$schema", data)
                self.assertIn("$id", data)

    def test_dataset_count(self):
        dataset_paths = sorted((ROOT / "datasets").glob("*/*/economics.json"))
        self.assertEqual(len(dataset_paths), 17)

    def test_skill_count(self):
        interface_paths = sorted((ROOT / "skills").glob("*/*/interface.json"))
        self.assertEqual(len(interface_paths), 15)


if __name__ == "__main__":
    unittest.main()
