from django.test import TestCase
from blog.models import animal


class AnimalTests(TestCase):

    def test_creacion_de_animal(self):

        animal_nombre_valido = animal.objects.create(
            nombre="nombre corto", tipo_de_animal ="tipo animal", edad="años"
        )
        self.assertEqual(animal.objects.all().count(), 1)
        self.assertIsNotNone(animal_nombre_valido.id)

