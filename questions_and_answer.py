import json
import os
import sys


def read_question_file(filename):
    if not os.path.isfile(filename):
        return None
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except ValueError as e:
            print(e)
            print('加载题库错误。')
            return None


def to_answer(letter, a_len):
    letter = letter.upper()
    if len(letter) == 1 and 'A' <= letter <= 'Z':
        digit = ord(letter) - ord('A')
        if 0 <= digit <= a_len:
            return digit, True
        else:
            return None, False
        return digit, True
    else:
        return None, False


def to_letter(n):
    return chr(ord('A') + n)


def ask_question(question, i):
    print('第{0}题：{1}'.format(i+1, question['question']))
    answers = question['answer']
    a_len = len(answers)
    for j in range(a_len):
        print('{0}:{1}'.format(to_letter(j), answers[j]))
    user_input = input('请输入答案:')
    user_answer, ok = to_answer(user_input, a_len)
    while not ok:
        user_input = input('输入错误，请重新输入选项')
        user_answer, ok = to_answer(user_input, a_len)

    return user_answer == question['t_answer']


def main(argv):
    if len(argv) != 2:
        print('请指定题库json文件')
        sys.exit(-1)
    filename = argv[1]

    question_json = read_question_file(filename)
    if not question_json:
        print('题库文件读取失败，请检查：{0}'.format(filename))
        sys.exit(-1)

    name = question_json['name']
    question_list = question_json['question_list']

    print('答题开始，当前题库为：{0}'.format(name))

    q_len = len(question_list)
    correct_count = 0
    for i, q in enumerate(question_list):

        if ask_question(q, i):
            correct_count += 1

    print("答题完成，共{0}道题目，你答对了{1}道题目，正确率{2}%".format(q_len, correct_count, correct_count/q_len*100))


if __name__ == '__main__':
    main(sys.argv)
