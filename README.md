# GenAI-Task4-Riya
Sales and price utilities using file handling only: open() with with blocks, modes (r, w, a), read() / readline() / readlines(), and basic text parsing. No pandas, csv module or external libraries.

Files
File	Task
task1_write_sales.py	Task 1 - Write sales to sales_data.txt (+ comma-separated extra)
task2_read_ways.py	Task 2 - read(), readline(), readlines() to integers
task3_append_sales.py	Task 3 - Append new sales (+ line count extra)
task4_summary_report.py	Task 4 - Total, highest, lowest, average
task5_product_info.py	Task 5 - Write products to products.txt from user input
task6_read_safely.py	Task 6 - Read a file safely using os.path.exists()
task7_export_discounts.py	Task 7 - Export discount_report.txt (+ summary extra)
How to run

Open a terminal inside this folder, then run the files in order:

python task1_write_sales.py
python task2_read_ways.py
python task3_append_sales.py
python task4_summary_report.py
python task5_product_info.py
python task6_read_safely.py
python task7_export_discounts.py

Tasks 2, 3 and 4 need sales_data.txt, which Task 1 creates. If it is missing, they print a message telling you to run Task 1 first. Task 3 appends every time it runs, so running it twice adds the sales twice. Run Task 1 again to reset the file.

Notes
All files are opened with with open(...), so they close automatically.
Newline characters are removed with .strip() before converting to integers.
Task 4 skips blank lines and handles an empty file.
Task 7 checks that the discount is a number and not more than 100.
