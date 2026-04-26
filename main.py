from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
from random import shuffle
from random import *

class Question():
    def __init__(self, question_text, right_answer_text, wrong1_text, wrong2_text, wrong3_text):
        self.question = question_text
        self.right_answer = right_answer_text
        self.wrong1 = wrong1_text
        self.wrong2 = wrong2_text
        self.wrong3 = wrong3_text
app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

RadioButtons = QButtonGroup()
RadioButtons.addButton(rbtn_1)
RadioButtons.addButton(rbtn_2)
RadioButtons.addButton(rbtn_3)
RadioButtons.addButton(rbtn_4)

AnsGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')

    RadioButtons.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioButtons.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Correct.setText(q.right_answer)
    lb_Question.setText(q.question)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    elif (answers[1].isChecked() or 
            answers[2].isChecked() or 
            answers[3].isChecked()):
            show_correct('Неверно!')
    print('Статистика:')
    print('- Верно отвечено:', window.score)
    print('- Всего вопросов:', window.total)
    print('Рейтинг -',  window.score/ window.total * 100, '%')


def show_correct(res):
    lb_Result.setText(res)
    show_result()

def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    ask(questions_list[cur_question])
    print('Статистика:')
    print('- Верно отвечено:', window.score)
    print('- Всего вопросов:', window.total)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btn_OK.clicked.connect(click_ok)

questions_list = []

questions_list.append(
    Question('Госудраственный язык Бразилии', 'Португальский', 
    'Испанский', 'Бразильский', 'Русский')
)
questions_list.append(
    Question('Какой национальности не существует', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты')
)
questions_list.append(
    Question('Столица США',  'Вашингтон', 'Лондон', 'Москва', 'Париж')
)
questions_list.append(
    Question('Самая длинная река в мире', 'Амазонка', 'Нил', 'Волга', 'Янцзы')
)
questions_list.append(
    Question('Какая планета самая большая в Солнечной системе?', 'Юпитер', 'Сатурн', 'Земля', 'Нептун')
)
questions_list.append(
    Question('Как называется светящийся орган у глубоководных рыб?', 'фотофор', 'биолампа', 'люминофор', 'светоточка')
)
questions_list.append(
    Question('Как называется слой старого уплотнённого снега в горах?', 'фирн', 'наст', 'лёд', 'сугроб')
)
questions_list.append(
    Question('Сколько камер в сердце дельфина?', '4', '2', '3', '1')
)
questions_list.append(
    Question('Какой язык считается «мёртвым»?', 'латынь', 'иврит', 'санскрит', 'баскский')
)
questions_list.append(
    Question('Из каких двух химических элементов состоит вода?', 'водород и кислород', 'азот и кислород', 'углерод и водород', 'кислород и сера')
)
questions_list.append(
    Question('Как называется начальная стадия шахматной партии?', 'дебют', 'миттельшпиль', 'эндшпиль', 'гамбит')
)
questions_list.append(
    Question('Какая команда выиграла первый чемпионат мира по футболу (1930 год)?', 'Уругвай', 'Италия', 'Бразилия', 'Аргентина')
)
questions_list.append(
    Question('Какой диаметр у стандартного мяча для настольного тенниса?', '40 мм', '38 мм', '42 мм', '45 мм')
)


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.resize(400, 300)
window.show()

window.total = 0
window.score = 0
next_question()
app.exec()