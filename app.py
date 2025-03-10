import streamlit as st
import pandas as pd
import time
import os
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Get current timestamp
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

# Auto-refresh to update the attendance file every 2 seconds
st_autorefresh(interval=2000, key="attendance_refresh")

st.title("📋 Face Recognition Attendance System")

# Define file path for today's attendance
attendance_file = f"Attendance/Attendance_{date}.csv"

# Ensure directory exists
if not os.path.exists("Attendance"):
    os.makedirs("Attendance")
    st.warning("⚠ 'Attendance' directory was missing and has been created.")

# Check if attendance file exists
if os.path.exists(attendance_file):
    # Load attendance data
    df = pd.read_csv(attendance_file)
    
    # Display attendance records
    st.success(f"✅ Attendance data loaded for {date}")
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.warning(f"⚠ No attendance data available for {date}. The file '{attendance_file}' was not found.")

st.write("Press **'o'** in the face recognition script to take attendance.")