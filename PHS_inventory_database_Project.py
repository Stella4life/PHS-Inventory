# Preventive Health Screening (PHS) Inventory Database
# Authors: Stella Anyokwu & Candice Lee
# Professor Sam Davis
# Final Project -HMI7540-01-SP26 Group Project 4

# Preventive Health Screening Inventory Database
# This program creates a simple centralized database for completed preventive health screenings.
# It stores only compliant/completed screening records and exports CSV reports.
# The database supports HEDIS and CMS Star Ratings quality improvement reporting.

import sqlite3
import csv


# -----------------------------
# Create or connect to database
# -----------------------------

def connect_database():
    # This creates the database file if it does not already exist.
    connection = sqlite3.connect("phs_inventory.db")
    return connection


# -----------------------------
# Create database table
# -----------------------------

def create_table():
    connection = connect_database()
    cursor = connection.cursor()

    # This table stores completed/compliant patient screening information from
    # physician offices, labs, radiology centers, endoscopy suites, and eye care centers.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS screenings (
            screening_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_first_name TEXT NOT NULL,
            patient_last_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            patient_gender TEXT,
            collection_hub TEXT,
            provider_name TEXT,
            screening_type TEXT NOT NULL,
            screening_result TEXT,
            screening_date TEXT,
            compliance_status TEXT DEFAULT 'Compliant',
            measure_type TEXT,
            report_year INTEGER
        )
    """)

    connection.commit()
    connection.close()

    print("Database and table created successfully.")


# -----------------------------
# Add fictitious compliant screening data
# -----------------------------

def add_sample_data():
    connection = connect_database()
    cursor = connection.cursor()

    # Fictitious completed screening records.
    # Compliance status is set to Compliant because only completed results are stored.
    sample_data = [
        ("Mary", "Johnson", "1962-04-12", "Female", "Radiology Center", "Dr. Angela Brown, MD",
         "Mammogram", "Normal", "2026-01-15", "Compliant", "Women's Health", 2026),

        ("Linda", "Smith", "1958-09-25", "Female", "Physician Office", "Dr. Michael Carter, MD",
         "Pap Smear", "Normal", "2026-02-10", "Compliant", "Women's Health", 2026),

        ("James", "Williams", "1955-11-03", "Male", "Endoscopy Suite", "Dr. Robert Lewis, MD",
         "Colonoscopy", "Normal", "2026-03-05", "Compliant", "Colorectal Cancer Screening", 2026),

        ("Patricia", "Davis", "1967-07-19", "Female", "Lab", "Dr. Susan Miller, MD",
         "FIT", "Negative", "2026-01-30", "Compliant", "Colorectal Cancer Screening", 2026),

        ("George", "Brown", "1970-02-14", "Male", "Physician Office", "Dr. Karen Wilson, MD",
         "Blood Pressure Screening", "138/82", "2026-02-20", "Compliant", "Cardiovascular Assessment", 2026),

        ("Barbara", "Taylor", "1964-12-08", "Female", "Lab", "Dr. Angela Brown, MD",
         "Comprehensive Lab Panel", "Completed", "2026-03-12", "Compliant", "Cardiovascular Assessment", 2026),

        ("William", "Anderson", "1959-05-21", "Male", "Lab", "Dr. Michael Carter, MD",
         "A1C Lab", "7.2", "2026-01-18", "Compliant", "Diabetic Management", 2026),

        ("Elizabeth", "Thomas", "1961-10-11", "Female", "Eye Care Center", "Dr. Nicole Harris, OD",
         "Diabetic Retinal Exam", "Completed", "2026-02-25", "Compliant", "Diabetic Management", 2026),

        ("Richard", "Moore", "1957-03-30", "Male", "Lab", "Dr. Robert Lewis, MD",
         "Cologuard", "Negative", "2026-03-20", "Compliant", "Colorectal Cancer Screening", 2026),

        ("Sandra", "Martin", "1969-06-06", "Female", "Physician Office", "Dr. Karen Wilson, MD",
         "Blood Pressure Screening", "150/90", "2026-02-11", "Compliant", "Cardiovascular Assessment", 2026)
    ]

    cursor.executemany("""
        INSERT INTO screenings (
            patient_first_name,
            patient_last_name,
            date_of_birth,
            patient_gender,
            collection_hub,
            provider_name,
            screening_type,
            screening_result,
            screening_date,
            compliance_status,
            measure_type,
            report_year
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, sample_data)

    connection.commit()
    connection.close()

    print("Sample fictitious compliant screening data added successfully.")
    print("Note: If you choose this option again, the same sample records will be added again.")


# -----------------------------
# Manually enter a new compliant screening record
# -----------------------------

