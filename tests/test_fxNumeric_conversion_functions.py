"""Tests for fxNumeric.conversion_functions."""

import math

import pytest

from formulite.fxNumeric import (
    acres_to_hectares,
    btu_to_joules,
    calories_to_joules,
    candela_to_lumens,
    degrees_to_gradians,
    foot_pounds_to_newton_meters,
    gallons_to_liters,
    gradians_to_degrees,
    grams_to_troy_ounces,
    hectares_to_acres,
    hertz_to_rpm,
    horsepower_to_watts,
    joules_to_btu,
    joules_to_calories,
    joules_to_kwh,
    kilometers_to_light_years,
    kmh_to_knots,
    knots_to_kmh,
    kwh_to_joules,
    light_years_to_kilometers,
    liters_to_gallons,
    lumens_to_candela,
    mach_to_ms,
    ms_to_mach,
    newton_meters_to_foot_pounds,
    newtons_to_pounds_force,
    pounds_force_to_newtons,
    rpm_to_hertz,
    troy_ounces_to_grams,
    watts_to_horsepower,
)
from formulite.fxNumeric.arithmetic_functions import adaptive_simpson
from formulite.fxNumeric.conversion_functions import (
    adiabatic_index_pressure,
    adiabatic_temperature,
    angular_momentum,
    antenna_gain_to_effective_area,
    atmospheres_to_pascals,
    bars_to_pascals,
    bernoulli_velocity,
    biot_number,
    bmi,
    boyle_law_volume,
    bulk_modulus_pressure,
    buoyancy_force,
    bytes_to_human_readable,
    capacitance_parallel_plate,
    capacitive_reactance,
    centripetal_acceleration,
    centripetal_force,
    charles_law_volume,
    color_temperature_to_rgb,
    compton_wavelength_shift,
    coulombs_force,
    cubic_meters_per_second_to_liters_per_minute,
    current_divider,
    decibel_add,
    density_to_specific_gravity,
    dew_point,
    doppler_frequency,
    drift_velocity,
    elastic_modulus,
    elastic_potential_energy,
    electric_field_parallel_plate,
    electric_potential,
    frequency_to_wavelength,
    froude_number,
    gay_lussac_pressure,
    grashof_number,
    gravitational_potential_energy,
    h_concentration_to_ph,
    heat_capacity,
    heat_engine_efficiency,
    heat_index,
    hookes_law,
    hsl_to_rgb,
    ideal_gas_pressure,
    impedance_series_rlc,
    impulse,
    inductive_reactance,
    kinematic_displacement,
    knudsen_number,
    liters_per_minute_to_cubic_meters_per_second,
    luminous_flux,
    mach_number,
    magnetic_field_solenoid,
    magnetic_flux_density,
    magnetic_force_charge,
    moment_of_inertia_point,
    momentum,
    nernst_potential,
    noise_figure_to_temperature,
    nusselt_number,
    orbital_period,
    parallel_resistance,
    pascals_to_atmospheres,
    pascals_to_bars,
    pascals_to_psi,
    pendulum_period,
    ph_to_h_concentration,
    photon_momentum,
    planck_radiation_peak,
    power_mechanical,
    power_physics,
    prandtl_number,
    pressure_at_depth,
    projectile_max_height,
    projectile_range,
    projectile_time_of_flight,
    psi_to_pascals,
    relativistic_energy,
    resistivity_resistance,
    reynolds_number,
    rgb_to_hsl,
    rl_time_constant,
    rms_voltage,
    signal_to_noise_ratio,
    snells_law_angle,
    sound_intensity_level,
    specific_impulse,
    strouhal_number,
    terminal_velocity,
    thermal_expansion_length,
    torque,
    voltage_divider,
    wave_frequency,
    wave_speed,
    wavelength_to_frequency,
    weber_number,
    wien_displacement_peak,
    wind_chill,
    work_done,
)
from formulite.fxNumeric.number_theory_functions import digit_factorial_sum, is_fibonacci_number
from formulite.fxNumeric.statistics_functions import softplus
from formulite.fxNumeric.trigonometry_functions import gudermannian, haversine_angle


class TestDFT:

    def test_magnitude(self):
        from formulite.fxNumeric.conversion_functions import dft_magnitude

        assert round(dft_magnitude([1, 0, -1, 0], 1), 6) == 2.0

    def test_phase(self):
        from formulite.fxNumeric.conversion_functions import dft_phase

        # DC component (k=0) of constant signal should have phase ~0
        assert dft_phase([1, 1, 1, 1], 0) == pytest.approx(0.0, abs=1e-6)

class TestSignalRms:

    def test_unit_signal(self):
        from formulite.fxNumeric.conversion_functions import signal_rms

        assert signal_rms([1, -1, 1, -1]) == pytest.approx(1.0)

class TestSignalSnr:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import signal_snr_db

        assert round(signal_snr_db(100, 1), 2) == 20.0

class TestNyquist:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import nyquist_frequency

        assert nyquist_frequency(44100) == 22050.0

class TestDecibelSum:

    def test_equal_levels(self):
        from formulite.fxNumeric.conversion_functions import decibel_sum

        assert round(decibel_sum(90, 90), 2) == 93.01

class TestStress:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import stress

        assert stress(1000, 0.01) == 100000.0

class TestStrain:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import strain

        assert strain(0.005, 1.0) == 0.005

class TestBendingMoment:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import bending_moment

        assert bending_moment(100, 2.5) == 250.0


# ── fxNumeric — Trigonometry / Geometry ──────────────────────────────────

class TestTemperatureConvert:

    def test_c_to_f(self):
        from formulite.fxNumeric.conversion_functions import temperature_convert
        assert temperature_convert(100, "C", "F") == 212.0

    def test_f_to_c(self):
        from formulite.fxNumeric.conversion_functions import temperature_convert
        assert temperature_convert(32, "F", "C") == 0.0

    def test_c_to_k(self):
        from formulite.fxNumeric.conversion_functions import temperature_convert
        assert temperature_convert(0, "C", "K") == 273.15

    def test_same_unit(self):
        from formulite.fxNumeric.conversion_functions import temperature_convert
        assert temperature_convert(50, "C", "C") == 50.0

    def test_invalid_unit(self):
        from formulite.fxNumeric.conversion_functions import temperature_convert

        with pytest.raises(ValueError):
            temperature_convert(0, "C", "X")

class TestAngleConvert:

    def test_deg_to_rad(self):
        from formulite.fxNumeric.conversion_functions import angle_convert
        assert angle_convert(180, "deg", "rad") == math.pi

    def test_grad_to_deg(self):
        from formulite.fxNumeric.conversion_functions import angle_convert
        assert angle_convert(200, "grad", "deg") == 180.0

    def test_same_unit(self):
        from formulite.fxNumeric.conversion_functions import angle_convert
        assert angle_convert(90, "deg", "deg") == 90.0

class TestCoordinateDmsToDecimal:

    def test_north(self):
        from formulite.fxNumeric.conversion_functions import coordinate_dms_to_decimal
        assert round(coordinate_dms_to_decimal(40, 26, 46, "N"), 4) == 40.4461

    def test_west(self):
        from formulite.fxNumeric.conversion_functions import coordinate_dms_to_decimal
        assert round(coordinate_dms_to_decimal(79, 58, 56, "W"), 4) == -79.9822

    def test_invalid_direction(self):
        from formulite.fxNumeric.conversion_functions import coordinate_dms_to_decimal

        with pytest.raises(ValueError):
            coordinate_dms_to_decimal(40, 26, 46, "X")

class TestCoordinateDecimalToDms:

    def test_positive_lat(self):
        from formulite.fxNumeric.conversion_functions import coordinate_decimal_to_dms

        deg, mins, secs, direction = coordinate_decimal_to_dms(40.4461)
        assert deg == 40
        assert mins == 26
        assert direction == "N"

    def test_negative_lon(self):
        from formulite.fxNumeric.conversion_functions import coordinate_decimal_to_dms

        deg, mins, secs, direction = coordinate_decimal_to_dms(-79.9822, is_longitude=True)
        assert deg == 79
        assert direction == "W"

    def test_out_of_range(self):
        from formulite.fxNumeric.conversion_functions import coordinate_decimal_to_dms

        with pytest.raises(ValueError):
            coordinate_decimal_to_dms(100, is_longitude=False)


