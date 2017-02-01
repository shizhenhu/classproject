# import pandas as pd
# frame = {'name': pd.Series(['A', 'B', 'C', 'D'], index=[1, 2, 3, 4]),
#          'age': pd.Series([12, 42, 23, 45], index=[2, 1, 3, 4]),
#          'T or F': pd.Series([True, True, False, False], index=[1, 2, 3, 4])}
# df = pd.DataFrame(frame)
# print(df)

from pandas import DataFrame, Series
olympic_medal_counts = {'contries': Series(['Russian Fed.', 'Norway', 'Canada', 'United States',
                                            'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                                            'Austria', 'France', 'Poland', 'China', 'Korea',
                                            'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                                            'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                                            'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']),
                        'gold': Series([13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]),
                        'silver': Series([11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]),
                        'bronze': Series([9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1])}
olympic_medal_counts_df = DataFrame(olympic_medal_counts)
print(olympic_medal_counts_df)

input("\n\nPress the enter key to exit.")