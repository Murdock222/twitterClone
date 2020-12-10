from django.shortcuts import render, HttpResponseRedirect, reverse
from tweet.models import Tweet
from tweet.forms import NewTweetForm
from twitteruser.models import TwitterProfile
from  django.utils import timezone 



def newTweet(request):
    if request.method == "POST":
        form = NewTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.object.create(author=TwitterProfile.get(username="username"), text=data.get(text="text"), tweet_time=timezone.now())
            new_tweet.save()
            return HttpResponseRedirect(reverse("homepage"))
    
    form = NewTweetForm()
    return render(request, "generic_form.html", {"form": form})