# ── Date Evaluations ────────────────────────────────────────────

class TestCoulombForce:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import coulomb_force

        assert round(coulomb_force(1e-6, 2e-6, 0.05), 2) == 7.19

    def test_zero_distance(self):
        from formulite.fxNumeric.conversion_functions import coulomb_force

        with pytest.raises(ValueError):
            coulomb_force(1e-6, 2e-6, 0)

class TestSchwarzschildRadius:

    def test_sun(self):
        from formulite.fxNumeric.conversion_functions import schwarzschild_radius

        assert round(schwarzschild_radius(1.989e30), 0) == 2954.0

    def test_negative_mass(self):
        from formulite.fxNumeric.conversion_functions import schwarzschild_radius

        with pytest.raises(ValueError):
            schwarzschild_radius(-1)

class TestDopplerShift:

    def test_receding(self):
        from formulite.fxNumeric.conversion_functions import doppler_shift

        assert round(doppler_shift(440, 30), 2) == 404.61

    def test_approaching(self):
        from formulite.fxNumeric.conversion_functions import doppler_shift

        result = doppler_shift(440, -30)

        assert result > 440  # frequency increases

class TestStefanBoltzmannPower:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import stefan_boltzmann_power

        assert round(stefan_boltzmann_power(1.0, 1.0, 300), 1) == 459.3

    def test_invalid_emissivity(self):
        from formulite.fxNumeric.conversion_functions import stefan_boltzmann_power

        with pytest.raises(ValueError):
            stefan_boltzmann_power(1.5, 1.0, 300)

class TestSpringPotentialEnergy:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import spring_potential_energy

        assert spring_potential_energy(200, 0.1) == 1.0

    def test_zero_displacement(self):
        from formulite.fxNumeric.conversion_functions import spring_potential_energy

        assert spring_potential_energy(200, 0) == 0.0

class TestLorentzFactor:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import lorentz_factor

        assert round(lorentz_factor(2.0e8), 4) == 1.3424

    def test_zero_velocity(self):
        from formulite.fxNumeric.conversion_functions import lorentz_factor

        assert lorentz_factor(0) == 1.0

    def test_exceeds_c(self):
        from formulite.fxNumeric.conversion_functions import lorentz_factor

        with pytest.raises(ValueError):
            lorentz_factor(3e8)

class TestMagneticForceOnWire:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import magnetic_force_on_wire

        assert round(magnetic_force_on_wire(5, 0.2, 0.3), 1) == 0.3

    def test_type_error(self):
        from formulite.fxNumeric.conversion_functions import magnetic_force_on_wire

        with pytest.raises(TypeError):
            magnetic_force_on_wire("a", 0.2, 0.3)

class TestInductorEnergy:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import inductor_energy

        assert inductor_energy(0.01, 5) == 0.125

    def test_negative_inductance(self):
        from formulite.fxNumeric.conversion_functions import inductor_energy

        with pytest.raises(ValueError):
            inductor_energy(-0.01, 5)


# ── Trigonometry / Geometry ──────────────────────────────────────────

class TestDragForce:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import drag_force

        assert drag_force(0.47, 1.225, 10, 0.01) == pytest.approx(0.287875)

    def test_zero_velocity(self):
        from formulite.fxNumeric.conversion_functions import drag_force

        assert drag_force(0.47, 1.225, 0, 0.01) == 0.0

class TestKineticEnergyRelativistic:

    def test_zero_velocity(self):
        from formulite.fxNumeric.conversion_functions import kinetic_energy_relativistic

        assert kinetic_energy_relativistic(1.0, 0) == pytest.approx(0.0)

    def test_exceeds_c(self):
        from formulite.fxNumeric.conversion_functions import kinetic_energy_relativistic

        with pytest.raises(ValueError):
            kinetic_energy_relativistic(1.0, 3e8)

class TestElectricFieldPoint:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import electric_field_point

        assert round(electric_field_point(1e-6, 0.1), 2) == 898755.18

    def test_zero_distance(self):
        from formulite.fxNumeric.conversion_functions import electric_field_point

        with pytest.raises(ValueError):
            electric_field_point(1e-6, 0)

class TestMagneticFlux:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import magnetic_flux

        assert magnetic_flux(0.5, 0.02) == pytest.approx(0.01)

    def test_type_error(self):
        from formulite.fxNumeric.conversion_functions import magnetic_flux

        with pytest.raises(TypeError):
            magnetic_flux("a", 0.02)

class TestResistorsParallelPair:

    def test_equal(self):
        from formulite.fxNumeric.conversion_functions import resistors_parallel_pair

        assert resistors_parallel_pair(100, 100) == 50.0

    def test_negative(self):
        from formulite.fxNumeric.conversion_functions import resistors_parallel_pair

        with pytest.raises(ValueError):
            resistors_parallel_pair(-100, 100)

class TestRcTimeConstant:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import rc_time_constant

        assert rc_time_constant(1000, 0.001) == 1.0

    def test_zero_r(self):
        from formulite.fxNumeric.conversion_functions import rc_time_constant

        with pytest.raises(ValueError):
            rc_time_constant(0, 0.001)

class TestThermalResistance:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import thermal_resistance

        assert thermal_resistance(0.1, 200, 0.01) == 0.05

    def test_zero_conductivity(self):
        from formulite.fxNumeric.conversion_functions import thermal_resistance

        with pytest.raises(ValueError):
            thermal_resistance(0.1, 0, 0.01)

class TestHeatTransferConduction:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import heat_transfer_conduction

        assert heat_transfer_conduction(200, 0.01, 50, 0.1) == 1000.0

    def test_zero_thickness(self):
        from formulite.fxNumeric.conversion_functions import heat_transfer_conduction

        with pytest.raises(ValueError):
            heat_transfer_conduction(200, 0.01, 50, 0)


# ── Trigonometry / Geometry ──────────────────────────────────────────

