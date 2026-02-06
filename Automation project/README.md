📊 CSV Price & Quantity Cleaning Automation

This project is a Python automation tool that validates, cleans, and logs CSV data containing price and quantity columns.
It removes rows with missing values while ensuring data loss stays within a user-defined threshold.

🚀 Features

✅ Validates CSV file existence, format, and required columns

🧹 Cleans rows with missing price or quantity values

📉 Prevents excessive data loss using a max deviation threshold

📝 Logs all steps to both console and file

💾 Saves cleaned data to a new CSV file

📁 Project Structure
Automation project/
│
├── main.py            # Entry point of the automation
├── cleaner.py         # Data cleaning logic
├── validator.py       # CSV validation logic
├── logger_config.py   # Logging configuration
├── automation.log     # Log file (auto-generated)
└── cleaned_output.csv # Output file (auto-generated)

🛠 Requirements

Python 3.9+

pandas

Install dependencies:

pip install pandas

▶️ How to Run

Open a terminal in the project folder

Run:

python main.py


Provide the requested inputs:

CSV file path

Price column name

Quantity column name

Maximum allowed deviation (e.g. 0.05 for 5%)

📌 Example Input
Enter CSV file path: "C:\Users\hsgvb\Documents\data\sales.csv"
Enter price column name: price
Enter quantity column name: quantity
Enter max allowed deviation (e.g. 0.05): 0.1

📤 Output

Cleaned CSV file saved as:

cleaned_output.csv


Logs written to:

automation.log

📈 Deviation Logic Explained

Deviation is calculated as:

(number of rows dropped) / (original number of rows)


If the deviation exceeds the max allowed value, the original dataset is returned to prevent excessive data loss.

🧾 Logging

Logs include:

Validation results

Number of rows dropped

Deviation percentage

Errors and warnings

Logs are written to:

Console

automation.log

🔒 Error Handling

The script safely handles:

Missing files

Empty CSVs

Missing columns

Invalid file formats

Excessive data loss

🔮 Future Improvements

Add unit tests

Convert to CLI with arguments

Support multiple column pairs

Add configuration file support

Enable log rotation

👤 Author

Created as a Python automation and data-cleaning practice project.