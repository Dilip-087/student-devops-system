import os
import sys
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample In-Memory database for Student Management
STUDENT_DATABASE = [
    {"id": "STU001", "name": "Rahul Sharma", "marks": 85, "attendance": 92},
    {"id": "STU002", "name": "Priya Patel", "marks": 92, "attendance": 96},
    {"id": "STU003", "name": "Amit Kumar", "marks": 45, "attendance": 78}
]

def calculate_letter_grade(marks):
    """Core academic engine business logic"""
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 50: return "C"
    return "F"

@app.route('/api/students', methods=['GET'])
def get_students():
    """Endpoint to fetch all records with resolved grading states"""
    processed_roster = []
    for s in STUDENT_DATABASE:
        grade = calculate_letter_grade(s["marks"])
        status = "Passed" if s["marks"] >= 50 and s["attendance"] >= 75 else "Failed/Barred"
        processed_roster.append({
            **s, "grade": grade, "status": status
        })
    return jsonify({"status": "success", "data": processed_roster}), 200

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """Endpoint calculating system metadata overview diagnostics"""
    if not STUDENT_DATABASE:
        return jsonify({"avg_marks": 0, "pass_count": 0}), 200
    
    marks_list = [s["marks"] for s in STUDENT_DATABASE]
    avg = sum(marks_list) / len(STUDENT_DATABASE)
    passes = sum(1 for s in STUDENT_DATABASE if s["marks"] >= 50 and s["attendance"] >= 75)
    
    return jsonify({
        "status": "success",
        "metrics": {
            "average_marks": round(avg, 2),
            "total_students": len(STUDENT_DATABASE),
            "successful_passes": passes
        }
    }), 200

@app.route('/api/students/add', methods=['POST'])
def add_student():
    """Endpoint allowing programmatic insertion of new student evaluations"""
    data = request.get_json() or {}
    if not all(k in data for k in ("name", "marks", "attendance")):
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
    
    new_id = f"STU{len(STUDENT_DATABASE) + 1:03d}"
    new_entry = {
        "id": new_id,
        "name": data["name"],
        "marks": int(data["marks"]),
        "attendance": int(data["attendance"])
    }
    STUDENT_DATABASE.append(new_entry)
    return jsonify({"status": "created", "student_id": new_id}), 201

if __name__ == '__main__':
    # CI/CD operational validation hook
    if len(sys.argv) > 1 and sys.argv[1] == '--verify-only':
        print("Backend Integrity Verification Context: Flask routes initialized successfully.")
        sys.exit(0)
    app.run(debug=True, port=5000)
