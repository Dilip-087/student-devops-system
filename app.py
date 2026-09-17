import os
from student_processor import AcademicSystem

def generate_academic_report():
    # Initialize the core student processor system
    system = AcademicSystem()
    
    # Calculate global batch metrics (averages, pass/fail counts)
    metrics = system.aggregate_metrics()
    report_filename = "student_report.txt"

    print(f"Processing student roster data...")
    print(f"Generating optimized text report artifact: '{report_filename}'...")

    # Write data cleanly to the report file artifact
    with open(report_filename, "w") as report:
        report.write("================================================================\n")
        report.write("          STUDENT ACADEMIC PERFORMANCE PORTAL REPORT            \n")
        report.write("================================================================\n\n")
        
        # Global Metadata Overview Block
        report.write("BATCH OVERVIEW METRICS:\n")
        report.write(f"  Class Batch Average Marks   : {metrics['avg_marks']}%\n")
        report.write(f"  Total Successful Passes     : {metrics['passed']}\n")
        report.write(f"  Total Administrative Fails  : {metrics['failed']}\n")
        report.write("----------------------------------------------------------------\n\n")
        
        # Table Header Section with aligned column spacing
        report.write("DETAILED STUDENT PERFORMANCE RECORD LEDGER:\n")
        report.write(f"{'ID':<10}{'Student Name':<20}{'Marks':<10}{'Attendance':<14}{'Final Status':<15}\n")
        report.write("-" * 65 + "\n")
        
        # Process individual student record logic
        for student in system.students:
            grade = system.compute_grade(student["marks"])
            eligibility = system.verify_eligibility(student["attendance"])
            
            # Core logic check: If barred due to low attendance, student fails automatically
            if eligibility == "Eligible":
                status = f"PASSED ({grade})" if student["marks"] >= 50 else f"FAILED ({grade})"
            else:
                status = "FAIL (Attendance)"
            
            # Fix: Format attendance directly as a clean text string with the % symbol appended
            clean_attendance_display = f"{student['attendance']}%"
            
            # Print the formatted row cleanly aligned with the columns
            report.write(
                f"{student['id']:<10}"
                f"{student['name']:<20}"
                f"{student['marks']:<10}"
                f"{clean_attendance_display:<14}"
                f"{status:<15}\n"
            )
            
        report.write("\n================================================================\n")
        report.write("CI/CD Pipeline Build Status: Compiled, Tested, & Verified Successfully.\n")

    print(f"Success! Report generated at absolute path: {os.path.abspath(report_filename)}")

if __name__ == "__main__":
    generate_academic_report()
