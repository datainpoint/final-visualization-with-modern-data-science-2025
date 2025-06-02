# final-visualization-with-modern-data-science-2025
Final: Visualization with Modern Data Science 2025.

## 01. Define a function `check_data_type()` which returns the data type of input via a `dict`.

```python
def check_data_type(x) -> dict:
    """
    >>> check_data_type(1)
    {'int': True, 'float': False, 'bool': False, 'str': False, 'NoneType': False}
    >>> check_data_type(1.0)
    {'int': False, 'float': True, 'bool': False, 'str': False, 'NoneType': False}
    >>> check_data_type(False)
    {'int': False, 'float': False, 'bool': True, 'str': False, 'NoneType': False}
    >>> check_data_type('5566')
    {'int': False, 'float': False, 'bool': False, 'str': True, 'NoneType': False}
    >>> check_data_type(None)
    {'int': False, 'float': False, 'bool': False, 'str': False, 'NoneType': True}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `check_data_structure()` which returns the data structure of input via a `dict`.

```python
def check_data_structure(x) -> dict:
    """
    >>> check_data_structure([2, 3, 5, 7, 11])
    {'list': True, 'tuple': False, 'dict': False, 'set': False}
    >>> check_data_structure((2, 3, 5, 7, 11))
    {'list': False, 'tuple': True, 'dict': False, 'set': False}
    >>> check_data_structure({'0': 2, '1': 3, '2': 5, '3': 7, '4': 11})
    {'list': False, 'tuple': False, 'dict': True, 'set': False}
    >>> check_data_structure({2, 3, 5, 7, 11})
    {'list': False, 'tuple': False, 'dict': False, 'set': True}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `manipulate_a_list()` which returns a given `list` with ascending, descending, or reversed order.

```python
def manipulate_a_list(x: list, order: str) -> list:
    """
    >>> manipulate_a_list([3, 2, 5, 11, 7], order='asc')
    [2, 3, 5, 7, 11]
    >>> manipulate_a_list([3, 2, 5, 11, 7], order='desc')
    [11, 7, 5, 3, 2]
    >>> manipulate_a_list([3, 2, 5, 11, 7], order='reverse')
    [7, 11, 5, 2, 3]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `is_prime()` which returns whether a given `int` is a prime number or not.

Source: https://en.wikipedia.org/wiki/Prime_number

```python
def is_prime(x: int) -> bool:
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `multiple_is_prime()` which returns whether a given `int` is a prime number or not in a `list`.

Source: https://en.wikipedia.org/wiki/Prime_number

```python
def multiple_is_prime(x: list) -> list:
    """
    >>> multiple_is_prime([1, 2, 3, 4, 5])
    [False, True, True, False, True]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `explain_mpa_rating()` which returns the description of a given MPA rating.

Souce: <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>

```python
def explain_mpa_rating(x: str) -> str:
    """
    >>> explain_mpa_rating("G")
    'General Audiences'
    >>> explain_mpa_rating("PG")
    'Parental Guidance Suggested'
    >>> explain_mpa_rating("PG-13")
    'Parents Strongly Cautioned'
    >>> explain_mpa_rating("R")
    'Restricted'
    >>> explain_mpa_rating("NC-17")
    'Adults Only'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `explain_multiple_mpa_ratings()` which returns the description of a given MPA ratings in a `list`.

Souce: <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>

```python
def explain_multiple_mpa_ratings(x: list) -> list:
    """
    >>> explain_multiple_mpa_ratings(["G", "PG", "PG-13", "R", "NC-17"])
    ['General Audiences', 'Parental Guidance Suggested', 'Parents Strongly Cautioned', 'Restricted', 'Adults Only']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `import_movies_parent_guides_csv()` which imports `movies.csv` and `parent_guides.csv` in working directory as Pandas DataFrames.

```python
def import_movies_parent_guides_csv() -> tuple:
    """
    >>> movies, parent_guides = import_movies_parent_guides_csv()
    >>> movies.shape
    (250, 6)
    >>> parent_guides.shape
    (8, 2)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `summarize_mpa_counts()` which summarizes the number of movies by `parent_guide_id`.

PS. The `'NULL'` in demo output is actually a string rather than a NULL value.

```python
def summarize_mpa_counts(df_x: pd.core.frame.DataFrame, df_y: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """
    >>> movies, parent_guides = import_movies_parent_guides_csv()
    >>> summarize_mpa_counts(movies, parent_guides)
        parent_guide_id parent_guide  number_of_movies
    0                1     Approved                24
    1                2            G                19
    2                3        NC-17                 1
    3                4           PG                38
    4                5        PG-13                36
    5                6       Passed                 5
    6                7            R               102
    7                8         NULL                25
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `summarize_mpa_counts_with_explanation()` which summarizes the number of movies by `parent_guide_id` and regroup the non-US MPAs to `"Not Available"`.

