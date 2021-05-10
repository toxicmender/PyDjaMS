from django.http import HttpResponse, HttpRequest
from django.http.response import Http404

from .models import Question


def index(request: HttpRequest, count: int = 5) -> HttpResponse:
    latest_questions_list = Question.objects.order_by("-pub_date")[:count]
    output: str = ", ".join([q.question_test for q in latest_questions_list])
    return HttpResponse("Hello, world. You're at the polls index.", output)


def detail(request: HttpRequest, question_id: int = 0) -> HttpResponse:
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist")
    return HttpResponse(f"You're looking at question: {question_id}")


def results(request: HttpRequest, question_id: int = 0) -> HttpResponse:
    return HttpResponse(f"You're looking at the results of question: {question_id}")


def vote(request: HttpRequest, question_id: int = 0) -> HttpResponse:
    return HttpResponse(f"You're voting on question: {question_id}")
