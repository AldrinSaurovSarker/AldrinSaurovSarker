from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    email = models.EmailField(max_length=254)
    tagline = models.CharField(max_length=50)
    about = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Profile"

    def __str__(self):
        return self.name


class Skills(models.Model):
    levelChoice = [
        ('Language', 'Language'),
        ('Framework', 'Framework'),
        ('Web Technology', 'Web Technology'),
        ('Database', 'Database'),
    ]

    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    level = models.CharField(max_length=50, choices=levelChoice)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


class Certificates(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    provider = models.CharField(max_length=50)
    issued = models.CharField(max_length=50)
    link = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"

    def __str__(self):
        return self.name


class Educations(models.Model):
    degree = models.CharField(max_length=50)
    subject = models.CharField(max_length=100, blank=True, default='')
    institution = models.CharField(max_length=150)
    duration = models.CharField(max_length=50)
    board = models.CharField(max_length=50, blank=True, default='')
    result = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"

    def __str__(self):
        return self.degree


class Experiences(models.Model):
    company_name = models.CharField(max_length=120)
    address = models.CharField(max_length=250)
    post = models.CharField(max_length=120)
    duration = models.CharField(max_length=120)
    desc = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return self.company_name


class Projects(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='vids', null=True, blank=True)
    href = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=100)
    ptype = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField()
    tools = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class Project_urls(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)
    background = models.CharField(max_length=100)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Project url"
        verbose_name_plural = "Project urls"

    def __str__(self):
        return f'{self.project} : {self.name}'


class Extras(models.Model):
    detail = models.TextField()

    class Meta:
        verbose_name = "Extra"
        verbose_name_plural = "Extras"
