# Preventive Health Screening Inventory System

## Project Overview

The Preventive Health Screening Inventory System is a centralized database project designed to manage, track, and report completed preventive health screenings. The purpose of the project is to support healthcare quality improvement by organizing screening data from multiple collection points, including physician offices, laboratories, radiology centers, endoscopy suites, and eye care centers.

This system provides a clear view of each patient’s completed preventive screening status and supports reporting needs related to HEDIS measures and CMS Star Ratings. By maintaining a centralized inventory of completed screenings, healthcare teams can identify compliant patients, organize preventive screening data, and export CSV reports to support healthcare quality improvement and patient outcomes.

## Purpose of the Project

Preventive health screenings are important for early detection, chronic disease management, and improved patient outcomes. However, screening information is often collected from different locations and may not always be stored in one centralized system.

This project addresses that problem by creating a simple database that captures completed screening results, organizes patient records, stores compliance status, and generates CSV reports for quality improvement review. Since the database is designed to store completed preventive screenings only, the compliance status is recorded as **Compliant**.

## Flowchart Summary

The project follows the workflow shown in the Preventive Health Screening Inventory flowchart.

The process begins in the physician office, where the patient’s screening needs are reviewed. If the patient is due for a preventive screening, the provider orders or refers the patient for the appropriate test. The order is then sent to the correct collection hub, such as a laboratory, radiology center, endoscopy suite, or eye care center.

Once the screening is performed and completed, the result is reviewed and uploaded into the Preventive Health Screening Inventory database. The database stores the completed screening result, records the patient as compliant, and allows the information to be exported into CSV reports for HEDIS and CMS Star Ratings quality improvement activities.

## Sample Data

The program includes fictitious patient screening records for demonstration purposes only. These records do not represent real patients.

The sample data includes completed screenings such as mammograms, Pap smears, colonoscopies, FIT tests, Cologuard tests, blood pressure screenings, comprehensive lab panels, A1C labs, and diabetic retinal exams. Each sample record is assigned a compliance status of **Compliant** because the database is designed to store completed screening results only.

## Preventive Screenings Included

The system is designed to manage several major categories of preventive health screenings.

### Colorectal Cancer Screening

Examples include:

- Colonoscopy
- FIT test
- Cologuard

### Women’s Health Screening

Examples include:

- Mammogram
- Pap smear

### Cardiovascular Assessment

Examples include:

- Blood pressure screening
- Comprehensive lab panel

### Diabetic Management

Examples include:

- A1C lab
- Diabetic retinal exam

## Project Features

This program allows the user to:

- Create a centralized SQLite database
- Add fictitious patient screening data
- Manually enter new completed preventive screening records
- View all screening records in the database
- Track the collection hub where the screening was completed
- Store provider information
- Record screening type, result, date, and compliance status
- Store **Compliant** as the only compliance status
- Export a full screening report to CSV
- Export a HEDIS/CMS compliance summary report to CSV
- Export a compliant patients report to CSV

## Database Fields

The database table is named `screenings`.

The table includes the following fields:

| Field Name | Description |
|---|---|
| screening_id | Unique ID assigned to each screening record |
| patient_first_name | Patient’s first name |
| patient_last_name | Patient’s last name |
| date_of_birth | Patient’s date of birth |
| patient_gender | Patient’s gender |
| collection_hub | Location where the screening was collected or performed |
| provider_name | Provider responsible for the screening |
| screening_type | Type of preventive screening completed |
| screening_result | Result of the screening |
| screening_date | Date the screening was completed |
| compliance_status | Patient’s compliance status, recorded as Compliant |
| measure_type | Quality measure category |
| report_year | Reporting year for HEDIS/CMS review |

## Collection Hubs

Collection hubs are the locations where preventive screenings may be completed before the results are uploaded into the database.

Examples include:

- Physician Office
- Lab
- Radiology Center
- Endoscopy Suite
- Eye Care Center

## Compliance Status

The compliance status for this project is **Compliant** only. This is because the Preventive Health Screening Inventory is designed to store completed screening results. Patients who have not completed a screening, are pending, or need follow-up are not stored in this inventory as active screening records.

## How to Run the Program

Open the project folder in Visual Studio Code. The main Python file for this project is:

```text
PHS_inventory_database_Project.py
```

Open the terminal in Visual Studio Code and run:

```bash
python PHS_inventory_database_Project.py
```

After the program runs, use the menu options to add sample fictitious data, enter new screening records, view records, and export CSV reports.

When the program runs, the following menu appears:

```text
Preventive Health Screening Inventory System
1. Add sample fictitious data
2. Enter new screening record
3. View all screening records
4. Export full screening report to CSV
5. Export HEDIS/CMS compliance report to CSV
6. Export compliant patients report to CSV
7. Exit program
```

The user can select a number from the menu to perform the desired action.

## Reports Generated

The program can generate CSV reports from the Preventive Health Screening Inventory database. These reports organize completed and compliant screening records so they can be reviewed for quality improvement, HEDIS measures, and CMS Star Ratings support.

### 1. Full Screening Report

File name:

```text
phs_full_screening_report.csv
```

This report includes all completed and compliant preventive screening records stored in the database.

### 2. HEDIS/CMS Compliance Summary Report

File name:

```text
phs_hedis_cms_compliance_report.csv
```

This report summarizes compliant screening records by measure type and compliance status.

### 3. Compliant Patients Report

File name:

```text
phs_compliant_patients_report.csv
```

This report lists patients with completed screenings marked as compliant.

## Importance to Healthcare Quality

This project supports healthcare quality improvement by making completed preventive screening information easier to organize and review. A centralized screening inventory can help healthcare organizations monitor completed screenings, prepare reports, and support quality measure review.

The system may also help healthcare teams evaluate screening activity by measure type, provider, collection hub, and reporting year. This information can support better planning, improved documentation, and stronger reporting for HEDIS and CMS Star Ratings.


## References

Centers for Medicare & Medicaid Services. (2026). *Home*. https://www.cms.gov

Google. (2026). *NotebookLM* [Large language model]. https://notebooklm.google.com/

National Committee for Quality Assurance. (2026). *Home*. https://www.ncqa.org

OpenAI. (2026). *ChatGPT (May 13 version)* [Large language model]. https://chat.openai.com/chat
