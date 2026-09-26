from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DATABASE = "tracker.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create database and table
def create_database():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS academics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            cgpa REAL NOT NULL,
            semester TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/academics", methods=["GET", "POST"])
@app.route("/save-academics", methods=["POST"])
def academics():

    if request.method == "POST":

        student_name = request.form["student_name"]
        cgpa = request.form["cgpa"]
        semester = request.form["semester"]

        conn = get_db_connection()

        conn.execute(
            """
            INSERT INTO academics
            (student_name, cgpa, semester)
            VALUES (?, ?, ?)
            """,
            (student_name, cgpa, semester)
        )

        conn.commit()
        conn.close()

        return "Academic details saved successfully! ✅"

    return render_template("academics.html")

@app.route("/attendance", methods=["GET", "POST"])
def attendance():

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            total_classes INTEGER NOT NULL,
            attended_classes INTEGER NOT NULL
        )
    """)

    if request.method == "POST":

        subject = request.form["subject"]
        total_classes = request.form["total_classes"]
        attended_classes = request.form["attended_classes"]

        conn.execute(
            """
            INSERT INTO attendance
            (subject, total_classes, attended_classes)
            VALUES (?, ?, ?)
            """,
            (subject, total_classes, attended_classes)
        )

        conn.commit()

    records = conn.execute(
        "SELECT * FROM attendance"
    ).fetchall()

    conn.close()

    return render_template(
        "attendance.html",
        records=records
    )

@app.route("/skills", methods=["GET", "POST"])
def skills():

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_name TEXT NOT NULL,
            skill_level TEXT NOT NULL,
            progress INTEGER NOT NULL
        )
    """)

    if request.method == "POST":

        skill_name = request.form["skill_name"]
        skill_level = request.form["skill_level"]
        progress = request.form["progress"]

        conn.execute("""
            INSERT INTO skills
            (skill_name, skill_level, progress)
            VALUES (?, ?, ?)
        """, (skill_name, skill_level, progress))

        conn.commit()

    records = conn.execute(
        "SELECT * FROM skills"
    ).fetchall()

    conn.close()

    return render_template(
        "skills.html",
        records=records
    )


@app.route("/certificates", methods=["GET", "POST"])
def certificates():

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS certificates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            certificate_name TEXT NOT NULL,
            organization TEXT NOT NULL,
            certificate_link TEXT NOT NULL
        )
    """)

    if request.method == "POST":

        certificate_name = request.form["certificate_name"]
        organization = request.form["organization"]
        certificate_link = request.form["certificate_link"]

        conn.execute("""
            INSERT INTO certificates
            (certificate_name, organization, certificate_link)
            VALUES (?, ?, ?)
        """, (
            certificate_name,
            organization,
            certificate_link
        ))

        conn.commit()

    records = conn.execute("""
        SELECT * FROM certificates
    """).fetchall()

    conn.close()

    return render_template(
        "certificates.html",
        records=records
    )


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/projects", methods=["GET", "POST"])
def projects():

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            description TEXT NOT NULL,
            technologies TEXT NOT NULL,
            github_link TEXT NOT NULL
        )
    """)

    if request.method == "POST":

        project_name = request.form["project_name"]
        description = request.form["description"]
        technologies = request.form["technologies"]
        github_link = request.form["github_link"]

        conn.execute("""
            INSERT INTO projects
            (project_name, description, technologies, github_link)
            VALUES (?, ?, ?, ?)
        """, (
            project_name,
            description,
            technologies,
            github_link
        ))

        conn.commit()

    records = conn.execute(
        "SELECT * FROM projects"
    ).fetchall()

    conn.close()

    return render_template(
        "projects.html",
        records=records
    )