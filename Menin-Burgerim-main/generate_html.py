#!/usr/bin/env python3
menu = {
  "burgers": [
    ("Чыныгы бургер", "Фирменный бургер с говядиной", 220, "chynygy_burger.jpg", None),
    ("Биф бургер", "Сочная говяжья котлета, салат, соус", 190, "bif_burger.jpg", None),
    ("Чикен бургер", "Нежная куриная котлета, овощи", 190, "chiken_burger.jpg", None),
    ("Двойной бургер", "Двойная котлета, двойной сыр", 280, "dvoynoy_burger.jpg", "Premium"),
    ("Школьный бургер", "Бургер для школьников (09:00-14:00)", 150, "shkolnyy_burger.jpg", None),
  ],
  "shawarma": [
    ("Мини шаурма", "Компактная шаурма с курицей", 200, "mini_shaurma.jpg", None),
    ("Стандарт шаурма", "Классическая шаурма", 220, "standart_shaurma.jpg", None),
    ("Макси шаурма", "Большая порция, много начинки", 250, "maksi_shaurma.jpg", "Хит"),
    ("Макси шаурма сыр менен", "Макси шаурма с сыром", 270, "maksi_shaurma_syr.jpg", None),
  ],
  "rolls": [
    ("Филадельфия с люкс", "Лосось, сливочный сыр, нори", 330, "filadelfiya_lyuks.jpg", "Хит"),
    ("Калифорния с лососем", "Лосось, авокадо, икра", 300, "kaliforniya_losos.jpg", None),
    ("Филадельфия классическая", "Лосось, сливочный сыр", 320, "filadelfiya_klass.jpg", None),
    ("Ролл с креветкой", "Креветка, сливочный сыр", 290, "roll_krevetka.jpg", None),
    ("Филадельфия с Угрем", "Угорь, сливочный сыр", 360, "filadelfiya_ugor.jpg", "Premium"),
    ("Калифорния", "Краб, авокадо, икра тобико", 300, "kaliforniya.jpg", None),
    ("Опаленный", "Обжаренный лосось сверху", 330, "opalennyy.jpg", None),
    ("Легенда ролл", "Фирменный ролл", 320, "legenda_roll.jpg", None),
    ("Ролл с огурцом", "Свежий огурец, рис, нори", 120, "roll_ogurec.jpg", None),
    ("Ролл с Лососем", "Лосось, рис, нори", 130, "roll_losos.jpg", None),
  ],
  "hot_rolls": [
    ("Горячий Лосось", "Лосось в хрустящей темпуре", 330, "goryachiy_losos.jpg", None),
    ("Горячий Цезарь", "Цезарь в темпуре", 330, "goryachiy_tsezar.jpg", None),
    ("Горячий ролл с креветкой", "Креветка в темпуре", 310, "goryachiy_krevetka.jpg", None),
    ("Горячий Калифорния", "Калифорния в темпуре", 330, "goryachiy_kaliforniya.jpg", None),
    ("Темпура с лососем с угрем", "Лосось и угорь в темпуре", 300, "tempura_losos_ugor.jpg", None),
    ("Калифорния Запеченная", "Запеченная с соусом", 300, "kaliforniya_zap.jpg", None),
    ("Цезарь", "Запеченный Цезарь", 300, "tsezar.jpg", None),
    ("Запеченная ролл с лососем", "Запеченный лосось", 300, "zap_roll_losos.jpg", None),
    ("Гавайская Запеченная", "Запеченная с ананасом", 300, "gavayskaya_zap.jpg", None),
  ],
  "pizza": [
    ("Чыныгы Пицца", "Фирменная пицца", "290/420/600", "chynygy_pizza.jpg", "Хит"),
    ("Пеперони", "Колбаса пеперони, моцарелла", "260/360/550", "peperoni.jpg", None),
    ("Мехико", "Острая пицца с халапеньо", "290/420/600", "mehiko.jpg", None),
    ("Сочный Бургер", "Пицца со вкусом бургера", "290/420/600", "sochnyy_burger_pizza.jpg", None),
    ("Куриный", "Курица, грибы, сыр", "290/420/600", "kurinyy_pizza.jpg", None),
    ("Сырный", "4 вида сыра", "250/300/500", "syrnyy_pizza.jpg", None),
    ("Маргарита", "Томаты, моцарелла, базилик", "250/300/500", "margarita.jpg", None),
    ("Курица Грибы", "Курица, шампиньоны, сыр", "290/420/600", "kuritsa_griby.jpg", None),
  ],
  "snacks": [
    ("Крылышки (4 шт)", "Хрустящие куриные крылышки", 150, "krylyshki.jpg", None),
    ("Крылышки (8 шт)", "Хрустящие куриные крылышки", 290, "krylyshki.jpg", None),
    ("Крылышки (12 шт)", "Хрустящие куриные крылышки", 420, "krylyshki.jpg", "Выгодно"),
    ("Картошка фри", "Хрустящая золотистая картошка", 80, "kartoshka_fri.jpg", None),
    ("Куриные наггетс (1 шт)", "Нежный куриный наггетс", 20, "naggets.jpg", None),
    ("Куриные стрипс", "Хрустящие куриные полоски", 150, "strips.jpg", None),
  ],
  "combo": [
    ("Комбо Биф", "Биф бургер + фри + соус + 0.5 суу", 320, "kombo_bif.jpg", "Выгодно"),
    ("Комбо Чикен", "Чикен бургер + фри + соус + 0.5 суу", 320, "kombo_chiken.jpg", "Выгодно"),
    ("Комбо Шаурма", "Шаурма + фри + соус + 0.5 суу", 340, "kombo_shaurma.jpg", "Выгодно"),
    ("Комбо для детей", "Детское меню", 150, "kombo_deti.jpg", None),
  ],
}

