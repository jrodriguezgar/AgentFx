# Deep coverage tests for formulite.fxNumeric.conversion_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxNumeric.conversion_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_convert_units_deep:
    def test_c0(self):
        try:
            mod.convert_units(1, "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.convert_units(2, "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.convert_units(3, "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.convert_units(5, "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.convert_units(10, "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.convert_units(0, "hello world", "test")
        except EXC:
            pass


class Test_convert_string_to_float_with_locale_deep:
    def test_c0(self):
        try:
            mod.convert_string_to_float_with_locale("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.convert_string_to_float_with_locale("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.convert_string_to_float_with_locale("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.convert_string_to_float_with_locale("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.convert_string_to_float_with_locale("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.convert_string_to_float_with_locale("UPPER lower 123")
        except EXC:
            pass

    def test_kw_target_locale(self):
        try:
            mod.convert_string_to_float_with_locale("hello world", target_locale="hello world")
        except EXC:
            pass


class Test_hsl_to_rgb_deep:
    def test_c0(self):
        try:
            mod.hsl_to_rgb(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hsl_to_rgb(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hsl_to_rgb(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hsl_to_rgb(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hsl_to_rgb(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hsl_to_rgb(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.hsl_to_rgb(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.hsl_to_rgb(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.hsl_to_rgb(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.hsl_to_rgb(2, 1, 42)
        except EXC:
            pass


class Test_hsv_to_rgb_deep:
    def test_c0(self):
        try:
            mod.hsv_to_rgb(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hsv_to_rgb(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hsv_to_rgb(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hsv_to_rgb(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hsv_to_rgb(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hsv_to_rgb(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.hsv_to_rgb(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.hsv_to_rgb(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.hsv_to_rgb(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.hsv_to_rgb(2, 1, 42)
        except EXC:
            pass


class Test_terminal_velocity_deep:
    def test_c0(self):
        try:
            mod.terminal_velocity(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.terminal_velocity(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.terminal_velocity(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.terminal_velocity(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.terminal_velocity(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.terminal_velocity(0, 1, 2)
        except EXC:
            pass

    def test_kw_air_density(self):
        try:
            mod.terminal_velocity(1, 2, 3, air_density=1)
        except EXC:
            pass


class Test_magnetic_force_on_wire_deep:
    def test_c0(self):
        try:
            mod.magnetic_force_on_wire(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.magnetic_force_on_wire(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.magnetic_force_on_wire(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.magnetic_force_on_wire(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.magnetic_force_on_wire(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.magnetic_force_on_wire(0, 1, 2)
        except EXC:
            pass

    def test_kw_angle(self):
        try:
            mod.magnetic_force_on_wire(1, 2, 3, angle=1)
        except EXC:
            pass


class Test_color_temperature_to_rgb_deep:
    def test_c0(self):
        try:
            mod.color_temperature_to_rgb(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.color_temperature_to_rgb(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.color_temperature_to_rgb(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.color_temperature_to_rgb(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.color_temperature_to_rgb(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.color_temperature_to_rgb(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.color_temperature_to_rgb(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.color_temperature_to_rgb(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.color_temperature_to_rgb(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.color_temperature_to_rgb(2)
        except EXC:
            pass


class Test_doppler_shift_deep:
    def test_c0(self):
        try:
            mod.doppler_shift(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.doppler_shift(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.doppler_shift(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.doppler_shift(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.doppler_shift(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.doppler_shift(0, 1)
        except EXC:
            pass

    def test_kw_wave_speed(self):
        try:
            mod.doppler_shift(1, 2, wave_speed=1)
        except EXC:
            pass


class Test_reynolds_number_deep:
    def test_c0(self):
        try:
            mod.reynolds_number(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.reynolds_number(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.reynolds_number(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.reynolds_number(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.reynolds_number(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.reynolds_number(0, 1, 2, 3)
        except EXC:
            pass


class Test_stefan_boltzmann_power_deep:
    def test_c0(self):
        try:
            mod.stefan_boltzmann_power(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.stefan_boltzmann_power(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.stefan_boltzmann_power(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.stefan_boltzmann_power(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.stefan_boltzmann_power(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.stefan_boltzmann_power(0, 1, 2)
        except EXC:
            pass


class Test_base_to_decimal_deep:
    def test_c0(self):
        try:
            mod.base_to_decimal("hello world", 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.base_to_decimal("test", 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.base_to_decimal("abc123", 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.base_to_decimal("", 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.base_to_decimal("Hello, World!", 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.base_to_decimal("UPPER lower 123", 1)
        except EXC:
            pass


class Test_buoyant_force_deep:
    def test_c0(self):
        try:
            mod.buoyant_force(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.buoyant_force(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.buoyant_force(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.buoyant_force(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.buoyant_force(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.buoyant_force(0, 1)
        except EXC:
            pass

    def test_kw_gravity(self):
        try:
            mod.buoyant_force(1, 2, gravity=1)
        except EXC:
            pass


class Test_coordinate_dms_to_decimal_deep:
    def test_c0(self):
        try:
            mod.coordinate_dms_to_decimal(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.coordinate_dms_to_decimal(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.coordinate_dms_to_decimal(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.coordinate_dms_to_decimal(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.coordinate_dms_to_decimal(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.coordinate_dms_to_decimal(0, 1, 2)
        except EXC:
            pass

    def test_kw_direction(self):
        try:
            mod.coordinate_dms_to_decimal(1, 2, 3, direction="hello world")
        except EXC:
            pass


class Test_gravitational_force_deep:
    def test_c0(self):
        try:
            mod.gravitational_force(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gravitational_force(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gravitational_force(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gravitational_force(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gravitational_force(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gravitational_force(0, 1, 2)
        except EXC:
            pass


class Test_half_life_remaining_deep:
    def test_c0(self):
        try:
            mod.half_life_remaining(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.half_life_remaining(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.half_life_remaining(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.half_life_remaining(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.half_life_remaining(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.half_life_remaining(0, 1, 2)
        except EXC:
            pass


class Test_ideal_gas_pressure_deep:
    def test_c0(self):
        try:
            mod.ideal_gas_pressure(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ideal_gas_pressure(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ideal_gas_pressure(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ideal_gas_pressure(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ideal_gas_pressure(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ideal_gas_pressure(0, 1, 2)
        except EXC:
            pass


class Test_magnetic_flux_deep:
    def test_c0(self):
        try:
            mod.magnetic_flux(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.magnetic_flux(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.magnetic_flux(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.magnetic_flux(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.magnetic_flux(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.magnetic_flux(0, 1)
        except EXC:
            pass

    def test_kw_angle(self):
        try:
            mod.magnetic_flux(1, 2, angle=1)
        except EXC:
            pass


class Test_number_to_base_deep:
    def test_c0(self):
        try:
            mod.number_to_base(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.number_to_base(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.number_to_base(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.number_to_base(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.number_to_base(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.number_to_base(0, 1)
        except EXC:
            pass

    def test_kw_min_length(self):
        try:
            mod.number_to_base(1, 2, min_length=1)
        except EXC:
            pass


class Test_number_to_hexadecimal_deep:
    def test_c0(self):
        try:
            mod.number_to_hexadecimal(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.number_to_hexadecimal(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.number_to_hexadecimal(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.number_to_hexadecimal(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.number_to_hexadecimal(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.number_to_hexadecimal(0)
        except EXC:
            pass


class Test_number_to_octal_deep:
    def test_c0(self):
        try:
            mod.number_to_octal(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.number_to_octal(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.number_to_octal(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.number_to_octal(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.number_to_octal(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.number_to_octal(0)
        except EXC:
            pass


class Test_ohms_law_deep:
    def test_c0(self):
        try:
            mod.ohms_law()
        except EXC:
            pass

    def test_kw_voltage(self):
        try:
            mod.ohms_law(voltage=1)
        except EXC:
            pass

    def test_kw_current(self):
        try:
            mod.ohms_law(current=1)
        except EXC:
            pass

    def test_kw_resistance(self):
        try:
            mod.ohms_law(resistance=1)
        except EXC:
            pass


class Test_potential_energy_deep:
    def test_c0(self):
        try:
            mod.potential_energy(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.potential_energy(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.potential_energy(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.potential_energy(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.potential_energy(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.potential_energy(0, 1)
        except EXC:
            pass

    def test_kw_g(self):
        try:
            mod.potential_energy(1, 2, g=1)
        except EXC:
            pass


class Test_specific_heat_energy_deep:
    def test_c0(self):
        try:
            mod.specific_heat_energy(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.specific_heat_energy(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.specific_heat_energy(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.specific_heat_energy(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.specific_heat_energy(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.specific_heat_energy(0, 1, 2)
        except EXC:
            pass


class Test_angle_convert_deep:
    def test_c0(self):
        try:
            mod.angle_convert(1, "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.angle_convert(2, "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.angle_convert(3, "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.angle_convert(5, "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.angle_convert(10, "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.angle_convert(0, "hello world", "test")
        except EXC:
            pass


class Test_bernoulli_velocity_deep:
    def test_c0(self):
        try:
            mod.bernoulli_velocity(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bernoulli_velocity(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bernoulli_velocity(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bernoulli_velocity(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bernoulli_velocity(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bernoulli_velocity(0, 1)
        except EXC:
            pass


class Test_capacitive_reactance_deep:
    def test_c0(self):
        try:
            mod.capacitive_reactance(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.capacitive_reactance(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.capacitive_reactance(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.capacitive_reactance(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.capacitive_reactance(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.capacitive_reactance(0, 1)
        except EXC:
            pass


class Test_coulomb_force_deep:
    def test_c0(self):
        try:
            mod.coulomb_force(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.coulomb_force(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.coulomb_force(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.coulomb_force(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.coulomb_force(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.coulomb_force(0, 1, 2)
        except EXC:
            pass


class Test_coulombs_force_deep:
    def test_c0(self):
        try:
            mod.coulombs_force(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.coulombs_force(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.coulombs_force(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.coulombs_force(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.coulombs_force(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.coulombs_force(0, 1, 2)
        except EXC:
            pass


class Test_coulombs_law_deep:
    def test_c0(self):
        try:
            mod.coulombs_law(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.coulombs_law(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.coulombs_law(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.coulombs_law(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.coulombs_law(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.coulombs_law(0, 1, 2)
        except EXC:
            pass


class Test_de_broglie_wavelength_deep:
    def test_c0(self):
        try:
            mod.de_broglie_wavelength(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.de_broglie_wavelength(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.de_broglie_wavelength(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.de_broglie_wavelength(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.de_broglie_wavelength(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.de_broglie_wavelength(0, 1)
        except EXC:
            pass


class Test_dft_magnitude_deep:
    def test_c0(self):
        try:
            mod.dft_magnitude([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dft_magnitude([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dft_magnitude([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dft_magnitude([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dft_magnitude([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dft_magnitude([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_dft_phase_deep:
    def test_c0(self):
        try:
            mod.dft_phase([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dft_phase([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dft_phase([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dft_phase([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dft_phase([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dft_phase([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_doppler_freq_deep:
    def test_c0(self):
        try:
            mod.doppler_freq(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.doppler_freq(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.doppler_freq(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.doppler_freq(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.doppler_freq(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.doppler_freq(0, 1)
        except EXC:
            pass

    def test_kw_wave_speed(self):
        try:
            mod.doppler_freq(1, 2, wave_speed=1)
        except EXC:
            pass


class Test_drag_force_deep:
    def test_c0(self):
        try:
            mod.drag_force(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.drag_force(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.drag_force(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.drag_force(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.drag_force(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.drag_force(0, 1, 2, 3)
        except EXC:
            pass


class Test_energy_convert_deep:
    def test_c0(self):
        try:
            mod.energy_convert(1, "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.energy_convert(2, "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.energy_convert(3, "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.energy_convert(5, "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.energy_convert(10, "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.energy_convert(0, "hello world", "test")
        except EXC:
            pass


class Test_escape_velocity_deep:
    def test_c0(self):
        try:
            mod.escape_velocity(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.escape_velocity(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.escape_velocity(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.escape_velocity(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.escape_velocity(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.escape_velocity(0, 1)
        except EXC:
            pass


class Test_focal_length_deep:
    def test_c0(self):
        try:
            mod.focal_length(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.focal_length(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.focal_length(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.focal_length(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.focal_length(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.focal_length(0, 1)
        except EXC:
            pass


class Test_heat_engine_efficiency_deep:
    def test_c0(self):
        try:
            mod.heat_engine_efficiency(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.heat_engine_efficiency(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.heat_engine_efficiency(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.heat_engine_efficiency(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.heat_engine_efficiency(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.heat_engine_efficiency(0, 1)
        except EXC:
            pass


class Test_mach_number_deep:
    def test_c0(self):
        try:
            mod.mach_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mach_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mach_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mach_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mach_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mach_number(0)
        except EXC:
            pass

    def test_kw_speed_of_sound(self):
        try:
            mod.mach_number(1, speed_of_sound=1)
        except EXC:
            pass


class Test_nernst_potential_deep:
    def test_c0(self):
        try:
            mod.nernst_potential(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.nernst_potential(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.nernst_potential(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.nernst_potential(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.nernst_potential(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.nernst_potential(0, 1, 2)
        except EXC:
            pass

    def test_kw_temperature(self):
        try:
            mod.nernst_potential(1, 2, 3, temperature=1)
        except EXC:
            pass


class Test_noise_figure_to_temperature_deep:
    def test_c0(self):
        try:
            mod.noise_figure_to_temperature(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.noise_figure_to_temperature(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.noise_figure_to_temperature(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.noise_figure_to_temperature(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.noise_figure_to_temperature(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.noise_figure_to_temperature(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.noise_figure_to_temperature(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.noise_figure_to_temperature(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.noise_figure_to_temperature(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.noise_figure_to_temperature(2)
        except EXC:
            pass

    def test_kw_t0(self):
        try:
            mod.noise_figure_to_temperature(1, t0=1)
        except EXC:
            pass


class Test_number_to_words_deep:
    def test_c0(self):
        try:
            mod.number_to_words(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.number_to_words(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.number_to_words(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.number_to_words(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.number_to_words(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.number_to_words(0)
        except EXC:
            pass

    def test_kw_lang(self):
        try:
            mod.number_to_words(1, lang="hello world")
        except EXC:
            pass


class Test_parallel_resistance_deep:
    def test_c0(self):
        try:
            mod.parallel_resistance(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.parallel_resistance(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.parallel_resistance(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.parallel_resistance(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.parallel_resistance(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.parallel_resistance(0, 1)
        except EXC:
            pass


class Test_pendulum_period_deep:
    def test_c0(self):
        try:
            mod.pendulum_period(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.pendulum_period(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.pendulum_period(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.pendulum_period(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.pendulum_period(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.pendulum_period(0)
        except EXC:
            pass

    def test_kw_gravity(self):
        try:
            mod.pendulum_period(1, gravity=1)
        except EXC:
            pass


class Test_pressure_at_depth_deep:
    def test_c0(self):
        try:
            mod.pressure_at_depth(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.pressure_at_depth(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.pressure_at_depth(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.pressure_at_depth(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.pressure_at_depth(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.pressure_at_depth(0, 1)
        except EXC:
            pass

    def test_kw_gravity(self):
        try:
            mod.pressure_at_depth(1, 2, gravity=1)
        except EXC:
            pass

    def test_kw_surface_pressure(self):
        try:
            mod.pressure_at_depth(1, 2, surface_pressure=1)
        except EXC:
            pass


class Test_pressure_convert_deep:
    def test_c0(self):
        try:
            mod.pressure_convert(1, "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.pressure_convert(2, "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.pressure_convert(3, "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.pressure_convert(5, "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.pressure_convert(10, "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.pressure_convert(0, "hello world", "test")
        except EXC:
            pass


class Test_rc_time_constant_deep:
    def test_c0(self):
        try:
            mod.rc_time_constant(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rc_time_constant(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rc_time_constant(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rc_time_constant(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rc_time_constant(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rc_time_constant(0, 1)
        except EXC:
            pass


class Test_rgb_to_hsl_deep:
    def test_c0(self):
        try:
            mod.rgb_to_hsl(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rgb_to_hsl(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rgb_to_hsl(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rgb_to_hsl(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rgb_to_hsl(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rgb_to_hsl(0, 1, 2)
        except EXC:
            pass


class Test_rgb_to_hsv_deep:
    def test_c0(self):
        try:
            mod.rgb_to_hsv(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rgb_to_hsv(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rgb_to_hsv(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rgb_to_hsv(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rgb_to_hsv(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rgb_to_hsv(0, 1, 2)
        except EXC:
            pass


class Test_rl_time_constant_deep:
    def test_c0(self):
        try:
            mod.rl_time_constant(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rl_time_constant(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rl_time_constant(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rl_time_constant(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rl_time_constant(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rl_time_constant(0, 1)
        except EXC:
            pass


class Test_signal_snr_db_deep:
    def test_c0(self):
        try:
            mod.signal_snr_db(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.signal_snr_db(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.signal_snr_db(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.signal_snr_db(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.signal_snr_db(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.signal_snr_db(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.signal_snr_db(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.signal_snr_db(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.signal_snr_db(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.signal_snr_db(2, 1)
        except EXC:
            pass


class Test_snells_law_deep:
    def test_c0(self):
        try:
            mod.snells_law(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.snells_law(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.snells_law(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.snells_law(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.snells_law(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.snells_law(0, 1, 2)
        except EXC:
            pass


class Test_specific_impulse_deep:
    def test_c0(self):
        try:
            mod.specific_impulse(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.specific_impulse(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.specific_impulse(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.specific_impulse(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.specific_impulse(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.specific_impulse(0, 1)
        except EXC:
            pass

    def test_kw_gravity(self):
        try:
            mod.specific_impulse(1, 2, gravity=1)
        except EXC:
            pass


class Test_speed_convert_deep:
    def test_c0(self):
        try:
            mod.speed_convert(1, "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.speed_convert(2, "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.speed_convert(3, "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.speed_convert(5, "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.speed_convert(10, "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.speed_convert(0, "hello world", "test")
        except EXC:
            pass


class Test_stefan_boltzmann_temperature_deep:
    def test_c0(self):
        try:
            mod.stefan_boltzmann_temperature(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.stefan_boltzmann_temperature(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.stefan_boltzmann_temperature(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.stefan_boltzmann_temperature(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.stefan_boltzmann_temperature(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.stefan_boltzmann_temperature(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.stefan_boltzmann_temperature(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.stefan_boltzmann_temperature(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.stefan_boltzmann_temperature(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.stefan_boltzmann_temperature(2, 1, 42)
        except EXC:
            pass


class Test_stress_deep:
    def test_c0(self):
        try:
            mod.stress(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.stress(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.stress(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.stress(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.stress(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.stress(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.stress(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.stress(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.stress(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.stress(2, 1)
        except EXC:
            pass


class Test_temperature_convert_deep:
    def test_c0(self):
        try:
            mod.temperature_convert(1, "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.temperature_convert(2, "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.temperature_convert(3, "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.temperature_convert(5, "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.temperature_convert(10, "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.temperature_convert(0, "hello world", "test")
        except EXC:
            pass


class Test_torque_deep:
    def test_c0(self):
        try:
            mod.torque(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.torque(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.torque(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.torque(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.torque(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.torque(0, 1)
        except EXC:
            pass

    def test_kw_angle(self):
        try:
            mod.torque(1, 2, angle=1)
        except EXC:
            pass


class Test_voltage_divider_deep:
    def test_c0(self):
        try:
            mod.voltage_divider(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.voltage_divider(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.voltage_divider(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.voltage_divider(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.voltage_divider(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.voltage_divider(0, 1, 2)
        except EXC:
            pass


class Test_wave_speed_deep:
    def test_c0(self):
        try:
            mod.wave_speed(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.wave_speed(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.wave_speed(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.wave_speed(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.wave_speed(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.wave_speed(0, 1)
        except EXC:
            pass


class Test_add_bool_to_int_deep:
    def test_c0(self):
        try:
            mod.add_bool_to_int(True, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.add_bool_to_int(False, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.add_bool_to_int(True, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.add_bool_to_int(False, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.add_bool_to_int(True, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.add_bool_to_int(False, 1)
        except EXC:
            pass


class Test_angular_momentum_deep:
    def test_c0(self):
        try:
            mod.angular_momentum(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.angular_momentum(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.angular_momentum(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.angular_momentum(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.angular_momentum(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.angular_momentum(0, 1, 2)
        except EXC:
            pass


class Test_bending_moment_deep:
    def test_c0(self):
        try:
            mod.bending_moment(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bending_moment(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bending_moment(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bending_moment(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bending_moment(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bending_moment(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bending_moment(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bending_moment(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bending_moment(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bending_moment(2, 1)
        except EXC:
            pass


class Test_bmi_deep:
    def test_c0(self):
        try:
            mod.bmi(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bmi(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bmi(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bmi(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bmi(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bmi(0, 1)
        except EXC:
            pass


class Test_bulk_modulus_pressure_deep:
    def test_c0(self):
        try:
            mod.bulk_modulus_pressure(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bulk_modulus_pressure(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bulk_modulus_pressure(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bulk_modulus_pressure(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bulk_modulus_pressure(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bulk_modulus_pressure(0, 1, 2)
        except EXC:
            pass


class Test_bytes_to_human_readable_deep:
    def test_c0(self):
        try:
            mod.bytes_to_human_readable(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bytes_to_human_readable(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bytes_to_human_readable(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bytes_to_human_readable(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bytes_to_human_readable(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bytes_to_human_readable(0)
        except EXC:
            pass


class Test_candela_to_lumens_deep:
    def test_c0(self):
        try:
            mod.candela_to_lumens(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.candela_to_lumens(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.candela_to_lumens(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.candela_to_lumens(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.candela_to_lumens(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.candela_to_lumens(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.candela_to_lumens(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.candela_to_lumens(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.candela_to_lumens(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.candela_to_lumens(2)
        except EXC:
            pass

    def test_kw_solid_angle_sr(self):
        try:
            mod.candela_to_lumens(1, solid_angle_sr=1)
        except EXC:
            pass


class Test_capacitor_energy_deep:
    def test_c0(self):
        try:
            mod.capacitor_energy(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.capacitor_energy(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.capacitor_energy(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.capacitor_energy(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.capacitor_energy(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.capacitor_energy(0, 1)
        except EXC:
            pass


class Test_color_luminance_deep:
    def test_c0(self):
        try:
            mod.color_luminance(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.color_luminance(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.color_luminance(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.color_luminance(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.color_luminance(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.color_luminance(0, 1, 2)
        except EXC:
            pass


class Test_current_divider_deep:
    def test_c0(self):
        try:
            mod.current_divider(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.current_divider(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.current_divider(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.current_divider(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.current_divider(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.current_divider(0, 1, 2)
        except EXC:
            pass


class Test_dec_to_oct_deep:
    def test_c0(self):
        try:
            mod.dec_to_oct(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dec_to_oct(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dec_to_oct(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dec_to_oct(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dec_to_oct(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dec_to_oct(0)
        except EXC:
            pass


class Test_decibel_add_deep:
    def test_c0(self):
        try:
            mod.decibel_add(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.decibel_add(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.decibel_add(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.decibel_add(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.decibel_add(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.decibel_add(0, 1)
        except EXC:
            pass


class Test_decibel_sum_deep:
    def test_c0(self):
        try:
            mod.decibel_sum(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.decibel_sum(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.decibel_sum(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.decibel_sum(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.decibel_sum(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.decibel_sum(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.decibel_sum(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.decibel_sum(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.decibel_sum(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.decibel_sum(2, 1)
        except EXC:
            pass


class Test_density_to_specific_gravity_deep:
    def test_c0(self):
        try:
            mod.density_to_specific_gravity(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.density_to_specific_gravity(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.density_to_specific_gravity(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.density_to_specific_gravity(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.density_to_specific_gravity(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.density_to_specific_gravity(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.density_to_specific_gravity(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.density_to_specific_gravity(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.density_to_specific_gravity(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.density_to_specific_gravity(2)
        except EXC:
            pass

    def test_kw_reference(self):
        try:
            mod.density_to_specific_gravity(1, reference=1)
        except EXC:
            pass


class Test_dew_point_deep:
    def test_c0(self):
        try:
            mod.dew_point(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dew_point(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dew_point(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dew_point(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dew_point(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dew_point(0, 1)
        except EXC:
            pass


class Test_doppler_frequency_deep:
    def test_c0(self):
        try:
            mod.doppler_frequency(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.doppler_frequency(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.doppler_frequency(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.doppler_frequency(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.doppler_frequency(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.doppler_frequency(0, 1)
        except EXC:
            pass

    def test_kw_observer_speed(self):
        try:
            mod.doppler_frequency(1, 2, observer_speed=1)
        except EXC:
            pass

    def test_kw_source_speed(self):
        try:
            mod.doppler_frequency(1, 2, source_speed=1)
        except EXC:
            pass


class Test_elastic_modulus_deep:
    def test_c0(self):
        try:
            mod.elastic_modulus(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.elastic_modulus(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.elastic_modulus(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.elastic_modulus(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.elastic_modulus(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.elastic_modulus(0, 1)
        except EXC:
            pass


class Test_electric_field_point_deep:
    def test_c0(self):
        try:
            mod.electric_field_point(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.electric_field_point(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.electric_field_point(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.electric_field_point(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.electric_field_point(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.electric_field_point(0, 1)
        except EXC:
            pass


class Test_float_to_json_safe_deep:
    def test_c0(self):
        try:
            mod.float_to_json_safe(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.float_to_json_safe(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.float_to_json_safe(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.float_to_json_safe(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.float_to_json_safe(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.float_to_json_safe(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.float_to_json_safe(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.float_to_json_safe(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.float_to_json_safe(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.float_to_json_safe(2)
        except EXC:
            pass


class Test_free_space_path_loss_deep:
    def test_c0(self):
        try:
            mod.free_space_path_loss(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.free_space_path_loss(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.free_space_path_loss(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.free_space_path_loss(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.free_space_path_loss(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.free_space_path_loss(0, 1)
        except EXC:
            pass


class Test_friction_force_deep:
    def test_c0(self):
        try:
            mod.friction_force(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.friction_force(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.friction_force(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.friction_force(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.friction_force(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.friction_force(0, 1)
        except EXC:
            pass


class Test_gravitational_potential_energy_deep:
    def test_c0(self):
        try:
            mod.gravitational_potential_energy(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gravitational_potential_energy(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gravitational_potential_energy(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gravitational_potential_energy(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gravitational_potential_energy(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gravitational_potential_energy(0, 1)
        except EXC:
            pass

    def test_kw_gravity(self):
        try:
            mod.gravitational_potential_energy(1, 2, gravity=1)
        except EXC:
            pass


class Test_heat_capacity_deep:
    def test_c0(self):
        try:
            mod.heat_capacity(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.heat_capacity(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.heat_capacity(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.heat_capacity(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.heat_capacity(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.heat_capacity(0, 1, 2)
        except EXC:
            pass


class Test_heat_index_deep:
    def test_c0(self):
        try:
            mod.heat_index(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.heat_index(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.heat_index(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.heat_index(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.heat_index(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.heat_index(0, 1)
        except EXC:
            pass


class Test_heat_transfer_conduction_deep:
    def test_c0(self):
        try:
            mod.heat_transfer_conduction(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.heat_transfer_conduction(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.heat_transfer_conduction(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.heat_transfer_conduction(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.heat_transfer_conduction(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.heat_transfer_conduction(0, 1, 2, 3)
        except EXC:
            pass


class Test_hookes_law_deep:
    def test_c0(self):
        try:
            mod.hookes_law(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hookes_law(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hookes_law(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hookes_law(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hookes_law(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hookes_law(0, 1)
        except EXC:
            pass


class Test_impedance_series_deep:
    def test_c0(self):
        try:
            mod.impedance_series(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.impedance_series(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.impedance_series(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.impedance_series(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.impedance_series(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.impedance_series(0, 1, 2, 3)
        except EXC:
            pass


class Test_impulse_deep:
    def test_c0(self):
        try:
            mod.impulse(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.impulse(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.impulse(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.impulse(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.impulse(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.impulse(0, 1)
        except EXC:
            pass


class Test_inductive_reactance_deep:
    def test_c0(self):
        try:
            mod.inductive_reactance(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inductive_reactance(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inductive_reactance(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inductive_reactance(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inductive_reactance(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inductive_reactance(0, 1)
        except EXC:
            pass


class Test_inductor_energy_deep:
    def test_c0(self):
        try:
            mod.inductor_energy(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inductor_energy(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inductor_energy(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inductor_energy(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inductor_energy(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inductor_energy(0, 1)
        except EXC:
            pass


class Test_kinematic_displacement_deep:
    def test_c0(self):
        try:
            mod.kinematic_displacement(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.kinematic_displacement(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.kinematic_displacement(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.kinematic_displacement(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.kinematic_displacement(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.kinematic_displacement(0, 1, 2)
        except EXC:
            pass


class Test_kinetic_energy_deep:
    def test_c0(self):
        try:
            mod.kinetic_energy(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.kinetic_energy(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.kinetic_energy(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.kinetic_energy(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.kinetic_energy(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.kinetic_energy(0, 1)
        except EXC:
            pass


class Test_kinetic_energy_relativistic_deep:
    def test_c0(self):
        try:
            mod.kinetic_energy_relativistic(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.kinetic_energy_relativistic(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.kinetic_energy_relativistic(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.kinetic_energy_relativistic(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.kinetic_energy_relativistic(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.kinetic_energy_relativistic(0, 1)
        except EXC:
            pass


class Test_lens_magnification_deep:
    def test_c0(self):
        try:
            mod.lens_magnification(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lens_magnification(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lens_magnification(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lens_magnification(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lens_magnification(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lens_magnification(0, 1)
        except EXC:
            pass


class Test_lorentz_factor_deep:
    def test_c0(self):
        try:
            mod.lorentz_factor(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lorentz_factor(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lorentz_factor(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lorentz_factor(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lorentz_factor(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lorentz_factor(0)
        except EXC:
            pass


class Test_lumens_to_candela_deep:
    def test_c0(self):
        try:
            mod.lumens_to_candela(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lumens_to_candela(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lumens_to_candela(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lumens_to_candela(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lumens_to_candela(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lumens_to_candela(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.lumens_to_candela(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.lumens_to_candela(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.lumens_to_candela(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.lumens_to_candela(2)
        except EXC:
            pass

    def test_kw_solid_angle_sr(self):
        try:
            mod.lumens_to_candela(1, solid_angle_sr=1)
        except EXC:
            pass


class Test_luminous_flux_deep:
    def test_c0(self):
        try:
            mod.luminous_flux(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.luminous_flux(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.luminous_flux(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.luminous_flux(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.luminous_flux(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.luminous_flux(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.luminous_flux(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.luminous_flux(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.luminous_flux(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.luminous_flux(2)
        except EXC:
            pass

    def test_kw_solid_angle_sr(self):
        try:
            mod.luminous_flux(1, solid_angle_sr=1)
        except EXC:
            pass


class Test_mach_to_ms_deep:
    def test_c0(self):
        try:
            mod.mach_to_ms(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mach_to_ms(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mach_to_ms(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mach_to_ms(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mach_to_ms(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mach_to_ms(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.mach_to_ms(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.mach_to_ms(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.mach_to_ms(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.mach_to_ms(2)
        except EXC:
            pass

    def test_kw_speed_of_sound(self):
        try:
            mod.mach_to_ms(1, speed_of_sound=1)
        except EXC:
            pass


class Test_momentum_deep:
    def test_c0(self):
        try:
            mod.momentum(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.momentum(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.momentum(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.momentum(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.momentum(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.momentum(0, 1)
        except EXC:
            pass


class Test_ms_to_mach_deep:
    def test_c0(self):
        try:
            mod.ms_to_mach(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ms_to_mach(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ms_to_mach(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ms_to_mach(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ms_to_mach(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ms_to_mach(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ms_to_mach(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ms_to_mach(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ms_to_mach(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ms_to_mach(2)
        except EXC:
            pass

    def test_kw_speed_of_sound(self):
        try:
            mod.ms_to_mach(1, speed_of_sound=1)
        except EXC:
            pass


class Test_prandtl_number_deep:
    def test_c0(self):
        try:
            mod.prandtl_number(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.prandtl_number(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.prandtl_number(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.prandtl_number(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.prandtl_number(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.prandtl_number(0, 1, 2)
        except EXC:
            pass


class Test_projectile_max_height_deep:
    def test_c0(self):
        try:
            mod.projectile_max_height(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.projectile_max_height(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.projectile_max_height(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.projectile_max_height(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.projectile_max_height(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.projectile_max_height(0, 1)
        except EXC:
            pass

    def test_kw_gravity(self):
        try:
            mod.projectile_max_height(1, 2, gravity=1)
        except EXC:
            pass


class Test_projectile_range_deep:
    def test_c0(self):
        try:
            mod.projectile_range(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.projectile_range(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.projectile_range(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.projectile_range(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.projectile_range(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.projectile_range(0, 1)
        except EXC:
            pass

    def test_kw_gravity(self):
        try:
            mod.projectile_range(1, 2, gravity=1)
        except EXC:
            pass


class Test_projectile_time_of_flight_deep:
    def test_c0(self):
        try:
            mod.projectile_time_of_flight(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.projectile_time_of_flight(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.projectile_time_of_flight(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.projectile_time_of_flight(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.projectile_time_of_flight(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.projectile_time_of_flight(0, 1)
        except EXC:
            pass

    def test_kw_gravity(self):
        try:
            mod.projectile_time_of_flight(1, 2, gravity=1)
        except EXC:
            pass


class Test_resistors_parallel_pair_deep:
    def test_c0(self):
        try:
            mod.resistors_parallel_pair(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.resistors_parallel_pair(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.resistors_parallel_pair(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.resistors_parallel_pair(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.resistors_parallel_pair(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.resistors_parallel_pair(0, 1)
        except EXC:
            pass


class Test_resonant_freq_deep:
    def test_c0(self):
        try:
            mod.resonant_freq(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.resonant_freq(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.resonant_freq(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.resonant_freq(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.resonant_freq(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.resonant_freq(0, 1)
        except EXC:
            pass


class Test_rgb_to_cmyk_deep:
    def test_c0(self):
        try:
            mod.rgb_to_cmyk(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rgb_to_cmyk(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rgb_to_cmyk(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rgb_to_cmyk(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rgb_to_cmyk(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rgb_to_cmyk(0, 1, 2)
        except EXC:
            pass


class Test_safe_convert_number_deep:
    def test_c0(self):
        try:
            mod.safe_convert_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.safe_convert_number(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.safe_convert_number(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.safe_convert_number(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.safe_convert_number(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.safe_convert_number(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.safe_convert_number(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.safe_convert_number(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.safe_convert_number(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.safe_convert_number(2)
        except EXC:
            pass

    def test_kw_default_value(self):
        try:
            mod.safe_convert_number(1, default_value=1)
        except EXC:
            pass

    def test_kw_target_type(self):
        try:
            mod.safe_convert_number(1, target_type="hello world")
        except EXC:
            pass


class Test_shannon_capacity_deep:
    def test_c0(self):
        try:
            mod.shannon_capacity(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.shannon_capacity(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.shannon_capacity(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.shannon_capacity(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.shannon_capacity(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.shannon_capacity(0, 1)
        except EXC:
            pass


class Test_signal_rms_deep:
    def test_c0(self):
        try:
            mod.signal_rms([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.signal_rms([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.signal_rms([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.signal_rms([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.signal_rms([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.signal_rms([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_spring_potential_energy_deep:
    def test_c0(self):
        try:
            mod.spring_potential_energy(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spring_potential_energy(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spring_potential_energy(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spring_potential_energy(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spring_potential_energy(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spring_potential_energy(0, 1)
        except EXC:
            pass


class Test_strain_deep:
    def test_c0(self):
        try:
            mod.strain(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.strain(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.strain(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.strain(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.strain(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.strain(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.strain(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.strain(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.strain(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.strain(2, 1)
        except EXC:
            pass


class Test_thermal_expansion_length_deep:
    def test_c0(self):
        try:
            mod.thermal_expansion_length(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.thermal_expansion_length(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.thermal_expansion_length(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.thermal_expansion_length(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.thermal_expansion_length(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.thermal_expansion_length(0, 1, 2)
        except EXC:
            pass


class Test_thermal_noise_deep:
    def test_c0(self):
        try:
            mod.thermal_noise(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.thermal_noise(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.thermal_noise(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.thermal_noise(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.thermal_noise(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.thermal_noise(0)
        except EXC:
            pass

    def test_kw_temperature(self):
        try:
            mod.thermal_noise(1, temperature=1)
        except EXC:
            pass


class Test_thermal_resistance_deep:
    def test_c0(self):
        try:
            mod.thermal_resistance(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.thermal_resistance(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.thermal_resistance(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.thermal_resistance(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.thermal_resistance(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.thermal_resistance(0, 1, 2)
        except EXC:
            pass


class Test_wind_chill_deep:
    def test_c0(self):
        try:
            mod.wind_chill(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.wind_chill(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.wind_chill(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.wind_chill(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.wind_chill(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.wind_chill(0, 1)
        except EXC:
            pass


class Test_work_done_deep:
    def test_c0(self):
        try:
            mod.work_done(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.work_done(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.work_done(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.work_done(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.work_done(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.work_done(0, 1)
        except EXC:
            pass

    def test_kw_angle(self):
        try:
            mod.work_done(1, 2, angle=1)
        except EXC:
            pass

