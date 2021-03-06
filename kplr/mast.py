# -*- coding: utf-8 -*-
"""
Adapters for the field names/types returned by the MAST API.

"""

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

__all__ = ["koi_adapter", "planet_adapter", "star_adapter", "dataset_adapter",
           "epic_adapter"]

import logging

import six

try:
    unicode
except NameError:
    unicode = str


class Adapter(object):
    """
    An :class:`Adapter` is a callable that maps a dictionary to another
    dictionary with different keys and specified data types. Missing/invalid
    values will be mapped to ``None``.

    :param parameters:
        A dictionary of mappers. The keys should be the keys that will be in
        the input dictionary and the values should be 2-tuples with the output
        key and the callable type converter.

    """

    def __init__(self, parameters):
        self._parameters = parameters

        # Add some general purpose parameters.
        self._parameters["Ang Sep (')"] = ("angular_separation", float)

    def __call__(self, row):
        row = dict(row)
        final = {}
        for longname, (shortname, conv) in self._parameters.items():
            try:
                final[shortname] = conv(row.pop(longname, None))
            except (ValueError, TypeError):
                final[shortname] = None

        for k in row:
            logging.warn("Unrecognized parameter: '{0}'".format(k))

        return final


koi_adapter = Adapter({
    "Kepler ID": ("kepid", int),
    "KOI Name": ("kepoi_name", six.text_type),
    "KOI Number": ("kepoi", six.text_type),
    "Kepler Disposition": ("koi_pdisposition", six.text_type),
    "NExScI Disposition": ("koi_disposition", six.text_type),
    "RA (J2000)": ("degree_ra", float),
    "Dec (J2000)": ("degree_dec", float),
    "Time of Transit Epoch": ("koi_time0bk", float),
    "Time err1": ("koi_time0bk_err1", float),
    "Time_err2": ("koi_time0bk_err2", float),
    "Period": ("koi_period", float),
    "Period err1": ("koi_period_err1", float),
    "Period err2": ("koi_period_err2", float),
    "Transit Depth": ("koi_depth", float),
    "Depth err1": ("koi_depth_err1", float),
    "Depth err2": ("koi_depth_err2", float),
    "Duration": ("koi_duration", float),
    "Duration err1": ("koi_duration_err1", float),
    "Duration err2": ("koi_duration_err2", float),
    "Ingress Duration": ("koi_ingress", float),
    "Ingress err1": ("koi_ingress_err1", float),
    "Ingress err2": ("koi_ingress_err2", float),
    "Impact Parameter": ("koi_impact", float),
    "Impact Parameter err1": ("koi_impact_err1", float),
    "Impact Parameter err2": ("koi_impact_err2", float),
    "Inclination": ("koi_incl", float),
    "Inclination err1": ("koi_incl_err1", float),
    "Inclination err2": ("koi_incl_err2", float),
    "Semi-major Axis": ("koi_sma", float),
    "Semi-major Axus err1": ("koi_sma_err1", float),
    "Semi-major Axis err2": ("koi_sma_err2", float),
    "Eccentricity": ("koi_eccen", float),
    "Eccentricity err1": ("koi_eccen_err1", float),
    "Eccentricity err2": ("koi_eccen_err2", float),
    "Long of Periastron": ("koi_longp", float),
    "Long err1": ("koi_longp_err1", float),
    "Long err2": ("koi_longp_err2", float),
    "r/R": ("koi_ror", float),
    "r/R err1": ("koi_ror_err1", float),
    "r/R err2": ("koi_ror_err2", float),
    "a/R": ("koi_dor", float),
    "a/R err1": ("koi_dor_err1", float),
    "a/R err2": ("koi_dor_err2", float),
    "Planet Radius": ("koi_prad", float),
    "Planet Radius err1": ("koi_prad_err1", float),
    "Planet Radius err2": ("koi_prad_err2", float),
    "Teq": ("koi_teq", int),
    "Teq err1": ("koi_teq_err1", int),
    "Teq err2": ("koi_teq_err2", int),
    "Teff": ("koi_steff", int),
    "Teff err1": ("koi_steff_err1", int),
    "Teff err2": ("koi_steff_err2", int),
    "log(g)": ("koi_slogg", float),
    "log(g) err1": ("koi_slogg_err1", float),
    "log(g) err2": ("koi_slogg_err2", float),
    "Metallicity": ("koi_smet", float),
    "Metallicity err1": ("koi_smet_err1", float),
    "Metallicity err2": ("koi_smet_err2", float),
    "Stellar Radius": ("koi_srad", float),
    "Stellar Radius err1": ("koi_srad_err1", float),
    "Stellar Radius err2": ("koi_srad_err2", float),
    "Stellar Mass": ("koi_smass", float),
    "Stellar Mass err2": ("koi_smass_err2", float),
    "Stellar Mass err1": ("koi_smass_err1", float),
    "Age": ("koi_sage", float),
    "Age err1": ("koi_sage_err1", float),
    "Age err2": ("koi_sage_err2", float),
    "Provenance": ("koi_sparprov", six.text_type),
    "Quarters": ("koi_quarters", six.text_type),
    "Limb Darkening Model": ("koi_limbdark_mod", six.text_type),
    "Limb Darkening Coeff1": ("koi_ldm_coeff1", float),
    "Limb Darkening Coeff2": ("koi_ldm_coeff2", float),
    "Limb Darkening Coeff3": ("koi_ldm_coeff3", float),
    "Limb Darkening Coeff4": ("koi_ldm_coeff4", float),
    "Transit Number": ("koi_num_transits", int),
    "Max single event sigma": ("koi_max_sngle_ev", float),
    "Max Multievent sigma": ("koi_max_mult_ev", float),
    "KOI count": ("koi_count", int),
    "Binary Discrimination": ("koi_bin_oedp_sig", float),
    "False Positive Bkgnd ID": ("koi_fp_bkgid", six.text_type),
    "J-band diff": ("koi_fp_djmag", six.text_type),
    "Comments": ("koi_comment", six.text_type),
    "Transit Model": ("koi_trans_mod", six.text_type),
    "Transit Model SNR": ("koi_model_snr", float),
    "Transit Model DOF": ("koi_model_dof", float),
    "Transit Model chisq": ("koi_model_chisq", float),
    "FWM motion signif.": ("koi_fwm_stat_sig", float),
    "gmag": ("koi_gmag", float),
    "gmag err": ("koi_gmag_err", float),
    "rmag": ("koi_rmag", float),
    "rmag err": ("koi_rmag_err", float),
    "imag": ("koi_imag", float),
    "imag err": ("koi_imag_err", float),
    "zmag": ("koi_zmag", float),
    "zmag err": ("koi_zmag_err", float),
    "Jmag": ("koi_jmag", float),
    "Jmag err": ("koi_jmag_err", float),
    "Hmag": ("koi_hmag", float),
    "Hmag err": ("koi_hmag_err", float),
    "Kmag": ("koi_kmag", float),
    "Kmag err": ("koi_kmag_err", float),
    "kepmag": ("koi_kepmag", float),
    "kepmag err": ("koi_kepmag_err", float),
    "Delivery Name": ("koi_delivname", six.text_type),
    "FWM SRA": ("koi_fwm_sra", float),
    "FWM SRA err": ("koi_fwm_sra_err", float),
    "FWM SDec": ("koi_fwm_sdec", float),
    "FWM SDec err": ("koi_fwm_sdec_err", float),
    "FWM SRAO": ("koi_fwm_srao", float),
    "FWM SRAO err": ("koi_fwm_srao_err", float),
    "FWM SDeco": ("koi_fwm_sdeco", float),
    "FWM SDeco err": ("koi_fwm_sdeco_err", float),
    "FWM PRAO": ("koi_fwm_prao", float),
    "FWM PRAO err": ("koi_fwm_prao_err", float),
    "FWM PDeco": ("koi_fwm_pdeco", float),
    "FWM PDeco err": ("koi_fwm_pdeco_err", float),
    "Dicco MRA": ("koi_dicco_mra", float),
    "Dicco MRA err": ("koi_dicco_mra_err", float),
    "Dicco MDec": ("koi_dicco_mdec", float),
    "Dicco MDec err": ("koi_dicco_mdec_err", float),
    "Dicco MSky": ("koi_dicco_msky", float),
    "Dicco MSky err": ("koi_dicco_msky_err", float),
    "Dicco FRA": ("koi_dicco_fra", float),
    "Dicco FRA err": ("koi_dicco_fra_err", float),
    "Dicco FDec": ("koi_dicco_fdec", float),
    "Dicco FDec err": ("koi_dicco_fdec_err", float),
    "Dicco FSky": ("koi_dicco_fsky", float),
    "Dicco FSky err": ("koi_dicco_fsky_err", float),
    "Dikco MRA": ("koi_dikco_mra", float),
    "Dikco MRA err": ("koi_dikco_mra_err", float),
    "Dikco MDec": ("koi_dikco_mdec", float),
    "Dikco MDec err": ("koi_dikco_mdec_err", float),
    "Dikco MSky": ("koi_dikco_msky", float),
    "Dikco MSky err": ("koi_dikco_msky_err", float),
    "Dikco FRA": ("koi_dikco_fra", float),
    "Dikco FRA err": ("koi_dikco_fra_err", float),
    "Dikco FDec": ("koi_dikco_fdec", float),
    "Dikco FDec err": ("koi_dikco_fdec_err", float),
    "Dikco FSky": ("koi_dikco_fsky", float),
    "Dikco FSky err": ("koi_dikco_fsky_err", float),
    "Last Update": ("rowupdate", six.text_type),
})

