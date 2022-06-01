import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi There")
        self.setLayout(qtw.QVBoxLayout())
        # label
        my_label = qtw.QLabel("pick sth mf")
        my_label.setFont(qtg.QFont('Helvetica',24))
        self.layout().addWidget(my_label)  

        # Create a button 
        my_button = qtw.QPushButton("I dare u",
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        # ## Create an Combo box
        # my_combo = qtw.QComboBox(self,
        # editable=True,insertPolicy=qtw.QComboBox.InsertAtBottom)
        # # Add Items to the Combo Box
        # my_combo.addItem("IDGAF ",qtw.QWidget)
        # my_combo.addItem("IDGAF ","f off")
        # my_combo.addItem("IDGAF",5)
        # my_combo.addItem("IDGAF")

        # self.layout().addWidget(my_combo)
        # this makes the magic appear 


        # Create Spin Bpx
        my_spin = qtw.QSpinBox(self,value=10,maximum=100,minimum=0,singleStep=5,prefix="#",suffix=' order')
        # Change font size of spin box
        my_spin.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_spin)



        self.show()

        def  press_it():
            my_label.setText(f'You Picked {my_spin.value()}')


            # ADd name to label
            # my_label.setText(f'You Picked {my_combo.currentData()}')
            # my_label.setText(f'You Picked {my_combo.currentText()}')
            # my_label.setText(f'You Picked {my_combo.currentIndex()}')

app =qtw.QApplication([])
mw =MainWindow()
app.exec_()







# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg

# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         # Add a title
#         self.setWindowTitle("hello world")    

#         # Set Vertical layout
#         self.setLayout(qtw.QVBoxLayout())   
#         # Create A Label
#         my_label =qtw.QLabel("Hello There")
#         my_label.setFont(qtg.QFont('Helvetica',18))
#         self.layout().addWidget(my_label)
#         # Create an entry
        # my_entry = qtw.QLineEdit()
        # my_entry.setObjectName("ma,e_field")
        # my_entry.setText('')
#         self.layout().addWidget(my_entry)
        # # Create a button 
        # my_button = qtw.QPushButton("I dare u",
        # clicked = lambda: press_it())
        # self.layout().addWidget(my_button)
#         self.show()
#         def  press_it():
#             # ADd name to label
#             my_label.setText(f'Hello {my_entry.text()}')
#             # Clear entry
#             my_entry.setText("")

# app = qtw.QApplication([])
# mw =MainWindow()

# app.exec_()