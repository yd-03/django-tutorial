from django.db import models


# class Book(models.Model):
#     """
#     書籍モデル
#     """

#     class Meta:
#         # テーブル名を定義
#         db_table = "book"

#     # フィールドを定義
#     title = models.CharField(
#         verbose_name="タイトル", max_length=255, unique=True
#     )  # verbose_nameはフィールドのラベル, max_lengthは最大文字数, uniqueは一意制約
#     price = models.IntegerField(
#         verbose_name="価格", null=True, blank=True
#     )  # nullはデータベースにNULLを許可するかどうか, blankはフォームの入力欄に空欄を許可するかどうか

#     def __str__(self):
#         return self.title


# 一対一のリレーションの実装例
# class Book(models.Model):
#     """
#     書籍モデル
#     """

#     class Meta:
#         # テーブル名を定義
#         db_table = "book"

#     # フィールドを定義
#     title = models.CharField(
#         verbose_name="タイトル", max_length=255
#     )  # verbose_nameはフィールドのラベル, max_lengthは最大文字数


# class BookStock(models.Model):
#     """
#     書籍在庫モデル
#     """

#     class Meta:
#         # テーブル名を定義
#         db_table = "book_stock"

#     # フィールドを定義
#     book = models.OneToOneField(
#         Book, verbose_name="本", on_delete=models.CASCADE
#     )  # on_deleteは親モデルが削除されたときの挙動
#     quantity = models.IntegerField(
#         verbose_name="在庫数", default=0
#     )  # verbose_nameはフィールドのラベル, defaultはデフォルト値


# 多対一のリレーションの実装例
# class Publisher(models.Model):
#     """
#     出版社モデル
#     """

#     class Meta:
#         # テーブル名を定義
#         db_table = "publisher"

#     # フィールドを定義
#     name = models.CharField(
#         verbose_name="出版社名", max_length=255
#     )  # verbose_nameはフィールドのラベル, max_lengthは最大文字数


# class Book(models.Model):
#     """
#     書籍モデル
#     """

#     class Meta:
#         # テーブル名を定義
#         db_table = "book"

#     # フィールドを定義
#     title = models.CharField(
#         verbose_name="タイトル", max_length=255
#     )  # verbose_nameはフィールドのラベル, max_lengthは最大文字数
#     publisher = models.ForeignKey(
#         Publisher, verbose_name="出版社", on_delete=models.PROTECT
#     )  # on_deleteは親モデルが削除されたときの挙動（PROTECTは削除を制限する）


# 多対多のリレーションの実装例
class Author(models.Model):
    """
    著者モデル
    """

    class Meta:
        # テーブル名を定義
        db_table = "author"

    # フィールドを定義
    name = models.CharField(
        verbose_name="著者名", max_length=255
    )  # verbose_nameはフィールドのラベル, max_lengthは最大文字数


class Book(models.Models):
    """
    書籍モデル
    """

    class Meta:
        # テーブル名を定義
        db_table = "book"

    # フィールドを定義
    title = models.CharField(
        verbose_name="タイトル", max_length=255
    )  # verbose_nameはフィールドのラベル, max_lengthは最大文字数
    authors = models.ManyToManyField(Author, verbose_name="著者")
