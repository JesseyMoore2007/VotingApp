from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.Submit_Button.clicked.connect(lambda: self.submit())

        self.__votes:list = []
        self.__john_votes = 0
        self.__jane_votes = 0

        first_row = ["ID", "Candidate", "John Votes", "Jane Votes"]
        with open("votes.csv", "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(first_row)

    def submit(self) -> None:
        '''
        This function happens when the user clicks the submit button.
        this function will validate all inputs and radio buttons before
        either throwing an error, or succesfully sending the vote into
        votes.csv
        :return:
        '''
        with open("votes.csv", "a", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            try:
                user_input = self.ID_Input.text()
                if user_input.isdigit() and len(user_input) == 6:
                    user_id:int = int(user_input)
                else:
                    raise ValueError("Enter Valid ID\n(6 numbers)")
                if user_id in self.__votes:
                    raise ValueError("Already Voted")
                else:
                    if self.John_Radio.isChecked():
                        candidate = "John"
                        self.__john_votes += 1
                    elif self.Jane_Radio.isChecked():
                        candidate = "Jane"
                        self.__jane_votes += 1
                    else:
                        raise ValueError("Pick A Candidate")
                    self.__votes.append(user_id)
                    csv_writer.writerow([user_id, candidate, self.__john_votes, self.__jane_votes])
            except ValueError as e:
                self.Error_Label.setStyleSheet("color: red")
                self.Error_Label.setText(str(e))
            else:
                self.Error_Label.setStyleSheet("color: green")
                self.Error_Label.setText(f"Vote Submitted!")
                self.clear()

    def clear(self):
        self.John_Radio.checked = False
        self.Jane_Radio.setChecked(False)
        self.ID_Input.setText("")
