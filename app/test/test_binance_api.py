from app.api.endpoints.binance_api import binance_api

demo_data = [
    {
        "symbol": "CAKEBNB",
        "priceChange": "0.00222000",
        "priceChangePercent": "4.983",
        "weightedAvgPrice": "0.04555490",
        "prevClosePrice": "0.04459000",
        "lastPrice": "0.04677000",
        "lastQty": "363.53000000",
        "bidPrice": "0.04677000",
        "bidQty": "959.57000000",
        "askPrice": "0.04682000",
        "askQty": "24.45000000",
        "openPrice": "0.04455000",
        "highPrice": "0.04758000",
        "lowPrice": "0.04354000",
        "volume": "564397.93000000",
        "quoteVolume": "25711.09046400",
        "openTime": 1633630765874,
        "closeTime": 1633717165874,
        "firstId": 7473561,
        "lastId": 7483807,
        "count": 10247,
    },
    {
        "symbol": "BETABTC",
        "priceChange": "0.00005803",
        "priceChangePercent": "5227.928",
        "weightedAvgPrice": "0.00006443",
        "prevClosePrice": "0.00000000",
        "lastPrice": "0.00005914",
        "lastQty": "70.00000000",
        "bidPrice": "0.00005911",
        "bidQty": "47.00000000",
        "askPrice": "0.00005919",
        "askQty": "5.00000000",
        "openPrice": "0.00000111",
        "highPrice": "0.00009480",
        "lowPrice": "0.00000111",
        "volume": "15969411.00000000",
        "quoteVolume": "1028.90462875",
        "openTime": 1633671540243,
        "closeTime": 1633757940243,
        "firstId": 0,
        "lastId": 125822,
        "count": 125823,
    },
    {
        "symbol": "BETABNB",
        "priceChange": "0.00748450",
        "priceChangePercent": "5415.702",
        "weightedAvgPrice": "0.00824652",
        "prevClosePrice": "0.00000000",
        "lastPrice": "0.00762270",
        "lastQty": "25.00000000",
        "bidPrice": "0.00760550",
        "bidQty": "877.00000000",
        "askPrice": "0.00762370",
        "askQty": "15.00000000",
        "openPrice": "0.00013820",
        "highPrice": "0.06000000",
        "lowPrice": "0.00013820",
        "volume": "29522440.00000000",
        "quoteVolume": "243457.45709740",
        "openTime": 1633671540168,
        "closeTime": 1633757940168,
        "firstId": 0,
        "lastId": 265658,
        "count": 265659,
    },
    {
        "symbol": "BETABUSD",
        "priceChange": "3.16355000",
        "priceChangePercent": "5269.071",
        "weightedAvgPrice": "3.50770798",
        "prevClosePrice": "0.00000000",
        "lastPrice": "3.22359000",
        "lastQty": "13.00000000",
        "bidPrice": "3.22047000",
        "bidQty": "620.00000000",
        "askPrice": "3.22359000",
        "askQty": "173.00000000",
        "openPrice": "0.06004000",
        "highPrice": "5.80000000",
        "lowPrice": "0.06004000",
        "volume": "139131459.00000000",
        "quoteVolume": "488032528.72984000",
        "openTime": 1633671540309,
        "closeTime": 1633757940309,
        "firstId": 0,
        "lastId": 1366427,
        "count": 1366428,
    },
    {
        "symbol": "BETAUSDT",
        "priceChange": "3.16220000",
        "priceChangePercent": "5269.455",
        "weightedAvgPrice": "3.51577929",
        "prevClosePrice": "0.00000000",
        "lastPrice": "3.22221000",
        "lastQty": "58.00000000",
        "bidPrice": "3.22222000",
        "bidQty": "55.00000000",
        "askPrice": "3.22324000",
        "askQty": "369.00000000",
        "openPrice": "0.06001000",
        "highPrice": "4.75000000",
        "lowPrice": "0.06001000",
        "volume": "363612312.00000000",
        "quoteVolume": "1278380637.67654000",
        "openTime": 1633671540356,
        "closeTime": 1633757940356,
        "firstId": 0,
        "lastId": 2118468,
        "count": 2118469,
    },
    {
        "symbol": "PPTBTC",
        "priceChange": "-0.00000510",
        "priceChangePercent": "-21.564",
        "weightedAvgPrice": "0.00002176",
        "prevClosePrice": "0.00002364",
        "lastPrice": "0.00001855",
        "lastQty": "578.40000000",
        "bidPrice": "0.00000000",
        "bidQty": "0.00000000",
        "askPrice": "0.00000000",
        "askQty": "0.00000000",
        "openPrice": "0.00002365",
        "highPrice": "0.00002640",
        "lowPrice": "0.00001750",
        "volume": "6228821.60000000",
        "quoteVolume": "135.51565365",
        "openTime": 1632906001274,
        "closeTime": 1632992401274,
        "firstId": 9886438,
        "lastId": 9929084,
        "count": 42647,
    },
    {
        "symbol": "STPTBTC",
        "priceChange": "-0.00000037",
        "priceChangePercent": "-11.859",
        "weightedAvgPrice": "0.00000311",
        "prevClosePrice": "0.00000313",
        "lastPrice": "0.00000275",
        "lastQty": "251.00000000",
        "bidPrice": "0.00000275",
        "bidQty": "66142.00000000",
        "askPrice": "0.00000276",
        "askQty": "23915.00000000",
        "openPrice": "0.00000312",
        "highPrice": "0.00000379",
        "lowPrice": "0.00000273",
        "volume": "74209736.00000000",
        "quoteVolume": "230.66846218",
        "openTime": 1633671880529,
        "closeTime": 1633758280529,
        "firstId": 3234501,
        "lastId": 3263691,
        "count": 29191,
    },
    {
        "symbol": "STPTUSDT",
        "priceChange": "-0.01829000",
        "priceChangePercent": "-10.865",
        "weightedAvgPrice": "0.16935938",
        "prevClosePrice": "0.16842000",
        "lastPrice": "0.15005000",
        "lastQty": "666.40000000",
        "bidPrice": "0.14986000",
        "bidQty": "3161.60000000",
        "askPrice": "0.15004000",
        "askQty": "37129.00000000",
        "openPrice": "0.16834000",
        "highPrice": "0.20675000",
        "lowPrice": "0.14887000",
        "volume": "250265718.30000000",
        "quoteVolume": "42384846.36757600",
        "openTime": 1633671880617,
        "closeTime": 1633758280617,
        "firstId": 9806815,
        "lastId": 9942184,
        "count": 135370,
    },
    {
        "symbol": "IQBUSD",
        "priceChange": "-0.00265000",
        "priceChangePercent": "-11.557",
        "weightedAvgPrice": "0.02018366",
        "prevClosePrice": "0.02291000",
        "lastPrice": "0.02028000",
        "lastQty": "87856.00000000",
        "bidPrice": "0.02019000",
        "bidQty": "1881.00000000",
        "askPrice": "0.02030000",
        "askQty": "19381.00000000",
        "openPrice": "0.02293000",
        "highPrice": "0.02400000",
        "lowPrice": "0.01750000",
        "volume": "2532230736.00000000",
        "quoteVolume": "51109687.98413000",
        "openTime": 1633671880980,
        "closeTime": 1633758280980,
        "firstId": 8016230,
        "lastId": 8243733,
        "count": 227504,
    },
    {
        "symbol": "SWRVBNB",
        "priceChange": "-0.00030500",
        "priceChangePercent": "-16.860",
        "weightedAvgPrice": "0.00167788",
        "prevClosePrice": "0.00181600",
        "lastPrice": "0.00150400",
        "lastQty": "112.00000000",
        "bidPrice": "0.00000000",
        "bidQty": "0.00000000",
        "askPrice": "0.00000000",
        "askQty": "0.00000000",
        "openPrice": "0.00180900",
        "highPrice": "0.00181400",
        "lowPrice": "0.00149100",
        "volume": "30879476.51000000",
        "quoteVolume": "51812.14293780",
        "openTime": 1632906001408,
        "closeTime": 1632992401408,
        "firstId": 971717,
        "lastId": 979207,
        "count": 7491,
    },
    {
        "symbol": "FILDOWNUSDT",
        "priceChange": "-0.00010410",
        "priceChangePercent": "-21.688",
        "weightedAvgPrice": "0.00038658",
        "prevClosePrice": "0.00048200",
        "lastPrice": "0.00037590",
        "lastQty": "370607.03000000",
        "bidPrice": "0.00037510",
        "bidQty": "531741.98000000",
        "askPrice": "0.00037660",
        "askQty": "8839323.92000000",
        "openPrice": "0.00048000",
        "highPrice": "0.00048670",
        "lowPrice": "0.00033860",
        "volume": "11225982080.07000000",
        "quoteVolume": "4339736.90196502",
        "openTime": 1633671880933,
        "closeTime": 1633758280933,
        "firstId": 6454616,
        "lastId": 6471314,
        "count": 16699,
    },
    {
        "symbol": "RADBTC",
        "priceChange": "-0.00004180",
        "priceChangePercent": "-12.356",
        "weightedAvgPrice": "0.00029893",
        "prevClosePrice": "0.00033890",
        "lastPrice": "0.00029650",
        "lastQty": "1.40000000",
        "bidPrice": "0.00029650",
        "bidQty": "1.60000000",
        "askPrice": "0.00029680",
        "askQty": "339.80000000",
        "openPrice": "0.00033830",
        "highPrice": "0.00034790",
        "lowPrice": "0.00027820",
        "volume": "265217.20000000",
        "quoteVolume": "79.28021111",
        "openTime": 1633671881003,
        "closeTime": 1633758281003,
        "firstId": 43913,
        "lastId": 54082,
        "count": 10170,
    },
    {
        "symbol": "RADBUSD",
        "priceChange": "-2.08800000",
        "priceChangePercent": "-11.454",
        "weightedAvgPrice": "16.38970027",
        "prevClosePrice": "18.23600000",
        "lastPrice": "16.14200000",
        "lastQty": "385.40000000",
        "bidPrice": "16.14000000",
        "bidQty": "287.10000000",
        "askPrice": "16.15500000",
        "askQty": "1.40000000",
        "openPrice": "18.23000000",
        "highPrice": "18.82600000",
        "lowPrice": "15.10100000",
        "volume": "1108421.30000000",
        "quoteVolume": "18166692.87630000",
        "openTime": 1633671879130,
        "closeTime": 1633758279130,
        "firstId": 472751,
        "lastId": 516015,
        "count": 43265,
    },
    {
        "symbol": "RADUSDT",
        "priceChange": "-2.07600000",
        "priceChangePercent": "-11.392",
        "weightedAvgPrice": "16.35457095",
        "prevClosePrice": "18.22300000",
        "lastPrice": "16.14700000",
        "lastQty": "100.30000000",
        "bidPrice": "16.14700000",
        "bidQty": "8.10000000",
        "askPrice": "16.15100000",
        "askQty": "8.00000000",
        "openPrice": "18.22300000",
        "highPrice": "18.82300000",
        "lowPrice": "15.11000000",
        "volume": "3343059.30000000",
        "quoteVolume": "54674300.50450000",
        "openTime": 1633671880998,
        "closeTime": 1633758280998,
        "firstId": 666784,
        "lastId": 770971,
        "count": 104188,
    },
    {
        "symbol": "STPTBUSD",
        "priceChange": "-0.01959000",
        "priceChangePercent": "-11.549",
        "weightedAvgPrice": "0.15956866",
        "prevClosePrice": "0.00000000",
        "lastPrice": "0.15004000",
        "lastQty": "691.00000000",
        "bidPrice": "0.14999000",
        "bidQty": "1549.50000000",
        "askPrice": "0.15015000",
        "askQty": "3799.20000000",
        "openPrice": "0.16963000",
        "highPrice": "0.17800000",
        "lowPrice": "0.14900000",
        "volume": "13471058.90000000",
        "quoteVolume": "2149558.81742600",
        "openTime": 1633671880989,
        "closeTime": 1633758280989,
        "firstId": 0,
        "lastId": 14495,
        "count": 14496,
    },
]


