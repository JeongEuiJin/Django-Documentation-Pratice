from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    PERSON_TYPES = (
        ('studnet','학생'),
        ('teacher', '선생'),
    )
    person_type = models.CharField(
        '유형',
        max_length=10,
        choices=PERSON_TYPES,
        default=PERSON_TYPES[0][0]
    )
    teacher = models.ForeignKey(
        'self',
        null=True,
        on_delete=models.CASCADE,
        blank=True,
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(
        max_length=1,
        choices=SHIRT_SIZES,
        help_text='남자는 L을 쓰세요',
    )
    def __str__(self):
        return self.name
