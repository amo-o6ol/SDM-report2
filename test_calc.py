import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):

    # 同値分割法に基づく正常ケース
    def test_valid_input_1(self):
        # 範囲内の正の整数の掛け算
        self.assertEqual(21, calc(3, 7))  # A = 3, B = 7 (有効な範囲)

    def test_valid_input_2(self):
        # 範囲内の正の整数の掛け算
        self.assertEqual(998001, calc(999, 999))  # A = 999, B = 999 (有効な最大値)

    def test_valid_input_3(self):
        # 範囲内の正の小数（無効なケース）
        self.assertEqual(-1, calc(0.1, 999))  # 小数（無効）

    # 同値分割法に基づく無効ケース
    def test_invalid_input_1(self):
        # 範囲外の値をテスト（1未満）
        self.assertEqual(-1, calc(0, 7))  # A = 0（無効）

    def test_invalid_input_2(self):
        # 範囲外の値をテスト（999より大きい）
        self.assertEqual(-1, calc(1000, 7))  # A = 1000（無効）

    def test_invalid_input_3(self):
        # 文字列を渡した場合（無効）
        self.assertEqual(-1, calc("a", 7))  # A = "a"（無効）

    def test_invalid_input_4(self):
        # 空文字を渡した場合（無効）
        self.assertEqual(-1, calc("", 7))  # A = ""（無効）

    # 境界値分析法に基づくテストケース
    def test_boundary_lower(self):
        # 境界値（1）での動作確認
        self.assertEqual(1, calc(1, 1))  # A = 1, B = 1（最小値）

    def test_boundary_upper(self):
        # 境界値（999）での動作確認
        self.assertEqual(998001, calc(999, 999))  # A = 999, B = 999（最大値）

    def test_boundary_lower_invalid(self):
        # 境界値以下の入力（無効）
        self.assertEqual(-1, calc(0, 1))  # A = 0（無効）

    def test_boundary_upper_invalid(self):
        # 境界値より大きい入力（無効）
        self.assertEqual(-1, calc(1000, 999))  # A = 1000（無効）

    # 境界値分析法（小数）
    def test_boundary_float_invalid(self):
        # 小数を渡した場合（無効）
        self.assertEqual(-1, calc(0.1, 999))  # A = 0.1（無効）

    # 例外ケース（無効な入力）
    def test_invalid_empty(self):
        self.assertEqual(-1, calc('', ''))  # 空文字（無効）

if __name__ == '__main__':
    unittest.main()