planet_adapter = Adapter({
    "Planet Name": ("kepler_name", six.text_type),
    "Kepler ID": ("kepid", int),
    "KOI Name": ("kepoi_name", six.text_type),
    "Alt Name": ("alt_name", six.text_type),
    "KOI Number": ("koi_number", six.text_type),  # Just `koi` in API.
    "RA (J2000)": ("degree_ra", float),
    "RA Error": ("ra_err", float),
    "Dec (J2000)": ("degree_dec", float),
    "Dec Error": ("dec_err", float),
    "2mass Name": ("tm_designation", six.text_type),
    "Planet temp": ("koi_teq", int),
    "Planet Radius": ("koi_prad", float),
    "Transit duration": ("koi_duration", float),
    "Period": ("koi_period", float),
    "Period err1": ("koi_period_err1", float),
    "Ingress Duration": ("koi_ingress", float),
    "Impact Parameter": ("koi_impact", float),
    "Inclination": ("koi_incl", float),
    "Provenance": ("koi_sparprov", six.text_type),
    "a/R": ("koi_dor", float),
    "Transit Number": ("koi_num_transits", int),
    "Transit Model": ("koi_trans_mod", six.text_type),
    "Time of transit": ("koi_time0bk", float),
    "Time of transit err1": ("koi_time0bk_err1", float),
    "Transit Depth": ("koi_depth", float),
    "Semi-major Axis": ("koi_sma", float),
    "r/R": ("koi_ror", float),
    "r/R err1": ("koi_ror_err1", float),
    "Age": ("koi_sage", float),
    "Metallicity": ("koi_smet", float),
    "Stellar Mass": ("koi_smass", float),
    "Stellar Radius": ("koi_srad", float),
    "Stellar Teff": ("koi_steff", int),
    "Logg": ("koi_slogg", float),
    "KEP Mag": ("koi_kepmag", float),
    "g Mag": ("koi_gmag", float),
    "r Mag": ("koi_rmag", float),
    "i Mag": ("koi_imag", float),
    "z Mag": ("koi_zmag", float),
    "J Mag": ("koi_jmag", float),
    "H Mag": ("koi_hmag", float),
    "K Mag": ("koi_kmag", float),
    "KOI List": ("koi_list_flag", six.text_type),
    "Last Update": ("koi_vet_date", six.text_type),
})

