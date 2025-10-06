from django.db import models
from django.conf import settings
"""
70 и 117 рядок добавлены окончания (s) к названиям классов, чтобы избежать дублирования
"""

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

class Product(models.Model):
    #Модель для товарів
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	category = models.ForeignKey(
		Category, null=True, blank=True, on_delete=models.SET_NULL, related_name="products"
	)

	def __str__(self):
		return self.name
"""
Повертає значення поля name відповідної моделі

Для моделі Product - повертається назва товару (наприклад, "Пальто", "Футболка чорна", "Червоні черевичкі" тощо)
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
    #Модель для елементів кошика покупок
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=["cart", "product"], name="unique_cart_product")
		]

	def __str__(self):
		return f"{self.quantity} x {self.product.name}"


class Products(models.Model):
    # Вибір статі
    GENDER_CHOICES = [
        ('M', 'Чоловіча'),
        ('F', 'Жіноча'),
        ('U', 'Унісекс'),
    ]

    # Вибір розміру
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]

    # Поля товару
    name = models.CharField(max_length=255, verbose_name="Назва")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="Зображення")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Стать")
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, verbose_name="Розмір")
    description = models.TextField(blank=True, verbose_name="Опис")

    # Зовнішній ключ на категорію
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Категорія"
    )

    def __str__(self):
        return self.name

"""
Повертає значення поля name відповідної моделі.

Для моделі Product – повертається назва товару 
(наприклад, "Футболка чорна", "Пальто зимове", "Кросівки Nike" тощо).
"""


class CartItems(models.Model):
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


