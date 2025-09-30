# Data Model

## Сутності та атрибути

| Назва сутності | Атрибути                                                                 | Тип даних       |
|----------------|---------------------------------------------------------------------------|-----------------|
| **Product**    | id, name, price, image, gender, size, description, category_id           | int, string, decimal, string, enum, string, text, int (FK) |
| **Category**   | id, name, description                                                    | int, string, text |
| **Cart**       | id, user_id, created_at, updated_at                                      | int, int (FK), datetime, datetime |
| **CartItem**   | id, cart_id, product_id, quantity                                        | int, int (FK), int (FK), int |

---

## Пояснення

- **Product**: Товар, який користувач може придбати. Має посилання на категорію.  
- **Category**: Категорія для групування товарів (наприклад, "Футболки", "Штани").  
- **Cart**: Кошик користувача, пов'язаний із user_id. Містить час створення/оновлення.  
- **CartItem**: Конкретна позиція у кошику (товар + кількість).  