Souce: <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>

```python
def summarize_mpa_counts_with_explanation(df_x: pd.core.frame.DataFrame, df_y: pd.core.frame.DataFrame) -> pd.core.series.Series:
    """
    >>> movies, parent_guides = import_movies_parent_guides_csv()
    >>> summarize_mpa_counts_with_explanation(movies, parent_guides)
    Adults Only                      1
    General Audiences               19
    Not Available                   54
    Parental Guidance Suggested     38
    Parents Strongly Cautioned      36
    Restricted                     102
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 11. Define a function `return_movies_mpa()` which returns MPA rating given movie's title.

Souce: <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>

```python
def return_movies_mpa(title: str, df_x: pd.core.frame.DataFrame, df_y: pd.core.frame.DataFrame) -> tuple:
    """
    >>> movies, parent_guides = import_movies_parent_guides_csv()
    >>> return_movies_mpa("The Shawshank Redemption", movies, parent_guides)
    (7, 'R', 'Restricted')
    >>> return_movies_mpa("The Dark Knight", movies, parent_guides)
    (5, 'PG-13', 'Parents Strongly Cautioned')
    >>> return_movies_mpa("Star Wars: Episode V - The Empire Strikes Back", movies, parent_guides)
    (4, 'PG', 'Parental Guidance Suggested')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 12. Define a function `import_time_series_confirmed_deaths()` which imports `time_series_covid19_confirmed_global.csv` and `time_series_covid19_deaths_global.csv` in working directory.

```python
def import_time_series_confirmed_deaths() -> tuple:
    """
    >>> time_series_confirmed, time_series_deaths = import_time_series_confirmed_deaths()
    >>> type(time_series_confirmed)
    pandas.core.frame.DataFrame
    >>> type(time_series_deaths)
    pandas.core.frame.DataFrame
    >>> time_series_confirmed.shape
    (289, 1147)
    >>> time_series_deaths.shape
    (289, 1147)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 13. Define a function `transform_time_series_confirmed_deaths()` which transforms both `time_series_covid19_confirmed_global.csv` and `time_series_covid19_deaths_global.csv` from wide format into long format.

```
       Province/State        Country/Region        Lat        Long     Date  \
0                 NaN           Afghanistan  33.939110   67.709953  1/22/20   
1                 NaN               Albania  41.153300   20.168300  1/22/20   
2                 NaN               Algeria  28.033900    1.659600  1/22/20   
3                 NaN               Andorra  42.506300    1.521800  1/22/20   
4                 NaN                Angola -11.202700   17.873900  1/22/20   
...               ...                   ...        ...         ...      ...   
330322            NaN    West Bank and Gaza  31.952200   35.233200   3/9/23   
330323            NaN  Winter Olympics 2022  39.904200  116.407400   3/9/23   
330324            NaN                 Yemen  15.552727   48.516388   3/9/23   
330325            NaN                Zambia -13.133897   27.849332   3/9/23   
330326            NaN              Zimbabwe -19.015438   29.154857   3/9/23   

        Confirmed  
0               0  
1               0  
2               0  
3               0  
4               0  
...           ...  
330322     703228  
330323        535  
330324      11945  
330325     343135  
330326     264276  

[330327 rows x 6 columns]
```

```
       Province/State        Country/Region        Lat        Long     Date  \
0                 NaN           Afghanistan  33.939110   67.709953  1/22/20   
1                 NaN               Albania  41.153300   20.168300  1/22/20   
2                 NaN               Algeria  28.033900    1.659600  1/22/20   
3                 NaN               Andorra  42.506300    1.521800  1/22/20   
4                 NaN                Angola -11.202700   17.873900  1/22/20   
...               ...                   ...        ...         ...      ...   
330322            NaN    West Bank and Gaza  31.952200   35.233200   3/9/23   
330323            NaN  Winter Olympics 2022  39.904200  116.407400   3/9/23   
330324            NaN                 Yemen  15.552727   48.516388   3/9/23   
330325            NaN                Zambia -13.133897   27.849332   3/9/23   
330326            NaN              Zimbabwe -19.015438   29.154857   3/9/23   

        Deaths  
0            0  
1            0  
2            0  
3            0  
4            0  
...        ...  
330322    5708  
330323       0  
330324    2159  
330325    4057  
330326    5671  

[330327 rows x 6 columns]
```


