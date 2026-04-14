from django.shortcuts import render, redirect
from feedback.models import Feedback
from django.views.generic import View

class FeedbackView(View):
    def post (self, request):
        form = FeedbackView(request.POST)
        if form.is_vali():
            form.save()
        return redirect("/")
    