cat_map = {"burgers":"burgers","shawarma":"shawarma","rolls":"rolls","hot_rolls":"hot_rolls","pizza":"pizza","snacks":"snacks","combo":"combo"}

cards = ""
for cat, items in menu.items():
    for name, desc, price, img, badge in items:
        badge_html = f'<span class="badge">{badge}</span>' if badge else ""
        is_combo = "combo" if cat == "combo" else ""
        if cat == "pizza":
            prices = str(price).split("/")
            size_html = '<div class="sizes"><span class="size-pill">25cm</span><span class="size-pill">30cm</span><span class="size-pill">40cm</span></div>'
            price_html = f'{prices[0]} <span class="unit">сом</span>'
        else:
            size_html = ""
            price_html = f'{price} <span class="unit">сом</span>'
        
        cards += f'''        <div class="menu-card {is_combo}" data-cat="{cat}">
          <div class="card-img-wrapper"><img src="menu/{img}" alt="{name}"></div>{badge_html}
          <h3>{name}</h3>
          <p class="desc">{desc}</p>
          {size_html}
          <div class="bottom"><span class="price">{price_html}</span><button class="btn-cart">+</button></div>
        </div>
'''

phone = "996775252527"

html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Менин Бургерим — бургеры, шаурма, пицца, роллы. Доставка по Баткену.">
  <title>Менин Бургерим — Бургеры, Шаурма, Пицца</title>
  <link rel="stylesheet" href="style.css">
  <link rel="icon" href="menu/logo.jpg" type="image/jpeg">