```python
def transform_time_series_confirmed_deaths() -> tuple:
    """
    >>> time_series_confirmed_long, time_series_deaths_long = transform_time_series_confirmed_deaths()
    >>> type(time_series_confirmed_long)
    pandas.core.frame.DataFrame
    >>> type(time_series_deaths_long)
    pandas.core.frame.DataFrame
    >>> time_series_confirmed_long.shape
    (330327, 6)
    >>> time_series_deaths_long.shape
    (330327, 6)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 14. Define a function `merge_time_series()` which merges the long formatted `time_series_covid19_confirmed_global.csv` and `time_series_covid19_deaths_global.csv` into one data frame.

```
           Date Province/State        Country/Region        Lat        Long  \
0       1/22/20            NaN           Afghanistan  33.939110   67.709953   
1       1/22/20            NaN               Albania  41.153300   20.168300   
2       1/22/20            NaN               Algeria  28.033900    1.659600   
3       1/22/20            NaN               Andorra  42.506300    1.521800   
4       1/22/20            NaN                Angola -11.202700   17.873900   
...         ...            ...                   ...        ...         ...   
330322   3/9/23            NaN    West Bank and Gaza  31.952200   35.233200   
330323   3/9/23            NaN  Winter Olympics 2022  39.904200  116.407400   
330324   3/9/23            NaN                 Yemen  15.552727   48.516388   
330325   3/9/23            NaN                Zambia -13.133897   27.849332   
330326   3/9/23            NaN              Zimbabwe -19.015438   29.154857   

        Confirmed  Deaths  
0               0       0  
1               0       0  
2               0       0  
3               0       0  
4               0       0  
...           ...     ...  
330322     703228    5708  
330323        535       0  
330324      11945    2159  
330325     343135    4057  
330326     264276    5671  

[330327 rows x 7 columns]
```

```python
def merge_time_series() -> pd.core.frame.DataFrame:
    """
    >>> merged_time_series = merge_time_series()
    >>> type(merged_time_series)
    pandas.core.frame.DataFrame
    >>> merged_time_series.shape
    (330327, 7)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 15. Define a function `groupby_date_country()` which summarizes `Confirmed` and `Death` by `Date` and `Country/Region` given merged, long formatted time_series dataframe.

```
          Date        Country/Region  Confirmed  Deaths
0       1/1/21           Afghanistan      52513    2201
1       1/1/21               Albania      58316    1181
2       1/1/21               Algeria      99897    2762
3       1/1/21               Andorra       8117      84
4       1/1/21                Angola      17568     405
...        ...                   ...        ...     ...
229738  9/9/22    West Bank and Gaza     702591    5706
229739  9/9/22  Winter Olympics 2022        535       0
229740  9/9/22                 Yemen      11932    2155
229741  9/9/22                Zambia     333204    4017
229742  9/9/22              Zimbabwe     256859    5596

[229743 rows x 4 columns]
```

```python
def groupby_date_country() -> pd.core.frame.DataFrame:
    """
    >>> groupby_time_series = groupby_date_country()
    >>> type(groupby_time_series)
    pandas.core.frame.DataFrame
    >>> groupby_time_series.shape
    (229743, 4)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 16. Define a function `format_date_column()` which formats `Date` column with ISO-8601 format `yyyy-mm-dd`(`%Y-%m-%d`) given summarized time_series dataframe.

```
             Date        Country/Region  Confirmed  Deaths
0      2020-01-22           Afghanistan          0       0
1      2020-01-22               Albania          0       0
2      2020-01-22               Algeria          0       0
3      2020-01-22               Andorra          0       0
4      2020-01-22                Angola          0       0
...           ...                   ...        ...     ...
229738 2023-03-09    West Bank and Gaza     703228    5708
229739 2023-03-09  Winter Olympics 2022        535       0
229740 2023-03-09                 Yemen      11945    2159
229741 2023-03-09                Zambia     343135    4057
229742 2023-03-09              Zimbabwe     264276    5671

[229743 rows x 4 columns]
```

```python
def format_date_column() -> pd.core.frame.DataFrame:
    """
    >>> formatted_time_series = format_date_column()
    >>> type(formatted_time_series)
    pandas.core.frame.DataFrame
    >>> formatted_time_series.shape
    (229743, 4)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 17. Define a function `summarize_table_shapes()` which summarizes the shapes of table in `taiwan_election_2024.db` in working directory as a dataframe. Given table names as following: `["aboriginal_legislators", "candidates", "districts", "election_types", "parties", "party_legislators", "polling_places", "presidents", "regional_legislators", "villages"]`

```
                    table    rows  columns
