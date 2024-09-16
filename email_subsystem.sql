-- Create the database
CREATE DATABASE IF NOT EXISTS email_subsystem;
USE email_subsystem;

-- Table: checklist
CREATE TABLE checklist (
    SL_No VARCHAR(4),
    Mail_ID VARCHAR(60),
    Item VARCHAR(500),
    Status VARCHAR(15)
);

-- Table: inbox
CREATE TABLE inbox (
    SL_No VARCHAR(4),
    FMail_ID VARCHAR(60),
    TMail_ID VARCHAR(60),
    Subject VARCHAR(50),
    Mail VARCHAR(1000),
    Status VARCHAR(15)
);

-- Table: user_details
CREATE TABLE user_details (
    SL_No VARCHAR(4),
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Mail_ID VARCHAR(60),
    Password VARCHAR(60),
    DOB VARCHAR(30),
    Gender VARCHAR(10),
    City_Of_Birth VARCHAR(30)
);
