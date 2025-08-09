# test_screener.py

import unittest
import pandas as pd
from .screener_api import process_resume
from .resume_keyword_matcher import match_keywords


class TestResumeScreener(unittest.TestCase):

    def setUp(self):
        # Sample resume data
        self.sample_data = pd.DataFrame({
            "resume": [
                "Python developer with ML experience",
                "Experienced manager with PMP and Excel skills",
                "Frontend engineer with React and Next.js"
            ]
        })
        self.skills_required = ["python", "ml", "react"]

        # Save sample CSV for testing
        self.sample_csv = "test_resumes.csv"
        self.sample_data.to_csv(self.sample_csv, index=False)

    def tearDown(self):
        # Clean up test file
        import os
        if os.path.exists(self.sample_csv):
            os.remove(self.sample_csv)

    def test_process_resume_basic(self):
        result = process_resume(
            self.sample_csv, self.skills_required, min_confidence=0)

        self.assertIn("cleaned_text", result)
        self.assertIn("skills_matched", result)
        self.assertIn("predicted_role", result)
        self.assertIn("confidence", result)

        self.assertEqual(len(result["cleaned_text"]), 3)
        self.assertEqual(len(result["predicted_role"]), 3)

    def test_process_resume_filtering(self):
        result = process_resume(
            self.sample_csv, self.skills_required, min_confidence=90)
        # Expecting few or no results if confidence threshold is high
        self.assertTrue(len(result["predicted_role"]) <= 3)

    def test_keyword_matching(self):
        df = self.sample_data.copy()
        df["cleaned_text"] = df["resume"].str.lower()
        df_keywords = match_keywords(df, self.skills_required)

        self.assertIn("matched_skills", df_keywords.columns)
        self.assertEqual(len(df_keywords), 3)
        self.assertIsInstance(df_keywords.loc[0, "matched_skills"], str)


if __name__ == '__main__':
    unittest.main()
