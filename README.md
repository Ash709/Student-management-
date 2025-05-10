# Student Record Management System (Python + MySQL)

A simple console-based student record management system using Python and MySQL.

## Features

- Add, view, update, delete student records
- Connects to MySQL using mysql-connector-python
- Clean CLI interface

## Setup Instructions

1. Install MySQL and create database/table:
   ```sql
   CREATE DATABASE school;
   USE school;
   CREATE TABLE students (
       id INT PRIMARY KEY,
       name VARCHAR(100),
       marks INT
   );
