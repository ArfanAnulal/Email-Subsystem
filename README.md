# Email Subsystem Database

This project includes the SQL scripts necessary to set up the `email_subsystem` MySQL database, which contains three tables: `checklist`, `inbox`, and `user_details`. These tables are designed to handle user data, email checklists, and inbox information. 

I created this during my high school years in 2021, when I first started learning Python and MySQL, which were my first programming languages. My goal was to build a Google Suite clone (Gmail, Google Drive) as a personal project. I aimed to implement email authentication and image upload functionality into the database, but I couldn't achieve that back then. As a result, if you try to use the photo upload option, the program exits. Please excuse my past self if the logic seems redundant 😅

The `#Mail` and `$Forgotpwd` files are for the GUI and password reset options, respectively. I had to stop halfway due to upcoming exams, but I've uploaded them in case anyone wants to build upon them.

## Table of Contents

- [Installation](#installation)
- [Database Structure](#database-structure)
  - [Checklist Table](#checklist-table)
  - [Inbox Table](#inbox-table)
  - [User Details Table](#user-details-table)
- [How to Use](#how-to-use)
- [License](#license)

## Installation

### Prerequisites:
- MySQL installed on your system
- A MySQL user account with privileges to create databases

### Steps:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/email-subsystem.git
   cd email-subsystem
2. Open your MySQL client and log in:
   ```bash
   mysql -u your_username -p
3. Create the `email_subsystem` database and its tables by running the SQL script:
   ```bash
   source path_to_this_repository/email_subsystem.sql;
4. The database with all the necessary tables will be created and ready to use.
5. Enter password of your MySQL database into each file at the location specified at the header of the file

## Database Structure

### Checklist Table

This table stores items associated with email checklists.

| Field   | Type        | Null | Description                         |
|---------|-------------|------|-------------------------------------|
| SL_No   | VARCHAR(4)  | YES  | Serial number for checklist items   |
| Mail_ID | VARCHAR(60) | YES  | Identifier for associated mail      |
| Item    | VARCHAR(500)| YES  | Description of the checklist item   |
| Status  | VARCHAR(15) | YES  | Current status of the item (e.g., completed, pending) |

### Inbox Table

This table stores information about emails in the inbox, including sender and recipient information.

| Field    | Type        | Null | Description                        |
|----------|-------------|------|------------------------------------|
| SL_No    | VARCHAR(4)  | YES  | Serial number for inbox items      |
| FMail_ID | VARCHAR(60) | YES  | Sender email ID                    |
| TMail_ID | VARCHAR(60) | YES  | Recipient email ID                 |
| Subject  | VARCHAR(50) | YES  | Email subject                      |
| Mail     | VARCHAR(1000)| YES  | Content of the email               |
| Status   | VARCHAR(15) | YES  | Status of the email (e.g., read/unread) |

### User Details Table

This table stores personal information about users.

| Field         | Type        | Null | Description                    |
|---------------|-------------|------|--------------------------------|
| SL_No         | VARCHAR(4)  | YES  | Serial number for user records |
| First_Name    | VARCHAR(50) | YES  | User's first name              |
| Last_Name     | VARCHAR(50) | YES  | User's last name               |
| Mail_ID       | VARCHAR(60) | YES  | User's email ID                |
| Password      | VARCHAR(60) | YES  | User's password                |
| DOB           | VARCHAR(30) | YES  | User's date of birth           |
| Gender        | VARCHAR(10) | YES  | User's gender                  |
| City_Of_Birth | VARCHAR(30) | YES  | User's city of birth           |

## How to Use

Once the database is set up, you can:
- Insert user data into the `user_details` table.
- Track emails and messages using the `inbox` table.
- Manage checklist items linked to specific emails in the `checklist` table.

The tables are flexible and can be modified to suit additional requirements for email systems.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

