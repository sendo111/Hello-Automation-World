from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import TblBook


class CreateTestData:
    # テストデータの作成
    def data_create(self):
        TblBook.objects.create(
            title='はじめての自動化',
            author='ハロー、オートメーションワールド！',
            publisher='ハロー、オートメーションワールド！',
            finished_date='2020-01-01',
            created_at=timezone.now(),
            updated_at=timezone.now()
        )


class BookTopTest(TestCase):
    # top画面のアクセステスト
    def test_top(self):
        res = self.client.get(reverse('haw:top'))
        self.assertEqual(res.status_code, 200)
        self.assertQuerysetEqual(res.context['books'], [])


class BookCreateTest(TestCase):
    # データ登録テスト
    def test_create(self):
        create_data = {
            'title': 'はじめての自動化',
            'author': 'ハロー、オートメーションワールド！',
            'publisher': 'ハロー、オートメーションワールド！',
            'finished_date': '2020-02-01',
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        }
        res = self.client.post(
            reverse('haw:create'),
            data=create_data
        )
        self.assertEqual(res.status_code, 302)


class BookUpdateTest(TestCase):
    # データ更新テスト
    def test_update(self):
        # テストデータを作成
        create_test_data = CreateTestData()
        create_test_data.data_create()

        update_data = {
            'title': 'はじめての自動化 第二版',
            'author': 'Hello, Automation World!',
        }
        res = self.client.post(
            reverse('haw:update', kwargs={'book_id': 1}),
            data=update_data
        )
        self.assertEqual(res.status_code, 200)


class BookDeleteTest(TestCase):
    # データ削除テスト
    def test_delete(self):
        # テストデータを作成
        create_test_data = CreateTestData()
        create_test_data.data_create()

        res = self.client.post(
            reverse('haw:delete', kwargs={'book_id': 1})
        )
        self.assertEqual(res.status_code, 302)
