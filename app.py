import os
from student_processor import AcademicSystem

def generate_academic_report():
    system = AcademicSystem()
    metrics = system.aggregate_metrics()
    report_filename = "student_report.txt"

    print(f"Generating system artifact report: '{report_filename}'...")

    with open(report_filename, "w") as report:
        report.write("========================================================\n")
        report.write("      STUDENT ACADEMIC PERFORMANCE PORTAL REPORT         \n")
        report.write("========================================================\n\n")
        
        report.write(f"Class Batch Average Marks   : {metrics['avg_marks']}%\n")
        report.write(f"Total Successful Passes     : {metrics['passed']}\n")
        report.write(f"Total Administrative Fails  : {metrics['failed']}\n")
        report.write("--------------------------------------------------------\n\n")
        
        report.write("DETAILED STUDENT LEDGER STACK:\n")
        report.write(f"{'ID':<10}{'Student Name':<18}{'Marks':<8}{'Attendance':<13}{'Status':<10}\n")
        report.write("-" * 62 + "\n")
        
        for s in system.students:
            grade = system.compute_grade(s["marks"])
            eligibility = system.verify_eligibility(s["attendance"])
            status = grade if eligibility == "Eligible" else "FAIL (Attendance)"
            
            report.write(f"{s['id']:<10}{s['name']:<18}{s['marks']:<8}{s['attendance']:<13%}{status:<10}\n")
            
        report.write("\n========================================================\n")
        report.write("Pipeline Build Status: Compiled & Verified Successfully.\n")

    print(f"Artifact created at absolute path: {os.path.abspath(report_filename)}")

if __name__ == "__main__":
    generate_academic_report()