def test_get_coin_price_high_should_return_list_of_high_price_more_50_percent():
    is_high = True
    percent_change = 50
    actual = binance_api.get_coin_price_binance(demo_data, is_high, percent_change)
    expected = [
        {
            "symbol": "BETABTC",
            "priceChange": "0.00005803",
            "priceChangePercent": "5227.928",
            "weightedAvgPrice": "0.00006443",
            "prevClosePrice": "0.00000000",
            "lastPrice": "0.00005914",
            "lastQty": "70.00000000",
            "bidPrice": "0.00005911",
            "bidQty": "47.00000000",
            "askPrice": "0.00005919",
            "askQty": "5.00000000",
            "openPrice": "0.00000111",
            "highPrice": "0.00009480",
            "lowPrice": "0.00000111",
            "volume": "15969411.00000000",
            "quoteVolume": "1028.90462875",
            "openTime": 1633671540243,
            "closeTime": 1633757940243,
            "firstId": 0,
            "lastId": 125822,
            "count": 125823,
        },
        {
            "symbol": "BETABNB",
            "priceChange": "0.00748450",
            "priceChangePercent": "5415.702",
            "weightedAvgPrice": "0.00824652",
            "prevClosePrice": "0.00000000",
            "lastPrice": "0.00762270",
            "lastQty": "25.00000000",
            "bidPrice": "0.00760550",
            "bidQty": "877.00000000",
            "askPrice": "0.00762370",
            "askQty": "15.00000000",
            "openPrice": "0.00013820",
            "highPrice": "0.06000000",
            "lowPrice": "0.00013820",
            "volume": "29522440.00000000",
            "quoteVolume": "243457.45709740",
            "openTime": 1633671540168,
            "closeTime": 1633757940168,
            "firstId": 0,
            "lastId": 265658,
            "count": 265659,
        },
        {
            "symbol": "BETABUSD",
            "priceChange": "3.16355000",
            "priceChangePercent": "5269.071",
            "weightedAvgPrice": "3.50770798",
            "prevClosePrice": "0.00000000",
            "lastPrice": "3.22359000",
            "lastQty": "13.00000000",
            "bidPrice": "3.22047000",
            "bidQty": "620.00000000",
            "askPrice": "3.22359000",
            "askQty": "173.00000000",
            "openPrice": "0.06004000",
            "highPrice": "5.80000000",
            "lowPrice": "0.06004000",
            "volume": "139131459.00000000",
            "quoteVolume": "488032528.72984000",
            "openTime": 1633671540309,
            "closeTime": 1633757940309,
            "firstId": 0,
            "lastId": 1366427,
            "count": 1366428,
        },
        {
            "symbol": "BETAUSDT",
            "priceChange": "3.16220000",
            "priceChangePercent": "5269.455",
            "weightedAvgPrice": "3.51577929",
            "prevClosePrice": "0.00000000",
            "lastPrice": "3.22221000",
            "lastQty": "58.00000000",
            "bidPrice": "3.22222000",
            "bidQty": "55.00000000",
            "askPrice": "3.22324000",
            "askQty": "369.00000000",
            "openPrice": "0.06001000",
            "highPrice": "4.75000000",
            "lowPrice": "0.06001000",
            "volume": "363612312.00000000",
            "quoteVolume": "1278380637.67654000",
            "openTime": 1633671540356,
            "closeTime": 1633757940356,
            "firstId": 0,
            "lastId": 2118468,
            "count": 2118469,
        },
    ]
    assert actual == expected


