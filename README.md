# 🛠️ File Automation Script using Python

## 📌 Project Overview
This project is a Python-based automation script that automatically moves all `.jpg` image files from a source folder to a destination folder.  
It helps automate repetitive file organization tasks and demonstrates basic file handling and automation using Python.

This project was developed as part of the **CodeAlpha Python Programming Internship (Task 3 – Automation)**.

---

## 🎯 Features
- Automatically detects `.jpg` files in a source folder  
- Moves image files to a destination folder  
- Leaves other file types unchanged  
- Displays status messages for each moved file  
- Simple and beginner-friendly automation script  

---

## 🛠️ Technologies Used
- Python  
- os module  
- shutil module  

---

## ▶️ How the Script Works
1. The script checks if the source and destination folders exist  
2. It scans all files in the source folder  
3. Files ending with `.jpg` are identified  
4. Each `.jpg` file is moved to the destination folder  
5. The script displays the total number of files moved  

---

## ▶️ How to Run the Project
1. Install Python (version 3.x)  
2. Create the following folder structure:

CodeAlpha_FileAutomation/

│── file_automation.py
│
├── source_files/
│ ├── img1.jpg
│ ├── img2.jpg
│ ├── notes.txt
│
├── destination_files/


3. Open terminal or IDLE  
4. Navigate to the project folder  
5. Run the script:

python file_automation.py


---

## 📊 Sample Output
```
✅ Moved: img1.jpg
✅ Moved: img2.jpg

🎉 Total .jpg files moved: 2


## 📂 Project Structure
```
CodeAlpha_FileAutomation/
│── file_automation.py
│── README.md
│
├── source_files/
├── destination_files/


---

## 📚 Learning Outcomes
- Learned how to automate file operations using Python  
- Gained hands-on experience with os and shutil modules  
- Understood directory traversal and file filtering  
- Built a real-world automation script  

---

## 👩‍💻 Author
Vani Sri Rao  
Python Programming Intern – CodeAlpha

