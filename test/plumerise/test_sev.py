__author__      = "Joel Dubowy"

import copy

#from numpy.testing import assert_approx_equal
from py.test import raises

from plumerise.sev import SEVPlumeRise

class TestSEVPlumeRise(object):

    def test_compute_without_frp(self):
        """Top level regression test of sorts for SEVPlumeRise

        Note: the expected output data in this test is not known to be
        correct.  It's simply a snapshot taken after initial implementation
        of the SEV model.  This test serves to ensure that future
        refactoring doesn't result in unexpected changes to output.
        """
        local_met =  {
            "2014-05-29T22:00:00": {
                "HBPL": 100.0,
                "HGTS": [
                    59.20695352193937, 127.28731809256338, 230.2522349481686, 351.68578134369875, 509.94193417445086, 706.7299646465185, 953.5253812220434, 1301.743826670549, 1732.0963974479655, 2181.7902676298922, 2652.883050652689, 3345.982389068354, 4259.947450680663, 5186.011915491956, 6104.352989489506, 7056.643626913428, 8006.417923710241, 8986.451540456597, 9972.250805846712, 10981.449306410641, 12009.765287655282, 13124.193667771762, 14217.209589756567, 15406.309765306385, 16658.518561184595, 17976.158502586513, 19355.563010823662, 20904.261267868987, 22702.76242092459, 24927.524263410254, 28825.25346629527
                ],
                "PBLH": 255.0,
                "PRES": [
                    993.0, 987.0, 976.0, 961.0, 944.0, 924.0, 897.0, 862.0, 820.0, 779.0, 737.0, 679.0, 609.0, 544.0, 486.0, 432.0, 384.0, 339.0, 299.0, 263.0, 230.0, 200.0, 174.0, 150.0, 130.0, 112.0, 96.9, 83.7, 72.3, 62.4, 53.9],
                "PRSS": 997.0,
                "RELH": [
                    27.977709329694118, 21.988055318553968, 18.163923812897735, 16.8122652405985, 18.37709010858054, 19.949714580345066, 17.07034134569377, 14.896109730262328, 11.494058082288117, 13.234038143327819, 17.31236043556044, 11.618446902157041, 8.87287438428925, 13.44937537189244, 26.25859160063417, 42.4424808519119, 50.18628194504284, 49.817673461702114, 46.554155931776606, 37.9822107195308, 16.212362419125235, 11.873449334871864, 10.77638297791008, 4.4600870331845845, 3.784629963478468, 1.3922270255735079, 1.0306197112466604, 0.6542503178182191, 0.25499839303366445, 0.12150363045195496, 0.06788887358293033
                ],
                "RH2M": None,
                "SHGT": 112.0,
                "SPHU": [
                    4.0, 3.5, 3.0, 2.8, 3.1, 3.3, 2.7, 2.1, 1.4, 1.4, 1.6, 0.91, 0.5, 0.52, 0.68, 0.74, 0.58, 0.36, 0.2, 0.1, 0.03, 0.02, 0.02, 0.01, 0.01, 0.004, 0.003, 0.002, 0.001, 0.001, 0.002
                ],
                "T02M": 18.2,
                "TEMP": [
                    19.7, 21.3, 21.7, 21.6, 21.5, 20.8, 19.6, 17.1, 14.0, 11.0, 8.1, 4.4, -1.9, -8.6, -15.3, -21.7, -28.0, -34.7, -41.6, -47.9, -52.7, -55.2, -56.0, -56.2, -56.8, -58.3, -60.6, -63.0, -64.4, -63.0, -62.2
                ],
                "TO2M": None,
                "TPOT": [
                    293.4, 295.6, 296.9, 298.1, 299.5, 300.7, 302.0, 302.8, 303.9, 305.2, 306.9, 310.0, 312.6, 314.9, 317.0, 319.7, 322.5, 325.0, 327.1, 330.1, 335.7, 345.1, 358.1, 373.0, 387.9, 401.7, 414.4, 427.2, 442.5, 464.6, 486.2
                ],
                "TPP3": None,
                "TPP6": None,
                "TPPA": 0.0,
                "U10M": 0.8,
                "UWND": [
                    0.45, 3.0, 5.1, 6.0, 3.7, 1.1, -0.46, -0.44, 1.7, 2.5, 3.2, 3.1, 3.2, 3.8, 5.0, 8.3, 11.7, 14.4, 16.4, 17.9, 19.3, 20.8, 21.0, 18.6, 14.1, 8.9, 4.9, 3.5, 3.2, 2.3, -2.9
                ],
                "V10M": -3.7,
                "VWND": [
                    -7.0, -10.6, -11.8, -11.7, -10.7, -8.3, -5.3, -1.1, 1.2, 3.1, 5.3, 7.0, 7.9, 8.0, 10.3, 13.0, 14.7, 15.9, 16.7, 17.0, 17.5, 18.1, 17.3, 15.5, 12.9, 11.2, 9.4, 7.8, 8.7, 7.2, 3.8
                ],
                "WDIR": [
                    356.6, 344.4, 336.7, 333.3, 341.1, 352.7, 5.3, 22.2, 235.8, 218.7, 211.2, 204.2, 202.3, 205.3, 206.2, 212.9, 218.7, 222.5, 224.9, 226.8, 228.1, 229.3, 230.8, 230.5, 227.9, 218.9, 207.6, 204.2, 200.5, 198.1, 143.0
                ],
                "WSPD": [
                    7.0, 11.0, 12.8, 13.1, 11.3, 8.4, 5.3, 1.2, 2.1, 4.0, 6.2, 7.7, 8.6, 8.9, 11.5, 15.4, 18.8, 21.5, 23.4, 24.6, 26.1, 27.5, 27.2, 24.2, 19.1, 14.3, 10.6, 8.6, 9.3, 7.6, 4.8
                ],
                "WWND": [
                    14.1, 28.2, 28.2, 42.1, 42.2, 53.4, 44.2, 27.3, 12.2, 0.0, 0.0, -6.8, -13.0, -11.6, -5.1, 0.0, 0.0, -13.1, -18.3, -18.1, -15.9, -6.3, 2.2, 7.6, 5.8, 2.3, 0.82, 0.21, 0.1, 0.32, -33.2
                ],
                "dew_point": [
                    0.5340983752879538, -1.44921062431888, -3.7374634180685575, -4.869848632742503, -3.7455641148491736, -3.2122962155935966, -6.324158058926912, -10.182927921109183, -15.989194165297647, -16.668717537803673, -15.735034537288072, -23.588996146564483, -31.680595198427824, -32.56855272395978, -30.973736381543745, -31.475772808718943, -35.538000402285576, -41.911369337949026, -49.046232305319734, -56.75575521826815, -68.13201374982145, -72.67272801015753, -74.07333318580058, -80.58215164914026, -82.18530467530584, -89.88148474229067, -93.39909193343084, -97.60995134201852, -98.58758642363296, -97.60995134201852, -97.05226666666667
                ],
                "lat": 37.4316976,
                "lng": -120.3990506,
                "pressure": [
                    993.0, 985.0, 973.0, 959.0, 941.0, 919.0, 892.0, 855.0, 811.0, 767.0, 723.0, 662.0, 588.0, 520.0, 459.0, 402.0, 351.0, 304.0, 262.0, 224.0, 190.0, 158.0, 131.0, 106.0, 84.0, 65.0, 49.0, 35.0, 23.0, 13.0, 4.0
                ],
                "pressure_at_surface": 0.0,
                "sunrise_hour": 5.0,
                "sunset_hour": 19.0
            }
        }
        fire_area = 200

        expected_plumerise = {
            "2014-05-29T22:00:00": {
                "percentile_000": 36.64500890444568,
                "percentile_005": 38.47725934966797,
                "percentile_010": 40.309509794890246,
                "percentile_015": 42.14176024011253,
                "percentile_020": 43.97401068533482,
                "percentile_025": 45.806261130557104,
                "percentile_030": 47.63851157577939,
                "percentile_035": 49.47076202100167,
                "percentile_040": 51.303012466223954,
                "percentile_045": 53.13526291144623,
                "percentile_050": 54.96751335666852,
                "percentile_055": 56.799763801890805,
                "percentile_060": 58.63201424711309,
                "percentile_065": 60.46426469233538,
                "percentile_070": 62.29651513755766,
                "percentile_075": 64.12876558277995,
                "percentile_080": 65.96101602800223,
                "percentile_085": 67.7932664732245,
                "percentile_090": 69.62551691844679,
                "percentile_095": 71.45776736366908,
                "percentile_100": 73.29001780889136,
                "smolder_fraction": 0.0
            }
        }
        actual = SEVPlumeRise().compute(local_met, fire_area)
        assert expected_plumerise == actual['hours']
