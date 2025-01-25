# ✨ Attendance Recognition System ✨

Welcome to the **Attendance Recognition System** repository! This project is designed to streamline attendance tracking using facial recognition technology. Below is an overview of the project, its structure, and how to get started.

---

## 🌐 Project Features

- 👨‍🎓 **Student Dataset Creation**: Easily create datasets for students using the `data_creation.py` script.
- 🕵️‍♂️ **Facial Recognition**: Detect and recognize student faces using advanced pre-trained models.
- 📃 **Attendance Logging**: Automatically log attendance into a CSV file (`attendance_log.csv`).
- 📊 **Data Preprocessing**: Preprocess and embed dataset images for improved model performance.
- 🏆 **Model Training**: Train an SVC model for robust facial recognition.
- 🔄 **Dashboard Visualization**: View attendance logs in an intuitive GUI dashboard.

---

## 🔠 Repository Structure

Here’s a breakdown of the repository contents:

### 📂 Folders
- **[datasets/](datasets/)**: Contains datasets of student images. These datasets are created using the [`data_creation.py`](data_creation.py) script.
- **[model/](model/)**: Stores pre-trained models:
  - [deploy.prototxt.txt](model/deploy.prototxt.txt)
  - [res10_300x300_ssd_iter_140000.caffemodel](model/res10_300x300_ssd_iter_140000.caffemodel)
- **[output/](output/)**: Stores output embedding files:
  - [embeddings.pickle](output/embeddings.pickle)
  - [le.pickle](output/le.pickle)
  - [recognizer.pickle](output/recognizer.pickle)

### 🗞️ Key Files

- **[`Attendance-recognition.py`](https://github.com/nasim-raj-laskar/FaceRec-Attendance/blob/main/Attendence-rcognition.py)**: 🔍 The main script for recognizing student faces and logging attendance into [`attendance_log.csv`](attendance_log.csv).
- **[`pre-processing.py`](https://github.com/nasim-raj-laskar/FaceRec-Attendance/blob/main/pre-proccessing.py)**: 🔄 Preprocesses dataset images and generates embeddings for model training.
- **[`model-training.py`](model-training.py)**: 🏋️‍♂️ Trains the SVC model for facial recognition.
- **[`recognition.py`](recognition.py)**: 🕵️ A standalone face detection script using data from [`student.csv`](student.csv).
- **[`dashboard.py`](dashboard.py)**: 📊 Displays attendance logs in a graphical user interface (GUI) using data from [`attendance_log.csv`](attendance_log.csv).
- **[`data_creation.py`](data_creation.py)**: 🖌 Script to create datasets for students.
- **Other Files**:
  - 🎮 [`openface.nn4.small2.v1.t7`](openface.nn4.small2.v1.t7) and [`haarcascade_frontalface_default.xml`](haarcascade_frontalface_default.xml): Pre-trained face detection models.
  - 📄 [`student.csv`](student.csv): Contains student data.
  - 📃 [`attendance_log.csv`](attendance_log.csv): Logs attendance records.
  - 🎨 [`block-diagram.png`](block-diagram.png): A visual representation of the project workflow.


## 🚀 Getting Started

### ⚙️ Prerequisites

Ensure you have the following installed:

- 💻 Python 3.8
- 📖 Required Python libraries:
  - OpenCV
  - NumPy
  - Scikit-learn
  - Pickle

### 🔧 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/FaceRec-Attendance.git
   cd attendance-recognition
   ```

### 🚪 Running the Project

1. 📸 **Create Student Datasets**:
   ```bash
   python data_creation.py
   ```
2. ⚙️ **Preprocess Images**:
   ```bash
   python pre-processing.py
   ```
3. 🏆 **Train the Model**:
   ```bash
   python model-training.py
   ```
4. 🕵️‍♂️ **Recognize Faces & Log Attendance**:
   ```bash
   python Attendance-recognition.py
   ```
5. 🔧 **View Attendance Logs in GUI**:
   ```bash
   python dashboard.py
   ```

---

## 🔧 How It Works

1. 📸 **Dataset Creation**: Use `data_creation.py` to capture images of students and store them in the `datasets/` folder.
2. 🔄 **Preprocessing**: The `pre-processing.py` script processes images and creates embeddings for better recognition.
3. 🏋️‍♂️ **Model Training**: Train the SVC model using `model-training.py` with the processed embeddings.
4. 🕵️ **Face Recognition**: The `Attendance-recognition.py` script identifies students from `student.csv` and logs their attendance.
5. 📊 **Dashboard**: Visualize attendance data in an interactive GUI via `dashboard.py`.

---



## 📊 Example Output

- Attendance logs are stored in `attendance_log.csv`.
- Example:
  ```csv
  Student Name,Date,Time
  John Doe,2024-12-20,10:30 AM
  ```

---

## 🔧 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/nasim-raj-laskar/FaceRec-Attendance/blob/main/LICENSE) file for more details.



