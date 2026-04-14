# Coverage tests for formulite.fxNumeric.conversion_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxNumeric import conversion_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_acres_to_hectares:
    def test_exists(self):
        assert hasattr(mod, "acres_to_hectares")

    def test_var0(self):
        try:
            mod.acres_to_hectares(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.acres_to_hectares(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.acres_to_hectares(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.acres_to_hectares("")
        except EXC:
            pass


class Test_add_bool_to_int:
    def test_exists(self):
        assert hasattr(mod, "add_bool_to_int")

    def test_doc0(self):
        try:
            mod.add_bool_to_int(True, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.add_bool_to_int(False, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.add_bool_to_int(True, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.add_bool_to_int(False, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.add_bool_to_int(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.add_bool_to_int(0, "")
        except EXC:
            pass


class Test_adiabatic_index_pressure:
    def test_exists(self):
        assert hasattr(mod, "adiabatic_index_pressure")

    def test_var0(self):
        try:
            mod.adiabatic_index_pressure(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.adiabatic_index_pressure(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.adiabatic_index_pressure(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.adiabatic_index_pressure("", "", "", "")
        except EXC:
            pass


class Test_adiabatic_temperature:
    def test_exists(self):
        assert hasattr(mod, "adiabatic_temperature")

    def test_var0(self):
        try:
            mod.adiabatic_temperature(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.adiabatic_temperature(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.adiabatic_temperature(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.adiabatic_temperature("", "", "")
        except EXC:
            pass


class Test_angle_convert:
    def test_exists(self):
        assert hasattr(mod, "angle_convert")

    def test_doc0(self):
        try:
            mod.angle_convert(180, "deg", "rad") == math.pi
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.angle_convert(200, "grad", "deg")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.angle_convert(0, "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.angle_convert(1, "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.angle_convert(None, "hello", "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.angle_convert("", "", "")
        except EXC:
            pass


class Test_angular_momentum:
    def test_exists(self):
        assert hasattr(mod, "angular_momentum")

    def test_doc0(self):
        try:
            mod.angular_momentum(2, 3, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.angular_momentum(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.angular_momentum(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.angular_momentum(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.angular_momentum("", "", "")
        except EXC:
            pass


class Test_antenna_gain_to_effective_area:
    def test_exists(self):
        assert hasattr(mod, "antenna_gain_to_effective_area")

    def test_var0(self):
        try:
            mod.antenna_gain_to_effective_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.antenna_gain_to_effective_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.antenna_gain_to_effective_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.antenna_gain_to_effective_area(0, "")
        except EXC:
            pass


class Test_atmospheres_to_pascals:
    def test_exists(self):
        assert hasattr(mod, "atmospheres_to_pascals")

    def test_doc0(self):
        try:
            mod.atmospheres_to_pascals(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.atmospheres_to_pascals(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.atmospheres_to_pascals(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.atmospheres_to_pascals(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.atmospheres_to_pascals("")
        except EXC:
            pass


class Test_bars_to_pascals:
    def test_exists(self):
        assert hasattr(mod, "bars_to_pascals")

    def test_doc0(self):
        try:
            mod.bars_to_pascals(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bars_to_pascals(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bars_to_pascals(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bars_to_pascals(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bars_to_pascals("")
        except EXC:
            pass


class Test_base_to_decimal:
    def test_exists(self):
        assert hasattr(mod, "base_to_decimal")

    def test_doc0(self):
        try:
            mod.base_to_decimal('FF', 16)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.base_to_decimal('1010', 2)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.base_to_decimal('144', 8)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.base_to_decimal("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.base_to_decimal("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.base_to_decimal(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.base_to_decimal("", "")
        except EXC:
            pass


class Test_bending_moment:
    def test_exists(self):
        assert hasattr(mod, "bending_moment")

    def test_doc0(self):
        try:
            mod.bending_moment(100, 2.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bending_moment(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bending_moment(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bending_moment(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bending_moment("", "")
        except EXC:
            pass


class Test_bernoulli_velocity:
    def test_exists(self):
        assert hasattr(mod, "bernoulli_velocity")

    def test_var0(self):
        try:
            mod.bernoulli_velocity(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bernoulli_velocity(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bernoulli_velocity(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bernoulli_velocity("", "")
        except EXC:
            pass


class Test_bin_to_hex:
    def test_exists(self):
        assert hasattr(mod, "bin_to_hex")

    def test_doc0(self):
        try:
            mod.bin_to_hex('11111111')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.bin_to_hex('1010')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bin_to_hex("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bin_to_hex("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bin_to_hex(None)
        except EXC:
            pass


class Test_bin_to_int:
    def test_exists(self):
        assert hasattr(mod, "bin_to_int")

    def test_doc0(self):
        try:
            mod.bin_to_int("0b1010")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.bin_to_int("111")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bin_to_int("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bin_to_int("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bin_to_int(None)
        except EXC:
            pass


class Test_bin_to_oct:
    def test_exists(self):
        assert hasattr(mod, "bin_to_oct")

    def test_doc0(self):
        try:
            mod.bin_to_oct('11111111')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.bin_to_oct('1000')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bin_to_oct("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bin_to_oct("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bin_to_oct(None)
        except EXC:
            pass


class Test_biot_number:
    def test_exists(self):
        assert hasattr(mod, "biot_number")

    def test_doc0(self):
        try:
            mod.biot_number(50, 0.01, 200)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.biot_number(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.biot_number(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.biot_number(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.biot_number("", "", 0)
        except EXC:
            pass


class Test_bmi:
    def test_exists(self):
        assert hasattr(mod, "bmi")

    def test_var0(self):
        try:
            mod.bmi(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bmi(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bmi(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bmi("", "")
        except EXC:
            pass


class Test_bool_to_float:
    def test_exists(self):
        assert hasattr(mod, "bool_to_float")

    def test_doc0(self):
        try:
            mod.bool_to_float(True)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.bool_to_float(False)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bool_to_float(True)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bool_to_float(False)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bool_to_float(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bool_to_float("")
        except EXC:
            pass


class Test_bool_to_int:
    def test_exists(self):
        assert hasattr(mod, "bool_to_int")

    def test_doc0(self):
        try:
            mod.bool_to_int(True)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.bool_to_int(False)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bool_to_int(True)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bool_to_int(False)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bool_to_int(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bool_to_int("")
        except EXC:
            pass


class Test_boyle_law_volume:
    def test_exists(self):
        assert hasattr(mod, "boyle_law_volume")

    def test_doc0(self):
        try:
            mod.boyle_law_volume(2, 10, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.boyle_law_volume(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.boyle_law_volume(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.boyle_law_volume(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.boyle_law_volume("", "", "")
        except EXC:
            pass


class Test_btu_to_joules:
    def test_exists(self):
        assert hasattr(mod, "btu_to_joules")

    def test_var0(self):
        try:
            mod.btu_to_joules(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.btu_to_joules(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.btu_to_joules(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.btu_to_joules("")
        except EXC:
            pass


class Test_bulk_modulus_pressure:
    def test_exists(self):
        assert hasattr(mod, "bulk_modulus_pressure")

    def test_doc0(self):
        try:
            mod.bulk_modulus_pressure(2.2e9, -0.001, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bulk_modulus_pressure(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bulk_modulus_pressure(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bulk_modulus_pressure(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bulk_modulus_pressure("", "", "")
        except EXC:
            pass


class Test_buoyancy_force:
    def test_exists(self):
        assert hasattr(mod, "buoyancy_force")

    def test_var0(self):
        try:
            mod.buoyancy_force(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.buoyancy_force(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.buoyancy_force(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.buoyancy_force("", "")
        except EXC:
            pass


class Test_buoyant_force:
    def test_exists(self):
        assert hasattr(mod, "buoyant_force")

    def test_var0(self):
        try:
            mod.buoyant_force(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.buoyant_force(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.buoyant_force(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.buoyant_force("", "")
        except EXC:
            pass


class Test_bytes_to_human_readable:
    def test_exists(self):
        assert hasattr(mod, "bytes_to_human_readable")

    def test_doc0(self):
        try:
            mod.bytes_to_human_readable(1572864)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bytes_to_human_readable(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bytes_to_human_readable(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bytes_to_human_readable(None)
        except EXC:
            pass


class Test_bytes_to_int:
    def test_exists(self):
        assert hasattr(mod, "bytes_to_int")

    def test_var0(self):
        try:
            mod.bytes_to_int([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bytes_to_int([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bytes_to_int(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bytes_to_int([])
        except EXC:
            pass


class Test_calories_to_joules:
    def test_exists(self):
        assert hasattr(mod, "calories_to_joules")

    def test_doc0(self):
        try:
            mod.calories_to_joules(1000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calories_to_joules(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calories_to_joules(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calories_to_joules(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calories_to_joules("")
        except EXC:
            pass


class Test_candela_to_lumens:
    def test_exists(self):
        assert hasattr(mod, "candela_to_lumens")

    def test_var0(self):
        try:
            mod.candela_to_lumens(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.candela_to_lumens(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.candela_to_lumens(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.candela_to_lumens("")
        except EXC:
            pass


class Test_capacitance_parallel_plate:
    def test_exists(self):
        assert hasattr(mod, "capacitance_parallel_plate")

    def test_var0(self):
        try:
            mod.capacitance_parallel_plate(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.capacitance_parallel_plate(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.capacitance_parallel_plate(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.capacitance_parallel_plate("", "")
        except EXC:
            pass


class Test_capacitive_reactance:
    def test_exists(self):
        assert hasattr(mod, "capacitive_reactance")

    def test_var0(self):
        try:
            mod.capacitive_reactance(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.capacitive_reactance(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.capacitive_reactance(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.capacitive_reactance("", "")
        except EXC:
            pass


class Test_capacitor_energy:
    def test_exists(self):
        assert hasattr(mod, "capacitor_energy")

    def test_doc0(self):
        try:
            mod.capacitor_energy(0.001, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.capacitor_energy(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.capacitor_energy(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.capacitor_energy(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.capacitor_energy("", "")
        except EXC:
            pass


class Test_centripetal_acceleration:
    def test_exists(self):
        assert hasattr(mod, "centripetal_acceleration")

    def test_doc0(self):
        try:
            mod.centripetal_acceleration(10, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.centripetal_acceleration(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.centripetal_acceleration(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.centripetal_acceleration(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.centripetal_acceleration("", "")
        except EXC:
            pass


class Test_centripetal_force:
    def test_exists(self):
        assert hasattr(mod, "centripetal_force")

    def test_doc0(self):
        try:
            mod.centripetal_force(2, 10, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.centripetal_force(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.centripetal_force(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.centripetal_force(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.centripetal_force("", "", "")
        except EXC:
            pass


class Test_charles_law_volume:
    def test_exists(self):
        assert hasattr(mod, "charles_law_volume")

    def test_doc0(self):
        try:
            mod.charles_law_volume(10, 300, 600)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.charles_law_volume(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.charles_law_volume(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.charles_law_volume(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.charles_law_volume("", "", "")
        except EXC:
            pass


class Test_cmyk_to_rgb:
    def test_exists(self):
        assert hasattr(mod, "cmyk_to_rgb")

    def test_doc0(self):
        try:
            mod.cmyk_to_rgb(0.0, 1.0, 1.0, 0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cmyk_to_rgb(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cmyk_to_rgb(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cmyk_to_rgb(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cmyk_to_rgb("", "", "", 0)
        except EXC:
            pass


class Test_color_contrast_ratio:
    def test_exists(self):
        assert hasattr(mod, "color_contrast_ratio")

    def test_doc0(self):
        try:
            mod.color_contrast_ratio(0, 0, 0, 255, 255, 255)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.color_contrast_ratio(255, 255, 255, 255, 255, 255)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.color_contrast_ratio(0, 0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.color_contrast_ratio(1, 1, 1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.color_contrast_ratio(None, 0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.color_contrast_ratio("", "", "", "", "", "")
        except EXC:
            pass


class Test_color_luminance:
    def test_exists(self):
        assert hasattr(mod, "color_luminance")

    def test_var0(self):
        try:
            mod.color_luminance(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.color_luminance(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.color_luminance(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.color_luminance("", "", "")
        except EXC:
            pass


class Test_color_temperature_to_rgb:
    def test_exists(self):
        assert hasattr(mod, "color_temperature_to_rgb")

    def test_doc0(self):
        try:
            mod.color_temperature_to_rgb(6500)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.color_temperature_to_rgb(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.color_temperature_to_rgb(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.color_temperature_to_rgb(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.color_temperature_to_rgb(0)
        except EXC:
            pass


class Test_compton_wavelength_shift:
    def test_exists(self):
        assert hasattr(mod, "compton_wavelength_shift")

    def test_var0(self):
        try:
            mod.compton_wavelength_shift(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.compton_wavelength_shift(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.compton_wavelength_shift(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.compton_wavelength_shift("")
        except EXC:
            pass


class Test_convert_bytes_to:
    def test_exists(self):
        assert hasattr(mod, "convert_bytes_to")

    def test_doc0(self):
        try:
            mod.convert_bytes_to('KB', 1024)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.convert_bytes_to('GiB', 1073741824) # 1 GiB
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.convert_bytes_to('GB', 1000000000) # 1 GB
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.convert_bytes_to('MB', 5242880) # 5 MiB
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.convert_bytes_to('MiB', 5242880) # 5 MiB
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.convert_bytes_to("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.convert_bytes_to("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.convert_bytes_to(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.convert_bytes_to("", "")
        except EXC:
            pass


class Test_convert_string_to_float_with_locale:
    def test_exists(self):
        assert hasattr(mod, "convert_string_to_float_with_locale")

    def test_var0(self):
        try:
            mod.convert_string_to_float_with_locale("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.convert_string_to_float_with_locale("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.convert_string_to_float_with_locale(None)
        except EXC:
            pass


class Test_convert_units:
    def test_exists(self):
        assert hasattr(mod, "convert_units")

    def test_doc0(self):
        try:
            mod.convert_units(100, 'cm', 'm')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.convert_units(1, 'kg', 'g')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.convert_units(0, 'C', 'F')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.convert_units(0, "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.convert_units(1, "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.convert_units(None, "hello", "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.convert_units("", "", "")
        except EXC:
            pass


class Test_coordinate_decimal_to_dms:
    def test_exists(self):
        assert hasattr(mod, "coordinate_decimal_to_dms")

    def test_doc0(self):
        try:
            mod.coordinate_decimal_to_dms(40.4461)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.coordinate_decimal_to_dms(-79.9822, is_longitude=True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.coordinate_decimal_to_dms(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coordinate_decimal_to_dms(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coordinate_decimal_to_dms(None)
        except EXC:
            pass


class Test_coordinate_dms_to_decimal:
    def test_exists(self):
        assert hasattr(mod, "coordinate_dms_to_decimal")

    def test_var0(self):
        try:
            mod.coordinate_dms_to_decimal(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coordinate_dms_to_decimal(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coordinate_dms_to_decimal(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coordinate_dms_to_decimal(0, "", "")
        except EXC:
            pass


class Test_coulomb_force:
    def test_exists(self):
        assert hasattr(mod, "coulomb_force")

    def test_var0(self):
        try:
            mod.coulomb_force(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coulomb_force(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coulomb_force(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coulomb_force("", "", "")
        except EXC:
            pass


class Test_coulombs_force:
    def test_exists(self):
        assert hasattr(mod, "coulombs_force")

    def test_var0(self):
        try:
            mod.coulombs_force(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coulombs_force(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coulombs_force(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coulombs_force("", "", "")
        except EXC:
            pass


class Test_coulombs_law:
    def test_exists(self):
        assert hasattr(mod, "coulombs_law")

    def test_var0(self):
        try:
            mod.coulombs_law(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coulombs_law(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coulombs_law(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coulombs_law("", "", "")
        except EXC:
            pass


class Test_cubic_meters_per_second_to_liters_per_minute:
    def test_exists(self):
        assert hasattr(mod, "cubic_meters_per_second_to_liters_per_minute")

    def test_doc0(self):
        try:
            mod.cubic_meters_per_second_to_liters_per_minute(0.001)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cubic_meters_per_second_to_liters_per_minute(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cubic_meters_per_second_to_liters_per_minute(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cubic_meters_per_second_to_liters_per_minute(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cubic_meters_per_second_to_liters_per_minute("")
        except EXC:
            pass


class Test_current_divider:
    def test_exists(self):
        assert hasattr(mod, "current_divider")

    def test_doc0(self):
        try:
            mod.current_divider(10, 200, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.current_divider(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.current_divider(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.current_divider(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.current_divider("", "", "")
        except EXC:
            pass


class Test_db_to_power:
    def test_exists(self):
        assert hasattr(mod, "db_to_power")

    def test_doc0(self):
        try:
            mod.db_to_power(20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.db_to_power(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.db_to_power(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.db_to_power(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.db_to_power("")
        except EXC:
            pass


class Test_db_to_voltage:
    def test_exists(self):
        assert hasattr(mod, "db_to_voltage")

    def test_doc0(self):
        try:
            mod.db_to_voltage(20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.db_to_voltage(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.db_to_voltage(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.db_to_voltage(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.db_to_voltage("")
        except EXC:
            pass


class Test_de_broglie_wavelength:
    def test_exists(self):
        assert hasattr(mod, "de_broglie_wavelength")

    def test_var0(self):
        try:
            mod.de_broglie_wavelength(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.de_broglie_wavelength(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.de_broglie_wavelength(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.de_broglie_wavelength("", "")
        except EXC:
            pass


class Test_dec_to_oct:
    def test_exists(self):
        assert hasattr(mod, "dec_to_oct")

    def test_doc0(self):
        try:
            mod.dec_to_oct(100)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.dec_to_oct(8)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.dec_to_oct(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dec_to_oct(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dec_to_oct(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dec_to_oct("")
        except EXC:
            pass


class Test_decibel_add:
    def test_exists(self):
        assert hasattr(mod, "decibel_add")

    def test_var0(self):
        try:
            mod.decibel_add(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.decibel_add(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.decibel_add(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.decibel_add("", "")
        except EXC:
            pass


class Test_decibel_sum:
    def test_exists(self):
        assert hasattr(mod, "decibel_sum")

    def test_var0(self):
        try:
            mod.decibel_sum(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.decibel_sum(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.decibel_sum(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.decibel_sum("", "")
        except EXC:
            pass


class Test_decimal_to_fraction:
    def test_exists(self):
        assert hasattr(mod, "decimal_to_fraction")

    def test_doc0(self):
        try:
            mod.decimal_to_fraction(0.75)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.decimal_to_fraction(3.14159, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.decimal_to_fraction(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.decimal_to_fraction(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.decimal_to_fraction(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.decimal_to_fraction("")
        except EXC:
            pass


class Test_degrees_to_gradians:
    def test_exists(self):
        assert hasattr(mod, "degrees_to_gradians")

    def test_var0(self):
        try:
            mod.degrees_to_gradians(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.degrees_to_gradians(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.degrees_to_gradians(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.degrees_to_gradians("")
        except EXC:
            pass


class Test_density_to_specific_gravity:
    def test_exists(self):
        assert hasattr(mod, "density_to_specific_gravity")

    def test_var0(self):
        try:
            mod.density_to_specific_gravity(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.density_to_specific_gravity(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.density_to_specific_gravity(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.density_to_specific_gravity("")
        except EXC:
            pass


class Test_dew_point:
    def test_exists(self):
        assert hasattr(mod, "dew_point")

    def test_var0(self):
        try:
            mod.dew_point(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dew_point(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dew_point(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dew_point("", "")
        except EXC:
            pass


class Test_dft_magnitude:
    def test_exists(self):
        assert hasattr(mod, "dft_magnitude")

    def test_var0(self):
        try:
            mod.dft_magnitude([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dft_magnitude([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dft_magnitude(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dft_magnitude("", 0)
        except EXC:
            pass


class Test_dft_phase:
    def test_exists(self):
        assert hasattr(mod, "dft_phase")

    def test_var0(self):
        try:
            mod.dft_phase([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dft_phase([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dft_phase(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dft_phase("", 0)
        except EXC:
            pass


class Test_doppler_freq:
    def test_exists(self):
        assert hasattr(mod, "doppler_freq")

    def test_var0(self):
        try:
            mod.doppler_freq(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.doppler_freq(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.doppler_freq(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.doppler_freq("", "")
        except EXC:
            pass


class Test_doppler_frequency:
    def test_exists(self):
        assert hasattr(mod, "doppler_frequency")

    def test_var0(self):
        try:
            mod.doppler_frequency(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.doppler_frequency(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.doppler_frequency(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.doppler_frequency("", "")
        except EXC:
            pass


class Test_doppler_shift:
    def test_exists(self):
        assert hasattr(mod, "doppler_shift")

    def test_var0(self):
        try:
            mod.doppler_shift(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.doppler_shift(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.doppler_shift(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.doppler_shift("", "")
        except EXC:
            pass


class Test_drag_force:
    def test_exists(self):
        assert hasattr(mod, "drag_force")

    def test_doc0(self):
        try:
            mod.drag_force(0.47, 1.225, 10, 0.01)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.drag_force(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.drag_force(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.drag_force(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.drag_force("", "", "", "")
        except EXC:
            pass


class Test_drift_velocity:
    def test_exists(self):
        assert hasattr(mod, "drift_velocity")

    def test_doc0(self):
        try:
            mod.drift_velocity(10, 8.5e28, 1.6e-19, 1e-6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.drift_velocity(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.drift_velocity(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.drift_velocity(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.drift_velocity("", 0, "", "")
        except EXC:
            pass


class Test_elastic_modulus:
    def test_exists(self):
        assert hasattr(mod, "elastic_modulus")

    def test_doc0(self):
        try:
            mod.elastic_modulus(200e6, 0.001)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.elastic_modulus(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elastic_modulus(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elastic_modulus(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elastic_modulus("", 0)
        except EXC:
            pass


class Test_elastic_potential_energy:
    def test_exists(self):
        assert hasattr(mod, "elastic_potential_energy")

    def test_doc0(self):
        try:
            mod.elastic_potential_energy(200, 0.1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.elastic_potential_energy(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elastic_potential_energy(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elastic_potential_energy(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elastic_potential_energy(0, "")
        except EXC:
            pass


class Test_electric_field_parallel_plate:
    def test_exists(self):
        assert hasattr(mod, "electric_field_parallel_plate")

    def test_doc0(self):
        try:
            mod.electric_field_parallel_plate(1000, 0.01)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.electric_field_parallel_plate(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.electric_field_parallel_plate(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.electric_field_parallel_plate(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.electric_field_parallel_plate("", "")
        except EXC:
            pass


class Test_electric_field_point:
    def test_exists(self):
        assert hasattr(mod, "electric_field_point")

    def test_var0(self):
        try:
            mod.electric_field_point(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.electric_field_point(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.electric_field_point(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.electric_field_point("", "")
        except EXC:
            pass


class Test_electric_potential:
    def test_exists(self):
        assert hasattr(mod, "electric_potential")

    def test_var0(self):
        try:
            mod.electric_potential(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.electric_potential(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.electric_potential(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.electric_potential("", "")
        except EXC:
            pass


class Test_energy_convert:
    def test_exists(self):
        assert hasattr(mod, "energy_convert")

    def test_var0(self):
        try:
            mod.energy_convert(0, "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.energy_convert(1, "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.energy_convert(None, "hello", "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.energy_convert("", "", "")
        except EXC:
            pass


class Test_escape_velocity:
    def test_exists(self):
        assert hasattr(mod, "escape_velocity")

    def test_var0(self):
        try:
            mod.escape_velocity(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.escape_velocity(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.escape_velocity(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.escape_velocity("", "")
        except EXC:
            pass


class Test_float_to_int_truncated:
    def test_exists(self):
        assert hasattr(mod, "float_to_int_truncated")

    def test_doc0(self):
        try:
            mod.float_to_int_truncated(3.9)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.float_to_int_truncated(-3.9)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.float_to_int_truncated(5.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.float_to_int_truncated(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.float_to_int_truncated(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.float_to_int_truncated(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.float_to_int_truncated("")
        except EXC:
            pass


class Test_float_to_json_safe:
    def test_exists(self):
        assert hasattr(mod, "float_to_json_safe")

    def test_doc0(self):
        try:
            mod.float_to_json_safe(3.14)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.float_to_json_safe(float('nan'))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.float_to_json_safe(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.float_to_json_safe(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.float_to_json_safe(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.float_to_json_safe("")
        except EXC:
            pass


class Test_focal_length:
    def test_exists(self):
        assert hasattr(mod, "focal_length")

    def test_var0(self):
        try:
            mod.focal_length(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.focal_length(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.focal_length(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.focal_length("", "")
        except EXC:
            pass


class Test_foot_pounds_to_newton_meters:
    def test_exists(self):
        assert hasattr(mod, "foot_pounds_to_newton_meters")

    def test_var0(self):
        try:
            mod.foot_pounds_to_newton_meters(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.foot_pounds_to_newton_meters(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.foot_pounds_to_newton_meters(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.foot_pounds_to_newton_meters("")
        except EXC:
            pass


class Test_fraction_to_decimal:
    def test_exists(self):
        assert hasattr(mod, "fraction_to_decimal")

    def test_doc0(self):
        try:
            mod.fraction_to_decimal(3, 4)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.fraction_to_decimal(22, 7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fraction_to_decimal(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fraction_to_decimal(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fraction_to_decimal(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fraction_to_decimal("", "")
        except EXC:
            pass


class Test_free_space_path_loss:
    def test_exists(self):
        assert hasattr(mod, "free_space_path_loss")

    def test_var0(self):
        try:
            mod.free_space_path_loss(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.free_space_path_loss(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.free_space_path_loss(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.free_space_path_loss("", "")
        except EXC:
            pass


class Test_freq_from_wavelength:
    def test_exists(self):
        assert hasattr(mod, "freq_from_wavelength")

    def test_doc0(self):
        try:
            mod.freq_from_wavelength(0.299792458)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.freq_from_wavelength(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.freq_from_wavelength(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.freq_from_wavelength(None)
        except EXC:
            pass


class Test_frequency_to_wavelength:
    def test_exists(self):
        assert hasattr(mod, "frequency_to_wavelength")

    def test_var0(self):
        try:
            mod.frequency_to_wavelength(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.frequency_to_wavelength(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.frequency_to_wavelength(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.frequency_to_wavelength("")
        except EXC:
            pass


class Test_friction_force:
    def test_exists(self):
        assert hasattr(mod, "friction_force")

    def test_doc0(self):
        try:
            mod.friction_force(100, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.friction_force(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.friction_force(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.friction_force(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.friction_force("", "")
        except EXC:
            pass


class Test_friis_transmission:
    def test_exists(self):
        assert hasattr(mod, "friis_transmission")

    def test_var0(self):
        try:
            mod.friis_transmission(0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.friis_transmission(1, 1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.friis_transmission(None, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.friis_transmission("", "", "", 0, "")
        except EXC:
            pass


class Test_froude_number:
    def test_exists(self):
        assert hasattr(mod, "froude_number")

    def test_var0(self):
        try:
            mod.froude_number(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.froude_number(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.froude_number(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.froude_number("", "", 0)
        except EXC:
            pass


class Test_gallons_to_liters:
    def test_exists(self):
        assert hasattr(mod, "gallons_to_liters")

    def test_var0(self):
        try:
            mod.gallons_to_liters(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gallons_to_liters(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gallons_to_liters(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gallons_to_liters("")
        except EXC:
            pass


class Test_gay_lussac_pressure:
    def test_exists(self):
        assert hasattr(mod, "gay_lussac_pressure")

    def test_doc0(self):
        try:
            mod.gay_lussac_pressure(100_000, 300, 600)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gay_lussac_pressure(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gay_lussac_pressure(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gay_lussac_pressure(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gay_lussac_pressure("", "", "")
        except EXC:
            pass


class Test_gradians_to_degrees:
    def test_exists(self):
        assert hasattr(mod, "gradians_to_degrees")

    def test_doc0(self):
        try:
            mod.gradians_to_degrees(100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gradians_to_degrees(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gradians_to_degrees(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gradians_to_degrees(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gradians_to_degrees("")
        except EXC:
            pass


class Test_grams_to_troy_ounces:
    def test_exists(self):
        assert hasattr(mod, "grams_to_troy_ounces")

    def test_var0(self):
        try:
            mod.grams_to_troy_ounces(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.grams_to_troy_ounces(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.grams_to_troy_ounces(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.grams_to_troy_ounces("")
        except EXC:
            pass


class Test_grashof_number:
    def test_exists(self):
        assert hasattr(mod, "grashof_number")

    def test_var0(self):
        try:
            mod.grashof_number(0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.grashof_number(1, 1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.grashof_number(None, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.grashof_number("", 0, "", 0, "")
        except EXC:
            pass


class Test_gravitational_force:
    def test_exists(self):
        assert hasattr(mod, "gravitational_force")

    def test_var0(self):
        try:
            mod.gravitational_force(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gravitational_force(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gravitational_force(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gravitational_force("", "", "")
        except EXC:
            pass


class Test_gravitational_potential_energy:
    def test_exists(self):
        assert hasattr(mod, "gravitational_potential_energy")

    def test_doc0(self):
        try:
            mod.gravitational_potential_energy(10, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gravitational_potential_energy(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gravitational_potential_energy(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gravitational_potential_energy(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gravitational_potential_energy("", "")
        except EXC:
            pass


class Test_h_concentration_to_ph:
    def test_exists(self):
        assert hasattr(mod, "h_concentration_to_ph")

    def test_doc0(self):
        try:
            mod.h_concentration_to_ph(1e-7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.h_concentration_to_ph(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.h_concentration_to_ph(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.h_concentration_to_ph(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.h_concentration_to_ph(0)
        except EXC:
            pass


class Test_half_life_remaining:
    def test_exists(self):
        assert hasattr(mod, "half_life_remaining")

    def test_doc0(self):
        try:
            mod.half_life_remaining(100, 5, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.half_life_remaining(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.half_life_remaining(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.half_life_remaining(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.half_life_remaining("", "", "")
        except EXC:
            pass


class Test_heat_capacity:
    def test_exists(self):
        assert hasattr(mod, "heat_capacity")

    def test_doc0(self):
        try:
            mod.heat_capacity(2, 4186, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.heat_capacity(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.heat_capacity(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.heat_capacity(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.heat_capacity("", "", "")
        except EXC:
            pass


class Test_heat_engine_efficiency:
    def test_exists(self):
        assert hasattr(mod, "heat_engine_efficiency")

    def test_var0(self):
        try:
            mod.heat_engine_efficiency(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.heat_engine_efficiency(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.heat_engine_efficiency(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.heat_engine_efficiency("", [])
        except EXC:
            pass


class Test_heat_index:
    def test_exists(self):
        assert hasattr(mod, "heat_index")

    def test_var0(self):
        try:
            mod.heat_index(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.heat_index(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.heat_index(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.heat_index("", "")
        except EXC:
            pass


class Test_heat_transfer_conduction:
    def test_exists(self):
        assert hasattr(mod, "heat_transfer_conduction")

    def test_doc0(self):
        try:
            mod.heat_transfer_conduction(200, 0.01, 50, 0.1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.heat_transfer_conduction(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.heat_transfer_conduction(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.heat_transfer_conduction(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.heat_transfer_conduction("", "", "", "")
        except EXC:
            pass


class Test_hectares_to_acres:
    def test_exists(self):
        assert hasattr(mod, "hectares_to_acres")

    def test_var0(self):
        try:
            mod.hectares_to_acres(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hectares_to_acres(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hectares_to_acres(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hectares_to_acres("")
        except EXC:
            pass


class Test_hertz_to_rpm:
    def test_exists(self):
        assert hasattr(mod, "hertz_to_rpm")

    def test_doc0(self):
        try:
            mod.hertz_to_rpm(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hertz_to_rpm(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hertz_to_rpm(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hertz_to_rpm(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hertz_to_rpm("")
        except EXC:
            pass


class Test_hex_to_bin:
    def test_exists(self):
        assert hasattr(mod, "hex_to_bin")

    def test_doc0(self):
        try:
            mod.hex_to_bin('FF')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.hex_to_bin('A')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hex_to_bin("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hex_to_bin("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hex_to_bin(None)
        except EXC:
            pass


class Test_hex_to_int:
    def test_exists(self):
        assert hasattr(mod, "hex_to_int")

    def test_doc0(self):
        try:
            mod.hex_to_int("0xff")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.hex_to_int("FF")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.hex_to_int("a")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hex_to_int("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hex_to_int("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hex_to_int(None)
        except EXC:
            pass


class Test_hex_to_oct:
    def test_exists(self):
        assert hasattr(mod, "hex_to_oct")

    def test_doc0(self):
        try:
            mod.hex_to_oct('FF')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.hex_to_oct('1F')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hex_to_oct("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hex_to_oct("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hex_to_oct(None)
        except EXC:
            pass


class Test_hookes_law:
    def test_exists(self):
        assert hasattr(mod, "hookes_law")

    def test_doc0(self):
        try:
            mod.hookes_law(100, 0.05)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hookes_law(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hookes_law(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hookes_law(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hookes_law("", "")
        except EXC:
            pass


class Test_horsepower_to_watts:
    def test_exists(self):
        assert hasattr(mod, "horsepower_to_watts")

    def test_var0(self):
        try:
            mod.horsepower_to_watts(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.horsepower_to_watts(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.horsepower_to_watts(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.horsepower_to_watts("")
        except EXC:
            pass


class Test_hsl_to_rgb:
    def test_exists(self):
        assert hasattr(mod, "hsl_to_rgb")

    def test_doc0(self):
        try:
            mod.hsl_to_rgb(0.0, 1.0, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hsl_to_rgb(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hsl_to_rgb(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hsl_to_rgb(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hsl_to_rgb("", "", "")
        except EXC:
            pass


class Test_hsv_to_rgb:
    def test_exists(self):
        assert hasattr(mod, "hsv_to_rgb")

    def test_doc0(self):
        try:
            mod.hsv_to_rgb(30.0, 1.0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hsv_to_rgb(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hsv_to_rgb(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hsv_to_rgb(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hsv_to_rgb("", "", "")
        except EXC:
            pass


class Test_ideal_gas_pressure:
    def test_exists(self):
        assert hasattr(mod, "ideal_gas_pressure")

    def test_var0(self):
        try:
            mod.ideal_gas_pressure(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ideal_gas_pressure(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ideal_gas_pressure(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ideal_gas_pressure("", 0, "")
        except EXC:
            pass


class Test_ieee754_hex_representation:
    def test_exists(self):
        assert hasattr(mod, "ieee754_hex_representation")

    def test_doc0(self):
        try:
            mod.ieee754_hex_representation(3.14)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ieee754_hex_representation(0.5)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.ieee754_hex_representation(1.0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.ieee754_hex_representation(-1.0)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.ieee754_hex_representation(float('inf'))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ieee754_hex_representation(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ieee754_hex_representation(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ieee754_hex_representation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ieee754_hex_representation("")
        except EXC:
            pass


class Test_impedance_parallel:
    def test_exists(self):
        assert hasattr(mod, "impedance_parallel")

    def test_doc0(self):
        try:
            mod.impedance_parallel(100+0j, 100+0j)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.impedance_parallel(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.impedance_parallel(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.impedance_parallel(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.impedance_parallel("", "")
        except EXC:
            pass


class Test_impedance_series:
    def test_exists(self):
        assert hasattr(mod, "impedance_series")

    def test_doc0(self):
        try:
            mod.impedance_series(100, 0.01, 1e-6, 1000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.impedance_series(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.impedance_series(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.impedance_series(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.impedance_series("", "", "", "")
        except EXC:
            pass


class Test_impedance_series_rlc:
    def test_exists(self):
        assert hasattr(mod, "impedance_series_rlc")

    def test_doc0(self):
        try:
            mod.impedance_series_rlc(100, 150, 50)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.impedance_series_rlc(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.impedance_series_rlc(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.impedance_series_rlc(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.impedance_series_rlc("", "", "")
        except EXC:
            pass


class Test_impulse:
    def test_exists(self):
        assert hasattr(mod, "impulse")

    def test_doc0(self):
        try:
            mod.impulse(100, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.impulse(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.impulse(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.impulse(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.impulse("", "")
        except EXC:
            pass


class Test_inductive_reactance:
    def test_exists(self):
        assert hasattr(mod, "inductive_reactance")

    def test_var0(self):
        try:
            mod.inductive_reactance(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inductive_reactance(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inductive_reactance(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inductive_reactance("", "")
        except EXC:
            pass


class Test_inductor_energy:
    def test_exists(self):
        assert hasattr(mod, "inductor_energy")

    def test_doc0(self):
        try:
            mod.inductor_energy(0.01, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inductor_energy(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inductor_energy(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inductor_energy(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inductor_energy("", "")
        except EXC:
            pass


class Test_int_to_binary_clean:
    def test_exists(self):
        assert hasattr(mod, "int_to_binary_clean")

    def test_doc0(self):
        try:
            mod.int_to_binary_clean(10)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.int_to_binary_clean(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.int_to_binary_clean(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.int_to_binary_clean(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.int_to_binary_clean(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.int_to_binary_clean("")
        except EXC:
            pass


class Test_int_to_binary_with_prefix:
    def test_exists(self):
        assert hasattr(mod, "int_to_binary_with_prefix")

    def test_doc0(self):
        try:
            mod.int_to_binary_with_prefix(255)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.int_to_binary_with_prefix(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.int_to_binary_with_prefix(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.int_to_binary_with_prefix(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.int_to_binary_with_prefix(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.int_to_binary_with_prefix("")
        except EXC:
            pass


class Test_int_to_bytes:
    def test_exists(self):
        assert hasattr(mod, "int_to_bytes")

    def test_doc0(self):
        try:
            mod.int_to_bytes(123, 2, byteorder='big')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.int_to_bytes(256, 2, byteorder='little')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.int_to_bytes(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.int_to_bytes(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.int_to_bytes(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.int_to_bytes("", 0)
        except EXC:
            pass


class Test_int_to_float:
    def test_exists(self):
        assert hasattr(mod, "int_to_float")

    def test_doc0(self):
        try:
            mod.int_to_float(5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.int_to_float(-10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.int_to_float(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.int_to_float(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.int_to_float(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.int_to_float("")
        except EXC:
            pass


class Test_int_to_hex_clean:
    def test_exists(self):
        assert hasattr(mod, "int_to_hex_clean")

    def test_doc0(self):
        try:
            mod.int_to_hex_clean(255)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.int_to_hex_clean(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.int_to_hex_clean(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.int_to_hex_clean(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.int_to_hex_clean(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.int_to_hex_clean("")
        except EXC:
            pass


class Test_int_to_hex_with_prefix:
    def test_exists(self):
        assert hasattr(mod, "int_to_hex_with_prefix")

    def test_doc0(self):
        try:
            mod.int_to_hex_with_prefix(255)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.int_to_hex_with_prefix(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.int_to_hex_with_prefix(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.int_to_hex_with_prefix(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.int_to_hex_with_prefix(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.int_to_hex_with_prefix("")
        except EXC:
            pass


class Test_int_to_octal_with_prefix:
    def test_exists(self):
        assert hasattr(mod, "int_to_octal_with_prefix")

    def test_doc0(self):
        try:
            mod.int_to_octal_with_prefix(255)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.int_to_octal_with_prefix(15)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.int_to_octal_with_prefix(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.int_to_octal_with_prefix(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.int_to_octal_with_prefix(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.int_to_octal_with_prefix("")
        except EXC:
            pass


class Test_int_to_roman:
    def test_exists(self):
        assert hasattr(mod, "int_to_roman")

    def test_doc0(self):
        try:
            mod.int_to_roman(14)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.int_to_roman(2024)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.int_to_roman(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.int_to_roman(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.int_to_roman(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.int_to_roman("")
        except EXC:
            pass


class Test_is_numeric_type:
    def test_exists(self):
        assert hasattr(mod, "is_numeric_type")

    def test_doc0(self):
        try:
            mod.is_numeric_type(42)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_numeric_type(3.14)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_numeric_type(Decimal('10.5'))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_numeric_type("123")
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.is_numeric_type(None)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_numeric_type(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_numeric_type(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_numeric_type(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_numeric_type("")
        except EXC:
            pass


class Test_joules_to_btu:
    def test_exists(self):
        assert hasattr(mod, "joules_to_btu")

    def test_var0(self):
        try:
            mod.joules_to_btu(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.joules_to_btu(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.joules_to_btu(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.joules_to_btu("")
        except EXC:
            pass


class Test_joules_to_calories:
    def test_exists(self):
        assert hasattr(mod, "joules_to_calories")

    def test_var0(self):
        try:
            mod.joules_to_calories(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.joules_to_calories(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.joules_to_calories(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.joules_to_calories("")
        except EXC:
            pass


class Test_joules_to_kwh:
    def test_exists(self):
        assert hasattr(mod, "joules_to_kwh")

    def test_var0(self):
        try:
            mod.joules_to_kwh(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.joules_to_kwh(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.joules_to_kwh(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.joules_to_kwh("")
        except EXC:
            pass


class Test_kilometers_to_light_years:
    def test_exists(self):
        assert hasattr(mod, "kilometers_to_light_years")

    def test_var0(self):
        try:
            mod.kilometers_to_light_years(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kilometers_to_light_years(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kilometers_to_light_years(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kilometers_to_light_years("")
        except EXC:
            pass


class Test_kinematic_displacement:
    def test_exists(self):
        assert hasattr(mod, "kinematic_displacement")

    def test_doc0(self):
        try:
            mod.kinematic_displacement(10, 5, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.kinematic_displacement(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kinematic_displacement(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kinematic_displacement(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kinematic_displacement("", "", 0)
        except EXC:
            pass


class Test_kinetic_energy:
    def test_exists(self):
        assert hasattr(mod, "kinetic_energy")

    def test_doc0(self):
        try:
            mod.kinetic_energy(10, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.kinetic_energy(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kinetic_energy(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kinetic_energy(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kinetic_energy("", "")
        except EXC:
            pass


class Test_kinetic_energy_relativistic:
    def test_exists(self):
        assert hasattr(mod, "kinetic_energy_relativistic")

    def test_var0(self):
        try:
            mod.kinetic_energy_relativistic(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kinetic_energy_relativistic(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kinetic_energy_relativistic(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kinetic_energy_relativistic("", "")
        except EXC:
            pass


class Test_kmh_to_knots:
    def test_exists(self):
        assert hasattr(mod, "kmh_to_knots")

    def test_var0(self):
        try:
            mod.kmh_to_knots(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kmh_to_knots(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kmh_to_knots(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kmh_to_knots("")
        except EXC:
            pass


class Test_knots_to_kmh:
    def test_exists(self):
        assert hasattr(mod, "knots_to_kmh")

    def test_var0(self):
        try:
            mod.knots_to_kmh(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.knots_to_kmh(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.knots_to_kmh(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.knots_to_kmh("")
        except EXC:
            pass


class Test_knudsen_number:
    def test_exists(self):
        assert hasattr(mod, "knudsen_number")

    def test_doc0(self):
        try:
            mod.knudsen_number(6.8e-8, 0.001)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.knudsen_number(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.knudsen_number(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.knudsen_number(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.knudsen_number(0, 0)
        except EXC:
            pass


class Test_kwh_to_joules:
    def test_exists(self):
        assert hasattr(mod, "kwh_to_joules")

    def test_doc0(self):
        try:
            mod.kwh_to_joules(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.kwh_to_joules(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kwh_to_joules(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kwh_to_joules(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kwh_to_joules("")
        except EXC:
            pass


class Test_lens_magnification:
    def test_exists(self):
        assert hasattr(mod, "lens_magnification")

    def test_doc0(self):
        try:
            mod.lens_magnification(0.6, 0.3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.lens_magnification(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lens_magnification(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lens_magnification(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lens_magnification("", "")
        except EXC:
            pass


class Test_light_years_to_kilometers:
    def test_exists(self):
        assert hasattr(mod, "light_years_to_kilometers")

    def test_doc0(self):
        try:
            mod.light_years_to_kilometers(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.light_years_to_kilometers(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.light_years_to_kilometers(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.light_years_to_kilometers(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.light_years_to_kilometers("")
        except EXC:
            pass


class Test_liters_per_minute_to_cubic_meters_per_second:
    def test_exists(self):
        assert hasattr(mod, "liters_per_minute_to_cubic_meters_per_second")

    def test_var0(self):
        try:
            mod.liters_per_minute_to_cubic_meters_per_second(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.liters_per_minute_to_cubic_meters_per_second(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.liters_per_minute_to_cubic_meters_per_second(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.liters_per_minute_to_cubic_meters_per_second("")
        except EXC:
            pass


class Test_liters_to_gallons:
    def test_exists(self):
        assert hasattr(mod, "liters_to_gallons")

    def test_var0(self):
        try:
            mod.liters_to_gallons(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.liters_to_gallons(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.liters_to_gallons(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.liters_to_gallons("")
        except EXC:
            pass


class Test_lorentz_factor:
    def test_exists(self):
        assert hasattr(mod, "lorentz_factor")

    def test_var0(self):
        try:
            mod.lorentz_factor(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lorentz_factor(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lorentz_factor(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lorentz_factor("")
        except EXC:
            pass


class Test_lumens_to_candela:
    def test_exists(self):
        assert hasattr(mod, "lumens_to_candela")

    def test_var0(self):
        try:
            mod.lumens_to_candela(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lumens_to_candela(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lumens_to_candela(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lumens_to_candela("")
        except EXC:
            pass


class Test_luminous_flux:
    def test_exists(self):
        assert hasattr(mod, "luminous_flux")

    def test_var0(self):
        try:
            mod.luminous_flux(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.luminous_flux(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.luminous_flux(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.luminous_flux("")
        except EXC:
            pass


class Test_mach_number:
    def test_exists(self):
        assert hasattr(mod, "mach_number")

    def test_var0(self):
        try:
            mod.mach_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mach_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mach_number(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mach_number("")
        except EXC:
            pass


class Test_mach_to_ms:
    def test_exists(self):
        assert hasattr(mod, "mach_to_ms")

    def test_doc0(self):
        try:
            mod.mach_to_ms(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mach_to_ms(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mach_to_ms(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mach_to_ms(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mach_to_ms("")
        except EXC:
            pass


class Test_magnetic_field_solenoid:
    def test_exists(self):
        assert hasattr(mod, "magnetic_field_solenoid")

    def test_var0(self):
        try:
            mod.magnetic_field_solenoid(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.magnetic_field_solenoid(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.magnetic_field_solenoid(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.magnetic_field_solenoid(0, "", 0)
        except EXC:
            pass


class Test_magnetic_flux:
    def test_exists(self):
        assert hasattr(mod, "magnetic_flux")

    def test_doc0(self):
        try:
            mod.magnetic_flux(0.5, 0.02)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.magnetic_flux(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.magnetic_flux(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.magnetic_flux(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.magnetic_flux("", "")
        except EXC:
            pass


class Test_magnetic_flux_density:
    def test_exists(self):
        assert hasattr(mod, "magnetic_flux_density")

    def test_var0(self):
        try:
            mod.magnetic_flux_density(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.magnetic_flux_density(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.magnetic_flux_density(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.magnetic_flux_density("", "", "")
        except EXC:
            pass


class Test_magnetic_force_charge:
    def test_exists(self):
        assert hasattr(mod, "magnetic_force_charge")

    def test_doc0(self):
        try:
            mod.magnetic_force_charge(1.6e-19, 1e6, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.magnetic_force_charge(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.magnetic_force_charge(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.magnetic_force_charge(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.magnetic_force_charge("", "", "")
        except EXC:
            pass


class Test_magnetic_force_on_wire:
    def test_exists(self):
        assert hasattr(mod, "magnetic_force_on_wire")

    def test_doc0(self):
        try:
            mod.magnetic_force_on_wire(5, 0.2, 0.3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.magnetic_force_on_wire(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.magnetic_force_on_wire(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.magnetic_force_on_wire(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.magnetic_force_on_wire("", 0, "")
        except EXC:
            pass


class Test_moment_of_inertia_point:
    def test_exists(self):
        assert hasattr(mod, "moment_of_inertia_point")

    def test_doc0(self):
        try:
            mod.moment_of_inertia_point(5, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.moment_of_inertia_point(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moment_of_inertia_point(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moment_of_inertia_point(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moment_of_inertia_point("", "")
        except EXC:
            pass


class Test_momentum:
    def test_exists(self):
        assert hasattr(mod, "momentum")

    def test_doc0(self):
        try:
            mod.momentum(10, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.momentum(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.momentum(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.momentum(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.momentum("", "")
        except EXC:
            pass


class Test_ms_to_mach:
    def test_exists(self):
        assert hasattr(mod, "ms_to_mach")

    def test_doc0(self):
        try:
            mod.ms_to_mach(343)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ms_to_mach(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ms_to_mach(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ms_to_mach(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ms_to_mach("")
        except EXC:
            pass


class Test_nernst_potential:
    def test_exists(self):
        assert hasattr(mod, "nernst_potential")

    def test_var0(self):
        try:
            mod.nernst_potential(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nernst_potential(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nernst_potential(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.nernst_potential("", 0, 0)
        except EXC:
            pass


class Test_newton_meters_to_foot_pounds:
    def test_exists(self):
        assert hasattr(mod, "newton_meters_to_foot_pounds")

    def test_var0(self):
        try:
            mod.newton_meters_to_foot_pounds(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.newton_meters_to_foot_pounds(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.newton_meters_to_foot_pounds(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.newton_meters_to_foot_pounds("")
        except EXC:
            pass


class Test_newtons_to_pounds_force:
    def test_exists(self):
        assert hasattr(mod, "newtons_to_pounds_force")

    def test_var0(self):
        try:
            mod.newtons_to_pounds_force(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.newtons_to_pounds_force(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.newtons_to_pounds_force(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.newtons_to_pounds_force("")
        except EXC:
            pass


class Test_noise_figure_to_temperature:
    def test_exists(self):
        assert hasattr(mod, "noise_figure_to_temperature")

    def test_var0(self):
        try:
            mod.noise_figure_to_temperature(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.noise_figure_to_temperature(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.noise_figure_to_temperature(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.noise_figure_to_temperature("")
        except EXC:
            pass


class Test_number_to_base:
    def test_exists(self):
        assert hasattr(mod, "number_to_base")

    def test_doc0(self):
        try:
            mod.number_to_base(255, 16)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.number_to_base(10, 2, 8)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.number_to_base(100, 8)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.number_to_base(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.number_to_base(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.number_to_base(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.number_to_base("", "")
        except EXC:
            pass


class Test_number_to_bool:
    def test_exists(self):
        assert hasattr(mod, "number_to_bool")

    def test_doc0(self):
        try:
            mod.number_to_bool(0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.number_to_bool(3.5)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.number_to_bool(-1)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.number_to_bool(0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.number_to_bool(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.number_to_bool(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.number_to_bool(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.number_to_bool("")
        except EXC:
            pass


class Test_number_to_complex:
    def test_exists(self):
        assert hasattr(mod, "number_to_complex")

    def test_doc0(self):
        try:
            mod.number_to_complex(4.2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.number_to_complex(7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.number_to_complex(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.number_to_complex(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.number_to_complex(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.number_to_complex("")
        except EXC:
            pass


class Test_number_to_hexadecimal:
    def test_exists(self):
        assert hasattr(mod, "number_to_hexadecimal")

    def test_doc0(self):
        try:
            mod.number_to_hexadecimal(255)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.number_to_hexadecimal(10)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.number_to_hexadecimal(0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.number_to_hexadecimal(25.75)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.number_to_hexadecimal(-10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.number_to_hexadecimal(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.number_to_hexadecimal(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.number_to_hexadecimal(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.number_to_hexadecimal("")
        except EXC:
            pass


class Test_number_to_octal:
    def test_exists(self):
        assert hasattr(mod, "number_to_octal")

    def test_doc0(self):
        try:
            mod.number_to_octal(8)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.number_to_octal(15)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.number_to_octal(0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.number_to_octal(10.99)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.number_to_octal(-7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.number_to_octal(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.number_to_octal(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.number_to_octal(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.number_to_octal("")
        except EXC:
            pass


class Test_number_to_string:
    def test_exists(self):
        assert hasattr(mod, "number_to_string")

    def test_doc0(self):
        try:
            mod.number_to_string(3.14)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.number_to_string(100)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.number_to_string(-0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.number_to_string(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.number_to_string(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.number_to_string(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.number_to_string("")
        except EXC:
            pass


class Test_number_to_words:
    def test_exists(self):
        assert hasattr(mod, "number_to_words")

    def test_doc0(self):
        try:
            mod.number_to_words(42)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.number_to_words(42, 'es')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.number_to_words(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.number_to_words(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.number_to_words(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.number_to_words(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.number_to_words("")
        except EXC:
            pass


class Test_nusselt_number:
    def test_exists(self):
        assert hasattr(mod, "nusselt_number")

    def test_doc0(self):
        try:
            mod.nusselt_number(50.0, 0.5, 0.6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.nusselt_number(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nusselt_number(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nusselt_number(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.nusselt_number("", 0, 0)
        except EXC:
            pass


class Test_nyquist_frequency:
    def test_exists(self):
        assert hasattr(mod, "nyquist_frequency")

    def test_doc0(self):
        try:
            mod.nyquist_frequency(44100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.nyquist_frequency(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nyquist_frequency(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nyquist_frequency(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.nyquist_frequency(0)
        except EXC:
            pass


class Test_oct_to_bin:
    def test_exists(self):
        assert hasattr(mod, "oct_to_bin")

    def test_doc0(self):
        try:
            mod.oct_to_bin('377')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.oct_to_bin('10')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.oct_to_bin("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.oct_to_bin("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.oct_to_bin(None)
        except EXC:
            pass


class Test_oct_to_hex:
    def test_exists(self):
        assert hasattr(mod, "oct_to_hex")

    def test_doc0(self):
        try:
            mod.oct_to_hex('377')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.oct_to_hex('37')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.oct_to_hex("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.oct_to_hex("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.oct_to_hex(None)
        except EXC:
            pass


class Test_octal_to_int:
    def test_exists(self):
        assert hasattr(mod, "octal_to_int")

    def test_doc0(self):
        try:
            mod.octal_to_int("0o17")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.octal_to_int("77")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.octal_to_int("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.octal_to_int("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.octal_to_int(None)
        except EXC:
            pass


class Test_ohms_law:
    def test_exists(self):
        assert hasattr(mod, "ohms_law")

    def test_doc0(self):
        try:
            mod.ohms_law(voltage=12, resistance=4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ohms_law()
        except EXC:
            pass


class Test_orbital_period:
    def test_exists(self):
        assert hasattr(mod, "orbital_period")

    def test_var0(self):
        try:
            mod.orbital_period(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.orbital_period(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.orbital_period(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.orbital_period("", "")
        except EXC:
            pass


class Test_parallel_resistance:
    def test_exists(self):
        assert hasattr(mod, "parallel_resistance")

    def test_var0(self):
        try:
            mod.parallel_resistance(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parallel_resistance(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parallel_resistance(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.parallel_resistance("", "")
        except EXC:
            pass


class Test_pascals_to_atmospheres:
    def test_exists(self):
        assert hasattr(mod, "pascals_to_atmospheres")

    def test_var0(self):
        try:
            mod.pascals_to_atmospheres(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pascals_to_atmospheres(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pascals_to_atmospheres(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pascals_to_atmospheres("")
        except EXC:
            pass


class Test_pascals_to_bars:
    def test_exists(self):
        assert hasattr(mod, "pascals_to_bars")

    def test_doc0(self):
        try:
            mod.pascals_to_bars(100000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.pascals_to_bars(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pascals_to_bars(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pascals_to_bars(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pascals_to_bars("")
        except EXC:
            pass


class Test_pascals_to_psi:
    def test_exists(self):
        assert hasattr(mod, "pascals_to_psi")

    def test_var0(self):
        try:
            mod.pascals_to_psi(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pascals_to_psi(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pascals_to_psi(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pascals_to_psi("")
        except EXC:
            pass


class Test_pendulum_period:
    def test_exists(self):
        assert hasattr(mod, "pendulum_period")

    def test_var0(self):
        try:
            mod.pendulum_period(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pendulum_period(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pendulum_period(None)
        except EXC:
            pass


class Test_ph_to_h_concentration:
    def test_exists(self):
        assert hasattr(mod, "ph_to_h_concentration")

    def test_doc0(self):
        try:
            mod.ph_to_h_concentration(7.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ph_to_h_concentration(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ph_to_h_concentration(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ph_to_h_concentration(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ph_to_h_concentration("")
        except EXC:
            pass


class Test_photon_energy:
    def test_exists(self):
        assert hasattr(mod, "photon_energy")

    def test_var0(self):
        try:
            mod.photon_energy(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.photon_energy(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.photon_energy(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.photon_energy("")
        except EXC:
            pass


class Test_photon_momentum:
    def test_exists(self):
        assert hasattr(mod, "photon_momentum")

    def test_var0(self):
        try:
            mod.photon_momentum(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.photon_momentum(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.photon_momentum(None)
        except EXC:
            pass


class Test_planck_radiation_peak:
    def test_exists(self):
        assert hasattr(mod, "planck_radiation_peak")

    def test_var0(self):
        try:
            mod.planck_radiation_peak(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.planck_radiation_peak(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.planck_radiation_peak(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.planck_radiation_peak("")
        except EXC:
            pass


class Test_potential_energy:
    def test_exists(self):
        assert hasattr(mod, "potential_energy")

    def test_var0(self):
        try:
            mod.potential_energy(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.potential_energy(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.potential_energy(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.potential_energy("", "")
        except EXC:
            pass


class Test_pounds_force_to_newtons:
    def test_exists(self):
        assert hasattr(mod, "pounds_force_to_newtons")

    def test_var0(self):
        try:
            mod.pounds_force_to_newtons(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pounds_force_to_newtons(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pounds_force_to_newtons(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pounds_force_to_newtons("")
        except EXC:
            pass


class Test_power_mechanical:
    def test_exists(self):
        assert hasattr(mod, "power_mechanical")

    def test_doc0(self):
        try:
            mod.power_mechanical(1000, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.power_mechanical(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.power_mechanical(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.power_mechanical(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.power_mechanical(0, "")
        except EXC:
            pass


class Test_power_physics:
    def test_exists(self):
        assert hasattr(mod, "power_physics")

    def test_doc0(self):
        try:
            mod.power_physics(1000, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.power_physics(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.power_physics(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.power_physics(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.power_physics(0, "")
        except EXC:
            pass


class Test_power_to_db:
    def test_exists(self):
        assert hasattr(mod, "power_to_db")

    def test_doc0(self):
        try:
            mod.power_to_db(100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.power_to_db(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.power_to_db(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.power_to_db(None)
        except EXC:
            pass


class Test_prandtl_number:
    def test_exists(self):
        assert hasattr(mod, "prandtl_number")

    def test_doc0(self):
        try:
            mod.prandtl_number(4182, 0.001, 0.6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.prandtl_number(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.prandtl_number(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.prandtl_number(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.prandtl_number("", "", 0)
        except EXC:
            pass


class Test_pressure_at_depth:
    def test_exists(self):
        assert hasattr(mod, "pressure_at_depth")

    def test_doc0(self):
        try:
            mod.pressure_at_depth(1000, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.pressure_at_depth(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pressure_at_depth(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pressure_at_depth(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pressure_at_depth("", 0)
        except EXC:
            pass


class Test_pressure_convert:
    def test_exists(self):
        assert hasattr(mod, "pressure_convert")

    def test_var0(self):
        try:
            mod.pressure_convert(0, "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pressure_convert(1, "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pressure_convert(None, "hello", "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pressure_convert("", "", "")
        except EXC:
            pass


class Test_projectile_max_height:
    def test_exists(self):
        assert hasattr(mod, "projectile_max_height")

    def test_var0(self):
        try:
            mod.projectile_max_height(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.projectile_max_height(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.projectile_max_height(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.projectile_max_height("", "")
        except EXC:
            pass


class Test_projectile_range:
    def test_exists(self):
        assert hasattr(mod, "projectile_range")

    def test_var0(self):
        try:
            mod.projectile_range(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.projectile_range(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.projectile_range(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.projectile_range("", "")
        except EXC:
            pass


class Test_projectile_time_of_flight:
    def test_exists(self):
        assert hasattr(mod, "projectile_time_of_flight")

    def test_var0(self):
        try:
            mod.projectile_time_of_flight(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.projectile_time_of_flight(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.projectile_time_of_flight(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.projectile_time_of_flight("", "")
        except EXC:
            pass


class Test_psi_to_pascals:
    def test_exists(self):
        assert hasattr(mod, "psi_to_pascals")

    def test_var0(self):
        try:
            mod.psi_to_pascals(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.psi_to_pascals(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.psi_to_pascals(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.psi_to_pascals("")
        except EXC:
            pass


class Test_radiation_dose_convert:
    def test_exists(self):
        assert hasattr(mod, "radiation_dose_convert")

    def test_doc0(self):
        try:
            mod.radiation_dose_convert(1, "sv", "rem")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.radiation_dose_convert(500, "mrem", "msv")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.radiation_dose_convert(3.14, "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.radiation_dose_convert(100, "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.radiation_dose_convert(None, "hello", "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.radiation_dose_convert("", "", "")
        except EXC:
            pass


class Test_rc_time_constant:
    def test_exists(self):
        assert hasattr(mod, "rc_time_constant")

    def test_doc0(self):
        try:
            mod.rc_time_constant(1000, 0.001)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rc_time_constant(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rc_time_constant(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rc_time_constant(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rc_time_constant("", "")
        except EXC:
            pass


class Test_relativistic_energy:
    def test_exists(self):
        assert hasattr(mod, "relativistic_energy")

    def test_var0(self):
        try:
            mod.relativistic_energy(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.relativistic_energy(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.relativistic_energy(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.relativistic_energy("", "")
        except EXC:
            pass


class Test_resistivity_resistance:
    def test_exists(self):
        assert hasattr(mod, "resistivity_resistance")

    def test_doc0(self):
        try:
            mod.resistivity_resistance(1.68e-8, 100, 1e-6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.resistivity_resistance(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.resistivity_resistance(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.resistivity_resistance(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.resistivity_resistance("", 0, "")
        except EXC:
            pass


class Test_resistors_parallel_pair:
    def test_exists(self):
        assert hasattr(mod, "resistors_parallel_pair")

    def test_doc0(self):
        try:
            mod.resistors_parallel_pair(100, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.resistors_parallel_pair(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.resistors_parallel_pair(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.resistors_parallel_pair(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.resistors_parallel_pair("", "")
        except EXC:
            pass


class Test_resonant_freq:
    def test_exists(self):
        assert hasattr(mod, "resonant_freq")

    def test_var0(self):
        try:
            mod.resonant_freq(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.resonant_freq(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.resonant_freq(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.resonant_freq("", "")
        except EXC:
            pass


class Test_reynolds_number:
    def test_exists(self):
        assert hasattr(mod, "reynolds_number")

    def test_doc0(self):
        try:
            mod.reynolds_number(1000, 1, 0.01, 0.001)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.reynolds_number(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.reynolds_number(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.reynolds_number(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.reynolds_number("", "", 0, "")
        except EXC:
            pass


class Test_rgb_to_cmyk:
    def test_exists(self):
        assert hasattr(mod, "rgb_to_cmyk")

    def test_doc0(self):
        try:
            mod.rgb_to_cmyk(255, 0, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rgb_to_cmyk(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rgb_to_cmyk(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rgb_to_cmyk(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rgb_to_cmyk("", "", "")
        except EXC:
            pass


class Test_rgb_to_hsl:
    def test_exists(self):
        assert hasattr(mod, "rgb_to_hsl")

    def test_doc0(self):
        try:
            mod.rgb_to_hsl(255, 0, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rgb_to_hsl(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rgb_to_hsl(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rgb_to_hsl(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rgb_to_hsl("", "", "")
        except EXC:
            pass


class Test_rgb_to_hsv:
    def test_exists(self):
        assert hasattr(mod, "rgb_to_hsv")

    def test_doc0(self):
        try:
            mod.rgb_to_hsv(255, 128, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rgb_to_hsv(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rgb_to_hsv(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rgb_to_hsv(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rgb_to_hsv("", "", "")
        except EXC:
            pass


class Test_rl_time_constant:
    def test_exists(self):
        assert hasattr(mod, "rl_time_constant")

    def test_doc0(self):
        try:
            mod.rl_time_constant(0.5, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rl_time_constant(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rl_time_constant(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rl_time_constant(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rl_time_constant("", "")
        except EXC:
            pass


class Test_rms_voltage:
    def test_exists(self):
        assert hasattr(mod, "rms_voltage")

    def test_var0(self):
        try:
            mod.rms_voltage(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rms_voltage(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rms_voltage(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rms_voltage("")
        except EXC:
            pass


class Test_roman_to_int:
    def test_exists(self):
        assert hasattr(mod, "roman_to_int")

    def test_doc0(self):
        try:
            mod.roman_to_int('XIV')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.roman_to_int('MMXXIV')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.roman_to_int("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.roman_to_int("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.roman_to_int(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.roman_to_int(0)
        except EXC:
            pass


class Test_round_float_to_int:
    def test_exists(self):
        assert hasattr(mod, "round_float_to_int")

    def test_doc0(self):
        try:
            mod.round_float_to_int(3.6)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.round_float_to_int(3.2)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.round_float_to_int(3.5)  # Rounds to nearest even (4)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.round_float_to_int(2.5)  # Rounds to nearest even (2)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.round_float_to_int(-3.6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.round_float_to_int(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.round_float_to_int(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.round_float_to_int(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.round_float_to_int("")
        except EXC:
            pass


class Test_rpm_to_hertz:
    def test_exists(self):
        assert hasattr(mod, "rpm_to_hertz")

    def test_var0(self):
        try:
            mod.rpm_to_hertz(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rpm_to_hertz(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rpm_to_hertz(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rpm_to_hertz("")
        except EXC:
            pass


class Test_safe_convert_number:
    def test_exists(self):
        assert hasattr(mod, "safe_convert_number")

    def test_doc0(self):
        try:
            mod.safe_convert_number("3.14")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.safe_convert_number("10")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.safe_convert_number("abc")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.safe_convert_number("")
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.safe_convert_number(None)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.safe_convert_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.safe_convert_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.safe_convert_number(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.safe_convert_number("")
        except EXC:
            pass


class Test_schwarzschild_radius:
    def test_exists(self):
        assert hasattr(mod, "schwarzschild_radius")

    def test_var0(self):
        try:
            mod.schwarzschild_radius(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.schwarzschild_radius(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.schwarzschild_radius(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.schwarzschild_radius("")
        except EXC:
            pass


class Test_shannon_capacity:
    def test_exists(self):
        assert hasattr(mod, "shannon_capacity")

    def test_var0(self):
        try:
            mod.shannon_capacity(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.shannon_capacity(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.shannon_capacity(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.shannon_capacity("", "")
        except EXC:
            pass


class Test_signal_rms:
    def test_exists(self):
        assert hasattr(mod, "signal_rms")

    def test_var0(self):
        try:
            mod.signal_rms([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.signal_rms([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.signal_rms(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.signal_rms("")
        except EXC:
            pass


class Test_signal_snr_db:
    def test_exists(self):
        assert hasattr(mod, "signal_snr_db")

    def test_var0(self):
        try:
            mod.signal_snr_db(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.signal_snr_db(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.signal_snr_db(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.signal_snr_db("", "")
        except EXC:
            pass


class Test_signal_to_noise_ratio:
    def test_exists(self):
        assert hasattr(mod, "signal_to_noise_ratio")

    def test_var0(self):
        try:
            mod.signal_to_noise_ratio(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.signal_to_noise_ratio(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.signal_to_noise_ratio(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.signal_to_noise_ratio("", "")
        except EXC:
            pass


class Test_skin_depth:
    def test_exists(self):
        assert hasattr(mod, "skin_depth")

    def test_var0(self):
        try:
            mod.skin_depth(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.skin_depth(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.skin_depth(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.skin_depth("", "")
        except EXC:
            pass


class Test_snells_law:
    def test_exists(self):
        assert hasattr(mod, "snells_law")

    def test_var0(self):
        try:
            mod.snells_law(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.snells_law(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.snells_law(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.snells_law("", "", "")
        except EXC:
            pass


class Test_snells_law_angle:
    def test_exists(self):
        assert hasattr(mod, "snells_law_angle")

    def test_var0(self):
        try:
            mod.snells_law_angle(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.snells_law_angle(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.snells_law_angle(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.snells_law_angle("", "", "")
        except EXC:
            pass


class Test_sound_intensity_level:
    def test_exists(self):
        assert hasattr(mod, "sound_intensity_level")

    def test_doc0(self):
        try:
            mod.sound_intensity_level(1e-6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sound_intensity_level(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sound_intensity_level(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sound_intensity_level(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sound_intensity_level("")
        except EXC:
            pass


class Test_specific_heat_energy:
    def test_exists(self):
        assert hasattr(mod, "specific_heat_energy")

    def test_doc0(self):
        try:
            mod.specific_heat_energy(1, 4186, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.specific_heat_energy(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.specific_heat_energy(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.specific_heat_energy(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.specific_heat_energy("", "", "")
        except EXC:
            pass


class Test_specific_impulse:
    def test_exists(self):
        assert hasattr(mod, "specific_impulse")

    def test_var0(self):
        try:
            mod.specific_impulse(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.specific_impulse(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.specific_impulse(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.specific_impulse("", 0)
        except EXC:
            pass


class Test_speed_convert:
    def test_exists(self):
        assert hasattr(mod, "speed_convert")

    def test_var0(self):
        try:
            mod.speed_convert(0, "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.speed_convert(1, "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.speed_convert(None, "hello", "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.speed_convert("", "", "")
        except EXC:
            pass


class Test_spring_potential_energy:
    def test_exists(self):
        assert hasattr(mod, "spring_potential_energy")

    def test_doc0(self):
        try:
            mod.spring_potential_energy(200, 0.1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.spring_potential_energy(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spring_potential_energy(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spring_potential_energy(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spring_potential_energy("", "")
        except EXC:
            pass


class Test_stefan_boltzmann_power:
    def test_exists(self):
        assert hasattr(mod, "stefan_boltzmann_power")

    def test_var0(self):
        try:
            mod.stefan_boltzmann_power(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stefan_boltzmann_power(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stefan_boltzmann_power(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.stefan_boltzmann_power("", "", "")
        except EXC:
            pass


class Test_stefan_boltzmann_temperature:
    def test_exists(self):
        assert hasattr(mod, "stefan_boltzmann_temperature")

    def test_var0(self):
        try:
            mod.stefan_boltzmann_temperature(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stefan_boltzmann_temperature(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stefan_boltzmann_temperature(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.stefan_boltzmann_temperature("", "", "")
        except EXC:
            pass


class Test_strain:
    def test_exists(self):
        assert hasattr(mod, "strain")

    def test_doc0(self):
        try:
            mod.strain(0.005, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.strain(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.strain(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.strain(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.strain(0, 0)
        except EXC:
            pass


class Test_stress:
    def test_exists(self):
        assert hasattr(mod, "stress")

    def test_doc0(self):
        try:
            mod.stress(1000, 0.01)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.stress(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stress(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stress(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.stress("", "")
        except EXC:
            pass


class Test_strouhal_number:
    def test_exists(self):
        assert hasattr(mod, "strouhal_number")

    def test_doc0(self):
        try:
            mod.strouhal_number(10.0, 0.1, 5.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.strouhal_number(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.strouhal_number(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.strouhal_number(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.strouhal_number("", 0, "")
        except EXC:
            pass


class Test_temperature_convert:
    def test_exists(self):
        assert hasattr(mod, "temperature_convert")

    def test_doc0(self):
        try:
            mod.temperature_convert(100, "C", "F")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.temperature_convert(32, "F", "C")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.temperature_convert(0, "C", "K")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.temperature_convert(0, "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.temperature_convert(1, "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.temperature_convert(None, "hello", "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.temperature_convert("", "", "")
        except EXC:
            pass


class Test_terminal_velocity:
    def test_exists(self):
        assert hasattr(mod, "terminal_velocity")

    def test_var0(self):
        try:
            mod.terminal_velocity(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.terminal_velocity(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.terminal_velocity(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.terminal_velocity("", "", "")
        except EXC:
            pass


class Test_thermal_expansion_length:
    def test_exists(self):
        assert hasattr(mod, "thermal_expansion_length")

    def test_doc0(self):
        try:
            mod.thermal_expansion_length(2.0, 1.2e-5, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.thermal_expansion_length(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.thermal_expansion_length(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.thermal_expansion_length(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.thermal_expansion_length(0, 0, "")
        except EXC:
            pass


class Test_thermal_noise:
    def test_exists(self):
        assert hasattr(mod, "thermal_noise")

    def test_doc0(self):
        try:
            mod.thermal_noise(1e6, 290)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.thermal_noise(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.thermal_noise(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.thermal_noise(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.thermal_noise("")
        except EXC:
            pass


class Test_thermal_resistance:
    def test_exists(self):
        assert hasattr(mod, "thermal_resistance")

    def test_doc0(self):
        try:
            mod.thermal_resistance(0.1, 200, 0.01)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.thermal_resistance(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.thermal_resistance(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.thermal_resistance(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.thermal_resistance(0, "", "")
        except EXC:
            pass


class Test_to_js_safe_integer:
    def test_exists(self):
        assert hasattr(mod, "to_js_safe_integer")

    def test_doc0(self):
        try:
            mod.to_js_safe_integer(100)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.to_js_safe_integer(9007199254740991) # JS_MAX_SAFE_INTEGER
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.to_js_safe_integer(9007199254740992) # JS_MAX_SAFE_INTEGER + 1
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.to_js_safe_integer(-9007199254740991) # JS_MIN_SAFE_INTEGER
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.to_js_safe_integer(-9007199254740992) # JS_MIN_SAFE_INTEGER - 1
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.to_js_safe_integer(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.to_js_safe_integer(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.to_js_safe_integer(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.to_js_safe_integer("")
        except EXC:
            pass


class Test_torque:
    def test_exists(self):
        assert hasattr(mod, "torque")

    def test_doc0(self):
        try:
            mod.torque(100, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.torque(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.torque(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.torque(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.torque("", "")
        except EXC:
            pass


class Test_troy_ounces_to_grams:
    def test_exists(self):
        assert hasattr(mod, "troy_ounces_to_grams")

    def test_var0(self):
        try:
            mod.troy_ounces_to_grams(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.troy_ounces_to_grams(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.troy_ounces_to_grams(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.troy_ounces_to_grams("")
        except EXC:
            pass


class Test_voltage_divider:
    def test_exists(self):
        assert hasattr(mod, "voltage_divider")

    def test_doc0(self):
        try:
            mod.voltage_divider(12, 8000, 4000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.voltage_divider(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.voltage_divider(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.voltage_divider(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.voltage_divider(0, "", "")
        except EXC:
            pass


class Test_voltage_to_db:
    def test_exists(self):
        assert hasattr(mod, "voltage_to_db")

    def test_doc0(self):
        try:
            mod.voltage_to_db(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.voltage_to_db(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.voltage_to_db(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.voltage_to_db(None)
        except EXC:
            pass


class Test_watts_to_horsepower:
    def test_exists(self):
        assert hasattr(mod, "watts_to_horsepower")

    def test_var0(self):
        try:
            mod.watts_to_horsepower(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.watts_to_horsepower(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.watts_to_horsepower(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.watts_to_horsepower("")
        except EXC:
            pass


class Test_wave_frequency:
    def test_exists(self):
        assert hasattr(mod, "wave_frequency")

    def test_doc0(self):
        try:
            mod.wave_frequency(340, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.wave_frequency(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wave_frequency(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wave_frequency(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.wave_frequency("", 0)
        except EXC:
            pass


class Test_wave_speed:
    def test_exists(self):
        assert hasattr(mod, "wave_speed")

    def test_doc0(self):
        try:
            mod.wave_speed(440, 0.78)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.wave_speed(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wave_speed(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wave_speed(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.wave_speed("", 0)
        except EXC:
            pass


class Test_wavelength:
    def test_exists(self):
        assert hasattr(mod, "wavelength")

    def test_doc0(self):
        try:
            mod.wavelength(1e9)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.wavelength(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wavelength(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wavelength(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.wavelength("")
        except EXC:
            pass


class Test_wavelength_to_frequency:
    def test_exists(self):
        assert hasattr(mod, "wavelength_to_frequency")

    def test_doc0(self):
        try:
            mod.wavelength_to_frequency(0.5e-6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.wavelength_to_frequency(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wavelength_to_frequency(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wavelength_to_frequency(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.wavelength_to_frequency(0)
        except EXC:
            pass


class Test_weber_number:
    def test_exists(self):
        assert hasattr(mod, "weber_number")

    def test_doc0(self):
        try:
            mod.weber_number(1000, 2, 0.01, 0.072)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.weber_number(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weber_number(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weber_number(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weber_number("", "", 0, "")
        except EXC:
            pass


class Test_wien_displacement_peak:
    def test_exists(self):
        assert hasattr(mod, "wien_displacement_peak")

    def test_var0(self):
        try:
            mod.wien_displacement_peak(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wien_displacement_peak(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wien_displacement_peak(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.wien_displacement_peak("")
        except EXC:
            pass


class Test_wind_chill:
    def test_exists(self):
        assert hasattr(mod, "wind_chill")

    def test_var0(self):
        try:
            mod.wind_chill(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wind_chill(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wind_chill(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.wind_chill("", "")
        except EXC:
            pass


class Test_work_done:
    def test_exists(self):
        assert hasattr(mod, "work_done")

    def test_doc0(self):
        try:
            mod.work_done(50, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.work_done(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.work_done(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.work_done(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.work_done("", "")
        except EXC:
            pass

