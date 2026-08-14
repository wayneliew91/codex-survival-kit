import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import validate_repo, validate_skill_dir


FIXTURE = Path(__file__).parent / "fixtures" / "valid-skill"


class ValidateSkillTests(unittest.TestCase):
    def make_skill(self, name="valid-skill"):
        root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        skill = root / "skills" / name
        skill.parent.mkdir(parents=True)
        shutil.copytree(FIXTURE, skill)
        return root, skill

    def test_valid_skill_has_no_errors(self):
        root, skill = self.make_skill()
        self.assertEqual(validate_skill_dir(skill, root), [])

    def test_missing_skill_md_is_reported(self):
        root, skill = self.make_skill()
        (skill / "SKILL.md").unlink()
        errors = validate_skill_dir(skill, root)
        self.assertTrue(any("missing SKILL.md" in e for e in errors))

    def test_frontmatter_rejects_extra_fields(self):
        root, skill = self.make_skill()
        path = skill / "SKILL.md"
        path.write_text(path.read_text().replace("description:", "metadata: nope\ndescription:"))
        errors = validate_skill_dir(skill, root)
        self.assertTrue(any("exactly name and description" in e for e in errors))

    def test_folder_must_match_frontmatter_name(self):
        root, skill = self.make_skill("different-folder")
        errors = validate_skill_dir(skill, root)
        self.assertTrue(any("folder name" in e for e in errors))

    def test_description_must_start_with_use_when(self):
        root, skill = self.make_skill()
        path = skill / "SKILL.md"
        path.write_text(path.read_text().replace("Use when", "Helps when"))
        errors = validate_skill_dir(skill, root)
        self.assertTrue(any("Use when" in e for e in errors))

    def test_broken_relative_markdown_link_is_reported(self):
        root, skill = self.make_skill()
        path = skill / "SKILL.md"
        path.write_text(path.read_text().replace("reference.md", "missing.md"))
        errors = validate_skill_dir(skill, root)
        self.assertTrue(any("broken relative link" in e for e in errors))

    def test_forbidden_auxiliary_skill_doc_is_reported(self):
        root, skill = self.make_skill()
        (skill / "README.md").write_text("redundant")
        errors = validate_skill_dir(skill, root)
        self.assertTrue(any("forbidden auxiliary file" in e for e in errors))

    def test_private_or_secret_patterns_are_reported(self):
        root, skill = self.make_skill()
        path = skill / "reference.md"
        sample_path = "C:" + "\\Users\\Example\\secret"
        sample_token = "sk" + "-proj-example"
        path.write_text(f"Local path: {sample_path} and token {sample_token}")
        errors = validate_skill_dir(skill, root)
        self.assertTrue(any("sensitive pattern" in e for e in errors))

    def test_repo_requires_openai_yaml_for_every_skill(self):
        root, skill = self.make_skill()
        (skill / "agents" / "openai.yaml").unlink()
        errors = validate_repo(root)
        self.assertTrue(any("agents/openai.yaml" in e for e in errors))

    def test_repo_validates_plugin_marketplace_when_present(self):
        root, skill = self.make_skill()
        marketplace = root / ".agents" / "plugins" / "marketplace.json"
        marketplace.parent.mkdir(parents=True)
        marketplace.write_text("{}")
        errors = validate_repo(root)
        self.assertTrue(any("marketplace" in e.lower() for e in errors))


if __name__ == "__main__":
    unittest.main()
