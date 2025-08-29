# commandhub.py
import streamlit as st
import subprocess
import psutil

st.set_page_config(page_title="CommandHub", layout="wide")
st.title("🖥️ CommandHub – All in One Command & Tool Platform")

# Sidebar
st.sidebar.header("CommandHub Controls")
option = st.sidebar.selectbox(
    "Choose Action",
    ("Execute Command", "System Monitor", "Tool Manager")
)

# -------------------------
# Execute Command
# -------------------------
if option == "Execute Command":
    st.header("💻 Execute System Commands")
    command = st.text_input("Enter a system command:")
    if st.button("Run Command"):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            st.code(output)
        except subprocess.CalledProcessError as e:
            st.error(f"Error: {e.output}")

# -------------------------
# System Monitor
# -------------------------
elif option == "System Monitor":
    st.header("📊 System Monitoring")
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    st.metric("CPU Usage", f"{cpu_usage}%")
    st.metric("Memory Usage", f"{memory.percent}%")
    st.metric("Disk Usage", f"{disk.percent}%")

    st.bar_chart({"CPU": [cpu_usage], "Memory": [memory.percent], "Disk": [disk.percent]})

# -------------------------
# Tool Manager
# -------------------------
elif option == "Tool Manager":
    st.header("🛠️ Tool Manager")
    st.write("You can add your favorite tool commands here to execute quickly.")
    tools = {"List Files": "ls -la", "Ping Google": "ping -c 4 google.com"}
    selected_tool = st.selectbox("Select Tool", list(tools.keys()))
    if st.button("Run Tool"):
        try:
            output = subprocess.check_output(tools[selected_tool], shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            st.code(output)
        except subprocess.CalledProcessError as e:
            st.error(f"Error: {e.output}")

