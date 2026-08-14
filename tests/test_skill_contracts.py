import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def skill_text(name: str) -> str:
    return (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")


def body_word_count(text: str) -> int:
    parts = text.split("---", 2)
    body = parts[2] if len(parts) == 3 else text
    return len(re.findall(r"\b\w+[\w'-]*\b", body))


class SkillContractTests(unittest.TestCase):
    def test_token_efficient_codex_contract(self):
        text = skill_text("token-efficient-codex")
        self.assertLessEqual(body_word_count(text), 500)
        for required in [
            "correctness",
            "security",
            "required verification",
            "start narrow",
            "checkpoint",
            "references/efficiency-patterns.md",
        ]:
            self.assertIn(required, text.lower())

    def test_tibo_reset_contract(self):
        text = skill_text("tibo-reset")
        self.assertLessEqual(body_word_count(text), 500)
        for required in [
            "confirmed",
            "probable",
            "unconfirmed",
            "contradicted",
            "cannot trigger",
            "current-source",
            "references/source-confidence.md",
        ]:
            self.assertIn(required, text.lower())

    def test_context_handoff_contract(self):
        text = skill_text("context-handoff")
        self.assertLessEqual(body_word_count(text), 500)
        for required in [
            "current truth",
            "next exact action",
            "verification",
            "hypotheses",
            "secrets",
            "assets/handoff-template.md",
        ]:
            self.assertIn(required, text.lower())

    def test_regression_guardian_contract(self):
        text = skill_text("regression-guardian")
        self.assertLessEqual(body_word_count(text), 500)
        for required in [
            "protected behavior",
            "regression contract",
            "supersession",
            "targeted",
            "verified",
            "references/regression-contract.md",
        ]:
            self.assertIn(required, text.lower())

    def test_repo_first_debugging_contract(self):
        text = skill_text("repo-first-debugging")
        self.assertLessEqual(body_word_count(text), 500)
        for required in [
            "repository",
            "reproduction",
            "hypothesis",
            "discriminating test",
            "out-of-scope",
            "references/evidence-loop.md",
        ]:
            self.assertIn(required, text.lower())


if __name__ == "__main__":
    unittest.main()
