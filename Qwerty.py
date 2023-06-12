from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Вопросы для умных!!!')
main_win.resize(800, 400)

num_question = -1

class Question():
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



text = QLabel('Какое животное самое быстрое на Земле?')
text1 = QPushButton('Ответить')

Group = QGroupBox('Варианты ответов')

level1 = QRadioButton('Гепард')
level2 = QRadioButton('Кот')
level3 = QRadioButton('Куала')
level4 = QRadioButton('Собака')

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(level1)
layout2.addWidget(level2)
layout3.addWidget(level3)
layout3.addWidget(level4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)

Group.setLayout(layout1)

Group3 = QButtonGroup()
Group3.addButton(level1)
Group3.addButton(level2)
Group3.addButton(level3)
Group3.addButton(level4)
 #список

answers = [level1, level2, level3, level4]

Group2 = QGroupBox('Ответ')
answer1 = QLabel('Правильно/Неправильно')
answer2 = QLabel('Гепард')

layoutN = QHBoxLayout()
layoutM = QHBoxLayout()
layoutN.addWidget(answer1)
layoutM.addWidget(answer2)

layout_1 = QVBoxLayout()
layout_1.addLayout(layoutN)
layout_1.addLayout(layoutM)

Group2.setLayout(layout_1)

layout4 = QHBoxLayout()
layout5 = QHBoxLayout()
layout6 = QHBoxLayout()

layout4.addWidget(text, alignment = Qt.AlignCenter)
layout5.addWidget(Group, alignment = Qt.AlignCenter)
layout5.addWidget(Group2, alignment = Qt.AlignCenter)
layout6.addWidget(text1, alignment = Qt.AlignCenter)
Group2.hide()

lay_main = QVBoxLayout()
lay_main.addLayout(layout4)
lay_main.addLayout(layout5)
lay_main.addLayout(layout6)

def show_question():
    Group2.hide()
    Group.show()
    text1.setText('Ответить')

def show_result():
    Group.hide()
    Group2.show()
    text1.setText('Cледующий вопрос')
    Group3.setExclusive(False)
    level1.setChecked(False)
    level2.setChecked(False)
    level3.setChecked(False)
    level4.setChecked(False)
    Group3.setExclusive(True)


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.text)
    answer2.setText(q.right_answer)
    show_question()

def correct(rs):
    answer1.setText(rs)
    show_result()

def next_question():
    global num_question
    num_question += 1
    if num_question >= len(questions):
        num_question = 0
    q = questions[num_question]
    ask(q)

def Check_answer():
    if answers[0].isChecked():
        correct('Правильно!')
    else:
        correct('Неправильно!')

def check_OK():
    if text1.text() == 'Ответить':
        Check_answer()
    else:
        next_question()

q = Question('Какое животное самое быстрое в мире?', 'Гепард', 'Кот', 'Куала', 'Собака')
q1 = Question('Какой персонаж в Dota2 имеет скилл Blackhole?', 'Enigma', 'Axe', 'Earthshaker', 'Magnus')
q2 = Question('Сколько хромосом у человека?', '46', '48', '42', '50')
q3 = Question('Столица Португалии?', 'Лиссабон', 'Варшава', 'Люксембург', 'Осло')
q4 = Question('На каком континенте находится Сенегал?', 'Евразия', 'Африка', 'Австралия', 'Южная Америка')

questions = list()
questions.append(q)
questions.append(q1)
questions.append(q2)
questions.append(q3)
questions.append(q4)

next_question()
text1.clicked.connect(check_OK)

main_win.setLayout(lay_main)
main_win.show()
app.exec_()




