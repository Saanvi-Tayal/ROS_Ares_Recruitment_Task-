# ROS 2 Simple Obstacle Avoidance 

---

## 🧠 The Core Idea: Sense -> Decide -> Act

Think of the robot like a living creature looping through three basic steps:
1. **Sense:** Check the front distance sensor to see what's ahead.
2. **Decide:** Use a basic `if/else` check (`Is the path clear?`).
3. **Act:** Tell the wheels to move forward or turn around based on that decision.

---

## 🚀 How to Run It

1. Make sure your ROS 2 environment is sourced.
2. Drop this script into your ROS 2 package's python directory.
3. Make the file executable:
   ```bash
   chmod +x your_script_name.py
   ```
4. Run the node:
   ```bash
   ros2 run your_package_name your_script_name
   ```