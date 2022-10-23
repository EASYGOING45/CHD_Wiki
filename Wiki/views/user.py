from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.db.models import Q
from ..models import *
# from .settings import *
# from .schedule import get_schedules
import datetime
import copy

def index(request):
    return render(request, "../templates/index.html")