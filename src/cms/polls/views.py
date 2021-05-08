from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request: HttpRequest, question_id: int = 0) -> HttpResponse:
    return HttpResponse(f"You're looking at question: {question_id}")


def results(request: HttpRequest, question_id: int = 0) -> HttpResponse:
    return HttpResponse(f"You're looking at the results of question: {question_id}")


def vote(request: HttpRequest, question_id: int = 0) -> HttpResponse:
    return HttpResponse(f"You're voting on question: {question_id}")
