from django.views import View
from django.template.response import TemplateResponse
from django.contrib.auth import login as auth_login
from django.http.response import HttpResponseRedirect
from django.urls import reverse


from .forms import LoginForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        """
        ログイン画面を表示する(GETリクエスト)

        args:
            request: リクエストオブジェクト
            args: パスパラメータ
            kwargs: クエリパラメータ

        return:
            ログイン画面のレスポンス
        """
        context = {
            "form": LoginForm(),
        }
        # ログイン画面用のテンプレートに空のフォームを渡す
        return TemplateResponse(request, "accounts/login.html", context)

    def post(self, request, *args, **kwargs):
        """
        ログイン処理を実行する(POSTリクエスト)

        args:
            request: リクエストオブジェクト
            args: パスパラメータ
            kwargs: クエリパラメータ

        return:
            ログイン成功時: ログイン画面のレスポンス
            ログイン失敗時: ログイン画面のレスポンス
        """
        # リクエストからフォームオブジェクトを作成
        form = LoginForm(request.POST)
        # バリデーションを実行
        if not form.is_valid():
            # バリデーションエラーがある場合は、ログイン画面を再表示
            context = {
                "form": form,
            }
            return TemplateResponse(request, "accounts/login.html", context)

        # バリデーションエラーがない場合
        # ユーザーオブジェクトをフォームから取得
        user = form.get_user()
        # ログイン処理を実行(セッションにユーザー情報を保存)
        auth_login(request, user)
        # 画面を用意するためのURLにリダイレクト
        return HttpResponseRedirect(reverse("accounts:login"))


login = LoginView.as_view()
