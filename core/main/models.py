from django.db import models

# Create your models here.

class BaseFooter(models.Model):
    img = models.ImageField('Base page Footer  image', upload_to='media')
    about = models.CharField('ABOUT Base Footer', max_length=50)
    ourLocation =  models.CharField('Our Location Base Footer', max_length=50)
    ourLocation1br =  models.CharField('Our Location Base Footer', max_length=50)
    ourLocation2br =  models.CharField('Our Location Base Footer', max_length=50)
    ourLocation3br =  models.CharField('Our Location Base Footer', max_length=50)
    customerCare = models.CharField('Customer Care Base Footer', max_length=50)
    customerCare1rb = models.CharField('Customer Care Base Footer', max_length=50)
    customerCare2br = models.CharField('Customer Care Base Footer', max_length=50)
    customerCare3br = models.CharField('Customer Care Base Footer', max_length=50)
    followUs = models.CharField('Follow Us Base Footer', max_length=50) 
    
    def __str__(self):
        return self.about
    
    class Meta:
        verbose_name = 'BaseFooter'
        verbose_name_plural = 'BaseFooters'





class HomePage(models.Model):
    nameH2 = models.CharField('About page 1', max_length=50)
    nameH1 = models.CharField('About page 2', max_length=50)
    img = models.ImageField('Home page image', upload_to='media')

    def __str__(self):
        return self.nameH1
    
    class Meta:
        verbose_name = 'HomePage'
        verbose_name_plural = 'HomePages'


class ExploreSomeOfOurLatest_Left(models.Model):
    nameH2 = models.CharField('EXPLORE SOME OF OUR LATEST', max_length=50)
    img = models.ImageField('EXPLORE image', upload_to='media')

    def __str__(self):
        return self.nameH2
    
    class Meta:
        verbose_name = 'ExploreSomeOfOurLatest_Left'
        verbose_name_plural = 'ExploreSomeOfOurLatests_Left'

class ExploreSomeOfOurLatest(models.Model):
    nameH4 = models.CharField('FOR WHOT', max_length=50)
    date = models.CharField('EXPLORE UPDATE DAY', max_length=50)
    seeMore =  models.CharField('EXPLORE SEE MORE', max_length=50)
    country =  models.CharField('COUNTRY', max_length=50)
    aboutThis =  models.CharField('ABOUT EXPLORE', max_length=50)

    def __str__(self):
        return self.nameH4
    
    class Meta:
        verbose_name = 'ExploreSomeOfOurLatest'
        verbose_name_plural = 'ExploreSomeOfOurLatests'



class CheckOut(models.Model):
    nameH2 = models.CharField('Check Out 1', max_length=50)
    nameH2br = models.CharField('Check Out 2', max_length=50)
    aboutThis =  models.CharField('ABOUT Check Out', max_length=50)
    aboutImg = models.CharField('ABOUT Check Out Image', max_length=50) 
    aboutImgSpan = models.CharField('ABOUT Check Out Image Span', max_length=50)
    img = models.ImageField('Check Out image', upload_to='media')


    def __str__(self):
        return self.nameH2
    
    class Meta:
        verbose_name = 'CheckOut'
        verbose_name_plural = 'CheckOuts'




# ----------- explore.html ---------------


class ExplorePage(models.Model):
    nameH2 = models.CharField('Explore page 1', max_length=50)
    nameH1 = models.CharField('Explore page 2', max_length=50)
    img = models.ImageField('Explore page image', upload_to='media')

    def __str__(self):
        return self.nameH1
    
    class Meta:
        verbose_name = 'ExplorePage'
        verbose_name_plural = 'ExplorePages'


# ------- about.html --------------
class AboutPage(models.Model):
    nameH2 = models.CharField('About page 1', max_length=50)
    nameH1 = models.CharField('About page 2', max_length=250)
    img = models.ImageField('About page image', upload_to='media')

    def __str__(self):
        return self.nameH1
    
    class Meta:
        verbose_name = 'AboutPage'
        verbose_name_plural = 'AboutPages'


class AboutUsPage(models.Model):
    nameH2 = models.CharField('About page 1', max_length=250)
    nameH1 = models.CharField('About page 2', max_length=250)
    img = models.ImageField('About page image', upload_to='media')
    # about1 = models.CharField('About page 2', max_length=550)
    # about2 = models.CharField('About page 2', max_length=550)


    def __str__(self):
        return self.nameH1
    
    class Meta:
        verbose_name = 'AboutUsPage'
        verbose_name_plural = 'AboutUsPages'

class AboutTeam(models.Model):
    name = models.CharField('Name', max_length=150)
    profession = models.CharField('Profession', max_length=250)
    about = models.CharField('About', max_length=250)
    img = models.ImageField('About Team image', upload_to='media')

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'AboutTeam'
        verbose_name_plural = 'AboutsTeam'



# --------- trending.html --------

class TrendingPage(models.Model):
    nameH2 = models.CharField('Trending name', max_length=250)
    nameH1 = models.CharField('About Trending', max_length=250)
    img = models.ImageField('Trending page image', upload_to='media')
   
    def __str__(self):
        return self.nameH2
    
    class Meta:
        verbose_name = 'TrendingPage'
        verbose_name_plural = 'TrendingPages'