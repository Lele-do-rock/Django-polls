from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from polls.models import Question, Choice
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

print()

def index(request):
    return HttpResponse("Olá... Seja bem vindo à enquete")

def sobre(request):
    return HttpResponse("Olá este é um app de enquete!")

def exibe_questao(request, question_id):
    questao = Question.objects.get(id=question_id)
    return HttpResponse(questao.question_text)

def ultimas_perguntas(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/perguntas.html', context)

def vote (request, question_id):
    return HttpResponse(f"Você vai na pergunta")

class QuestionCreateView(CreateView):
    model = Question
    success_url = reverse_lazy ('index')

class QuestionUpdateView(UpdateView):
    model = Question
    template_name = 'polls/question_form.html'
    fields = ('question_text', 'pub_date', )
    success_url = reverse_lazy('polls_list')

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls/question_detail.html'
    context_object_name = 'question'

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'polls/question_confirm_delete_form.html'
    success_url = reverse_lazy('polls_list')

class QuestionListView(ListView):
    model = Question
    template_name = 'polls/question_list.html'
    context_object_name= 'questions'

class SobreTemplateView(TemplateView):
    template_name = 'polls/sobre.html'


@login_required # controle de acesso usando o decorador de função
def sobre(request):
    return HttpResponse('Este é um app de enquete!')

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question