0  aboriginal_legislators  338105        7
1              candidates     331        4
2               districts   17795        5
3          election_types       5        2
4                 parties      35        2
5       party_legislators  284720        7
6          polling_places   88975        8
7              presidents   53385        7
8    regional_legislators   77032        8
9                villages    5227        2
```

```python
def summarize_table_shapes() -> pd.core.frame.DataFrame:
    """
    >>> table_shapes = summarize_table_shapes()
    >>> type(table_shapes)
    pandas.core.frame.DataFrame
    >>> table_shapes.shape
    (10, 3)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 18. Define a function `summarize_presidential_votes()` which summarizes the votes of president/vice president election.

```
   party candidates    votes
0  民主進步黨    賴清德/蕭美琴  5586019
1  中國國民黨    侯友宜/趙少康  4671021
2  台灣民眾黨    柯文哲/吳欣盈  3690466
```

```python
def summarize_presidential_votes() -> pd.core.frame.DataFrame:
    """
    >>> presidential_votes = summarize_presidential_votes()
    >>> type(presidential_votes)
    pandas.core.frame.DataFrame
    >>> presidential_votes.shape
    (3, 3)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 19. Define a function `summarize_regional_aborinal_legislator_votes()` which summarizes the votes of regional and aboriginal legislator election by party.

```
   election_type      party    votes
0       區域及原住民立委      民主進步黨  6095276
1       區域及原住民立委      中國國民黨  5510850
2       區域及原住民立委          無  1069758
3       區域及原住民立委      台灣民眾黨   403357
4       區域及原住民立委       時代力量    96589
5       區域及原住民立委  小民參政歐巴桑聯盟    78138
6       區域及原住民立委      社會民主黨    74375
7       區域及原住民立委    臺灣雙語無法黨    55937
8       區域及原住民立委      司法改革黨    38685
9       區域及原住民立委       台灣維新    33347
10      區域及原住民立委       台灣基進    32583
11      區域及原住民立委      人民最大黨    25216
12      區域及原住民立委       台灣綠黨    15557
13      區域及原住民立委      喜樂島聯盟    15433
14      區域及原住民立委    中華統一促進黨    13203
15      區域及原住民立委      制度救世島    11260
16      區域及原住民立委         新黨     9143
17      區域及原住民立委    台灣麻將最大黨     7839
18      區域及原住民立委      復康聯盟黨     7441
19      區域及原住民立委        勞動黨     6453
20      區域及原住民立委      司法正義黨     6331
21      區域及原住民立委      中華聯合黨     4139
22      區域及原住民立委      台灣國民黨     3293
23      區域及原住民立委      台灣革命黨     3072
24      區域及原住民立委    中華文化共和黨     2583
25      區域及原住民立委     家庭基本收入     2361
26      區域及原住民立委  台灣整復師聯盟工黨     1881
27      區域及原住民立委      中華婦女黨     1029
28      區域及原住民立委      人民民主黨      836
29      區域及原住民立委        經濟黨      472
30      區域及原住民立委    中華愛國同心黨      310
31      區域及原住民立委     合一行動聯盟      174
32      區域及原住民立委      興中同盟會      136
```

```python
def summarize_regional_aborinal_legislator_votes() -> pd.core.frame.DataFrame:
    """
    >>> regional_aborinal_legislator_votes = summarize_regional_aborinal_legislator_votes()
    >>> type(regional_aborinal_legislator_votes)
    pandas.core.frame.DataFrame
    >>> regional_aborinal_legislator_votes.shape
    (33, 3)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 20. Define a function `summarize_party_legislator_votes()` which summarizes the votes of party legislator election.

```
   election_type      party    votes
0          不分區立委      民主進步黨  4982062
1          不分區立委      中國國民黨  4764576
2          不分區立委      台灣民眾黨  3040615
3          不分區立委       時代力量   353412
4          不分區立委  小民參政歐巴桑聯盟   128613
5          不分區立委       台灣綠黨   117298
6          不分區立委       台灣基進    95078
7          不分區立委        親民黨    69818
8          不分區立委    臺灣雙語無法黨    44852
9          不分區立委     台灣團結聯盟    43375
10         不分區立委         新黨    40288
11         不分區立委      司法改革黨    37615
12         不分區立委      制度救世島    19665
13         不分區立委    中華統一促進黨    17423
14         不分區立委      人民最大黨    11746
15         不分區立委       台灣維新    10300
```

```python
def summarize_party_legislator_votes() -> pd.core.frame.DataFrame:
    """
    >>> party_legislator_votes = summarize_party_legislator_votes()
    >>> type(party_legislator_votes)
    pandas.core.frame.DataFrame
    >>> party_legislator_votes.shape
    (16, 3)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```