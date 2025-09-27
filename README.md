# Leopard-Web-Store

## Project Overview
Leopard-Web-Store is a modern online clothing store inspired by street fashion with an emphasis on leopard prints and casual wear.  
The platform provides a seamless shopping experience, fast navigation, and personalization features, targeting both young people and adults.

## Target Audience
- Men and women aged 18–35 interested in trendy streetwear and casual clothing.
- Users with average incomes seeking affordable clothing with fast delivery in Ukraine.
- User roles:
  - **Guests**: Browse products.
  - **Registered users**: Shopping cart, favorites, order history.
  - **Administrators**: Product and order management.

## Product Catalog
Main categories:
- **Outerwear**: T-shirts (classic, oversized, leopard print), shirts, sweaters, hoodies, polo shirts.
- **Bottom wear**: Jeans, chinos, cargo pants, shorts, joggers, leggings.
- **Additional categories**: Dresses, skirts (for women); jackets (for men).  
  - Sizes: **S–XXL** (size chart included).
  - Price range: **500–2000 UAH**.
  - Products managed via admin panel (imported from CSV/JSON).

## Site Structure and UX/UI
- **Home Page**: Gender/unisex selection, promotional banners, product feed, search with autocomplete.
- **Catalog**: Filters (price, size, color, date), sorting, pagination (10–20 items per page).
- **Product Page**: Multiple photos, size selection, add-to-cart/favorites, discount display, reviews, detailed description.
- **Cart**: Product table, delivery address (Google Maps API), shipping options (Nova Poshta, Ukrposhta), promo code, payment (LiqPay/Fondy).
- **Other Pages**: Registration/login (email + Google OAuth), profile, admin panel (CRUD for products/orders), 404 page.
- **Design**: Minimalist with leopard accents, black/white palette, Roboto font, smooth CSS transitions.

## Core Functionality
- **Authentication**: JWT-based sessions.
- **Cart/Favorites**: LocalStorage + database synchronization.
- **Orders**: JSON/PDF generation, email notifications.
- **Security**: HTTPS, input validation.
- **Scalability**: Dockerized deployment, PostgreSQL database.

## Technology Stack
- **Backend**: Python, Django, Django REST Framework, SQLite.
- **Frontend**: HTML5, CSS3, Bootstrap 5, Vanilla JavaScript (ES6), React (optional).
- **Development Tools**: Git/GitHub, Docker, GitHub Actions (CI/CD).
- **Design**: Figma prototypes.

## Development Plan
**Timeline**: 3 months (12 weeks) until MVP launch. Agile methodology (2-week sprints, daily stand-ups).  

### Week 1: Preparation and Planning
- Set up GitHub repository and Trello board.
- Create wireframes in Figma.
- Initialize Django project (SQLite for testing).
- Build initial HTML/CSS structure with Bootstrap.

### Weeks 2–3: Backend Development
- Define Django models (Product, Category, Cart, CartItem).
- Configure Django Admin and add test products.
- Implement REST API with DRF (products, cart, auth).
- Basic authentication with Django auth.

### Weeks 3–4: Frontend Development
- Build UI components with Bootstrap.
- Implement product listing, filters, product page, and cart.
- Connect frontend to API using fetch.
- Store cart locally with LocalStorage.

### Weeks 5–6: Integration and Functionality
- Connect frontend with backend API.
- Synchronize cart and implement order placement.
- Add reviews and favorites functionality.

### Week 7: Testing and Corrections
- QA testing across browsers and devices.
- API testing with Postman.
- Optimize images and caching.

### Post-Release
- Collect user feedback.
- Upgrade authentication (JWT), improve frontend with React.

---

## License
This project is currently under development. Licensing will be added at a later stage.
