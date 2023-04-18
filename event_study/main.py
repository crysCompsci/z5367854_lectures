
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
""" main.py

Main module for the event_study package. Will run the event study for a single
stock.
"""
from event_study import download
from event_study import mk_rets
from event_study import mk_events
from event_study import mk_cars
from event_study import test_hypo


def main(tic, update_csv=True):
    """ Implements the event study for a given stock ticker `tic`.

    Parameters
    ----------
    tic : str
        Ticker

    update_csv : bool
        If True, data will be downloaded. Defaults to True.

    Notes
    -----
    This function will perform the following tasks:

    Step 1: download.get_data(tic)
      Download stock price and recommendation data for a given `tic` and create
      the files <prc csv> and <rec csv>

    Step 2: mk_rets.mk_ret_df(tic) --> dataframe
      For a given `tic`, create stock returns from `<prc csv>` and join the market
      returns.

    Step 3: mk_events.mk_event_df(tic) --> dataframe
      Process the recommendations in `<rec csv>` and create a data frame with the
      events of interest.

    Step 4: mk_cars.mk_cars_df(ret_df, event_df) --> dataframe
      Creates a dataframe with the CARs for each event of interest, where:
      `ret_df` : dataframe
          Output of `mk_rets.mk_ret_df`
      `event_df` : dataframe
          Output of `mk_events.mk_event_df`

    Step 5: test_hypo.calc_tstats(cars_df)
      Hypothesis testing using t-statistics, where
      `car_df` : dataframe
        The output of mk_cars.mk_cars_df(ret_df, event_df)


    """
    # Step 1: Download stock price and recommendation data for `tic`
    if update_csv is True:
        download.get_data(tic)
    else:
        print("Parameter `update_csv` set to False, skipping downloads...")

    # Step 2: Create a data frame with stock (tic) and market returns
    ret_df = mk_rets.mk_ret_df(tic)

    # Step 3: Create a data frame with the events
    event_df = mk_events.mk_event_df(tic)

    # Step 4: Calculate CARs for each event
    cars_df = mk_cars.mk_cars_df(ret_df, event_df)

    # Step 5: Hypothesis testing using t-statistics
    res = test_hypo.calc_tstats(cars_df)
    print(res)


if __name__ == "__main__":
    tic = 'TSLA'
    update_csv = False
    main(tic=tic, update_csv=update_csv)
