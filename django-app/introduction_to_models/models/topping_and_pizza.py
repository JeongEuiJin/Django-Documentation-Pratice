from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        # topping_string = ''
        #
        # for topping in self.toppings.all():
        #     topping_string += topping.name
        #     topping_string += ', '
        # topping_string = topping_string[:-2]
        # return '{} ({})'.format(
        #     self.name,
        #     topping_string
        # )
        return '{} ({})'.format(self.name,', '.join([t.name for t in self.toppings()]))

        # 자신이 가지고있는 토핑목록을 뒤에 출력
        # ex) 치즈피자 (치즈, 토마스)
        # return self.name

    class Meta:
        ordering = ('name',)
