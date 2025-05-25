import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load saved model
model = joblib.load(r'D:\Internship_project\StudentPerformance\student_pass_predictor.joblib')



# Function to predict pass/fail
def predict_pass():
    try:
        # Example inputs - replace these with real GUI input entries
        inputs = [
            int(entry_age.get()),
            int(entry_studytime.get()),
            # Add all features you want here in correct order
            # Must match model training feature order!
        ]
        inputs = np.array(inputs).reshape(1, -1)

        prediction = model.predict(inputs)[0]
        result = "Pass" if prediction == 1 else "Fail"
        messagebox.showinfo("Prediction Result", f"Student will likely: {result}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create GUI window
root = tk.Tk()
root.title("Student Pass Predictor")

tk.Label(root, text="Age").grid(row=0, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=0, column=1)

tk.Label(root, text="Study Time").grid(row=1, column=0)
entry_studytime = tk.Entry(root)
entry_studytime.grid(row=1, column=1)

# Add other inputs here following the pattern above

tk.Button(root, text="Predict", command=predict_pass).grid(row=10, column=0, columnspan=2)

root.mainloop()
