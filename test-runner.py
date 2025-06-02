import unittest
import importlib
import sqlite3
import pandas as pd

class TestFinal(unittest.TestCase):
    def test_01(self):
        self.assertEqual(asgmt.check_data_type(1), {'int': True, 'float': False, 'bool': False, 'str': False, 'NoneType': False})
        self.assertEqual(asgmt.check_data_type(1.0), {'int': False, 'float': True, 'bool': False, 'str': False, 'NoneType': False})
        self.assertEqual(asgmt.check_data_type(False), {'int': False, 'float': False, 'bool': True, 'str': False, 'NoneType': False})
        self.assertEqual(asgmt.check_data_type("5566"), {'int': False, 'float': False, 'bool': False, 'str': True, 'NoneType': False})
        self.assertEqual(asgmt.check_data_type(None), {'int': False, 'float': False, 'bool': False, 'str': False, 'NoneType': True})
    def test_02(self):
        self.assertEqual(asgmt.check_data_structure([2, 3, 5, 7, 11]), {'list': True, 'tuple': False, 'dict': False, 'set': False})
        self.assertEqual(asgmt.check_data_structure((2, 3, 5, 7, 11)), {'list': False, 'tuple': True, 'dict': False, 'set': False})
        self.assertEqual(asgmt.check_data_structure({'0': 2, '1': 3, '2': 5, '3': 7, '4': 11}), {'list': False, 'tuple': False, 'dict': True, 'set': False})
        self.assertEqual(asgmt.check_data_structure({2, 3, 5, 7, 11}), {'list': False, 'tuple': False, 'dict': False, 'set': True})
    def test_03(self):
        self.assertEqual(asgmt.manipulate_a_list([3, 2, 5, 11, 7], order='asc'), [2, 3, 5, 7, 11])
        self.assertEqual(asgmt.manipulate_a_list([3, 2, 5, 11, 7], order='desc'), [11, 7, 5, 3, 2])
        self.assertEqual(asgmt.manipulate_a_list([3, 2, 5, 11, 7], order='reverse'), [7, 11, 5, 2, 3])
        self.assertEqual(asgmt.manipulate_a_list([3, 2, 5], order='asc'), [2, 3, 5])
        self.assertEqual(asgmt.manipulate_a_list([3, 2, 5], order='desc'), [5, 3, 2])
        self.assertEqual(asgmt.manipulate_a_list([3, 2, 5], order='reverse'), [5, 2, 3])
    def test_04(self):
        self.assertFalse(asgmt.is_prime(1))
        self.assertTrue(asgmt.is_prime(2))
        self.assertTrue(asgmt.is_prime(3))
        self.assertFalse(asgmt.is_prime(4))
        self.assertTrue(asgmt.is_prime(5))
        self.assertFalse(asgmt.is_prime(6))
        self.assertTrue(asgmt.is_prime(7))
    def test_05(self):
        self.assertEqual(asgmt.multiple_is_prime([1, 2, 3, 4, 5]), [False, True, True, False, True])
        self.assertEqual(asgmt.multiple_is_prime([6, 7]), [False, True])
        self.assertEqual(asgmt.multiple_is_prime([8, 9, 10]), [False, False, False])
    def test_06(self):
        self.assertEqual(asgmt.explain_mpa_rating("G"), 'General Audiences')
        self.assertEqual(asgmt.explain_mpa_rating("PG"), 'Parental Guidance Suggested')
        self.assertEqual(asgmt.explain_mpa_rating("PG-13"), 'Parents Strongly Cautioned')
        self.assertEqual(asgmt.explain_mpa_rating("R"), 'Restricted')
        self.assertEqual(asgmt.explain_mpa_rating("NC-17"), 'Adults Only')
    def test_07(self):
        self.assertEqual(asgmt.explain_multiple_mpa_ratings(["G"]), ['General Audiences'])
        self.assertEqual(asgmt.explain_multiple_mpa_ratings(["PG"]), ['Parental Guidance Suggested'])
        self.assertEqual(asgmt.explain_multiple_mpa_ratings(["PG-13"]), ['Parents Strongly Cautioned'])
        self.assertEqual(asgmt.explain_multiple_mpa_ratings(["R"]), ['Restricted'])
        self.assertEqual(asgmt.explain_multiple_mpa_ratings(["NC-17"]), ['Adults Only'])
    def test_08(self):
        movies, parent_guides = asgmt.import_movies_parent_guides_csv()
        self.assertEqual(movies.shape, (250, 6))
        self.assertEqual(parent_guides.shape, (8, 2))
    def test_09(self):
        movies, parent_guides = asgmt.import_movies_parent_guides_csv()
        ans = asgmt.summarize_mpa_counts(movies, parent_guides)
        self.assertEqual(ans.shape, (8, 3))
        self.assertEqual(ans.iloc[:, 2].sum(), 250)
    def test_10(self):
        movies, parent_guides = asgmt.import_movies_parent_guides_csv()
        ans = asgmt.summarize_mpa_counts_with_explanation(movies, parent_guides)
        self.assertEqual(ans.size, 6)
        self.assertEqual(ans.sum(), 250)
    def test_11(self):
        movies, parent_guides = asgmt.import_movies_parent_guides_csv()
        self.assertEqual(asgmt.return_movies_mpa("The Shawshank Redemption", movies, parent_guides), (7, 'R', 'Restricted'))
        self.assertEqual(asgmt.return_movies_mpa("The Dark Knight", movies, parent_guides), (5, 'PG-13', 'Parents Strongly Cautioned'))
        self.assertEqual(asgmt.return_movies_mpa("Star Wars: Episode V - The Empire Strikes Back", movies, parent_guides), (4, 'PG', 'Parental Guidance Suggested'))
        self.assertEqual(asgmt.return_movies_mpa("The Godfather", movies, parent_guides), (7, 'R', 'Restricted'))
        self.assertEqual(asgmt.return_movies_mpa("Inception", movies, parent_guides), (5, 'PG-13', 'Parents Strongly Cautioned'))
    def test_12(self):
        time_series_confirmed, time_series_deaths = asgmt.import_time_series_confirmed_deaths()
        self.assertEqual(time_series_confirmed.shape, (289, 1147))
        self.assertEqual(time_series_deaths.shape, (289, 1147))
    def test_13(self):
        time_series_confirmed_long, time_series_deaths_long = asgmt.transform_time_series_confirmed_deaths()
        self.assertEqual(time_series_confirmed_long.shape, (330327, 6))
        self.assertEqual(time_series_deaths_long.shape, (330327, 6))
    def test_14(self):
        merged_time_series = asgmt.merge_time_series()
        self.assertEqual(merged_time_series.shape, (330327, 7))
    def test_15(self):
        groupby_time_series = asgmt.groupby_date_country()
        self.assertEqual(groupby_time_series.shape, (229743, 4))
    def test_16(self):
        formatted_time_series = asgmt.format_date_column()
        self.assertEqual(formatted_time_series.shape, (229743, 4))
    def test_17(self):
        table_shapes = asgmt.summarize_table_shapes()
        self.assertEqual(table_shapes.shape, (10, 3))
        self.assertEqual(table_shapes.iloc[:, 1].min(), 5)
        self.assertEqual(table_shapes.iloc[:, 2].min(), 2)
        self.assertEqual(table_shapes.iloc[:, 1].max(), 338105)
        self.assertEqual(table_shapes.iloc[:, 2].max(), 8)
        table_list = ["aboriginal_legislators", "candidates", "districts", "election_types", "parties", "party_legislators", "polling_places", "presidents", "regional_legislators", "villages"]
        table_names = table_shapes.iloc[:, 0].to_list()
        for tbl in table_list:
            self.assertIn(tbl, table_names)
    def test_18(self):
        presidential_votes = asgmt.summarize_presidential_votes()
        self.assertEqual(presidential_votes.shape, (3, 3))
        self.assertEqual(presidential_votes.iloc[:, 2].max(), 5586019)
        self.assertEqual(presidential_votes.iloc[:, 2].min(), 3690466)
        parties = presidential_votes.iloc[:, 0].to_list()
        candidates = presidential_votes.iloc[:, 1].to_list()
        for party in ["民主進步黨", "中國國民黨", "台灣民眾黨"]:
            self.assertIn(party, parties)
        for candidate in ["賴清德/蕭美琴", "侯友宜/趙少康", "柯文哲/吳欣盈"]:
            self.assertIn(candidate, candidates)
    def test_19(self):
        regional_aborinal_legislator_votes = asgmt.summarize_regional_aborinal_legislator_votes()
        self.assertEqual(regional_aborinal_legislator_votes.shape, (33, 3))
        election_types = regional_aborinal_legislator_votes.iloc[:, 0].to_list()
        self.assertIn("區域及原住民立委", election_types)
        parties = regional_aborinal_legislator_votes.iloc[:, 1].to_list()
        for party in ["民主進步黨", "中國國民黨", "台灣民眾黨", "小民參政歐巴桑聯盟", "社會民主黨", "時代力量", "無"]:
            self.assertIn(party, parties)
    def test_20(self):
        party_legislator_votes = asgmt.summarize_party_legislator_votes()
        self.assertEqual(party_legislator_votes.shape, (16, 3))
        election_types = party_legislator_votes.iloc[:, 0].to_list()
        self.assertIn("不分區立委", election_types)
        parties = party_legislator_votes.iloc[:, 1].to_list()
        for party in ["民主進步黨", "中國國民黨", "台灣民眾黨", "小民參政歐巴桑聯盟", "台灣綠黨", "時代力量"]:
            self.assertIn(party, parties)
        
asgmt = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestFinal)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")