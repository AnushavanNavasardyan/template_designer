from django.contrib import admin
from .models import BaseFooter, HomePage, ExploreSomeOfOurLatest_Left, ExploreSomeOfOurLatest, CheckOut, AboutPage, AboutUsPage, AboutTeam,  ExplorePage, TrendingPage

# Register your models here.
# ----- BASE FOOTER
admin.site.register(BaseFooter)

# ----- INDEX.HTML
admin.site.register(HomePage)
admin.site.register(ExploreSomeOfOurLatest_Left)
admin.site.register(ExploreSomeOfOurLatest)
admin.site.register(CheckOut)

# ------- about.html --------------
admin.site.register(AboutPage)
admin.site.register(AboutUsPage)
admin.site.register(AboutTeam)


# ----------- explore.html ---------------
admin.site.register(ExplorePage)


# --------- trending.html --------
admin.site.register(TrendingPage)


