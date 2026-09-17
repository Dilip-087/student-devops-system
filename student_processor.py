class AcademicSystem:
    def __init__(self):
        # Database simulation holding student objects
        self.students = [
            {"id": "STU001", "name": "Rahul Sharma", "marks": 85, "attendance": 92},
            {"id": "STU002", "name": "Priya Patel", "marks": 92, "attendance": 96},
            {"id": "STU003", "name": "Amit Kumar", "marks": 45, "attendance": 78},
            {"id": "STU004", "name": "Sneha Reddy", "marks": 78, "attendance": 88},
            {"id": "STU005", "name": "Vikram Singh", "marks": 38, "attendance": 60}
        ]

    def compute_grade(self, marks):
        """Calculates letter grades based on institutional standards"""
        if not isinstance(marks, (int, float)) or marks < 0 or marks > 100:
            raise ValueError("Invalid marks value provided.")
        
        if marks >= 90: return "A+"
        elif marks >= 80: return "A"
        elif marks >= 70: return "B"
        elif marks >= 50: return "C"
        else: return "F"

    def verify_eligibility(self, attendance):
        """Students with less than 75% attendance fail criteria eligibility"""
        return "Eligible" if attendance >= 75 else "Barred (Low Attendance)"

    def aggregate_metrics(self):
        """Calculates batch metadata values"""
        if not self.students:
            return {"avg_marks": 0, "passed": 0, "failed": 0}
            
        all_marks = [s["marks"] for s in self.students]
        avg = sum(all_marks) / len(self.students)
        passed = sum(1 for s in self.students if s["marks"] >= 50 and s["attendance"] >= 75)
        
        return {
            "avg_marks": round(avg, 2),
            "passed": passed,
            "failed": len(self.students) - passed
        }
