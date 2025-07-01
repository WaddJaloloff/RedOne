from django.db import models
from googletrans import Translator
import re


translator = Translator()

# 🔁 Tarjimada istisno qilinadigan so'zlar
EXCLUDED_PHRASES = ['Red One', 'Redist']

def translate_preserve_exceptions(text, src='ru', dest='uz'):
    try:
        placeholders = {}

        # Qavs ichidagilarni saqlab qolish
        paren_pattern = r'\([^()]*\)'
        paren_matches = re.findall(paren_pattern, text)
        for i, match in enumerate(paren_matches):
            key = f"__PAREN_{i}__"
            placeholders[key] = match
            text = text.replace(match, key)

        # Maxsus frazalarni saqlab qolish
        for i, phrase in enumerate(EXCLUDED_PHRASES):
            pattern = re.compile(re.escape(phrase), re.IGNORECASE)
            matches = pattern.findall(text)
            for j, match in enumerate(matches):
                key = f"__PHRASE_{i}_{j}__"
                placeholders[key] = match
                text = text.replace(match, key)

        # 🚫 1. \n belgilari o‘rniga oddiy bo‘sh joy

        text = text.replace('\n', ' ')

        # 🚫 2. Ortiqcha bo‘sh joylarni tozalash
        text = re.sub(r'\s+', ' ', text).strip()

        # ✅ Tarjima
        translated_text = translator.translate(text, src=src, dest=dest).text

        # ✅ Saqlangan joylarni tiklash
        for key, value in placeholders.items():
            translated_text = translated_text.replace(key, value)

        return translated_text

    except Exception as e:
        print(f"Tarjima qilishda xatolik: {e}")
        return text



class Categories(models.Model):
    category_uz = models.CharField(max_length=30)
    category_ru = models.CharField(max_length=30)

    def __str__(self):
        return self.category_uz


class Product(models.Model):
    name_ru = models.CharField(max_length=200)
    name_uz = models.CharField(max_length=200, blank=True)
    size1 = models.CharField(max_length=10)
    price1 = models.IntegerField()
    size2 = models.CharField(max_length=10, null=True, blank=True)
    price2 = models.IntegerField(null=True, blank=True)
    about_ru = models.TextField(null=True, blank=True)
    about_uz = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_uz or self.name_ru

    def save(self, *args, **kwargs):
        if not self.about_uz and self.about_ru:
            self.about_uz = translate_preserve_exceptions(self.about_ru)

        if not self.name_ru and self.name_uz:
            self.name_ru = self.name_uz

        super().save(*args, **kwargs)

    @property
    def formatted_price1(self):
        return f"{self.price1:,}".replace(",", " ")

    @property
    def formatted_price2(self):
        if self.price2:
            return f"{self.price2:,}".replace(",", " ")
        return ""


class TopProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Qaysi tartibda chiqishini belgilang")

    def __str__(self):
        return f"Top: {self.product.name_uz}"