star_adapter = Adapter({
    "Kepler ID": ("kic_kepler_id", int),
    "RA (J2000)": ("kic_degree_ra", float),
    "Dec (J2000)": ("kic_dec", float),
    "RA PM (arcsec/yr)": ("kic_pmra", float),
    "Dec PM (arcsec/yr)": ("kic_pmdec", float),
    "u Mag": ("kic_umag", float),
    "g Mag": ("kic_gmag", float),
    "r Mag": ("kic_rmag", float),
    "i Mag": ("kic_imag", float),
    "z Mag": ("kic_zmag", float),
    "Gred Mag": ("kic_gredmag", float),
    "D51 Mag": ("kic_d51mag", float),
    "J Mag": ("kic_jmag", float),
    "H Mag": ("kic_hmag", float),
    "K Mag": ("kic_kmag", float),
    "Kepler Mag": ("kic_kepmag", float),
    "2MASS ID": ("kic_2mass_id", six.text_type),
    "2MASS Designation": ("kic_tmid", int),
    "SCP ID": ("kic_scpid", int),
    "Alt ID": ("kic_altid", int),
    "Alt ID Source": ("kic_altsource", int),
    "Star/Gal ID": ("kic_galaxy", int),
    "Isolated/Blend ID": ("kic_blend", int),
    "Var. ID": ("kic_variable", int),
    "Teff (deg K)": ("kic_teff", int),
    "Log G (cm/s/s)": ("kic_logg", float),
    "Metallicity (solar=0.0)": ("kic_feh", float),
    "E(B-V)": ("kic_ebminusv", float),
    "A_V": ("kic_av", float),
    "Radius (solar=1.0)": ("kic_radius", float),
    "Kepmag Source": ("kic_cq", six.text_type),
    "Photometry Qual": ("kic_pq", int),
    "Astrophysics Qual": ("kic_aq", int),
    "Catalog key": ("kic_catkey", int),
    "Scp Key": ("kic_scpkey", int),
    "Parallax (arcsec)": ("kic_parallax", float),
    "Gal Lon (deg)": ("kic_glon", float),
    "Gal Lat (deg)": ("kic_glat", float),
    "Total PM (arcsec/yr)": ("kic_pmtotal", float),
    "g-r color": ("kic_grcolor", float),
    "J-K color": ("kic_jkcolor", float),
    "g-K color": ("kic_gkcolor", float),
    "RA hours (J2000)": ("kic_ra", float),
    "Flag": ("flag", int),
})

