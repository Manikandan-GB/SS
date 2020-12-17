from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ..model import QuestionAnswers, QuestionAnswersOption, QuizQuestions, UserScores
from ..forms import PythonQuizForm

def quizpageview(request, id):
    quiz_file_name = "sample_quiz_{0}.html".format(str(id))
    quiz_info = QuestionAnswersOption.objects.all()

    if request.method == "GET":
        return render(request, quiz_file_name, {'data': quiz_info})
    if request.method == "POST":
        # This methods should get the answers validated or the question and answer in a list[dict format]
        # eg: [{questoin_1: answer}, {question_2: answer}]
        quiz_id = id
        question_mark = 1
        python_quiz_form = PythonQuizForm(request.POST)
        if python_quiz_form.is_valid():
            # Store the data in Table for each question and answer and return to home page on success.
            user = request.user
            answered_questions=len(python_quiz_form)
            correct_answers = 0
            for ques, ans in python_quiz_form.ieritems():
                res = QuestionAnswers.objects.get(question_answer = ans)
                if res:
                    res +=1
                score = UserScores(user = user, quiz = quiz_id, questions_answered = answered_questions,
                                 questions_answered_correctly = correct_answers, user_score = correct_answers*question_mark)
                score.save()

            return HttpResponse(request, 'quizindex.html')

        return render(request, quiz_file_name, {'data': python_quiz_form})






