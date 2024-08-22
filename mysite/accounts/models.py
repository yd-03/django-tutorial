from django.db import models


class Book(models.Model):
    """
    書籍モデル
    """

    class Meta:
        # テーブル名を定義
        db_table = "book"

    # フィールドを定義
    title = models.CharField(
        verbose_name="タイトル", max_length=255, unique=True
    )  # verbose_nameはフィールドのラベル, max_lengthは最大文字数, uniqueは一意制約
    price = models.IntegerField(
        verbose_name="価格", null=True, blank=True
    )  # nullはデータベースにNULLを許可するかどうか, blankはフォームの入力欄に空欄を許可するかどうか

    def __str__(self):
        return self.title