def enter_new_screening():
    print("\nEnter New Completed Preventive Health Screening Record")

    patient_first_name = input("Patient first name: ")
    patient_last_name = input("Patient last name: ")
    date_of_birth = input("Date of birth (YYYY-MM-DD): ")
    patient_gender = input("Gender: ")

    print("\nExamples of collection hubs:")
    print("Physician Office, Lab, Radiology Center, Endoscopy Suite, Eye Care Center")
    collection_hub = input("Collection hub: ")

    provider_name = input("Provider name with credentials: ")

    print("\nExamples of screening types:")
    print("Colonoscopy, FIT, Cologuard, Mammogram, Pap Smear, Blood Pressure Screening")
    print("Comprehensive Lab Panel, A1C Lab, Diabetic Retinal Exam")
    screening_type = input("Screening type: ")

    screening_result = input("Screening result: ")
    screening_date = input("Screening date (YYYY-MM-DD): ")

    # Compliance status is not entered by the user because only completed/compliant
    # screening results are stored in the PHS Inventory.
    compliance_status = "Compliant"

    print("\nExamples of measure types:")
    print("Colorectal Cancer Screening, Women's Health, Cardiovascular Assessment, Diabetic Management")
    measure_type = input("Measure type: ")

    # This prevents the program from crashing if the year is entered incorrectly.
    try:
        report_year = int(input("Report year: "))
    except ValueError:
        print("Invalid year entered. Report year has been set to 2026.")
        report_year = 2026

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO screenings (
            patient_first_name,
            patient_last_name,
            date_of_birth,
            patient_gender,
            collection_hub,
            provider_name,
            screening_type,
            screening_result,
            screening_date,
            compliance_status,
            measure_type,
            report_year
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        patient_first_name,
        patient_last_name,
        date_of_birth,
        patient_gender,
        collection_hub,
        provider_name,
        screening_type,
        screening_result,
        screening_date,
        compliance_status,
        measure_type,
        report_year
    ))

    connection.commit()
    connection.close()

    print("New completed/compliant screening record added successfully.")


# -----------------------------
# View all compliant records in the database
# -----------------------------

def view_all_records():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM screenings WHERE compliance_status = 'Compliant'")
    records = cursor.fetchall()

    connection.close()

    print("\nPreventive Health Screening Inventory Compliant Records")
    print("-" * 80)

    if len(records) == 0:
        print("No compliant records found.")
    else:
        for record in records:
            print(record)


# -----------------------------
# Export full compliant database report to CSV
# -----------------------------

def export_full_report_to_csv():
    connection = connect_database()
    cursor = connection.cursor()

    # This report exports only compliant completed screening records.
    cursor.execute("SELECT * FROM screenings WHERE compliance_status = 'Compliant'")
    records = cursor.fetchall()

    column_names = [
        "Screening ID",
        "Patient First Name",
        "Patient Last Name",
        "Date of Birth",
        "Gender",
        "Collection Hub",
        "Provider Name",
        "Screening Type",
        "Screening Result",
        "Screening Date",
        "Compliance Status",
        "Measure Type",
        "Report Year"
    ]

    file_name = "phs_full_compliant_screening_report.csv"

    with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(records)

    connection.close()

    print(f"Full compliant screening report exported successfully as {file_name}.")


# -----------------------------
# Export HEDIS/CMS compliant summary report to CSV
# -----------------------------

def export_compliance_report_to_csv():
    connection = connect_database()
    cursor = connection.cursor()

    # This report summarizes only compliant completed screenings by measure type.
    cursor.execute("""
        SELECT
            measure_type,
            compliance_status,
            COUNT(*) AS total_patients
        FROM screenings
        WHERE compliance_status = 'Compliant'
        GROUP BY measure_type, compliance_status
        ORDER BY measure_type, compliance_status
    """)

    records = cursor.fetchall()

    column_names = [
        "Measure Type",
        "Compliance Status",
        "Total Patients"
    ]

    file_name = "phs_hedis_cms_compliant_summary_report.csv"

    with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(records)

    connection.close()

    print(f"HEDIS/CMS compliant summary report exported successfully as {file_name}.")


# -----------------------------
# Export compliant patients report to CSV
# -----------------------------

def export_compliant_patients_report_to_csv():
    connection = connect_database()
    cursor = connection.cursor()

    # This report pulls only patients with completed/compliant preventive screenings.
    cursor.execute("""
        SELECT
            patient_first_name,
            patient_last_name,
            date_of_birth,
            collection_hub,
            provider_name,
            screening_type,
            screening_result,
            screening_date,
            compliance_status,
            measure_type,
            report_year
        FROM screenings
        WHERE compliance_status = 'Compliant'
        ORDER BY patient_last_name
    """)

    records = cursor.fetchall()

    column_names = [
        "Patient First Name",
        "Patient Last Name",
        "Date of Birth",
        "Collection Hub",
        "Provider Name",
        "Screening Type",
        "Screening Result",
        "Screening Date",
        "Compliance Status",
        "Measure Type",
        "Report Year"
    ]

    file_name = "phs_compliant_patients_report.csv"

    with open(file_name, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(records)

    connection.close()

    print(f"Compliant patients report exported successfully as {file_name}.")


# -----------------------------
# Main menu
# -----------------------------

def main_menu():
    create_table()

    while True:
        print("\nPreventive Health Screening Inventory System")
        print("1. Add sample fictitious compliant data")
        print("2. Enter new completed screening record")
        print("3. View all compliant screening records")
        print("4. Export full compliant screening report to CSV")
        print("5. Export HEDIS/CMS compliant summary report to CSV")
        print("6. Export compliant patients report to CSV")
        print("7. Exit program")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_sample_data()

        elif choice == "2":
            enter_new_screening()

        elif choice == "3":
            view_all_records()

        elif choice == "4":
            export_full_report_to_csv()

        elif choice == "5":
            export_compliance_report_to_csv()

        elif choice == "6":
            export_compliant_patients_report_to_csv()

        elif choice == "7":
            print("Program closed. Preventive Health Screening Inventory System ended.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 7.")


# -----------------------------
# Run the program
# -----------------------------

if __name__ == "__main__":
    main_menu()