</head>
<body>
  <header class="header" id="header">
    <div class="container">
      <a href="#" class="logo">
        <img src="menu/logo.jpg" alt="Менин Бургерим" class="logo-img">
        Менин<span>Бургерим</span>
      </a>
      <nav class="nav-links" id="navLinks">
        <a href="#home">Главная</a>
        <a href="#menu">Меню</a>
        <a href="#contacts">Контакты</a>
        <a href="https://wa.me/{phone}" class="btn btn-primary" style="padding:9px 20px;font-size:.9rem" target="_blank">Заказать</a>
      </nav>
      <div class="burger-menu" id="burgerMenu"><span></span><span></span><span></span></div>
    </div>
  </header>

  <section class="hero" id="home">
    <div class="container">
      <div class="hero-content">
        <div class="hero-badge">Доставка по Баткену</div>
        <h1>Вкусные бургеры<br><span class="hl">и не только!</span></h1>
        <p>Сочные бургеры, ароматная шаурма, хрустящая пицца и свежие роллы. Заказывайте прямо сейчас!</p>
        <div class="hero-buttons">
          <a href="#menu" class="btn btn-primary">Смотреть меню</a>
          <a href="https://wa.me/{phone}" class="btn btn-outline" target="_blank">WhatsApp &rarr;</a>
        </div>
      </div>
      <div class="hero-visual">
        <div class="hero-img-wrapper">
          <img src="menu/glavnoe_foto.png" alt="Бургер" class="hero-img">
        </div>
      </div>
    </div>
  </section>

  <section class="menu-section" id="menu">
    <div class="container">
      <h2 class="section-title reveal">Наше меню</h2>
      <p class="section-sub reveal">Выбери категорию и найди своё любимое блюдо</p>
      <div class="tabs reveal" id="tabs">
        <button class="tab active" data-cat="all">Всё</button>
        <button class="tab" data-cat="burgers">Бургеры</button>
        <button class="tab" data-cat="shawarma">Шаурма</button>
        <button class="tab" data-cat="rolls">Роллы</button>
        <button class="tab" data-cat="hot_rolls">Горячие</button>
        <button class="tab" data-cat="pizza">Пицца</button>
        <button class="tab" data-cat="snacks">Снеки</button>
        <button class="tab" data-cat="combo">Комбо</button>
      </div>
      <div class="menu-grid" id="menuGrid">
{cards}
      </div>
    </div>
  </section>

  <section class="contacts" id="contacts">
    <div class="container">
      <h2 class="section-title reveal">Контакты</h2>
      <p class="section-sub reveal">Звоните или пишите — мы на связи!</p>
      <div class="contact-row reveal">
        <a href="https://wa.me/{phone}" class="contact-item" target="_blank"><span class="icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg></span> WhatsApp</a>
        <a href="tel:+{phone}" class="contact-item"><span class="icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg></span> 0775 25 25 27</a>
        <a href="https://instagram.com/memin_burgerim" class="contact-item" target="_blank"><span class="icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></span> @memin_burgerim</a>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-inner">
        <span class="footer-copy">&copy; 2025 Менин Бургерим. Все права защищены.</span>
        <div class="footer-socials">
          <a href="https://instagram.com/memin_burgerim" target="_blank"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
          <a href="https://wa.me/{phone}" target="_blank"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg></a>
          <a href="tel:+{phone}"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg></a>
        </div>
      </div>
    </div>
  </footer>

  <!-- CART UI -->
  <div class="cart-overlay" id="cartOverlay"></div>
  <div class="cart-sidebar" id="cartSidebar">
    <div class="cart-header">
      <h2>Корзина</h2>
      <button class="cart-close" id="cartClose">&#10005;</button>
    </div>
    <div class="cart-items" id="cartItems">
      <div class="cart-empty" style="display:flex;align-items:center;justify-content:center;gap:8px;">Корзина пуста <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg></div>
    </div>
    <div class="cart-footer">
      <div class="cart-total"><span>Итого:</span><span id="cartTotalPrice">0</span></div>
      <div class="cart-input-group">
        <label for="cartAddress" class="cart-input-label">Адрес доставки</label>
        <input type="text" id="cartAddress" placeholder="Улица, дом, квартира..." class="cart-input">
      </div>
      <div class="cart-actions">
        <button class="btn-clear" id="btnClearCart" title="Очистить корзину"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg></button>
        <button class="btn btn-primary btn-order btn-order-full" id="btnOrderWhatsapp">Оформить заказ</button>
      </div>
    </div>
  </div>

  <button class="cart-floating-btn" id="cartFloatingBtn">
    <span class="cart-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg></span>
    <span class="cart-badge" id="cartBadge">0</span>
  </button>

  <script src="script.js"></script>
</body>
</html>'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("index.html created!")
