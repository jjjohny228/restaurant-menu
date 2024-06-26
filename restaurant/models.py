from django.conf import settings
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='menus'
    )
    date = models.DateField()
    items = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Menu for {self.restaurant.name} with items: {self.items}'


class Vote(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='votes')
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee} voted for {self.menu}'
