from django.db import models
from django.conf import settings

class Category(models.Model):
    # Модель для категорій товарів
    name = models.CharField(max_length=255, unique=True, verbose_name="Категорія")

    class Meta:
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name
"""
Повертає значення поля name відповідної моделі

Для моделі Category - повертається назва категорії (наприклад, "Верхній одяг", "Аксесуари", "Взуття" тощо)
"""

class Gender(models.Model):
    """Фіксовані варіанти статі товару."""
    GENDER_CHOICES = [
        ('M', 'Чоловіча'),
        ('F', 'Жіноча'),
        ('U', 'Унісекс'),
    ]

    code = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        unique=True,
        verbose_name="Стать"
    )

    class Meta:
        verbose_name = "Стать"
        verbose_name_plural = "Статі"

    def __str__(self):
        return self.get_code_display()

    class Size(models.Model):
        """Фіксовані варіанти розміру товару."""
        SIZE_CHOICES = [
            ('XS', 'XS'),
            ('S', 'S'),
            ('M', 'M'),
            ('L', 'L'),
            ('XL', 'XL'),
            ('XXL', 'XXL'),
        ]

        code = models.CharField(
            max_length=3,
            choices=SIZE_CHOICES,
            unique=True,
            verbose_name="Розмір"
        )

        class Meta:
            verbose_name = "Розмір"
            verbose_name_plural = "Розміри"

        def __str__(self):
            return self.code

class Product(models.Model):
    """Основна модель товару."""
    name = models.CharField(max_length=255, verbose_name="Назва")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="Зображення")
    description = models.TextField(blank=True, verbose_name="Опис")

    gender = models.ForeignKey("Gender", on_delete=models.SET_NULL, null=True, verbose_name="Стать")
    size = models.ForeignKey("Size", on_delete=models.SET_NULL, null=True, verbose_name="Розмір")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Категорія"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    def __str__(self):
        return self.name

"""
Повертає значення поля name відповідної моделі.

Для моделі Product – повертається назва товару 
(наприклад, "Футболка чорна", "Пальто зимове", "Кросівки Nike" тощо).
"""

class Cart(models.Model):
    #Модель для кошика покупок
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="carts")
	items = models.ManyToManyField(Product, through="CartItem", related_name="carts")
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Cart(user={self.user})"
"""
Повертає рядкове представлення об'єкта кошика у форматі: Cart(user=ім'я_користувача)
   
Наприклад, якщо користувач має ім'я "john_doe", то метод поверне: Cart(user=john_doe)

"""

class CartItem(models.Model):
    # Модель для елементів кошика покупок
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cart", "product"], name="unique_cart_product")
        ]

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total_price(self):
        return self.product.price * self.quantity

"""
Метод __str__ повертає назву товару та кількість у вигляді рядка.

Для моделі CartItem – повертається, наприклад: 
"Футболка чорна × 2", "Пальто зимове × 1", "Кросівки Nike × 3" тощо.

Метод get_total_price повертає загальну ціну цього товару в кошику (ціна * кількість).
"""


