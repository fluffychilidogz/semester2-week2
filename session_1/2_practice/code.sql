-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit

Select Books.title, Members.name, Loans.loan_date
From
Books Left Join Members Left Join Loans
On Books.id = Loans.book_id;
-- write your sql code here