class TestPendulumPeriod:

    def test_basic(self):
        assert pendulum_period(1.0) == pytest.approx(2.006409, rel=1e-4)

    def test_negative_length_raises(self):
        with pytest.raises(ValueError):
            pendulum_period(-1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            pendulum_period("1")

class TestProjectileRange:

    def test_basic(self):
        assert projectile_range(50, math.pi / 4) == pytest.approx(254.842, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            projectile_range("50", 45)

class TestProjectileMaxHeight:

    def test_basic(self):
        assert projectile_max_height(50, math.pi / 4) == pytest.approx(63.7105, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            projectile_max_height("50", 45)

class TestProjectileTimeOfFlight:

    def test_basic(self):
        assert projectile_time_of_flight(50, math.pi / 4) == pytest.approx(7.20802, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            projectile_time_of_flight("50", 45)

class TestPressureAtDepth:

    def test_basic(self):
        assert pressure_at_depth(1000, 10) == pytest.approx(199_391.5, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            pressure_at_depth("1000", 10)

class TestBernoulliVelocity:

    def test_basic(self):
        assert bernoulli_velocity(5000, 1.225) == pytest.approx(90.3508, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            bernoulli_velocity("5000", 1.225)

class TestWorkDone:

    def test_basic(self):
        assert work_done(100, 5, math.radians(30)) == pytest.approx(433.0127, rel=1e-3)

    def test_zero_angle(self):
        assert work_done(100, 5, 0) == pytest.approx(500.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            work_done("100", 5, 30)

class TestGravitationalPotentialEnergy:

    def test_basic(self):
        assert gravitational_potential_energy(10, 20) == pytest.approx(1962.0, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            gravitational_potential_energy("10", 20)


# ── Trigonometry / Geometry ──────────────────────────────────────────────────

class TestCentripetalAcceleration:

    def test_basic(self):
        assert centripetal_acceleration(10, 5) == pytest.approx(20.0)

    def test_zero_radius_raises(self):
        with pytest.raises(ValueError):
            centripetal_acceleration(10, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            centripetal_acceleration("10", 5)

class TestOrbitalPeriod:

    def test_iss(self):
        # ISS orbit ~ 408 km altitude, period ~ 5555 s
        result = orbital_period(6.371e6 + 408_000, 5.972e24)
        assert result == pytest.approx(5554.76, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            orbital_period("6e6", 5.972e24)

class TestPowerMechanical:

    def test_basic(self):
        assert power_mechanical(1000, 5) == pytest.approx(200.0)

    def test_zero_time_raises(self):
        with pytest.raises(ValueError):
            power_mechanical(1000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            power_mechanical("1000", 5)

class TestAngularMomentum:

    def test_basic(self):
        assert angular_momentum(2, 3, 4) == pytest.approx(24.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            angular_momentum("2", 3, 4)

class TestMomentOfInertiaPoint:

    def test_basic(self):
        assert moment_of_inertia_point(5, 3) == pytest.approx(45.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            moment_of_inertia_point("5", 3)

class TestSoundIntensityLevel:

    def test_basic(self):
        assert sound_intensity_level(1e-6) == pytest.approx(60.0)

    def test_custom_ref(self):
        assert sound_intensity_level(1.0, 1.0) == pytest.approx(0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            sound_intensity_level("1e-6")

class TestBulkModulusPressure:

    def test_basic(self):
        assert bulk_modulus_pressure(2.2e9, -0.001, 1.0) == pytest.approx(2_200_000.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            bulk_modulus_pressure("2.2e9", -0.001, 1.0)

class TestCentripetalForce:

    def test_basic(self):
        assert centripetal_force(2, 10, 5) == pytest.approx(40.0)

    def test_zero_radius_raises(self):
        with pytest.raises(ValueError):
            centripetal_force(2, 10, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            centripetal_force("2", 10, 5)


# ── Trigonometry / Geometry ──────────────────────────────────────────────────

class TestTorque:

    def test_perpendicular(self):
        assert torque(100, 0.5) == pytest.approx(50.0)

    def test_zero_force(self):
        assert torque(0, 0.5) == pytest.approx(0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            torque("100", 0.5)

class TestElasticPotentialEnergy:

    def test_basic(self):
        assert elastic_potential_energy(200, 0.1) == pytest.approx(1.0)

    def test_zero_disp(self):
        assert elastic_potential_energy(200, 0) == pytest.approx(0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            elastic_potential_energy("200", 0.1)

class TestElectricPotential:

    def test_basic(self):
        assert electric_potential(1e-6, 0.1) == pytest.approx(89875.52, rel=1e-4)

    def test_zero_dist_raises(self):
        with pytest.raises(ValueError):
            electric_potential(1e-6, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            electric_potential("1e-6", 0.1)

class TestCapacitanceParallelPlate:

    def test_basic(self):
        assert capacitance_parallel_plate(0.01, 0.001) == pytest.approx(8.854e-11, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            capacitance_parallel_plate("0.01", 0.001)

class TestMagneticFieldSolenoid:

    def test_basic(self):
        assert magnetic_field_solenoid(1000, 2, 0.5) == pytest.approx(0.005027, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            magnetic_field_solenoid("1000", 2, 0.5)

class TestSnellsLawAngle:

    def test_basic(self):
        assert snells_law_angle(1.0, 1.5, math.pi / 4) == pytest.approx(0.49088, rel=1e-3)

    def test_total_reflection_raises(self):
        with pytest.raises(ValueError):
            snells_law_angle(1.5, 1.0, math.pi / 2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            snells_law_angle("1.0", 1.5, math.pi / 4)

class TestDriftVelocity:

    def test_basic(self):
        assert drift_velocity(10, 8.5e28, 1.6e-19, 1e-6) == pytest.approx(0.000735, rel=1e-2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            drift_velocity("10", 8.5e28, 1.6e-19, 1e-6)

class TestKinematicDisplacement:

    def test_basic(self):
        assert kinematic_displacement(10, 5, 2) == pytest.approx(75.0)

    def test_zero_time(self):
        assert kinematic_displacement(10, 0, 2) == pytest.approx(0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            kinematic_displacement("10", 5, 2)


# ── Trigonometry / Geometry ──────────────────────────────────────────────────

class TestHeatCapacity:

    def test_basic(self):
        assert heat_capacity(2, 4186, 10) == pytest.approx(83720.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            heat_capacity("2", 4186, 10)

class TestAdiabaticIndexPressure:

    def test_basic(self):
        assert adiabatic_index_pressure(100_000, 1.0, 0.5, 1.4) == pytest.approx(263901.58, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            adiabatic_index_pressure("100000", 1.0, 0.5, 1.4)

class TestMagneticForceCharge:

    def test_basic(self):
        assert magnetic_force_charge(1.6e-19, 1e6, 0.5) == pytest.approx(8e-14, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            magnetic_force_charge("1.6e-19", 1e6, 0.5)

class TestElectricFieldParallelPlate:

    def test_basic(self):
        assert electric_field_parallel_plate(1000, 0.01) == pytest.approx(100_000.0)

    def test_zero_distance_raises(self):
        with pytest.raises(ValueError):
            electric_field_parallel_plate(1000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            electric_field_parallel_plate("1000", 0.01)

class TestResistivityResistance:

    def test_basic(self):
        assert resistivity_resistance(1.68e-8, 100, 1e-6) == pytest.approx(1.68, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            resistivity_resistance("1.68e-8", 100, 1e-6)

class TestWaveFrequency:

    def test_basic(self):
        assert wave_frequency(340, 0.5) == pytest.approx(680.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            wave_frequency("340", 0.5)

class TestPhotonMomentum:

    def test_basic(self):
        assert photon_momentum(500e-9) == pytest.approx(1.3252e-27, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            photon_momentum("500e-9")

class TestRelativisticEnergy:

    def test_at_rest(self):
        C = 299792458.0
        assert relativistic_energy(1, 0) == pytest.approx(C ** 2, rel=1e-6)

    def test_superluminal_raises(self):
        with pytest.raises(ValueError):
            relativistic_energy(1, 3e8)

    def test_type_error(self):
        with pytest.raises(TypeError):
            relativistic_energy("1", 0)


# ── Trigonometry / Geometry ──────────────────────────────────────────────────

class TestCoulombsForce:
    def test_basic(self):
        assert coulombs_force(1e-6, 2e-6, 0.05) == pytest.approx(7.19, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            coulombs_force("a", 1, 1)

    def test_zero_distance(self):
        with pytest.raises(ValueError):
            coulombs_force(1, 1, 0)

class TestRlTimeConstant:
    def test_basic(self):
        assert rl_time_constant(0.5, 100) == pytest.approx(0.005)

    def test_type_error(self):
        with pytest.raises(TypeError):
            rl_time_constant("a", 1)

    def test_negative(self):
        with pytest.raises(ValueError):
            rl_time_constant(-1, 100)

class TestDopplerFrequency:
    def test_source_moving(self):
        assert doppler_frequency(440, 343, 0, 30) == pytest.approx(482.17, rel=1e-3)

    def test_observer_moving(self):
        result = doppler_frequency(440, 343, 30, 0)
        assert result == pytest.approx(440 * 373 / 343, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            doppler_frequency("a", 343)

    def test_source_speed_exceeds_wave(self):
        with pytest.raises(ValueError):
            doppler_frequency(440, 343, 0, 343)

class TestThermalExpansionLength:
    def test_basic(self):
        assert thermal_expansion_length(2.0, 1.2e-5, 100) == pytest.approx(0.0024, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            thermal_expansion_length("a", 1, 1)

    def test_negative_length(self):
        with pytest.raises(ValueError):
            thermal_expansion_length(-1, 1e-5, 100)

class TestWienDisplacementPeak:
    def test_sun(self):
        assert wien_displacement_peak(5778) == pytest.approx(5.015e-7, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            wien_displacement_peak("a")

    def test_zero_temp(self):
        with pytest.raises(ValueError):
            wien_displacement_peak(0)

class TestComptonWavelengthShift:
    def test_max_shift(self):
        assert compton_wavelength_shift(math.pi) == pytest.approx(4.853e-12, rel=1e-3)

    def test_zero_angle(self):
        assert compton_wavelength_shift(0) == pytest.approx(0.0, abs=1e-20)

    def test_type_error(self):
        with pytest.raises(TypeError):
            compton_wavelength_shift("a")

class TestParallelResistance:
    def test_basic(self):
        assert parallel_resistance(100, 200) == pytest.approx(66.6667, rel=1e-4)

    def test_equal(self):
        assert parallel_resistance(100, 100) == pytest.approx(50.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            parallel_resistance("a", 1)

    def test_negative(self):
        with pytest.raises(ValueError):
            parallel_resistance(-1, 100)

class TestVoltageDivider:
    def test_basic(self):
        assert voltage_divider(12, 8000, 4000) == pytest.approx(4.0)

    def test_equal_resistors(self):
        assert voltage_divider(10, 100, 100) == pytest.approx(5.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            voltage_divider("a", 1, 1)

    def test_negative_r(self):
        with pytest.raises(ValueError):
            voltage_divider(12, -1, 100)


# ---------------------------------------------------------------------------
# Trigonometry / Geometry
# ---------------------------------------------------------------------------

class TestSpecificImpulse:
    def test_basic(self):
        assert specific_impulse(2_000_000, 700) == pytest.approx(291.35, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            specific_impulse("a", 1)

    def test_zero_thrust(self):
        with pytest.raises(ValueError):
            specific_impulse(0, 100)

class TestCapacitiveReactance:
    def test_basic(self):
        assert capacitive_reactance(60, 10e-6) == pytest.approx(265.26, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            capacitive_reactance("a", 1)

    def test_zero_freq(self):
        with pytest.raises(ValueError):
            capacitive_reactance(0, 1e-6)

class TestInductiveReactance:
    def test_basic(self):
        assert inductive_reactance(60, 0.5) == pytest.approx(188.4956, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            inductive_reactance("a", 1)

    def test_zero_inductance(self):
        with pytest.raises(ValueError):
            inductive_reactance(60, 0)

class TestMagneticFluxDensity:
    def test_basic(self):
        assert magnetic_flux_density(1.2566370614e-6, 10, 0.05) == pytest.approx(4e-05, rel=1e-3)

    def test_type_error(self):
        with pytest.raises(TypeError):
            magnetic_flux_density("a", 1, 1)

    def test_zero_distance(self):
        with pytest.raises(ValueError):
            magnetic_flux_density(1e-6, 10, 0)

class TestCurrentDivider:
    def test_basic(self):
        result = current_divider(10, 200, 100)
        assert result == pytest.approx(10 * 100 / 300, rel=1e-4)

    def test_equal_resistors(self):
        assert current_divider(10, 100, 100) == pytest.approx(5.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            current_divider("a", 1, 1)

    def test_negative_r(self):
        with pytest.raises(ValueError):
            current_divider(10, -1, 100)

class TestBuoyancyForce:
    def test_basic(self):
        assert buoyancy_force(1000, 0.01) == pytest.approx(98.0665, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            buoyancy_force("a", 1)

    def test_zero_volume(self):
        with pytest.raises(ValueError):
            buoyancy_force(1000, 0)

class TestGrashofNumber:
    def test_basic(self):
        assert grashof_number(9.81, 3.41e-3, 20, 0.5, 1.5e-5) == pytest.approx(
            371690000.0, rel=1e-3
        )

    def test_type_error(self):
        with pytest.raises(TypeError):
            grashof_number("a", 1, 1, 1, 1)

    def test_zero_viscosity(self):
        with pytest.raises(ValueError):
            grashof_number(9.81, 1e-3, 10, 1, 0)

class TestBoyleLawVolume:
    def test_basic(self):
        assert boyle_law_volume(2, 10, 4) == pytest.approx(5.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            boyle_law_volume("a", 1, 1)

    def test_zero_pressure(self):
        with pytest.raises(ValueError):
            boyle_law_volume(2, 10, 0)

class TestCharlesLawVolume:
    def test_basic(self):
        assert charles_law_volume(10, 300, 600) == pytest.approx(20.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            charles_law_volume("a", 1, 1)

    def test_zero_temp(self):
        with pytest.raises(ValueError):
            charles_law_volume(10, 0, 300)


# ---------------------------------------------------------------------------
# Trigonometry / Geometry
# ---------------------------------------------------------------------------

class TestGayLussacPressure:
    def test_basic(self):
        assert gay_lussac_pressure(100_000, 300, 600) == pytest.approx(200_000.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            gay_lussac_pressure("a", 1, 1)

    def test_zero_temp(self):
        with pytest.raises(ValueError):
            gay_lussac_pressure(100, 0, 300)

class TestRmsVoltage:
    def test_basic(self):
        assert rms_voltage(325) == pytest.approx(229.81, rel=1e-3)

    def test_zero(self):
        assert rms_voltage(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            rms_voltage("a")

    def test_negative(self):
        with pytest.raises(ValueError):
            rms_voltage(-1)

class TestImpedanceSeriesRlc:
    def test_basic(self):
        assert impedance_series_rlc(100, 150, 50) == pytest.approx(
            141.421356, rel=1e-4
        )

    def test_resonance(self):
        # At resonance X_L == X_C → Z = R
        assert impedance_series_rlc(100, 50, 50) == pytest.approx(100.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            impedance_series_rlc("a", 1, 1)

    def test_negative(self):
        with pytest.raises(ValueError):
            impedance_series_rlc(-1, 0, 0)

class TestNernstPotential:
    def test_sodium(self):
        # Na+ at 37°C: ~66.6 mV
        result = nernst_potential(1, 145, 12) * 1000
        assert result == pytest.approx(66.6, rel=1e-2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            nernst_potential(1.5, 145, 12)

    def test_zero_z(self):
        with pytest.raises(ValueError):
            nernst_potential(0, 145, 12)

class TestHeatEngineEfficiency:
    def test_basic(self):
        assert heat_engine_efficiency(600, 300) == pytest.approx(0.5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            heat_engine_efficiency("a", 1)

    def test_cold_ge_hot(self):
        with pytest.raises(ValueError):
            heat_engine_efficiency(300, 300)

class TestBiotNumber:
    def test_basic(self):
        assert biot_number(50, 0.01, 200) == pytest.approx(0.0025)

    def test_type_error(self):
        with pytest.raises(TypeError):
            biot_number("a", 1, 1)

    def test_zero_k(self):
        with pytest.raises(ValueError):
            biot_number(50, 0.01, 0)

class TestPlanckRadiationPeak:
    def test_sun(self):
        assert planck_radiation_peak(5778) == pytest.approx(
            82850947237685.0, rel=1e-3
        )

    def test_type_error(self):
        with pytest.raises(TypeError):
            planck_radiation_peak("a")

    def test_zero_temp(self):
        with pytest.raises(ValueError):
            planck_radiation_peak(0)

class TestAdiabaticTemperature:
    def test_compression(self):
        assert adiabatic_temperature(300, 1, 0.5) == pytest.approx(395.85, rel=1e-3)

    def test_expansion(self):
        result = adiabatic_temperature(300, 1, 2)
        assert result < 300  # expansion cools

    def test_type_error(self):
        with pytest.raises(TypeError):
            adiabatic_temperature("a", 1, 1)

    def test_gamma_le_1(self):
        with pytest.raises(ValueError):
            adiabatic_temperature(300, 1, 0.5, 1)


# ---------------------------------------------------------------------------
# Trigonometry / Geometry
# ---------------------------------------------------------------------------

class TestAdaptiveSimpson:
    def test_sine_integral(self):
        result = adaptive_simpson(math.sin, 0, math.pi)
        assert result == pytest.approx(2.0, abs=1e-8)

    def test_polynomial(self):
        f = lambda x: x**2
        result = adaptive_simpson(f, 0, 3)
        assert result == pytest.approx(9.0, abs=1e-8)

    def test_type_error(self):
        with pytest.raises(TypeError):
            adaptive_simpson("not_a_func", 0, 1)


# ---------------------------------------------------------------------------
# fxNumeric — conversion_functions.py
# ---------------------------------------------------------------------------

from formulite.fxNumeric.conversion_functions import (
    luminous_flux,
    noise_figure_to_temperature,
    antenna_gain_to_effective_area,
    radiation_dose_convert,
)

class TestLuminousFlux:
    def test_full_sphere(self):
        result = luminous_flux(100)
        assert result == pytest.approx(100 * 4 * math.pi, rel=1e-6)

    def test_type_error(self):
        with pytest.raises(TypeError):
            luminous_flux("bright")

    def test_negative(self):
        with pytest.raises(ValueError):
            luminous_flux(-1)

class TestNoiseFigureToTemperature:
    def test_3db(self):
        result = noise_figure_to_temperature(3.0)
        assert result == pytest.approx(290 * (10**(3/10) - 1), rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            noise_figure_to_temperature("loud")

class TestAntennaGainToEffectiveArea:
    def test_basic(self):
        result = antenna_gain_to_effective_area(10, 1e9)
        assert isinstance(result, float)
        assert result > 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            antenna_gain_to_effective_area("big", 1e9)

    def test_zero_frequency(self):
        with pytest.raises(ValueError):
            antenna_gain_to_effective_area(10, 0)

class TestColorTemperatureToRgb:

    def test_daylight(self):
        r, g, b = color_temperature_to_rgb(6500)
        assert r == 255
        assert 250 <= g <= 255
        assert 245 <= b <= 255

    def test_out_of_range(self):

        with pytest.raises(ValueError):
            color_temperature_to_rgb(500)

class TestRgbHslConversion:

    def test_red(self):
        h, s, l = rgb_to_hsl(255, 0, 0)
        assert h == 0.0
        assert s == 1.0
        assert l == 0.5

    def test_roundtrip(self):
        h, s, l = rgb_to_hsl(100, 150, 200)
        r, g, b = hsl_to_rgb(h, s, l)
        assert abs(r - 100) <= 1
        assert abs(g - 150) <= 1
        assert abs(b - 200) <= 1

class TestSignalToNoiseRatio:

    def test_basic(self):
        assert round(signal_to_noise_ratio(100, 1), 2) == 20.0

    def test_negative_power(self):

        with pytest.raises(ValueError):
            signal_to_noise_ratio(-1, 1)


# ── fxNumeric ── trigonometry_functions ──────────────────────────────────

class TestWavelengthFrequency:

    def test_wavelength_to_freq(self):
        f = wavelength_to_frequency(0.5e-6)
        assert f == pytest.approx(599584916000000.0, rel=1e-6)

    def test_freq_to_wavelength(self):
        w = frequency_to_wavelength(100e6)
        assert round(w, 4) == 2.9979

    def test_roundtrip(self):
        f = wavelength_to_frequency(1.0)
        w = frequency_to_wavelength(f)
        assert abs(w - 1.0) < 1e-10

    def test_negative_wavelength(self):

        with pytest.raises(ValueError):
            wavelength_to_frequency(-1)

    def test_negative_frequency(self):

        with pytest.raises(ValueError):
            frequency_to_wavelength(-1)

class TestColourSpaceConversions:
    """RGB ↔ HSV, RGB ↔ CMYK, luminance, contrast."""

    def test_rgb_to_hsv_red(self):
        from formulite.fxNumeric.conversion_functions import rgb_to_hsv

        h, s, v = rgb_to_hsv(255, 0, 0)
        assert h == 0.0
        assert s == 1.0
        assert v == 1.0

    def test_rgb_to_hsv_type_error(self):
        from formulite.fxNumeric.conversion_functions import rgb_to_hsv

        with pytest.raises(TypeError):
            rgb_to_hsv(255.0, 0, 0)

    def test_hsv_to_rgb_red(self):
        from formulite.fxNumeric.conversion_functions import hsv_to_rgb

        assert hsv_to_rgb(0.0, 1.0, 1.0) == (255, 0, 0)

    def test_rgb_hsv_roundtrip(self):
        from formulite.fxNumeric.conversion_functions import rgb_to_hsv, hsv_to_rgb

        h, s, v = rgb_to_hsv(100, 150, 200)
        r, g, b = hsv_to_rgb(h, s, v)
        assert abs(r - 100) <= 1
        assert abs(g - 150) <= 1
        assert abs(b - 200) <= 1

    def test_rgb_to_cmyk_red(self):
        from formulite.fxNumeric.conversion_functions import rgb_to_cmyk

        assert rgb_to_cmyk(255, 0, 0) == (0.0, 1.0, 1.0, 0.0)

    def test_rgb_to_cmyk_black(self):
        from formulite.fxNumeric.conversion_functions import rgb_to_cmyk

        assert rgb_to_cmyk(0, 0, 0) == (0.0, 0.0, 0.0, 1.0)

    def test_cmyk_to_rgb_red(self):
        from formulite.fxNumeric.conversion_functions import cmyk_to_rgb

        assert cmyk_to_rgb(0.0, 1.0, 1.0, 0.0) == (255, 0, 0)

    def test_rgb_cmyk_roundtrip(self):
        from formulite.fxNumeric.conversion_functions import rgb_to_cmyk, cmyk_to_rgb

        c, m, y, k = rgb_to_cmyk(128, 64, 32)
        r, g, b = cmyk_to_rgb(c, m, y, k)
        assert abs(r - 128) <= 1
        assert abs(g - 64) <= 1
        assert abs(b - 32) <= 1

    def test_color_luminance_white(self):
        from formulite.fxNumeric.conversion_functions import color_luminance

        assert round(color_luminance(255, 255, 255), 1) == 1.0

    def test_color_luminance_black(self):
        from formulite.fxNumeric.conversion_functions import color_luminance

        assert color_luminance(0, 0, 0) == 0.0

    def test_color_contrast_ratio_bw(self):
        from formulite.fxNumeric.conversion_functions import color_contrast_ratio

        assert color_contrast_ratio(0, 0, 0, 255, 255, 255) == 21.0

    def test_color_contrast_ratio_same(self):
        from formulite.fxNumeric.conversion_functions import color_contrast_ratio

        assert color_contrast_ratio(128, 128, 128, 128, 128, 128) == 1.0


# =====================================================================
# fxNumeric — statistics_functions (ML activations)
# =====================================================================

class TestJoulesToCalories:
    def test_basic(self):
        assert round(joules_to_calories(4184), 2) == 1000.0

    def test_zero(self):
        assert joules_to_calories(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            joules_to_calories("abc")

class TestCaloriesToJoules:
    def test_basic(self):
        assert calories_to_joules(1000) == 4184.0

    def test_zero(self):
        assert calories_to_joules(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            calories_to_joules("abc")

class TestKwhToJoules:
    def test_basic(self):
        assert kwh_to_joules(1) == 3600000.0

    def test_zero(self):
        assert kwh_to_joules(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            kwh_to_joules("abc")

class TestJoulesToKwh:
    def test_basic(self):
        assert round(joules_to_kwh(3600000), 4) == 1.0

    def test_zero(self):
        assert joules_to_kwh(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            joules_to_kwh("abc")

class TestBtuToJoules:
    def test_basic(self):
        assert round(btu_to_joules(1), 2) == 1055.06

    def test_zero(self):
        assert btu_to_joules(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            btu_to_joules("abc")

class TestJoulesToBtu:
    def test_basic(self):
        assert round(joules_to_btu(1055.06), 4) == 1.0

    def test_zero(self):
        assert joules_to_btu(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            joules_to_btu("abc")

class TestWattsToHorsepower:
    def test_basic(self):
        assert round(watts_to_horsepower(745.7), 4) == 1.0

    def test_zero(self):
        assert watts_to_horsepower(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            watts_to_horsepower("abc")

class TestHorsepowerToWatts:
    def test_basic(self):
        assert round(horsepower_to_watts(1), 2) == 745.7

    def test_zero(self):
        assert horsepower_to_watts(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            horsepower_to_watts("abc")

class TestGradiansToDegrees:
    def test_basic(self):
        assert gradians_to_degrees(100) == 90.0

    def test_full_circle(self):
        assert gradians_to_degrees(400) == 360.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            gradians_to_degrees("abc")

class TestDegreesToGradians:
    def test_basic(self):
        assert round(degrees_to_gradians(90), 4) == 100.0

    def test_full_circle(self):
        assert round(degrees_to_gradians(360), 4) == 400.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            degrees_to_gradians("abc")

class TestKnotsToKmh:
    def test_basic(self):
        assert round(knots_to_kmh(1), 4) == 1.852

    def test_zero(self):
        assert knots_to_kmh(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            knots_to_kmh("abc")

class TestKmhToKnots:
    def test_basic(self):
        assert round(kmh_to_knots(1.852), 4) == 1.0

    def test_zero(self):
        assert kmh_to_knots(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            kmh_to_knots("abc")

class TestMachToMs:
    def test_basic(self):
        assert mach_to_ms(1) == 343.0

    def test_custom_speed(self):
        assert mach_to_ms(2, 300) == 600.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            mach_to_ms("abc")

class TestMsToMach:
    def test_basic(self):
        assert ms_to_mach(343) == 1.0

    def test_zero_speed_of_sound(self):
        with pytest.raises(ValueError):
            ms_to_mach(100, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            ms_to_mach("abc")

class TestNewtonMetersToFootPounds:
    def test_basic(self):
        assert round(newton_meters_to_foot_pounds(1), 4) == 0.7376

    def test_zero(self):
        assert newton_meters_to_foot_pounds(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            newton_meters_to_foot_pounds("abc")

class TestFootPoundsToNewtonMeters:
    def test_basic(self):
        assert round(foot_pounds_to_newton_meters(0.7376), 4) == 1.0001

    def test_zero(self):
        assert foot_pounds_to_newton_meters(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            foot_pounds_to_newton_meters("abc")

class TestHertzToRpm:
    def test_basic(self):
        assert hertz_to_rpm(1) == 60.0

    def test_zero(self):
        assert hertz_to_rpm(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            hertz_to_rpm("abc")

class TestRpmToHertz:
    def test_basic(self):
        assert round(rpm_to_hertz(60), 4) == 1.0

    def test_zero(self):
        assert rpm_to_hertz(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            rpm_to_hertz("abc")

class TestCandelaToLumens:
    def test_basic(self):
        assert round(candela_to_lumens(1), 2) == 12.57

    def test_custom_angle(self):
        assert candela_to_lumens(10, 1.0) == 10.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            candela_to_lumens("abc")

class TestLumensToCandela:
    def test_basic(self):
        assert round(lumens_to_candela(12.57), 4) == 1.0003

    def test_zero_angle(self):
        with pytest.raises(ValueError):
            lumens_to_candela(100, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            lumens_to_candela("abc")

class TestAcresToHectares:
    def test_basic(self):
        assert round(acres_to_hectares(1), 4) == 0.4047

    def test_zero(self):
        assert acres_to_hectares(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            acres_to_hectares("abc")

class TestHectaresToAcres:
    def test_basic(self):
        assert round(hectares_to_acres(1), 4) == 2.4711

    def test_zero(self):
        assert hectares_to_acres(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            hectares_to_acres("abc")

class TestGallonsToLiters:
    def test_us(self):
        assert round(gallons_to_liters(1), 4) == 3.7854

    def test_imperial(self):
        assert round(gallons_to_liters(1, us=False), 4) == 4.5461

    def test_type_error(self):
        with pytest.raises(TypeError):
            gallons_to_liters("abc")

class TestLitersToGallons:
    def test_us(self):
        assert round(liters_to_gallons(3.78541), 4) == 1.0

    def test_imperial(self):
        assert round(liters_to_gallons(4.54609, us=False), 4) == 1.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            liters_to_gallons("abc")

class TestNewtonsToPoundsForce:
    def test_basic(self):
        assert round(newtons_to_pounds_force(4.44822), 4) == 1.0

    def test_zero(self):
        assert newtons_to_pounds_force(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            newtons_to_pounds_force("abc")

class TestPoundsForceToNewtons:
    def test_basic(self):
        assert round(pounds_force_to_newtons(1), 4) == 4.4482

    def test_zero(self):
        assert pounds_force_to_newtons(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            pounds_force_to_newtons("abc")

class TestTroyOuncesToGrams:
    def test_basic(self):
        assert round(troy_ounces_to_grams(1), 4) == 31.1035

    def test_zero(self):
        assert troy_ounces_to_grams(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            troy_ounces_to_grams("abc")

class TestGramsToTroyOunces:
    def test_basic(self):
        assert round(grams_to_troy_ounces(31.1035), 4) == 1.0

    def test_zero(self):
        assert grams_to_troy_ounces(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            grams_to_troy_ounces("abc")

class TestLightYearsToKilometers:
    def test_basic(self):
        assert light_years_to_kilometers(1) == 9460730472580.8

    def test_zero(self):
        assert light_years_to_kilometers(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            light_years_to_kilometers("abc")

class TestKilometersToLightYears:
    def test_basic(self):
        assert round(kilometers_to_light_years(9460730472580.8), 4) == 1.0

    def test_zero(self):
        assert kilometers_to_light_years(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            kilometers_to_light_years("abc")

class TestPressureConversions:
    """Tests for pressure conversion functions."""

    def test_pa_to_atm(self):
        assert pascals_to_atmospheres(101325) == pytest.approx(1.0, rel=1e-9)

    def test_atm_to_pa(self):
        assert atmospheres_to_pascals(1) == 101325.0

    def test_roundtrip_atm(self):
        assert pascals_to_atmospheres(atmospheres_to_pascals(2.5)) == pytest.approx(2.5, rel=1e-9)

    def test_bar_to_pa(self):
        assert bars_to_pascals(1) == 100000.0

    def test_pa_to_bar(self):
        assert pascals_to_bars(100000) == 1.0

    def test_psi_to_pa(self):
        assert round(psi_to_pascals(14.696), 0) == 101325.0

    def test_pa_to_psi(self):
        assert round(pascals_to_psi(101325), 3) == 14.696

    def test_type_error(self):
        with pytest.raises(TypeError):
            pascals_to_atmospheres("bad")

class TestFlowConversions:
    """Tests for flow rate conversions."""

    def test_lpm_to_cms(self):
        assert round(liters_per_minute_to_cubic_meters_per_second(60), 6) == 0.001

    def test_cms_to_lpm(self):
        assert cubic_meters_per_second_to_liters_per_minute(0.001) == 60.0

    def test_roundtrip(self):
        val = 42.0
        result = cubic_meters_per_second_to_liters_per_minute(
            liters_per_minute_to_cubic_meters_per_second(val)
        )
        assert result == pytest.approx(val, rel=1e-9)

class TestBytesToHumanReadable:
    """Tests for bytes_to_human_readable."""

    def test_mb(self):
        assert bytes_to_human_readable(1572864) == "1.50 MB"

    def test_bytes(self):
        assert bytes_to_human_readable(512) == "512 B"

    def test_kb(self):
        assert bytes_to_human_readable(2048) == "2.00 KB"

    def test_zero(self):
        assert bytes_to_human_readable(0) == "0 B"

    def test_type_error(self):
        with pytest.raises(TypeError):
            bytes_to_human_readable(1.5)

    def test_value_error(self):
        with pytest.raises(ValueError):
            bytes_to_human_readable(-1)

class TestDensityToSpecificGravity:
    """Tests for density_to_specific_gravity."""

    def test_iron(self):
        assert round(density_to_specific_gravity(7874), 2) == 7.9

    def test_water(self):
        assert density_to_specific_gravity(997) == pytest.approx(1.0, rel=1e-3)

    def test_value_error(self):
        with pytest.raises(ValueError):
            density_to_specific_gravity(1000, reference=0)

class TestSoftplus:

    def test_zero(self):
        assert round(softplus(0), 4) == 0.6931

    def test_large(self):
        # For large x, softplus(x) ≈ x
        assert softplus(50) == pytest.approx(50.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            softplus("x")


# ---------------------------------------------------------------------------
# fxNumeric — conversion_functions.py
# ---------------------------------------------------------------------------

from formulite.fxNumeric.conversion_functions import (
    prandtl_number,
    froude_number,
    weber_number,
)

class TestPrandtlNumber:

    def test_water(self):
        assert prandtl_number(4182, 0.001, 0.6) == 6.97

    def test_zero_k(self):
        with pytest.raises(ValueError):
            prandtl_number(4182, 0.001, 0)

class TestFroudeNumber:

    def test_basic(self):
        assert round(froude_number(5, 9.81, 2), 4) == 1.1288

    def test_zero_length(self):
        with pytest.raises(ValueError):
            froude_number(5, 9.81, 0)

class TestWeberNumber:

    def test_basic(self):
        result = weber_number(1000, 2, 0.01, 0.072)
        assert round(result, 2) == 555.56

    def test_zero_sigma(self):
        with pytest.raises(ValueError):
            weber_number(1000, 2, 0.01, 0)

class TestIsFibonacciNumber:

    def test_fibonacci_values(self):
        fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

        for n in fibs:
            assert is_fibonacci_number(n) is True, f"{n} should be Fibonacci"

    def test_non_fibonacci(self):
        non_fibs = [4, 6, 7, 9, 10, 14, 15, 22, 100]

        for n in non_fibs:
            assert is_fibonacci_number(n) is False, f"{n} should not be Fibonacci"

    def test_negative(self):
        with pytest.raises(ValueError):
            is_fibonacci_number(-1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_fibonacci_number(3.14)

    def test_bool_type_error(self):
        with pytest.raises(TypeError):
            is_fibonacci_number(True)


# ── fxNumeric · conversion_functions ──────────────────────────────────────

from formulite.fxNumeric.conversion_functions import (
    ph_to_h_concentration,
    h_concentration_to_ph,
)

class TestPhToHConcentration:

    def test_neutral(self):
        result = ph_to_h_concentration(7.0)
        assert abs(result - 1e-7) < 1e-12

    def test_acidic(self):
        result = ph_to_h_concentration(3.0)
        assert abs(result - 1e-3) < 1e-8

    def test_basic(self):
        result = ph_to_h_concentration(12.0)
        assert abs(result - 1e-12) < 1e-17

    def test_type_error(self):
        with pytest.raises(TypeError):
            ph_to_h_concentration("7")

class TestHConcentrationToPh:

    def test_neutral(self):
        result = h_concentration_to_ph(1e-7)
        assert abs(result - 7.0) < 1e-9

    def test_roundtrip(self):
        ph = 4.5
        conc = ph_to_h_concentration(ph)
        result = h_concentration_to_ph(conc)
        assert abs(result - ph) < 1e-9

    def test_zero_concentration(self):
        with pytest.raises(ValueError):
            h_concentration_to_ph(0)

    def test_negative_concentration(self):
        with pytest.raises(ValueError):
            h_concentration_to_ph(-0.001)

    def test_type_error(self):
        with pytest.raises(TypeError):
            h_concentration_to_ph("1e-7")

class TestDigitFactorialSum:

    def test_factorion_145(self):
        assert digit_factorial_sum(145) == 145

    def test_123(self):
        # 1! + 2! + 3! = 1 + 2 + 6 = 9
        assert digit_factorial_sum(123) == 9

    def test_zero(self):
        assert digit_factorial_sum(0) == 1  # 0! = 1

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            digit_factorial_sum(-1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            digit_factorial_sum(14.5)


# ── fxNumeric · conversion_functions ─────────────────────────────────

from formulite.fxNumeric.conversion_functions import (
    nusselt_number,
    strouhal_number,
    knudsen_number,
)

class TestNusseltNumber:

    def test_basic(self):
        result = nusselt_number(50.0, 0.5, 0.6)
        assert abs(result - 41.6666666) < 1e-4

    def test_zero_k_raises(self):
        with pytest.raises(ValueError):
            nusselt_number(50, 0.5, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            nusselt_number("50", 0.5, 0.6)

class TestStrouhalNumber:

    def test_basic(self):
        result = strouhal_number(10.0, 0.1, 5.0)
        assert abs(result - 0.2) < 1e-10

    def test_zero_velocity_raises(self):
        with pytest.raises(ValueError):
            strouhal_number(10, 0.1, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            strouhal_number("10", 0.1, 5)

class TestKnudsenNumber:

    def test_basic(self):
        result = knudsen_number(6.8e-8, 0.001)
        assert abs(result - 6.8e-5) < 1e-10

    def test_zero_length_raises(self):
        with pytest.raises(ValueError):
            knudsen_number(6.8e-8, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            knudsen_number("6.8e-8", 0.001)

class TestPressureConvert:

    def test_atm_to_psi(self):
        from formulite.fxNumeric.conversion_functions import pressure_convert
        result = pressure_convert(1, "atm", "psi")
        assert round(result, 4) == 14.6959

    def test_identity(self):
        from formulite.fxNumeric.conversion_functions import pressure_convert
        result = pressure_convert(100, "pa", "pa")
        assert result == 100.0

class TestEnergyConvert:

    def test_kwh_to_j(self):
        from formulite.fxNumeric.conversion_functions import energy_convert
        result = energy_convert(1, "kwh", "j")
        assert round(result) == 3_600_000

    def test_cal_to_j(self):
        from formulite.fxNumeric.conversion_functions import energy_convert
        result = energy_convert(1, "cal", "j")
        assert abs(result - 4.184) < 1e-6

class TestSpeedConvert:

    def test_kmh_to_mph(self):
        from formulite.fxNumeric.conversion_functions import speed_convert
        result = speed_convert(100, "km/h", "mph")
        assert round(result, 4) == 62.1371

    def test_mach_to_ms(self):
        from formulite.fxNumeric.conversion_functions import speed_convert
        result = speed_convert(1, "mach", "m/s")
        assert result == 343.0


# ============================================================================
# TRIGONOMETRY CORE
# ============================================================================

class TestOhmsLaw:

    def test_solve_current(self):
        from formulite.fxNumeric.conversion_functions import ohms_law
        assert ohms_law(voltage=12, resistance=4) == 3.0

    def test_solve_voltage(self):
        from formulite.fxNumeric.conversion_functions import ohms_law
        assert ohms_law(current=3, resistance=4) == 12

    def test_solve_resistance(self):
        from formulite.fxNumeric.conversion_functions import ohms_law
        assert ohms_law(voltage=12, current=3) == 4.0

    def test_too_few(self):
        from formulite.fxNumeric.conversion_functions import ohms_law
        with pytest.raises(ValueError):
            ohms_law(voltage=12)

class TestCoulombsLaw:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import coulombs_law
        assert round(coulombs_law(1e-6, 2e-6, 0.05), 2) == 7.19

    def test_zero_distance(self):
        from formulite.fxNumeric.conversion_functions import coulombs_law
        with pytest.raises(ValueError):
            coulombs_law(1e-6, 1e-6, 0)

class TestGravitationalForce:

    def test_earth_surface(self):
        from formulite.fxNumeric.conversion_functions import gravitational_force
        result = round(gravitational_force(5.972e24, 80, 6.371e6), 1)
        assert result == 785.6

    def test_zero_distance(self):
        from formulite.fxNumeric.conversion_functions import gravitational_force
        with pytest.raises(ValueError):
            gravitational_force(1, 1, 0)

class TestKineticEnergy:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import kinetic_energy
        assert kinetic_energy(10, 3) == 45.0

    def test_zero_velocity(self):
        from formulite.fxNumeric.conversion_functions import kinetic_energy
        assert kinetic_energy(10, 0) == 0.0

    def test_negative_mass(self):
        from formulite.fxNumeric.conversion_functions import kinetic_energy
        with pytest.raises(ValueError):
            kinetic_energy(-1, 5)

class TestPotentialEnergy:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import potential_energy
        assert round(potential_energy(10, 5), 4) == 490.3325

    def test_zero_height(self):
        from formulite.fxNumeric.conversion_functions import potential_energy
        assert potential_energy(10, 0) == 0.0

class TestEscapeVelocity:

    def test_earth(self):
        from formulite.fxNumeric.conversion_functions import escape_velocity
        assert round(escape_velocity(5.972e24, 6.371e6), 0) == 11186.0

    def test_zero_radius(self):
        from formulite.fxNumeric.conversion_functions import escape_velocity
        with pytest.raises(ValueError):
            escape_velocity(1e24, 0)

class TestSnellsLaw:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import snells_law
        assert round(snells_law(1.0, math.radians(30), 1.5), 6) == 0.339837

    def test_total_internal_reflection(self):
        from formulite.fxNumeric.conversion_functions import snells_law
        with pytest.raises(ValueError):
            snells_law(1.5, math.radians(80), 1.0)


# =====================================================================
# Trigonometry
# =====================================================================

class TestBMI:

    def test_basic(self):
        assert round(bmi(70, 1.75), 2) == 22.86

    def test_zero_height_raises(self):
        with pytest.raises(ValueError):
            bmi(70, 0)

    def test_negative_weight_raises(self):
        with pytest.raises(ValueError):
            bmi(-70, 1.75)


# ──────────────────────────────────────────────
# Engineering: wind_chill
# ──────────────────────────────────────────────

class TestWindChill:

    def test_basic(self):
        assert round(wind_chill(-5, 30), 2) == -13.0

    def test_warm_temp_raises(self):
        with pytest.raises(ValueError):
            wind_chill(15, 30)

    def test_low_wind_raises(self):
        with pytest.raises(ValueError):
            wind_chill(-5, 3)


# ──────────────────────────────────────────────
# Engineering: heat_index
# ──────────────────────────────────────────────

class TestHeatIndex:

    def test_basic(self):
        assert round(heat_index(35, 75), 1) == 53.3

    def test_cool_temp_raises(self):
        with pytest.raises(ValueError):
            heat_index(20, 50)

    def test_humidity_out_of_range(self):
        with pytest.raises(ValueError):
            heat_index(35, 110)


# ──────────────────────────────────────────────
# Engineering: dew_point
# ──────────────────────────────────────────────

class TestDewPoint:

    def test_basic(self):
        assert round(dew_point(25, 50), 2) == 13.84

    def test_zero_humidity_raises(self):
        with pytest.raises(ValueError):
            dew_point(25, 0)

    def test_full_humidity(self):
        # At 100% humidity, dew point equals temperature
        assert round(dew_point(25, 100), 1) == 25.0


# ──────────────────────────────────────────────
# Engineering: decibel_add
# ──────────────────────────────────────────────

class TestDecibelAdd:

    def test_same_levels(self):
        assert round(decibel_add(90, 90), 2) == 93.01

    def test_zero_levels(self):
        assert round(decibel_add(0, 0), 2) == 3.01

    def test_type_error(self):
        with pytest.raises(TypeError):
            decibel_add("90", 90)


# ──────────────────────────────────────────────
# Engineering: terminal_velocity
# ──────────────────────────────────────────────

class TestTerminalVelocity:

    def test_basic(self):
        assert round(terminal_velocity(80, 1.0, 0.7), 2) == 42.78

    def test_negative_mass_raises(self):
        with pytest.raises(ValueError):
            terminal_velocity(-80, 1.0, 0.7)


# ──────────────────────────────────────────────
# Engineering: elastic_modulus
# ──────────────────────────────────────────────

class TestElasticModulus:

    def test_basic(self):
        assert elastic_modulus(200e6, 0.001) == 200000000000.0

    def test_zero_strain_raises(self):
        with pytest.raises(ValueError):
            elastic_modulus(200e6, 0)


# ──────────────────────────────────────────────
# Engineering: hookes_law
# ──────────────────────────────────────────────

class TestHookesLaw:

    def test_basic(self):
        assert hookes_law(100, 0.05) == -5.0

    def test_zero_displacement(self):
        assert hookes_law(100, 0) == 0.0

    def test_negative_spring_raises(self):
        with pytest.raises(ValueError):
            hookes_law(-100, 0.05)


# ──────────────────────────────────────────────
# Trigonometry: gudermannian
# ──────────────────────────────────────────────

class TestIdealGasPressure:

    def test_basic(self):
        result = ideal_gas_pressure(1, 273.15, 0.0224)
        assert round(result, 0) == 101388.0

    def test_zero_volume_raises(self):
        with pytest.raises(ValueError):
            ideal_gas_pressure(1, 300, 0)


# ──────────────────────────────────────────────
# Physics: centripetal_force
# ──────────────────────────────────────────────

class TestCentripetalForceV2:

    def test_basic(self):
        assert centripetal_force(10, 5, 2) == 125.0

    def test_zero_radius_raises(self):
        with pytest.raises(ValueError):
            centripetal_force(10, 5, 0)


# ──────────────────────────────────────────────
# Physics: momentum
# ──────────────────────────────────────────────

class TestMomentum:

    def test_basic(self):
        assert momentum(10, 5) == 50.0

    def test_negative_velocity(self):
        assert momentum(10, -5) == -50.0

    def test_zero_mass_raises(self):
        with pytest.raises(ValueError):
            momentum(0, 5)


# ──────────────────────────────────────────────
# Physics: impulse
# ──────────────────────────────────────────────

class TestImpulse:

    def test_basic(self):
        assert impulse(100, 0.5) == 50.0

    def test_zero_time_raises(self):
        with pytest.raises(ValueError):
            impulse(100, 0)


# ──────────────────────────────────────────────
# Physics: wave_speed
# ──────────────────────────────────────────────

class TestWaveSpeed:

    def test_basic(self):
        assert wave_speed(440, 0.78) == pytest.approx(343.2)

    def test_zero_frequency_raises(self):
        with pytest.raises(ValueError):
            wave_speed(0, 0.78)


# ──────────────────────────────────────────────
# Physics: reynolds_number
# ──────────────────────────────────────────────

class TestReynoldsNumber:

    def test_basic(self):
        assert reynolds_number(1000, 1, 0.01, 0.001) == 10000.0

    def test_zero_viscosity_raises(self):
        with pytest.raises(ValueError):
            reynolds_number(1000, 1, 0.01, 0)


# ──────────────────────────────────────────────
# Physics: mach_number
# ──────────────────────────────────────────────

class TestMachNumber:

    def test_basic(self):
        assert round(mach_number(680), 2) == 1.98

    def test_subsonic(self):
        assert mach_number(170) < 1.0

    def test_custom_speed_of_sound(self):
        assert mach_number(340, 340) == pytest.approx(1.0)


# ──────────────────────────────────────────────
# Physics: power_physics
# ──────────────────────────────────────────────

class TestPowerPhysics:

    def test_basic(self):
        assert power_physics(1000, 5) == 200.0

    def test_zero_time_raises(self):
        with pytest.raises(ValueError):
            power_physics(1000, 0)


# ──────────────────────────────────────────────
# Trigonometry: haversine_angle
# ──────────────────────────────────────────────

class TestSpecificHeatEnergy:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import specific_heat_energy

        assert specific_heat_energy(1, 4186, 10) == 41860.0

    def test_negative_mass(self):
        from formulite.fxNumeric.conversion_functions import specific_heat_energy

        with pytest.raises(ValueError):
            specific_heat_energy(-1, 4186, 10)

class TestBuoyantForce:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import buoyant_force

        assert round(buoyant_force(1000, 0.01), 2) == 98.07

    def test_type_error(self):
        from formulite.fxNumeric.conversion_functions import buoyant_force

        with pytest.raises(TypeError):
            buoyant_force("a", 0.01)

class TestFrictionForce:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import friction_force

        assert friction_force(100, 0.5) == 50.0

    def test_negative_coefficient(self):
        from formulite.fxNumeric.conversion_functions import friction_force

        with pytest.raises(ValueError):
            friction_force(100, -0.5)

class TestPhotonEnergy:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import photon_energy

        assert photon_energy(5e14) == pytest.approx(3.313035075e-19)

    def test_negative_frequency(self):
        from formulite.fxNumeric.conversion_functions import photon_energy

        with pytest.raises(ValueError):
            photon_energy(-1)

class TestDeBroglieWavelength:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import de_broglie_wavelength

        assert de_broglie_wavelength(9.109e-31, 1e6) == pytest.approx(7.274e-10, rel=1e-3)

    def test_zero_mass(self):
        from formulite.fxNumeric.conversion_functions import de_broglie_wavelength

        with pytest.raises(ValueError):
            de_broglie_wavelength(0, 1e6)

class TestFocalLength:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import focal_length

        assert round(focal_length(0.3, 0.6), 1) == 0.2

    def test_zero_distance(self):
        from formulite.fxNumeric.conversion_functions import focal_length

        with pytest.raises(ValueError):
            focal_length(0, 0.6)

class TestLensMagnification:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import lens_magnification

        assert lens_magnification(0.6, 0.3) == -2.0

    def test_zero_object(self):
        from formulite.fxNumeric.conversion_functions import lens_magnification

        with pytest.raises(ValueError):
            lens_magnification(0.6, 0)

class TestHalfLifeRemaining:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import half_life_remaining

        assert half_life_remaining(100, 5, 10) == 25.0

    def test_zero_time(self):
        from formulite.fxNumeric.conversion_functions import half_life_remaining

        assert half_life_remaining(100, 5, 0) == 100.0

    def test_negative_time(self):
        from formulite.fxNumeric.conversion_functions import half_life_remaining

        with pytest.raises(ValueError):
            half_life_remaining(100, 5, -1)

class TestCapacitorEnergy:

    def test_basic(self):
        from formulite.fxNumeric.conversion_functions import capacitor_energy

        assert capacitor_energy(0.001, 10) == 0.05

    def test_negative_capacitance(self):
        from formulite.fxNumeric.conversion_functions import capacitor_energy

        with pytest.raises(ValueError):
            capacitor_energy(-0.001, 10)


# ── Trigonometry / Geometry ──────────────────────────────────────────
