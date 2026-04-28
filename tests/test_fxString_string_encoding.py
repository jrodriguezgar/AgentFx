"""Tests for fxString.string_encoding."""


import pytest

from shortfx.fxString.string_operations import caesar_cipher


class TestCaesarCipher:

    def test_encrypt_basic(self):
        from shortfx.fxString.string_encoding import caesar_cipher

        assert caesar_cipher("Hello World", 3) == "Khoor Zruog"

    def test_decrypt_basic(self):
        from shortfx.fxString.string_encoding import caesar_cipher

        assert caesar_cipher("Khoor Zruog", 3, decrypt=True) == "Hello World"

    def test_shift_zero(self):
        from shortfx.fxString.string_encoding import caesar_cipher

        assert caesar_cipher("abc", 0) == "abc"

    def test_non_alpha_preserved(self):
        from shortfx.fxString.string_encoding import caesar_cipher

        assert caesar_cipher("123!@#", 5) == "123!@#"

    def test_type_error(self):
        from shortfx.fxString.string_encoding import caesar_cipher

        with pytest.raises(TypeError):
            caesar_cipher(123, 3)

class TestVigenereCipher:

    def test_encrypt(self):
        from shortfx.fxString.string_encoding import vigenere_cipher

        assert vigenere_cipher("Hello World", "KEY") == "Rijvs Uyvjn"

    def test_decrypt(self):
        from shortfx.fxString.string_encoding import vigenere_cipher

        assert vigenere_cipher("Rijvs Uyvjn", "KEY", decrypt=True) == "Hello World"

    def test_roundtrip(self):
        from shortfx.fxString.string_encoding import vigenere_cipher

        original = "Attack at dawn!"
        encrypted = vigenere_cipher(original, "SECRET")
        decrypted = vigenere_cipher(encrypted, "SECRET", decrypt=True)
        assert decrypted == original

    def test_invalid_key(self):
        from shortfx.fxString.string_encoding import vigenere_cipher

        with pytest.raises(ValueError):
            vigenere_cipher("text", "123")

class TestCaesarCipherV2:
    def test_basic(self):
        assert caesar_cipher("abc", 3) == "def"

    def test_wrap(self):
        assert caesar_cipher("xyz", 3) == "abc"

    def test_preserves_non_alpha(self):
        assert caesar_cipher("a-b", 1) == "b-c"

    def test_type_error(self):
        with pytest.raises(TypeError):
            caesar_cipher(123, 3)
