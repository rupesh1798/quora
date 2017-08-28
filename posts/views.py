from django.shortcuts import render, get_object_or_404
from .models import Question, Answer, Comment
from .forms import AnswerForm

def question_list(request):
    questions = Question.objects.order_by('published_date')
    answers = Answer.objects.order_by('date')
    return render(request, 'posts/home.html', {'questions': questions, 'answers':answers})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question = question).order_by('date')
    return render(request, 'posts/post_detail.html', {'question': question, 'answers':answers})
def add_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.date = timezone.now()
            answer.save()
            return redirect('question_detail', pk=post.pk)
    else:
        form = AnswerForm()
    return render(request, 'posts/add_answer.html', {'form': form, 'question': question})
