from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BaseFooter, HomePage, ExploreSomeOfOurLatest_Left, ExploreSomeOfOurLatest, CheckOut, AboutPage, AboutUsPage, AboutTeam, ExplorePage, TrendingPage

# Create your views here.

# class BaseFooterListView(ListView):
#     template_name = 'base.html'

#     def get(self, request):
#         baseFooters = BaseFooter.objects.all()
#         return render(request, self.template_name, {
#             'baseFooters':baseFooters
#         })


class HomePageListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        baseFooters = BaseFooter.objects.all()

        homePages = HomePage.objects.all()
        exploreSomeOfOurLatest_Left = ExploreSomeOfOurLatest_Left.objects.all() 
        exploreSomeOfOurLatests = ExploreSomeOfOurLatest.objects.all()
        checkOut = CheckOut.objects.all()

        return render(request, self.template_name, {
            'baseFooters':baseFooters,
            'homePages':homePages,
            'exploreSomeOfOurLatest_Left':exploreSomeOfOurLatest_Left,
            'exploreSomeOfOurLatests':exploreSomeOfOurLatests,
            'checkOut':checkOut,
        })



# ----------- explore.html ---------------

class ExplorePageListView(ListView):
    template_name = 'explore.html'

    def get(self, request):
        explorePages = ExplorePage.objects.all()


        return render(request, self.template_name, {
            'explorePages':explorePages,
        })



# ------- about.html --------------

class AboutPageListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        aboutPages = AboutPage.objects.all()
        aboutUsPages = AboutUsPage.objects.all()
        aboutTeams = AboutTeam.objects.all()


        return render(request, self.template_name, {
            'aboutPages':aboutPages,
            'aboutUsPages':aboutUsPages,
            'aboutTeams':aboutTeams
        })


# --------- trending.html --------


class TrendingPageListView(ListView):
    template_name = 'trending.html'

    def get(self, request):
        trendingPages = TrendingPage.objects.all()

        return render(request, self.template_name, {
            'trendingPages':trendingPages,
        })


# ------ contact.html -------------

def contact(request):
    return render(request, 'contact.html')