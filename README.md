# Django Online Shop

Bu Django yaratilgan zamonaviy onlayn do'kon loyihasi.

## Loyihani ishga tushirish

1. Loyihani clone qiling:
```bash
git clone <repository-url>
cd django-shop-main
```

2. Virtual muhitni yarating va faollashtiring:
```bash
python -m venv venv
# Windows uchun
venv\Scripts\activate
# Linux/Mac uchun
source venv/bin/activate
```

3. Kerakli kutubxonalarni o'rnating:
```bash
pip install -r requirements.txt
```

4. Ma'lumotlar bazasini migrate qiling:
```bash
python manage.py migrate
```

5. Serverni ishga tushiring:
```bash
python manage.py runserver
```

## Loyiha tuzilishi

- `api/` - REST API endpointlari
- `config/` - Loyiha sozlamalari
- `main/` - Asosiy ilova
- `templates/` - HTML shablonlar
- `user/` - Foydalanuvchilar bilan ishlash moduli

## Texnologiyalar

- Django
- Django REST Framework
- SQLite
- HTML/CSS
- JavaScript

## Imkoniyatlar

- Foydalanuvchilar ro'yxatdan o'tishi va tizimga kirishi
- Mahsulotlarni ko'rish va qidirish
- Savat bilan ishlash
- Buyurtma berish
- Admin panel orqali boshqarish

## Hissa qo'shish

Loyihani yaxshilash bo'yicha takliflaringiz bo'lsa, "Pull Request" yuborishingiz mumkin.

## Litsenziya

  [MIT](https://choosealicense.com/licenses/mit/)
# virtual muhitni yarating va faollashtirish
python -m venv venv
# Windows uchun
venv\Scripts\activate
# Linux/Mac uchun
source venv/bin/activate
# Kerakli kutubxonalar:
pip install -r requirements.txt
# Ma'lumotlar bazasini migrate qilish:
python manage.py migrate
# Serverni ishga tushirish:
python manage.py runserver




#  Texnologiyalar
Django
Django REST Framework
SQLite
HTML/CSS
JavaScript

#  Loyiha tuzilishi
api/ - REST API endpointlari
config/ - Loyiha sozlamalari
main/ - Asosiy ilova
templates/ - HTML shablonlar
user/ - Foydalanuvchilar bilan ishlash moduli

#  Imkoniyatlar
Foydalanuvchilar ro'yxatdan o'tishi va tizimga kirishi
Mahsulotlarni ko'rish va qidirish
Savat bilan ishlash
Buyurtma berish
Admin panel orqali boshqarish