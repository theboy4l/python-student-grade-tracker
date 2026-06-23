# 📊 Student Grade Tracker

A Python command-line application that allows users to manage student grades using a CSV file.  
It demonstrates file handling, sorting, input validation, and basic data analysis in Python.

---

## 🚀 Features

- ➕ Add new students with validated names and grades
- 📋 View all students sorted by highest grade
- 🔍 Search for a student by name
- 📊 Calculate class average using statistical functions
- 💾 Persistent data storage using CSV files

---

## 🛠️ Built With

- Python 3
- CSV module (file handling)
- Statistics module (average calculation)
- OS module (file checks)
- Sys module (program exit handling)

---

## 📂 Project Structure

```text
student-grade-tracker/
│
├── project.py          # Main application logic
├── students.csv        # Data storage (auto-created/updated)
├── README.md           # Project documentation
├── requirements.txt    # Dependencies (none required)
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/student-grade-tracker.git
   cd student-grade-tracker
   ```

2. **Ensure Python 3 is installed**
   ```bash
   python --version
   ```

3. **Run the application**
   ```bash
   python project.py
   ```

> No additional dependencies are required. All modules used are part of the Python standard library.

---

## 💡 Usage

Once the program is running, you will be presented with an interactive menu:

```
=============================
   Student Grade Tracker
=============================
1. Add Student
2. View All Students
3. Search Student
4. Class Average
5. Exit
```

### ➕ Add a Student
Enter a student's name and a grade between **0 and 100**. The application validates both inputs before saving to the CSV file.

### 📋 View All Students
Displays all students sorted from **highest to lowest grade** in a formatted table.

### 🔍 Search for a Student
Enter a name to look up a specific student's grade. The search is **case-insensitive**.

### 📊 Class Average
Calculates and displays the **mean grade** across all students using Python's `statistics` module.

### 🚪 Exit
Safely exits the program.

---

## 📄 Data Storage

Student records are stored in `students.csv` in the following format:

```csv
Name,Grade
Alice,92
Bob,85
Charlie,78
```

The file is **automatically created** on first run if it does not already exist.

---

## ✅ Input Validation

- **Name:** Must be a non-empty string containing only alphabetic characters and spaces.
- **Grade:** Must be a numeric value between `0` and `100` (inclusive).
- Invalid inputs prompt the user to re-enter the value.

---

## 🧪 Example Output

```
Enter student name: Alice
Enter grade (0-100): 92
✅ Student 'Alice' added successfully!

--- All Students (Sorted by Grade) ---
Name        Grade
----        -----
Alice       92
Bob         85
Charlie     78

📊 Class Average: 85.00
```

---

## 🙌 Acknowledgements

Built as a Python fundamentals project to practice:
- File I/O with the `csv` module
- Data validation and error handling
- Sorting and statistical analysis
- CLI-based user interaction

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).