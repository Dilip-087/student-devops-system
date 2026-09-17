import os
import sys

def build_static_frontend_view():
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Academic Performance Management Portal</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; margin: 0; padding: 20px; color: #333; }
        .container { max-width: 1000px; margin: 0 auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; margin-top: 0; }
        .dashboard-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 30px; }
        .card { background: #ebf5fb; padding: 20px; border-left: 5px solid #3498db; border-radius: 6px; }
        .card h3 { margin: 0 0 5px 0; color: #566573; font-size: 14px; text-transform: uppercase; }
        .card p { margin: 0; font-size: 24px; font-weight: bold; color: #2c3e50; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #e5e8e8; }
        th { background-color: #34495e; color: white; text-transform: uppercase; font-size: 13px; }
        tr:hover { background-color: #f9f9f9; }
        .badge { padding: 5px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; }
        .badge-pass { background-color: #d4efdf; color: #196f3d; }
        .badge-fail { background-color: #fadbd8; color: #78281f; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Student Performance Evaluation Dashboard</h1>
        
        <div class="dashboard-grid">
            <div class="card"><h3>Class Average</h3><p>74.33%</p></div>
            <div class="card"><h3>Total Enrolled</h3><p>3 Students</p></div>
            <div class="card"><h3>Passing Rate</h3><p>66.6%</p></div>
        </div>

        <h3>Active Academic Roster Ledger</h3>
        <table>
            <thead>
                <tr>
                    <th>Student ID</th>
                    <th>Full Name</th>
                    <th>Scored Marks</th>
                    <th>Attendance Status</th>
                    <th>Letter Grade</th>
                    <th>Compliance Status</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>STU001</td><td>Rahul Sharma</td><td>85%</td><td>92%</td><td>A</td><td><span class="badge badge-pass">Passed</span></td></tr>
                <tr><td>STU002</td><td>Priya Patel</td><td>92%</td><td>96%</td><td>A+</td><td><span class="badge badge-pass">Passed</span></td></tr>
                <tr><td>STU003</td><td>Amit Kumar</td><td>45%</td><td>78%</td><td>F</td><td><span class="badge badge-fail">Failed/Barred</span></td></tr>
            </tbody>
        </table>
    </div>
</body>
</html>
"""
    output_path = "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print(f"Frontend Structural Build Engine Complete: Web dashboard generated at '{os.path.abspath(output_path)}'")

if __name__ == '__main__':
    # CI/CD sanity checking trigger check
    build_static_frontend_view()
    if len(sys.argv) > 1 and sys.argv[1] == '--verify-only':
        sys.exit(0)