def test_get_coin_price_low_should_return_list_of_low_price_more_50_percent():
    is_high = False
    percent_change = 10
    actual = binance_api.get_coin_price_binance(demo_data, is_high, percent_change)
    expected = [
        {
            "symbol": "PPTBTC",
            "priceChange": "-0.00000510",
            "priceChangePercent": "-21.564",
            "weightedAvgPrice": "0.00002176",
            "prevClosePrice": "0.00002364",
            "lastPrice": "0.00001855",
            "lastQty": "578.40000000",
            "bidPrice": "0.00000000",
            "bidQty": "0.00000000",
            "askPrice": "0.00000000",
            "askQty": "0.00000000",
            "openPrice": "0.00002365",
            "highPrice": "0.00002640",
            "lowPrice": "0.00001750",
            "volume": "6228821.60000000",
            "quoteVolume": "135.51565365",
            "openTime": 1632906001274,
            "closeTime": 1632992401274,
            "firstId": 9886438,
            "lastId": 9929084,
            "count": 42647,
        },
        {
            "symbol": "STPTBTC",
            "priceChange": "-0.00000037",
            "priceChangePercent": "-11.859",
            "weightedAvgPrice": "0.00000311",
            "prevClosePrice": "0.00000313",
            "lastPrice": "0.00000275",
            "lastQty": "251.00000000",
            "bidPrice": "0.00000275",
            "bidQty": "66142.00000000",
            "askPrice": "0.00000276",
            "askQty": "23915.00000000",
            "openPrice": "0.00000312",
            "highPrice": "0.00000379",
            "lowPrice": "0.00000273",
            "volume": "74209736.00000000",
            "quoteVolume": "230.66846218",
            "openTime": 1633671880529,
            "closeTime": 1633758280529,
            "firstId": 3234501,
            "lastId": 3263691,
            "count": 29191,
        },
        {
            "symbol": "STPTUSDT",
            "priceChange": "-0.01829000",
            "priceChangePercent": "-10.865",
            "weightedAvgPrice": "0.16935938",
            "prevClosePrice": "0.16842000",
            "lastPrice": "0.15005000",
            "lastQty": "666.40000000",
            "bidPrice": "0.14986000",
            "bidQty": "3161.60000000",
            "askPrice": "0.15004000",
            "askQty": "37129.00000000",
            "openPrice": "0.16834000",
            "highPrice": "0.20675000",
            "lowPrice": "0.14887000",
            "volume": "250265718.30000000",
            "quoteVolume": "42384846.36757600",
            "openTime": 1633671880617,
            "closeTime": 1633758280617,
            "firstId": 9806815,
            "lastId": 9942184,
            "count": 135370,
        },
        {
            "symbol": "IQBUSD",
            "priceChange": "-0.00265000",
            "priceChangePercent": "-11.557",
            "weightedAvgPrice": "0.02018366",
            "prevClosePrice": "0.02291000",
            "lastPrice": "0.02028000",
            "lastQty": "87856.00000000",
            "bidPrice": "0.02019000",
            "bidQty": "1881.00000000",
            "askPrice": "0.02030000",
            "askQty": "19381.00000000",
            "openPrice": "0.02293000",
            "highPrice": "0.02400000",
            "lowPrice": "0.01750000",
            "volume": "2532230736.00000000",
            "quoteVolume": "51109687.98413000",
            "openTime": 1633671880980,
            "closeTime": 1633758280980,
            "firstId": 8016230,
            "lastId": 8243733,
            "count": 227504,
        },
        {
            "symbol": "SWRVBNB",
            "priceChange": "-0.00030500",
            "priceChangePercent": "-16.860",
            "weightedAvgPrice": "0.00167788",
            "prevClosePrice": "0.00181600",
            "lastPrice": "0.00150400",
            "lastQty": "112.00000000",
            "bidPrice": "0.00000000",
            "bidQty": "0.00000000",
            "askPrice": "0.00000000",
            "askQty": "0.00000000",
            "openPrice": "0.00180900",
            "highPrice": "0.00181400",
            "lowPrice": "0.00149100",
            "volume": "30879476.51000000",
            "quoteVolume": "51812.14293780",
            "openTime": 1632906001408,
            "closeTime": 1632992401408,
            "firstId": 971717,
            "lastId": 979207,
            "count": 7491,
        },
        {
            "symbol": "FILDOWNUSDT",
            "priceChange": "-0.00010410",
            "priceChangePercent": "-21.688",
            "weightedAvgPrice": "0.00038658",
            "prevClosePrice": "0.00048200",
            "lastPrice": "0.00037590",
            "lastQty": "370607.03000000",
            "bidPrice": "0.00037510",
            "bidQty": "531741.98000000",
            "askPrice": "0.00037660",
            "askQty": "8839323.92000000",
            "openPrice": "0.00048000",
            "highPrice": "0.00048670",
            "lowPrice": "0.00033860",
            "volume": "11225982080.07000000",
            "quoteVolume": "4339736.90196502",
            "openTime": 1633671880933,
            "closeTime": 1633758280933,
            "firstId": 6454616,
            "lastId": 6471314,
            "count": 16699,
        },
        {
            "symbol": "RADBTC",
            "priceChange": "-0.00004180",
            "priceChangePercent": "-12.356",
            "weightedAvgPrice": "0.00029893",
            "prevClosePrice": "0.00033890",
            "lastPrice": "0.00029650",
            "lastQty": "1.40000000",
            "bidPrice": "0.00029650",
            "bidQty": "1.60000000",
            "askPrice": "0.00029680",
            "askQty": "339.80000000",
            "openPrice": "0.00033830",
            "highPrice": "0.00034790",
            "lowPrice": "0.00027820",
            "volume": "265217.20000000",
            "quoteVolume": "79.28021111",
            "openTime": 1633671881003,
            "closeTime": 1633758281003,
            "firstId": 43913,
            "lastId": 54082,
            "count": 10170,
        },
        {
            "symbol": "RADBUSD",
            "priceChange": "-2.08800000",
            "priceChangePercent": "-11.454",
            "weightedAvgPrice": "16.38970027",
            "prevClosePrice": "18.23600000",
            "lastPrice": "16.14200000",
            "lastQty": "385.40000000",
            "bidPrice": "16.14000000",
            "bidQty": "287.10000000",
            "askPrice": "16.15500000",
            "askQty": "1.40000000",
            "openPrice": "18.23000000",
            "highPrice": "18.82600000",
            "lowPrice": "15.10100000",
            "volume": "1108421.30000000",
            "quoteVolume": "18166692.87630000",
            "openTime": 1633671879130,
            "closeTime": 1633758279130,
            "firstId": 472751,
            "lastId": 516015,
            "count": 43265,
        },
        {
            "symbol": "RADUSDT",
            "priceChange": "-2.07600000",
            "priceChangePercent": "-11.392",
            "weightedAvgPrice": "16.35457095",
            "prevClosePrice": "18.22300000",
            "lastPrice": "16.14700000",
            "lastQty": "100.30000000",
            "bidPrice": "16.14700000",
            "bidQty": "8.10000000",
            "askPrice": "16.15100000",
            "askQty": "8.00000000",
            "openPrice": "18.22300000",
            "highPrice": "18.82300000",
            "lowPrice": "15.11000000",
            "volume": "3343059.30000000",
            "quoteVolume": "54674300.50450000",
            "openTime": 1633671880998,
            "closeTime": 1633758280998,
            "firstId": 666784,
            "lastId": 770971,
            "count": 104188,
        },
        {
            "symbol": "STPTBUSD",
            "priceChange": "-0.01959000",
            "priceChangePercent": "-11.549",
            "weightedAvgPrice": "0.15956866",
            "prevClosePrice": "0.00000000",
            "lastPrice": "0.15004000",
            "lastQty": "691.00000000",
            "bidPrice": "0.14999000",
            "bidQty": "1549.50000000",
            "askPrice": "0.15015000",
            "askQty": "3799.20000000",
            "openPrice": "0.16963000",
            "highPrice": "0.17800000",
            "lowPrice": "0.14900000",
            "volume": "13471058.90000000",
            "quoteVolume": "2149558.81742600",
            "openTime": 1633671880989,
            "closeTime": 1633758280989,
            "firstId": 0,
            "lastId": 14495,
            "count": 14496,
        },
    ]
    assert actual == expected


def test_get_price_of_cake_list_should_return_price_of_pair_cake_list():
    coin_name = "CAKE"
    actual = binance_api.get_specific_coin_price_binance(demo_data, coin_name)
    expected = [
        {
            "symbol": "CAKEBNB",
            "priceChange": "0.00222000",
            "priceChangePercent": "4.983",
            "weightedAvgPrice": "0.04555490",
            "prevClosePrice": "0.04459000",
            "lastPrice": "0.04677000",
            "lastQty": "363.53000000",
            "bidPrice": "0.04677000",
            "bidQty": "959.57000000",
            "askPrice": "0.04682000",
            "askQty": "24.45000000",
            "openPrice": "0.04455000",
            "highPrice": "0.04758000",
            "lowPrice": "0.04354000",
            "volume": "564397.93000000",
            "quoteVolume": "25711.09046400",
            "openTime": 1633630765874,
            "closeTime": 1633717165874,
            "firstId": 7473561,
            "lastId": 7483807,
            "count": 10247,
        }
    ]
    assert actual == expected


def test_get_price_of_unknow_coin_should_return_empty_list():
    coin_name = "SUPREMO"
    actual = binance_api.get_specific_coin_price_binance(demo_data, coin_name)
    expected = []
    assert actual == expected
