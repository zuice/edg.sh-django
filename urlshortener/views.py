import os
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


from urlshortener.forms import UrlForm
from urlshortener.models import Url


@login_required(login_url="/auth/login")
def dashboard_view(request: HttpRequest):
    urls = Url.objects.filter(user_id=request.user.id)
    app_url = os.environ.get("APP_URL")

    return render(request, "dashboard.html", {"urls": urls, "app_url": app_url})


def link_view(_: HttpRequest, slug: str):
    url = Url.objects.get(slug=slug)
    url.clicks += 1
    url.save()
    return redirect(url.url)


@login_required(login_url="/auth/login")
def create_view(request: HttpRequest):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.user_id = request.user.id
            url.save()

            return redirect("index")
    else:
        form = UrlForm()

    return render(request, "create.html", {"form": form})
