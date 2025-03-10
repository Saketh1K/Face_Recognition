Here's a **README.md** file for your project. You can place this in your GitHub repository to help others understand and use your **Face Recognition Attendance System**.  

---

### **README.md**
```markdown
# Face Recognition Attendance System

This project is a **Face Recognition Attendance System** that detects and identifies faces to log attendance automatically. It uses **OpenCV**, **scikit-learn**, and **Streamlit** for real-time face detection, recognition, and attendance tracking.

## 🚀 Features
- 📷 **Face Detection** using OpenCV's Haar cascades
- 🧠 **Face Recognition** using K-Nearest Neighbors (KNN)
- 📜 **Attendance Logging** with timestamps
- 📊 **Live Dashboard** using Streamlit
- 🔄 **Auto Refresh** to update attendance records in real time

---

## 📂 Project Structure
```
📁 Face_Recognition
│── 📁 data              # Stores trained face data (names.pkl, faces.pkl)
│── 📁 Attendance        # Stores attendance CSV files
│── 📄 add_faces.py      # Script to add new faces to the dataset
│── 📄 test.py           # Main face recognition and attendance script
│── 📄 app.py            # Streamlit-based attendance dashboard
│── 📄 README.md         # Project documentation (this file)




```

---

## 🛠 Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Saketh1K/Face_Recognition.git
   cd Face_Recognition
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure OpenCV's Haarcascade File is Available**  
   Download `haarcascade_frontalface_default.xml` from [here](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the `data/` folder.

---

## 🎯 Usage

### 1️⃣ **Add New Faces**
Run the script to capture face data:
   ```bash
   python add_faces.py
   ```
   - Enter your name when prompted.
   - The script captures 100 images and saves them for training.

### 2️⃣ **Start Face Recognition & Attendance Logging**
   ```bash
   python test.py
   ```
   - Press **'o'** to log attendance.
   - Press **'q'** to quit.

### 3️⃣ **Launch Attendance Dashboard**
   ```bash
   streamlit run app.py
   ```
   - Opens a web dashboard to view real-time attendance.

## 🏗 Future Improvements
- 🏷️ Improve accuracy with deep learning (e.g., CNNs)
- 🌍 Cloud storage for attendance records


### 📌 Next Steps:
- Save this file as **README.md** in your project folder.
- Add and push it to GitHub:
  ```bash
  git add README.md
  git commit -m "Added README file"
  git push origin main
  ```


