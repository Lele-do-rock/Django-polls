from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from polls.models import Question, Choice
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

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

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context['form_title'] = 'Editando pegunta'

        question_id = self.kwargs.get('pk')
        Choices = Choice.objects.filter(question_pk=question_id)
        context['question_choices'] = Choices

        return context

class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'polls/choice_forn.html'
    fields = ('choice_text',)
    succes_message = 'Alternativa registrada com sucesso'

    def dispatch(self, request, *args, **kwargs):
        self.question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        return super(ChoiceCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))

        context = super(ChoiceCreateView, self).get_context_data(**kwargs)
        context['form_title'] = f'Alternativa para: {question.question_text}'

        return context

    def form_valid(self, form):
        form.instance.question = self.question
        messages.success(self.request, self.success_messages)
        return super(ChoiceCreateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        Question_id = self.kwargs.get('pk')
        return reverse_lazy('poll_edit', kwargs={'pk': Question_id})

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls/question_detail.html'
    context_object_name = 'question'

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'polls/question_confirm_delete_form.html'
    success_url = reverse_lazy('polls_all')
    success_message = 'Pergunta excluída com sucesso.'


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

def form_valid(self, request, *args, **kwargs):
    messages.success(self.request, self.success_message)
    return super(QuestionDeleteView, self).form_valid(request, *args, **kwargs)