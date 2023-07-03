from django.db import models

from users.models import CustomUser


class UserPets(models.Model):

    class Meta:
        db_table = 'userpets'
        verbose_name = 'Питомцы пользователя'
        verbose_name_plural = 'Питомцы пользователя'
        ordering = ['pk']

    PET_TYPE = (
        (1, 'Кошка'),
        (2, 'Собака'),
        (3, 'Попугай'),
        (4, 'Другое'),
    )
    pet_name = models.CharField(
        max_length=255, unique=True,
        verbose_name='Имя питомца'
    )
    pet_type = models.PositiveSmallIntegerField(
        choices=PET_TYPE, default=1, verbose_name='Тип питомца',
    )
    pet_owner = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT,
        related_name='pets',
    )
    pet_pic = models.ImageField(
        blank=True, null=True, 
        upload_to=(f'uploads/pets/'), 
        verbose_name='Изображение питомца',
    )
    def __str__(self):
        return f"Питомец: {self.pet_name}, {self.pet_owner}'а."
