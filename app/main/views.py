from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_news,search_news
from .forms import ReviewForm
from ..models import Review