dataset_adapter = Adapter({
    "Kepler ID": ("ktc_kepler_id", int),
    "Investigation ID": ("ktc_investigation_id", six.text_type),
    "Pep ID": ("sci_pep_id", int),
    "Dataset Name": ("sci_data_set_name", six.text_type),
    "Quarter": ("sci_data_quarter", int),
    "Data Release": ("sci_data_rel", int),
    "RA (J2000)": ("sci_ra", float),
    "Dec (J2000)": ("sci_dec", float),
    "Target Type": ("ktc_target_type", six.text_type),
    "Archive Class": ("sci_archive_class", six.text_type),
    "Ref": ("refnum", int),
    "Actual Start Time": ("sci_start_time", six.text_type),
    "Actual End Time": ("sci_end_time", six.text_type),
    "Release Date": ("sci_release_date", six.text_type),
    "RA PM": ("kic_pmra", float),
    "Dec PM": ("kic_pmdec", float),
    "U Mag": ("kic_umag", float),
    "G Mag": ("kic_gmag", float),
    "R Mag": ("kic_rmag", float),
    "I Mag": ("kic_imag", float),
    "Z Mag": ("kic_zmag", float),
    "GRed Mag": ("kic_gredmag", float),
    "D51 Mag": ("kic_d51mag", float),
    "J Mag": ("twoMass_jmag", float),
    "H Mag": ("twoMass_hmag", float),
    "K Mag": ("twoMass_kmag", float),
    "KEP Mag": ("kic_kepmag", float),
    "2MASS ID": ("twoMass_2mass_id", six.text_type),
    "2MASS Designation": ("twoMass_tmid", int),
    "2MASS conflict flag": ("twoMass_conflictFlag", six.text_type),
    "SCP ID": ("kic_scpid", int),
    "Alt ID": ("kic_altid", int),
    "Alt ID Source": ("kic_altsource", int),
    "Star/Gal ID": ("kic_galaxy", int),
    "Isolated/Blend ID": ("kic_blend", int),
    "Var. ID": ("kic_variable", int),
    "Teff": ("kic_teff", int),
    "Log G": ("kic_logg", float),
    "Metallicity": ("kic_feh", float),
    "E(B-V)": ("kic_ebminusv", float),
    "A_V": ("kic_av", float),
    "Radius": ("kic_radius", float),
    "Kepmag Source": ("kic_cq", six.text_type),
    "Photometry Qual": ("kic_pq", int),
    "Astrophysics Qual": ("kic_aq", int),
    "Catalog key": ("kic_catkey", int),
    "Scp Key": ("kic_scpkey", int),
    "Parallax": ("kic_parallax", float),
    "Gal Lon": ("kic_glon", float),
    "Gal Lat": ("kic_glat", float),
    "Total PM": ("kic_pmtotal", float),
    "G-R color": ("kic_grcolor", float),
    "J-K color": ("twoMass_jkcolor", float),
    "G-K color": ("twoMass_gkcolor", float),
    "Processing Date": ("sci_generation_date", six.text_type),
    "crowding": ("sci_crowdsap", float),
    "contamination": ("sci_contamination", float),
    "flux fraction": ("sci_flfrcsap", float),
    "cdpp3": ("sci_Cdpp3_0", float),
    "cdpp6": ("sci_Cdpp6_0", float),
    "cdpp12": ("sci_Cdpp12_0", float),
    "Module": ("sci_module", int),
    "Output": ("sci_output", int),
    "Channel": ("sci_channel", int),
    "Skygroup_ID": ("sci_skygroup_id", int),
    "Condition flag": ("condition_flag", six.text_type),
})

