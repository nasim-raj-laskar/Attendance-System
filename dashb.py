import sys
import csv
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class AttendanceDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Attendance Dashboard")
        self.setGeometry(100, 100, 1000, 700)
        self.setStyleSheet("background-color: #f0f8ff;")     
        self.layout = QVBoxLayout(self)
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)  
        self.table.setHorizontalHeaderLabels(["Name", "Roll Number", "Timestamp"])
        self.table.setStyleSheet(
            "QTableWidget {background-color: #ffffff; color: #333333; border: 1px solid #ccc;} "
            "QHeaderView::section {background-color: #87CEFA; font-weight: bold;}")
        self.layout.addWidget(self.table)
        self.load_button = QPushButton("Load Attendance Data", self)
        self.load_button.setStyleSheet("QPushButton {background-color: #32CD32; color: white; font-size: 16px; padding: 10px; border-radius: 5px;} "
            "QPushButton:hover {background-color: #228B22;}")
        self.load_button.clicked.connect(self.load_attendance_data)
        self.layout.addWidget(self.load_button)

        self.chart_canvas = FigureCanvas(plt.figure(figsize=(8, 4)))
        self.layout.addWidget(self.chart_canvas)

    def load_attendance_data(self):
        attendance_data = []
        try:
            with open('Attendence-System-Face-Recognition/attendance_log.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
                headers = next(reader)
                attendance_data = list(reader)

            self.table.setRowCount(len(attendance_data))
            for i, row in enumerate(attendance_data):
                for j, value in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(value))
            self.visualize_data(attendance_data)
        except FileNotFoundError:
            QMessageBox.warning(self, "File Not Found", "Attendance log file not found!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def visualize_data(self, data):
        attendance_counts = {}
        for row in data:
            if len(row) >= 2: 
                name = row[0]
                attendance_counts[name] = attendance_counts.get(name, 0) + 1

        if not attendance_counts:
            QMessageBox.warning(self, "No Data", "No valid attendance data to visualize.")
            return

        self.chart_canvas.figure.clear()
        ax = self.chart_canvas.figure.add_subplot(111)
        ax.bar(attendance_counts.keys(), attendance_counts.values(), color='#ff6347')  
        ax.set_title("Attendance Records", fontsize=16, color='#333333')
        ax.set_xlabel("Student Name", fontsize=12, color='#333333')
        ax.set_ylabel("Attendance Count", fontsize=12, color='#333333')
        ax.set_xticks(range(len(attendance_counts)))
        ax.set_xticklabels(attendance_counts.keys(), rotation=45, ha='right', color='#333333')
        ax.tick_params(axis='y', labelcolor='#333333')
        ax.set_facecolor('#f0f8ff')
        self.chart_canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AttendanceDashboard()
    window.show()
    sys.exit(app.exec_())
