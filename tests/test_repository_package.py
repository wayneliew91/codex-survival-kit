import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "token-efficient-codex",
    "tibo-reset",
    "context-handoff",
    "regression-guardian",
    "repo-first-debugging",
    "high-signal-response",
}


class RepositoryPackageTests(unittest.TestCase):
    def test_exact_skill_set_exists(self):
        actual = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
        self.assertEqual(actual, EXPECTED_SKILLS)

    def test_public_repository_files_exist(self):
        for rel in [
            "README.md",
            "LICENSE",
            "CONTRIBUTING.md",
            "SECURITY.md",
            "CODE_OF_CONDUCT.md",
            ".github/workflows/validate.yml",
            ".github/ISSUE_TEMPLATE/bug_report.yml",
            ".github/ISSUE_TEMPLATE/skill_request.yml",
            ".github/pull_request_template.md",
        ]:
            with self.subTest(rel=rel):
                self.assertTrue((ROOT / rel).is_file(), rel)

    def test_readme_names_all_skills_and_reset_disclaimer(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        for name in EXPECTED_SKILLS:
            self.assertIn(name, text)
        self.assertIn("cannot trigger", text)
        self.assertIn("skill-installer", text)

    def test_openai_metadata_has_default_prompt_with_skill_name(self):
        for name in EXPECTED_SKILLS:
            text = (ROOT / "skills" / name / "agents" / "openai.yaml").read_text(encoding="utf-8")
            with self.subTest(name=name):
                self.assertIn(f"${name}", text)
                self.assertIn("short_description:", text)
                self.assertIn("display_name:", text)


if __name__ == "__main__":
    unittest.main()
