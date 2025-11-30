# Case: Django
Bu case de bir django uygulaması ayağa kaldırıp. Arka tarafta sayfaya her girildiğinde sayfaya girilme tıklanma miktarını arttıran bir uygulama yapılmalı ben her sayfaya girdiğimde sayfa bir arttırmalı.
no user authentication

# Django Counter App

## How to Run

1. Start the app:
   ```
   docker compose up -d --build
   ```

2. Open your browser and go to:
   ```
   http://localhost:8000
   ```

3. Each time you refresh the page, the number increases.

## How to Run Tests

Run tests with:
```
docker compose exec -it backend python manage.py test
```
