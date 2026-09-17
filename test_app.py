import unittest
from student_processor import AcademicSystem

class TestAcademicPerformanceSystem(unittest.TestCase):
    def setUp(self):
        self.system = AcademicSystem()

    def test_grade_calculation(self):
        """Validates that grading tiers compute accurately"""
        self.assertEqual(self.system.compute_grade(95), "A+")
        self.assertEqual(self.system.compute_grade(82), "A")
        self.assertEqual(self.system.compute_grade(40), "F")

    def test_invalid_grade_exception(self):
        """Ensures logic breaks cleanly and error-handles illegal inputs"""
        with self.assertRaises(ValueError):
            self.system.compute_grade(150)

    def test_attendance_eligibility(self):
        """Verifies attendance rule restrictions behave properly"""
        self.assertEqual(self.system.verify_eligibility(80), "Eligible")
        self.assertEqual(self.system.verify_eligibility(70), "Barred (Low Attendance)")

if __name__ == "__main__":
    unittest.main()