epic_adapter = Adapter({
    "EPIC": ("id", int),
    "RA": ("k2_ra", float),
    "Dec": ("k2_dec", float),
    "KepMag": ("kp", float),
    "HIP": ("hip", int),
    "TYC": ("tyc", six.text_type),
    "UCAC": ("ucac", six.text_type),
    "2MASS": ("twomass", six.text_type),
    "SDSS": ("sdss", six.text_type),
    "Object type": ("objtype", six.text_type),
    "Kepflag": ("kepflag", six.text_type),
    "pmra": ("pmra", float),
    "e_pmra": ("e_pmra", float),
    "pmdec": ("pmdec", float),
    "e_pmdec": ("e_pmdec", float),
    "plx": ("plx", float),
    "e_plx": ("e_plx", float),
    "Bmag": ("bmag", float),
    "e_Bmag": ("e_bmag", float),
    "Vmag": ("vmag", float),
    "e_Vmag": ("e_vmag", float),
    "umag": ("umag", float),
    "e_umag": ("e_umag", float),
    "gmag": ("gmag", float),
    "e_gmag": ("e_gmag", float),
    "rmag": ("rmag", float),
    "e_rmag": ("e_rmag", float),
    "imag": ("imag", float),
    "e_imag": ("e_imag", float),
    "zmag": ("zmag", float),
    "e_zmag": ("e_zmag", float),
    "Jmag": ("jmag", float),
    "e_Jmag": ("e_jmag", float),
    "Hmag": ("hmag", float),
    "e_Hmag": ("e_hmag", float),
    "Kmag": ("kmag", float),
    "e_Kmag": ("e_kmag", float),
    "w1mag": ("w1mag", float),
    "e_w1mag": ("e_w1mag", float),
    "w2mag": ("w2mag", float),
    "e_w2mag": ("e_w2mag", float),
    "w3mag": ("w3mag", float),
    "e_w3mag": ("e_w3mag", float),
    "w4mag": ("w4mag", float),
    "e_w4mag": ("e_w4mag", float),
    "Teff": ("teff", float),
    "e_teff": ("e_teff", float),
    "logg": ("logg", float),
    "e_logg": ("e_logg", float),
    "[Fe/H]": ("feh", float),
    "e_[Fe/H]": ("e_feh", float),
    "Radius": ("rad", float),
    "e_rad": ("e_rad", float),
    "mass": ("mass", float),
    "e_mass": ("e_mass", float),
    "rho": ("rho", float),
    "e_rho": ("e_rho", float),
    "lum": ("lum", float),
    "e_lum": ("e_lum", float),
    "Distance": ("d", float),
    "e_d": ("e_d", float),
    "E(B-V)": ("ebv", float),
    "2MASS Flag": ("mflg", six.text_type),
    "Nearest Neighbor": ("prox", float),
    "Nomad ID": ("nomad", six.text_type),
})

