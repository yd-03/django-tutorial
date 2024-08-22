# django-tutorial

## プロジェクト構成

```
mysite 　　　  ← ベースディレクトリ
├── config    ← 設定ディレクトリ
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

- ベースディレクトリ名を任意の名前にする（今回は`mysite`とする）
- 設定ディレクトリ名を `config` とする

```bash
mkdir mysite
cd mysite/
django-admin startproject config .
```
