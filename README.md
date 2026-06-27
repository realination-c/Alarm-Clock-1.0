# Object-Oriented Alarm Clock (Python & Tkinter)

A clean, structured alarm clock application built using **Object-Oriented Programming (OOP)** principles in Python with a graphical interface (GUI) powered by Tkinter.

## 🚀 Features

* **OOP Architecture:** Fully encapsulated logic within an `AlarmClock` class for better maintainability and code readability.
* **Smart Time Validation:** Strict checks for user input format (`HH:MM`), preventing errors and invalid time entry.
* **Custom Alarm Sound:** Dynamic file selection dialog allows users to choose any custom `.mp3` or `.wav` file.
* **Precise Clock Loop:** Runs a lightweight background check using Tkinter's event loop (`.after()`) without freezing the UI.
* **Control Buttons:** Start, stop, and configure the alarm dynamically with immediate interface feedback.

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** (Graphical User Interface)
* **OS & Datetime** (System file management and real-time clock tracking)

## 💻 How to Run

1. Make sure you have Python installed.
2. Clone the repository and navigate to the project folder.
3. Run the application:

```bash
python main.py