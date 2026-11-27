# Автотесты — ЛР 9 по тестированию ПО

![Run tests](../../actions/workflows/run-tests.yml/badge.svg)

Автотесты запускаются автоматически в GitHub Actions при каждом push в ветку `main`.

## Состав

- `calculator.py` — класс Calculator
- `tests/test_calculator.py` — модульные тесты калькулятора (ЛР 6)
- `tests/test_api.py` — тесты REST API JSONPlaceholder (ЛР 5)
- `.github/workflows/run-tests.yml` — настройка GitHub Actions

## Локальный запуск

```
pip install -r requirements.txt
pytest -v
```
