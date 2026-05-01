# Preventive Health Screening Inventory System

## Project Overview

The Preventive Health Screening Inventory System is a centralized database project designed to manage, track, and report completed preventive health screenings. The purpose of the project is to support healthcare quality improvement by organizing screening data from multiple collection points, including physician offices, laboratories, radiology centers, endoscopy suites, and eye care centers.

This system helps provide a clear view of each patient’s preventive screening status and supports reporting needs related to HEDIS measures and CMS Star Ratings. By maintaining a centralized inventory of completed screenings, healthcare teams can identify compliant patients, patients needing follow-up, and opportunities to improve preventive care outcomes.

## Purpose of the Project

Preventive health screenings are important for early detection, chronic disease management, and improved patient outcomes. However, screening information is often collected from different locations and may not always be stored in one centralized system.

This project addresses that problem by creating a simple database that can capture screening results, organize patient records, update compliance status, and generate CSV reports for quality improvement review.

## Flowchart Summary

The project follows the workflow shown in the Preventive Health Screening Inventory flowchart.

The process begins in the physician office, where the patient’s screening needs are reviewed. If the patient is due for a preventive screening, the provider orders or refers the patient for the appropriate test. The order is then sent to the correct collection hub, such as a laboratory, radiology center, endoscopy suite, or eye care center.

Once the screening is performed, the completed result is reviewed. If follow-up is needed, the patient may return for additional screening or evaluation. If the screening is completed and valid, the result is sent to the Preventive Health Screening Inventory database. The database stores the result, updates the patient’s compliance status, and generates reports that can be used for HEDIS and CMS Star Ratings quality improvement activities.

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

This Python program allows the user to:

- Create a centralized SQLite database
- Add fictitious patient screening data
- Manually enter new preventive screening records
- View all screening records in the database
- Track the collection hub where the screening was completed
- Store provider information
- Record screening type, result, date, and compliance status
- Export a full screening report to CSV
- Export a HEDIS/CMS compliance summary report to CSV
- Export a follow-up report for patients who need additional action

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
| compliance_status | Patient’s compliance status |
| measure_type | Quality measure category |
| report_year | Reporting year for HEDIS/CMS review |

## Collection Hubs

The system includes collection hubs that match the flowchart process. These are the locations where screenings may be completed before being uploaded to the database.

Examples include:

- Physician Office
- Lab
- Radiology Center
- Endoscopy Suite
- Eye Care Center

## Compliance Status Options

The system allows the following compliance status values:

- Compliant
- Needs Follow-up
- Non-Compliant
- Pending

These values help identify whether a patient has completed a required screening or still needs additional action.

## Reports Generated

The program can generate three CSV reports.

### 1. Full Screening Report

File name:

```text
phs_full_screening_report.csv



