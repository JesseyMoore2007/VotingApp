from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.Submit_Button.clicked.connect(lambda: self.submit())

        self.votes:dict = {}

        first_row = ["ID", "Candidate"]
        with open("votes.csv", "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(first_row)

    def submit(self) -> None:
        with open("votes.csv", "a", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            try:
                if self.ID_Input.text().isdigit() or len(self.ID_Input.text()) != 6:
                    user_id:int = int(self.ID_Input.text())
                else:
                    raise ValueError("Enter Valid ID\n(6 numbers)")
                if user_id in self.votes:
                    raise ValueError("Already Voted")
                else:
                    if self.John_Radio.isChecked():
                        candidate = "John"
                    elif self.Jane_Radio.isChecked():
                        candidate = "Jane"
                    else:
                        raise ValueError("Pick A Candidate")
                    self.votes[user_id] = candidate
                    csv_writer.writerow([user_id, candidate])
            except ValueError as e:
                self.Error_Label.setStyleSheet("color: red")
                self.Error_Label.setText(str(e))
            else:
                self.Error_Label.setStyleSheet("color: green")
                self.Error_Label.setText("Vote Submitted!")
