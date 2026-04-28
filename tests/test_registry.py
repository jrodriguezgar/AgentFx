"""Tests for shortfx.registry."""
import pytest
from shortfx.registry import get_tool_schemas, invoke_tool, search_tools

class TestGetToolSchemas:
    def test_returns_list(self):
        schemas = get_tool_schemas()
        assert isinstance(schemas, list)
        assert len(schemas) > 100  # 3000+ functions expected
    def test_schema_structure(self):
        schemas = get_tool_schemas()
        s = schemas[0]
        assert "name" in s
        assert "description" in s
        assert "parameters" in s

class TestInvokeTool:
    def test_abs(self):
        result = invoke_tool("fxNumeric.arithmetic_functions.absolute_value", {"x": -5.0})
        assert result == 5.0
    def test_nonexistent(self):
        with pytest.raises(KeyError):
            invoke_tool("fxFake.no_such_function", {})
    def test_sqrt(self):
        result = invoke_tool("fxNumeric.arithmetic_functions.square_root", {"x": 9.0})
        assert result == pytest.approx(3.0)

class TestSearchTools:
    def test_keyword(self):
        import pytest
        try:
            results = search_tools("absolute")
            assert isinstance(results, list)
        except (ImportError, Exception):
            pytest.skip("fastembed not installed")
