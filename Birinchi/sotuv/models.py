from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Notebook(models.Model):
    nom = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    narx = models.PositiveIntegerField()
    yangi = models.BooleanField()
    rasm = models.FileField()

    def __str__(self):
        return f" {self.nom} : modeli-{self.model},  narxi-{self.narx}"


# Universirer jadvali

TURLAR = [
    ("HP", "HP"),
    ("Acer", "Acer"),
    ("Asus", "Asus"),
    ("Lenovo", "Lenovo"),
]


class Universiter(models.Model):
    nomi = models.CharField(max_length=100, choices=TURLAR)
    sana = models.DateField(auto_now_add=True)
    talaba_soni = models.BigIntegerField()
    sayt = models.CharField(max_length=100)
    yillik = models.CharField(max_length=2, default=4)
    rasmi = models.FileField(unique=True, blank=True, null=True)

    def __str__(self):
        return f" {self.nomi} : talabalar soni-{self.talaba_soni},  rasmi -{self.rasmi}"


class Talaba(models.Model):
    ism = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    yosh = models.IntegerField()
    jinsi = models.CharField(max_length=6, choices=[("erkak", "erkak"), ("ayol", "ayol")])

    def __str__(self):
        return f" {self.ism}, jinsi {self.jinsi}, yoshi {self.yosh} "


class Foydalanuvchi(models.Model):
    username = models.CharField(max_length=30, unique=True)
    login = models.CharField(max_length=20)
    parol = models.IntegerField()
    email = models.CharField(max_length=50)
    talaba = models.BooleanField(default=True)
    resm = models.FileField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"username {self.username} parol {self.parol}, talaba {self.talaba}"


class Aktyor(models.Model):
    ism = models.CharField(max_length=30)
    tugilgan_yil = models.PositiveIntegerField()
    davlat = models.CharField(max_length=30)

    def __str__(self):
        return f"Aktyor {self.ism} {self.tugilgan_yil} yildada {self.davlat} tug'ilgan"


class Rejissor(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.IntegerField()
    kinolar_soni = models.IntegerField()

    def __str__(self):
        return f" rejissor {self.ism} kinolar soni {self.kinolar_soni}"


class Kino(models.Model):
    nom = models.CharField(max_length=30)
    yil = models.DateField()
    aktyorlar = models.ManyToManyField(Aktyor)
    rejissor = models.ForeignKey(Rejissor, on_delete=models.CASCADE)

    janr = models.CharField(max_length=20)

    def __str__(self):
        return f"kino- {self.nom} {self.rejissor} janri {self.janr}"


class Profil(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=20)
    yosh = models.CharField(max_length=20)
    jins = models.CharField(max_length=10, choices=[("erkak", "erkak"), ("ayol", "ayol")])

    def __str__(self):
        return f"{self.ism} yoshi {self.yosh}"


class Kurs(models.Model):
    nom = models.CharField(max_length=20)
    daraja = models.CharField(max_length=20,
                              choices=[("boshlangich", "boshlangich"), ("orta", "orta"), ("yuqori", "yuqori")])
    narx = models.IntegerField()
    chegirma = models.CharField(max_length=2, default=0)

    def __str__(self):
        return f"{self.nom} daraja {self.daraja} narx {self.narx} chegirma {self.chegirma}"


class Xarid(models.Model):
    profile = models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    sana = models.DateField()
    holat = models.CharField(max_length=20,
                             choices=[("tugadi", "tugadi"), ("davomiy", "davomiy"), ("boshlanmagan", "boshlanmagan")])

    def __str__(self):
        return f"{self.profile}  {self.kurs} narx {self.sana} holati {self.holat}"


class Izoh(models.Model):
    baho = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], default=3)
    matn = models.TextField()
    sana = models.DateField()
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.baho}  {self.profil}  {self.kurs} "


class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profil} {self.kurs}"


class Imtixon(models.Model):
    sana = models.DateField
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    universitet = models.ForeignKey(Universiter, on_delete=models.CASCADE)
    manzil = models.CharField(max_length=30)

    def __str__(self):
        return f"Imtixon sanasi: {self.sana}, Talaba: {self.talaba}, Universitet: {self.universitet}"


class Nazoratchi(models.Model):
    ism = models.CharField(max_length=30)
    kasb = models.CharField(max_length=30)
    imtihon = models.ForeignKey(Imtixon, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ismi: {self.ism}, Kasbi: {self.kasb}, Imtixon: {self.imtihon}"


class Natija(models.Model):
    imtixon = models.OneToOneField(Imtixon, on_delete=models.CASCADE)
    ball = models.BigIntegerField(validators=[MaxValueValidator(189), MinValueValidator(0)])
    natija = models.CharField(max_length=30, choices=[("budjet", "budjet"), ("kontrakt", "kontrakt"),
                                                      ("superkontrakt", "superkontrakt"), ("Yiqildi", "Yiqildi")])

    def __str__(self):
        return f"{self.imtixon},ball={self.ball}, {self.natija}"


class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    familiya = models.CharField(max_length=30)
    jinsi = models.CharField(max_length=10, choices=[("ayol", "ayol"), ("erkak", "erkak")])
    yosh = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(15)])

    def __str__(self):
        return f"O'qituvchi: {self.ism} {self.familiya} yoshi: {self.yosh}"


class Fan(models.Model):
    nomi = models.CharField(max_length=35)
    oqituvchi = models.ForeignKey(Ustoz, on_delete=models.CASCADE)
    credit = models.IntegerField()

    def __str__(self):
        return f"Nomi: {self.nomi} o'qituvchi: {self.oqituvchi} credit {self.credit}"
