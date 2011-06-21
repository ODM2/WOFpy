import unittest
import private_config

sys.path.append('../implementations/')

from daos.odm.odm_dao import OdmDao


class TestOdmDao(unittest.TestCase):
    def setUp(self):
        self.dao = OdmDao(private_config.lbr_connection_string)

        self.known_site_codes = (
            'USU-LBR-Mendon',
            'USU-LBR-Paradise',
            'USU-LBR-ExpFarm',
            'USU-LBR-SFLower',
            'USU-LBR-EFLower',
            'USU-LBR-EFWeather',
            'USU-LBR-SFUpper',
            'USU-LBR-ParadiseRepeater',
            'USU-LBR-EFRepeater',
            'USU-LBR-Wellsville',
            'USU-LBR-Confluence',
            '10105900'
        )

        self.fake_codes = (
            'junk',
            'trash',
            'fake'
        )

        self.known_var_codes = (
            'USU3',
            'USU4',
            'USU5',
            'USU6',
            'USU7',
            'USU8',
            'USU9',
            'USU10',
            'USU11',
            'USU12',
            'USU13',
            'USU14',
            'USU15',
            'USU16',
            'USU17',
            'USU18',
            'USU19',
            'USU20',
            'USU21',
            'USU22',
            'USU23',
            'USU24',
            'USU25',
            'USU26',
            'USU27',
            'USU28',
            'USU29',
            'USU30',
            'USU31',
            'USU32',
            'USU33',
            'USU34',
            'USU35',
            'USU36',
            'USU37',
            'USU38',
            'USU39',
            'USU40',
            'USU41',
            'USU42',
            'USU43'
        )

        self.known_series = [
            ('USU-LBR-Mendon','USU3','2005-08-04 18:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU4','2005-08-04 18:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU5','2005-08-04 18:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU6','2005-08-04 18:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU7','2005-08-04 18:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU8','2005-08-04 18:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU9','2005-08-04 18:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU10','2005-08-04 18:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU11','2005-08-04 18:30:00.000','2007-08-16 20:30:00.000'),
            ('USU-LBR-Mendon','USU12','2005-08-04 18:30:00.000','2007-08-16 20:30:00.000'),
            ('USU-LBR-Mendon','USU13','2005-08-04 18:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU32','2007-08-16 23:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU33','2007-08-16 23:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU34','2007-08-16 23:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU35','2007-08-16 23:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU36','2007-08-16 23:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU37','2007-08-16 23:30:00.000','2008-03-27 19:30:00.000'),
            ('USU-LBR-Mendon','USU39','2007-10-04 19:00:00.000','2008-02-12 22:15:00.000'),
            ('USU-LBR-Mendon','USU39','2005-04-28 03:00:00.000','2007-06-07 21:20:00.000'),
            ('USU-LBR-Mendon','USU40','2007-10-04 19:00:00.000','2008-02-12 22:15:00.000'),
            ('USU-LBR-Mendon','USU40','2005-10-28 04:30:00.000','2007-06-07 21:20:00.000'),
            ('USU-LBR-Mendon','USU41','2007-10-04 19:00:00.000','2008-02-12 22:15:00.000'),
            ('USU-LBR-Mendon','USU41','2005-04-28 03:00:00.000','2007-06-07 21:20:00.000'),
            ('USU-LBR-Paradise','USU3','2005-06-29 21:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU4','2005-06-29 21:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU5','2005-06-29 21:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU6','2005-06-29 21:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU7','2005-06-29 21:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU8','2005-06-29 21:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU9','2005-06-29 21:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU10','2005-06-29 21:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU32','2007-08-16 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU33','2007-08-16 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU34','2007-08-16 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU35','2007-08-16 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU36','2007-08-16 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Paradise','USU39','2005-05-20 04:30:00.000','2007-06-07 21:40:00.000'),
            ('USU-LBR-Paradise','USU39','2007-10-04 18:00:00.000','2008-02-12 20:55:00.000'),
            ('USU-LBR-Paradise','USU40','2005-10-04 21:32:00.000','2007-06-07 21:40:00.000'),
            ('USU-LBR-Paradise','USU40','2007-10-04 18:00:00.000','2008-02-12 20:55:00.000'),
            ('USU-LBR-Paradise','USU41','2005-05-20 04:30:00.000','2007-06-07 21:40:00.000'),
            ('USU-LBR-Paradise','USU41','2007-10-04 18:00:00.000','2008-02-12 20:55:00.000'),
            ('USU-LBR-ExpFarm','USU14','2007-06-29 21:00:00.000','2008-04-09 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU15','2007-06-29 21:00:00.000','2008-04-09 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU16','2007-06-29 21:00:00.000','2008-04-09 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU17','2007-06-29 21:00:00.000','2008-04-09 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU18','2007-07-06 22:00:00.000','2008-04-09 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU19','2007-07-06 22:00:00.000','2008-04-09 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU20','2007-07-06 22:00:00.000','2008-04-09 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU21','2007-07-11 22:00:00.000','2008-04-09 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU22','2007-07-06 22:00:00.000','2008-04-09 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU23','2007-07-07 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU24','2007-07-07 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU25','2007-07-08 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU26','2007-07-07 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU27','2007-07-08 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU28','2007-07-07 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU29','2007-07-13 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU30','2007-07-07 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-ExpFarm','USU31','2007-07-07 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-SFLower','USU3','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU4','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU5','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU6','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU7','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU8','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU9','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU10','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU13','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU32','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU33','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU34','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU35','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU36','2007-07-26 20:00:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFLower','USU39','2007-10-04 16:00:00.000','2008-02-12 18:10:00.000'),
            ('USU-LBR-SFLower','USU40','2007-10-04 16:00:00.000','2008-02-12 18:10:00.000'),
            ('USU-LBR-SFLower','USU41','2007-10-04 16:00:00.000','2008-02-12 18:10:00.000'),
            ('USU-LBR-EFLower','USU3','2007-08-02 19:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU4','2007-08-02 19:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU5','2007-08-02 19:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU6','2007-08-02 19:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU7','2007-08-02 19:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU8','2007-08-02 19:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU9','2007-08-02 19:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU10','2007-08-02 19:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU13','2007-08-02 19:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU32','2007-08-02 19:30:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU33','2007-08-02 19:30:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU34','2007-08-02 20:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU35','2007-08-02 19:30:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU36','2007-08-02 19:30:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFLower','USU39','2007-10-04 17:00:00.000','2008-02-12 19:25:00.000'),
            ('USU-LBR-EFLower','USU40','2007-10-04 17:00:00.000','2008-02-12 19:25:00.000'),
            ('USU-LBR-EFLower','USU41','2007-10-04 17:00:00.000','2008-02-12 19:25:00.000'),
            ('USU-LBR-EFWeather','USU14','2007-08-03 22:00:00.000','2008-04-09 02:00:00.000'),
            ('USU-LBR-EFWeather','USU15','2007-08-03 20:00:00.000','2008-04-09 02:00:00.000'),
            ('USU-LBR-EFWeather','USU16','2007-08-03 20:00:00.000','2008-04-09 02:00:00.000'),
            ('USU-LBR-EFWeather','USU17','2007-08-03 20:00:00.000','2008-04-09 02:00:00.000'),
            ('USU-LBR-EFWeather','USU18','2007-08-03 20:00:00.000','2008-04-09 02:00:00.000'),
            ('USU-LBR-EFWeather','USU19','2007-08-03 20:00:00.000','2008-04-09 02:00:00.000'),
            ('USU-LBR-EFWeather','USU20','2007-08-03 20:00:00.000','2008-04-09 02:00:00.000'),
            ('USU-LBR-EFWeather','USU21','2007-08-03 20:00:00.000','2008-04-09 02:00:00.000'),
            ('USU-LBR-EFWeather','USU22','2007-08-03 20:00:00.000','2008-04-09 02:00:00.000'),
            ('USU-LBR-EFWeather','USU23','2007-08-04 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-EFWeather','USU24','2007-08-04 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-EFWeather','USU25','2007-08-05 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-EFWeather','USU26','2007-08-05 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-EFWeather','USU27','2007-08-05 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-EFWeather','USU28','2007-08-04 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-EFWeather','USU29','2007-08-05 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-EFWeather','USU30','2007-08-04 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-EFWeather','USU31','2007-08-04 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-SFUpper','USU3','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU4','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU5','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU6','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU7','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU8','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU9','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU10','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU13','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU32','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU33','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU34','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU35','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU36','2007-10-31 21:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-SFUpper','USU39','2007-11-07 17:00:00.000','2008-02-12 17:25:00.000'),
            ('USU-LBR-SFUpper','USU40','2007-11-07 17:00:00.000','2008-02-12 17:25:00.000'),
            ('USU-LBR-SFUpper','USU41','2007-11-07 17:00:00.000','2008-02-12 17:25:00.000'),
            ('USU-LBR-ParadiseRepeater','USU3','2007-10-29 23:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-ParadiseRepeater','USU23','2007-10-30 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-ParadiseRepeater','USU38','2007-10-29 23:00:00.000','2008-04-09 08:30:00.000'),
            ('USU-LBR-EFRepeater','USU3','2007-10-29 23:00:00.000','2008-04-09 09:00:00.000'),
            ('USU-LBR-EFRepeater','USU23','2007-10-30 06:00:00.000','2008-04-08 07:00:00.000'),
            ('USU-LBR-EFRepeater','USU38','2007-10-29 23:00:00.000','2008-04-09 09:00:00.000'),
            ('USU-LBR-Wellsville','USU3','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU4','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU5','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU6','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU7','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU8','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU9','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU10','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU13','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU32','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU33','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU34','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU35','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU36','2007-11-05 21:30:00.000','2008-04-06 03:30:00.000'),
            ('USU-LBR-Wellsville','USU39','2007-11-07 20:00:00.000','2008-02-12 21:40:00.000'),
            ('USU-LBR-Wellsville','USU40','2007-11-07 20:00:00.000','2008-02-12 21:40:00.000'),
            ('USU-LBR-Wellsville','USU41','2007-11-07 20:00:00.000','2008-02-12 21:40:00.000'),
            ('USU-LBR-Confluence','USU3','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU4','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU5','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU6','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU7','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU8','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU9','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU10','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU13','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU32','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU33','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU34','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU35','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU36','2007-11-15 00:30:00.000','2008-04-09 21:00:00.000'),
            ('USU-LBR-Confluence','USU39','2007-11-21 19:00:00.000','2008-02-12 20:05:00.000'),
            ('USU-LBR-Confluence','USU40','2007-11-21 19:00:00.000','2008-02-12 20:05:00.000'),
            ('USU-LBR-Confluence','USU41','2007-11-21 19:00:00.000','2008-02-12 20:05:00.000'),
            ('10105900','USU42','2007-12-16 07:00:00.000','2008-04-09 22:45:00.000'),
            ('10105900','USU43','2007-12-16 07:00:00.000','2008-04-09 22:45:00.000')
        ]

    def test_get_all_sites(self):
        siteResultList = self.dao.get_all_sites()
        resultSiteCodes = [s.SiteCode for s in siteResultList]
        for known_code in self.known_site_codes:
            self.assertTrue(known_code in resultSiteCodes)

    def test_get_site_by_code(self):
        for known_code in self.known_site_codes:
            siteResult = self.dao.get_site_by_code(known_code)
            self.assertEqual(known_code, siteResult.SiteCode)

    def test_get_sites_by_codes(self):
        siteResultList = self.dao.get_sites_by_codes(self.known_site_codes)
        resultSiteCodes = [s.SiteCode for s in siteResultList]
        for known_code in self.known_site_codes:
            self.assertTrue(known_code in resultSiteCodes)

    def test_get_all_variables(self):
        varResultList = self.dao.get_all_variables()
        resultVarCodes = [v.VariableCode for v in varResultList]
        for known_code in self.known_var_codes:
            self.assertTrue(known_code in resultVarCodes)

    def test_get_var_by_code(self):
        for known_code in self.known_var_codes:
            varResult = self.dao.get_variable_by_code(known_code)
            self.assertEqual(known_code, varResult.VariableCode)

    def test_get_vars_by_codes(self):
        varResultList = self.dao.get_variables_by_codes(self.known_var_codes)
        resultVarCodes = [v.VariableCode for v in varResultList]
        for known_code in self.known_var_codes:
            self.assertTrue(known_code in resultVarCodes)