k2_dataset_adapter = Adapter({
    "K2 ID": ("ktc_k2_id", int),
    "Dataset Name": ("sci_data_set_name", six.text_type),
    "Campaign": ("sci_campaign", int),
    "Object type": ("objtype", six.text_type),
    "Data Release": ("sci_data_rel", int),
    "RA (J2000)": ("sci_ra", float),
    "Dec (J2000)": ("sci_dec", float),
    "Target Type": ("ktc_target_type", six.text_type),
    "Archive Class": ("sci_archive_class", six.text_type),
    "Ref": ("refnum", int),
    "Actual Start Time": ("sci_start_time", six.text_type),
    "Actual End Time": ("sci_end_time", six.text_type),
    "Investigation ID": ("ktc_investigation_id", six.text_type),
    "RA PM": ("pmRA", float),
    "RA PM Err": ("e_pmRA", float),
    "Dec PM": ("pmDEC", float),
    "Dec PM Err": ("e_pmDEC", float),
    "Plx": ("plx", float),
    "Plx Err": ("e_plx", float),
    "U Mag": ("umag", float),
    "U Mag Err": ("e_umag", float),
    "B Mag": ("bmag", float),
    "B Mag Err": ("e_bmag", float),
    "V Mag": ("vmag", float),
    "V Mag Err": ("e_vmag", float),
    "G Mag": ("gmag", float),
    "G Mag Err": ("e_gmag", float),
    "R Mag": ("rmag", float),
    "R Mag Err": ("e_rmag", float),
    "I Mag": ("imag", float),
    "I Mag Err": ("e_imag", float),
    "Z Mag": ("zmag", float),
    "Z Mag Err": ("e_zmag", float),
    "J Mag": ("jmag", float),
    "J Mag Err": ("e_jmag", float),
    "H Mag": ("hmag", float),
    "H Mag Err": ("e_hmag", float),
    "K Mag": ("kmag", float),
    "K Mag Err": ("e_kmag", float),
    "KEP Mag": ("kp", float),
    "Kep Flag": ("kepflag", six.text_type),
    "Hip ID": ("hip", int),
    "Tyc ID": ("tyc", six.text_type),
    "SDSS ID": ("sdss", six.text_type),
    "UCAC ID": ("ucac", six.text_type),
    "2MASS ID": ("twoMass", six.text_type),
    "2MASS Flag": ("mflg", six.text_type),
    "Processing Date": ("sci_generation_date", six.text_type),
    "crowding": ("sci_crowdsap", float),
    "contamination": ("sci_contamination", float),
    "flux fraction": ("sci_flfrcsap", float),
    "cdpp3": ("sci_Cdpp3_0", float),
    "cdpp6": ("sci_Cdpp6_0", float),
    "cdpp12": ("sci_Cdpp12_0", float),
    "Module": ("sci_module", int),
    "Output": ("sci_output", int),
    "Channel": ("sci_channel", int),
    "Nearest Neighbor": ("prox", float),
    "Nomad ID": ("nomad", six.text_type),
})

target_adapter = Adapter({
    "masterRA": ("masterRA", float),
    "masterDec": ("masterDec", float),
    "Kepler_ID":("kic_kepler_id", int),
    "2MASS_ID":("twomass_2mass_id", str),
    "U_UBV":("U_UBV", float),
    "gr":("gr", float),
    "Parallax (arcsec)":("kic_parallax", float),
    "Channel_0": ("Channel_0", int),
    "Channel_1": ("Channel_1", int),
    "Channel_2": ("Channel_2", int),
    "Channel_3": ("Channel_3", int),
    "Module_0": ("Module_0", int),
    "Module_1": ("Module_1", int),
    "Module_2": ("Module_2", int),
    "Module_3": ("Module_3", int),
    "Row_0": ("Row_0", int),
    "Row_1": ("Row_1", int),
    "Row_2": ("Row_2", int),
    "Row_3": ("Row_3", int),
    "Column_0": ("Column_0", int),
    "Column_1": ("Column_1", int),
    "Column_2": ("Column_2", int),
    "Column_3": ("Column_3", int),
})