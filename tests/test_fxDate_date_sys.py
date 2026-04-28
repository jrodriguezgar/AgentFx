"""Tests for fxDate.date_sys."""


from shortfx.fxDate.date_sys import seconds_since_midnight


class TestSecondsSinceMidnight:

    def test_returns_nonnegative_float(self):
        result = seconds_since_midnight()
        assert isinstance(result, float)
        assert 0 <= result < 86400


# ── D. Month Offsets ─────────────────────────────────────────────────────────
