

```python
from stocker.stocker import Stocker
import quandl
import yaml

import pandas as pd
import numpy as np
import datetime 
from dateutil.relativedelta import relativedelta
```

# Using Stocker package to get data before 2018


```python
with open("./api_key.yaml", 'r') as stream:
    try:
        data_loaded = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
```


```python
api_key = data_loaded['api_key']
quandl.ApiConfig.api_key = api_key
```


```python
tickers = pd.read_csv('./tickers.csv')
```


```python
ticker_list = [i for i in tickers.ticker]
```


```python
def agg_stock_data(ticker):
    stock_object = Stocker(ticker)
    stock_history_df = stock_object.stock
    stock_history_df.columns = [i.lower() for i in stock_history_df.columns]
    stock_history_df = (
        stock_history_df
        .pipe(lambda x: x.assign(ticker=ticker))
    )
    return stock_history_df
```


```python
first = True
for tick in ticker_list:
    if first:
        agg_df = agg_stock_data(tick)
        if agg_df.date.min().year <= 2006 and agg_df.date.max().year == 2018:
            first = False
    else:
        df = agg_stock_data(tick)
        if df.date.min().year <= 2006 and df.date.max().year == 2018:
            agg_df = pd.concat([agg_df, df], axis=0)
```

    PRO Stocker Initialized. Data covers 2007-07-26 to 2018-03-27.
    MCBC Stocker Initialized. Data covers 1998-05-20 to 2018-03-27.
    ENOC Stocker Initialized. Data covers 2007-05-18 to 2017-08-07.
    LINC Stocker Initialized. Data covers 2005-06-23 to 2018-03-27.
    SYF Stocker Initialized. Data covers 2014-07-31 to 2018-03-27.
    FLDM Stocker Initialized. Data covers 2011-02-10 to 2018-03-27.
    ECHO Stocker Initialized. Data covers 2009-10-02 to 2018-03-27.
    DISH Stocker Initialized. Data covers 1995-06-21 to 2018-03-27.
    NRCIA Stocker Initialized. Data covers 2013-05-23 to 2018-03-27.
    NAT Stocker Initialized. Data covers 1997-09-30 to 2018-03-27.
    THOR Stocker Initialized. Data covers 1996-01-02 to 2015-10-08.
    FTNT Stocker Initialized. Data covers 2009-11-18 to 2018-03-27.
    FMD Stocker Initialized. Data covers 2003-10-31 to 2016-08-22.
    GIS Stocker Initialized. Data covers 1983-06-10 to 2018-03-27.
    ASC Stocker Initialized. Data covers 2013-08-01 to 2018-03-27.
    WRE Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    QRHC Stocker Initialized. Data covers 2010-01-05 to 2018-03-27.
    ROST Stocker Initialized. Data covers 1986-07-09 to 2018-03-27.
    HIBB Stocker Initialized. Data covers 1996-10-11 to 2018-03-27.
    HIL Stocker Initialized. Data covers 2004-08-12 to 2018-03-27.
    NTRS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    VRTX Stocker Initialized. Data covers 1991-07-24 to 2018-03-27.
    WAGE Stocker Initialized. Data covers 2012-05-11 to 2018-03-27.
    IO Stocker Initialized. Data covers 1991-04-02 to 2018-03-27.
    XCO Stocker Initialized. Data covers 2006-02-09 to 2017-12-22.
    ZBH Stocker Initialized. Data covers 2001-07-25 to 2018-03-27.
    BMI Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    BRLI Stocker Initialized. Data covers 1993-11-22 to 2015-08-20.
    GPT Stocker Initialized. Data covers 2004-08-02 to 2018-03-27.
    DY Stocker Initialized. Data covers 1990-09-24 to 2018-03-27.
    NUVA Stocker Initialized. Data covers 2004-05-13 to 2018-03-27.
    YUME Stocker Initialized. Data covers 2013-08-07 to 2018-02-02.
    DD Stocker Initialized. Data covers 1962-01-02 to 2017-08-31.
    CMS Stocker Initialized. Data covers 1984-12-31 to 2018-03-27.
    ATNI Stocker Initialized. Data covers 1991-11-14 to 2018-03-27.
    TEN Stocker Initialized. Data covers 1982-01-04 to 2018-03-27.
    EXC Stocker Initialized. Data covers 1980-01-02 to 2018-03-27.
    BEBE Stocker Initialized. Data covers 1998-06-17 to 2017-12-15.
    CSRA Stocker Initialized. Data covers 2015-11-30 to 2018-03-27.
    ORI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    LYB Stocker Initialized. Data covers 2010-04-28 to 2018-03-27.
    REI Stocker Initialized. Data covers 2007-04-10 to 2018-03-27.
    TRR Stocker Initialized. Data covers 1991-12-16 to 2017-06-21.
    MACK Stocker Initialized. Data covers 2012-03-29 to 2018-03-27.
    PEP Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    AVID Stocker Initialized. Data covers 2014-12-08 to 2018-03-27.
    AAMC Stocker Initialized. Data covers 2012-12-13 to 2018-03-27.
    CCG Stocker Initialized. Data covers 2010-10-14 to 2016-03-02.
    CBRL Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    PACW Stocker Initialized. Data covers 2000-06-05 to 2018-03-27.
    TGE Stocker Initialized. Data covers 1994-09-22 to 2015-02-11.
    AXP Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    CNW Stocker Initialized. Data covers 1980-01-02 to 2015-10-29.
    EGLT Stocker Initialized. Data covers 2014-02-06 to 2018-03-27.
    FPRX Stocker Initialized. Data covers 2013-09-18 to 2018-03-27.
    SAFT Stocker Initialized. Data covers 2002-11-22 to 2018-03-27.
    GES Stocker Initialized. Data covers 1996-08-08 to 2018-03-27.
    CYBX Stocker Initialized. Data covers 1993-02-11 to 2015-10-16.
    ITMN Stocker Initialized. Data covers 2000-03-24 to 2014-09-29.
    BDGE Stocker Initialized. Data covers 1999-01-12 to 2018-03-27.
    CST Stocker Initialized. Data covers 2013-04-17 to 2017-06-27.
    ARW Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    ICON Stocker Initialized. Data covers 1990-03-06 to 2018-03-27.
    MDAS Stocker Initialized. Data covers 2007-12-13 to 2016-01-27.
    MHLD Stocker Initialized. Data covers 2008-05-06 to 2018-03-27.
    HZO Stocker Initialized. Data covers 1998-06-03 to 2018-03-27.
    NYMT Stocker Initialized. Data covers 2004-07-26 to 2018-03-27.
    OME Stocker Initialized. Data covers 1998-04-03 to 2017-12-19.
    ASTE Stocker Initialized. Data covers 1986-06-19 to 2018-03-27.
    SPR Stocker Initialized. Data covers 2006-11-28 to 2018-03-27.
    ACXM Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    COLM Stocker Initialized. Data covers 1998-03-27 to 2018-03-27.
    AIMC Stocker Initialized. Data covers 2006-12-15 to 2018-03-27.
    TECD Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    LE Stocker Initialized. Data covers 2014-03-20 to 2018-03-27.
    DYN Stocker Initialized. Data covers 2012-10-03 to 2018-03-27.
    IBTX Stocker Initialized. Data covers 2013-04-04 to 2018-03-27.
    CRZO Stocker Initialized. Data covers 1997-08-06 to 2018-03-27.
    NATH Stocker Initialized. Data covers 1993-02-26 to 2018-03-27.
    NWLI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AUXL Stocker Initialized. Data covers 2004-07-26 to 2015-01-29.
    MYGN Stocker Initialized. Data covers 1995-10-06 to 2018-03-27.
    TRNO Stocker Initialized. Data covers 2010-02-10 to 2018-03-27.
    LRN Stocker Initialized. Data covers 2007-12-13 to 2018-03-27.
    RKT Stocker Initialized. Data covers 1994-03-03 to 2015-07-01.
    LEE Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    LQ Stocker Initialized. Data covers 2014-04-09 to 2018-03-27.
    ITCI Stocker Initialized. Data covers 2014-01-07 to 2018-03-27.
    NRIM Stocker Initialized. Data covers 1993-10-25 to 2018-03-27.
    TRGP Stocker Initialized. Data covers 2010-12-07 to 2018-03-27.
    BDN Stocker Initialized. Data covers 1986-07-24 to 2018-03-27.
    WNC Stocker Initialized. Data covers 1991-11-08 to 2018-03-27.
    MFLX Stocker Initialized. Data covers 2004-06-25 to 2016-07-27.
    NCI Stocker Initialized. Data covers 1996-10-04 to 2018-03-27.
    IBCP Stocker Initialized. Data covers 2010-02-02 to 2018-03-27.
    FBNC Stocker Initialized. Data covers 1992-12-09 to 2018-03-27.
    LF Stocker Initialized. Data covers 2002-07-25 to 2016-04-04.
    INCY Stocker Initialized. Data covers 1993-11-04 to 2018-03-27.
    SRDX Stocker Initialized. Data covers 1998-03-04 to 2018-03-27.
    NPK Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    PCBK Stocker Initialized. Data covers 1999-04-26 to 2017-10-31.
    RSG Stocker Initialized. Data covers 1998-07-01 to 2018-03-27.
    TAM Stocker Initialized. Data covers 2000-01-03 to 2014-12-05.
    HSY Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    SNPS Stocker Initialized. Data covers 1992-02-26 to 2018-03-27.
    TSCO Stocker Initialized. Data covers 1994-02-18 to 2018-03-27.
    EXAR Stocker Initialized. Data covers 1990-03-26 to 2017-05-12.
    BKH Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    HY Stocker Initialized. Data covers 2012-10-01 to 2018-03-27.
    HMST Stocker Initialized. Data covers 2012-02-10 to 2018-03-27.
    MRGE Stocker Initialized. Data covers 1998-05-07 to 2015-10-13.
    HST Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    TSO Stocker Initialized. Data covers 1983-04-06 to 2017-07-31.
    SEIC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AHS Stocker Initialized. Data covers 2001-11-13 to 2016-10-26.
    LL Stocker Initialized. Data covers 2007-11-09 to 2018-03-27.
    STL Stocker Initialized. Data covers 1999-01-08 to 2018-03-27.
    FOSL Stocker Initialized. Data covers 1993-04-08 to 2018-03-07.
    CACB Stocker Initialized. Data covers 1994-01-21 to 2017-05-30.
    HPTX Stocker Initialized. Data covers 2012-07-26 to 2015-05-07.
    RTN Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    GLRE Stocker Initialized. Data covers 2007-05-24 to 2018-03-27.
    VTR Stocker Initialized. Data covers 1997-05-05 to 2018-03-27.
    XRX Stocker Initialized. Data covers 1977-01-03 to 2018-03-27.
    OVAS Stocker Initialized. Data covers 2012-11-12 to 2018-03-27.
    TPC Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    BZH Stocker Initialized. Data covers 1994-02-23 to 2018-03-27.
    LDRH Stocker Initialized. Data covers 2013-10-09 to 2016-07-12.
    BWC Stocker Initialized. Data covers 2010-08-02 to 2015-06-30.
    SNV Stocker Initialized. Data covers 1990-01-12 to 2018-03-27.
    SAFM Stocker Initialized. Data covers 1989-12-20 to 2018-03-27.
    IL Stocker Initialized. Data covers 2010-08-06 to 2017-01-19.
    CHMT Stocker Initialized. Data covers 2010-10-26 to 2017-04-20.
    CBK Stocker Initialized. Data covers 1992-03-31 to 2018-03-27.
    LEA Stocker Initialized. Data covers 2009-11-09 to 2018-03-27.
    ZAZA Stocker Initialized. Data covers 1992-03-03 to 2015-10-02.
    ABCO Stocker Initialized. Data covers 2001-11-13 to 2017-11-17.
    ISRL Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    PATK Stocker Initialized. Data covers 1990-03-27 to 2018-03-27.
    CMO Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    SYX Stocker Initialized. Data covers 1995-06-27 to 2018-03-27.
    OSIS Stocker Initialized. Data covers 1997-10-02 to 2018-03-27.
    OLED Stocker Initialized. Data covers 1996-04-12 to 2018-03-27.
    MTRN Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    UHAL Stocker Initialized. Data covers 1994-11-04 to 2018-03-27.
    MHFI Stocker Initialized. Data covers 1985-07-01 to 2016-04-27.
    CUB Stocker Initialized. Data covers 1989-02-21 to 2018-03-27.
    PX Stocker Initialized. Data covers 1992-06-17 to 2018-03-27.
    CNBC Stocker Initialized. Data covers 1996-05-30 to 2014-06-30.
    IPCC Stocker Initialized. Data covers 2003-02-12 to 2018-03-27.
    ETR Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    RBCN Stocker Initialized. Data covers 2007-11-16 to 2018-03-27.
    CNO Stocker Initialized. Data covers 2003-09-10 to 2018-03-27.
    STAG Stocker Initialized. Data covers 2011-04-15 to 2018-03-27.
    BR Stocker Initialized. Data covers 2007-04-02 to 2018-03-27.
    ELGX Stocker Initialized. Data covers 1996-06-21 to 2018-03-27.
    FII Stocker Initialized. Data covers 1998-05-14 to 2018-03-27.
    AMSF Stocker Initialized. Data covers 2005-11-18 to 2018-03-27.
    PLMT Stocker Initialized. Data covers 2011-08-08 to 2015-08-31.
    RS Stocker Initialized. Data covers 1994-09-16 to 2018-03-27.
    SLRC Stocker Initialized. Data covers 2010-02-09 to 2018-03-27.
    UVV Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    END Stocker Initialized. Data covers 2002-02-27 to 2014-10-07.
    XLS Stocker Initialized. Data covers 2011-10-13 to 2015-05-28.
    MDCI Stocker Initialized. Data covers 1986-07-22 to 2014-09-30.
    VG Stocker Initialized. Data covers 2006-05-24 to 2018-03-27.
    DEL Stocker Initialized. Data covers 1996-12-12 to 2018-02-20.
    MOV Stocker Initialized. Data covers 1993-09-30 to 2018-03-27.
    BLMN Stocker Initialized. Data covers 2012-08-08 to 2018-03-27.
    TXTR Stocker Initialized. Data covers 2013-06-07 to 2016-06-10.
    DJCO Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    BKE Stocker Initialized. Data covers 1992-05-11 to 2018-03-27.
    HMTV Stocker Initialized. Data covers 2013-04-05 to 2018-03-27.
    IMMU Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CBL Stocker Initialized. Data covers 1993-10-28 to 2018-03-27.
    MCF Stocker Initialized. Data covers 1994-04-04 to 2018-03-27.
    FOE Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    KRG Stocker Initialized. Data covers 2004-08-12 to 2018-03-27.
    SWS Stocker Initialized. Data covers 1991-10-11 to 2014-12-31.
    VAR Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    CORE Stocker Initialized. Data covers 2005-04-13 to 2018-03-27.
    DGICA Stocker Initialized. Data covers 2003-07-03 to 2018-03-27.
    NPO Stocker Initialized. Data covers 2002-05-24 to 2018-03-27.
    FRC Stocker Initialized. Data covers 2010-12-09 to 2018-03-27.
    GPK Stocker Initialized. Data covers 1992-12-10 to 2018-03-27.
    OB Stocker Initialized. Data covers 2006-11-09 to 2017-09-27.
    WSO Stocker Initialized. Data covers 1984-06-07 to 2018-03-27.
    SFG Stocker Initialized. Data covers 1999-04-16 to 2016-03-07.
    MAN Stocker Initialized. Data covers 1988-10-05 to 2018-03-27.
    FCN Stocker Initialized. Data covers 1996-05-09 to 2018-03-27.
    GWW Stocker Initialized. Data covers 1984-12-17 to 2018-03-27.
    CCOI Stocker Initialized. Data covers 2002-02-05 to 2018-03-27.
    HA Stocker Initialized. Data covers 1995-06-21 to 2018-03-27.
    LCI Stocker Initialized. Data covers 1997-01-02 to 2018-03-27.
    BMS Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    HLF Stocker Initialized. Data covers 2004-12-16 to 2018-03-27.
    KRC Stocker Initialized. Data covers 1997-01-30 to 2018-03-27.
    WAL Stocker Initialized. Data covers 2005-07-01 to 2018-03-27.
    HSII Stocker Initialized. Data covers 1999-04-27 to 2018-03-27.
    RELL Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CE Stocker Initialized. Data covers 2005-01-21 to 2018-03-27.
    FCFS Stocker Initialized. Data covers 1992-08-17 to 2018-03-27.
    TNDM Stocker Initialized. Data covers 2013-11-14 to 2018-03-27.
    SYNA Stocker Initialized. Data covers 2002-01-29 to 2018-03-27.
    ARTNA Stocker Initialized. Data covers 1996-05-24 to 2018-03-27.
    AF Stocker Initialized. Data covers 1993-11-18 to 2017-09-29.
    BBGI Stocker Initialized. Data covers 2000-02-11 to 2018-03-27.
    HERO Stocker Initialized. Data covers 2005-10-27 to 2016-06-14.
    TAHO Stocker Initialized. Data covers 2010-09-23 to 2018-03-27.
    BBBY Stocker Initialized. Data covers 1992-06-05 to 2018-03-07.
    MDXG Stocker Initialized. Data covers 2008-02-12 to 2018-03-27.
    TLYS Stocker Initialized. Data covers 2012-05-04 to 2018-03-27.
    WRB Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    EBF Stocker Initialized. Data covers 1987-09-24 to 2018-03-27.
    LPNT Stocker Initialized. Data covers 1999-05-12 to 2018-03-27.
    CR Stocker Initialized. Data covers 1984-11-01 to 2018-03-27.
    BMY Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    EDE Stocker Initialized. Data covers 1973-05-03 to 2016-12-30.
    SFNC Stocker Initialized. Data covers 1992-11-02 to 2018-03-27.
    AN Stocker Initialized. Data covers 1992-03-03 to 2018-03-07.
    NPSP Stocker Initialized. Data covers 1994-05-26 to 2015-02-20.
    XCRA Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CI Stocker Initialized. Data covers 1982-03-31 to 2018-03-27.
    TRK Stocker Initialized. Data covers 1995-02-24 to 2018-03-27.
    COWN Stocker Initialized. Data covers 2006-07-13 to 2018-03-27.
    TAX Stocker Initialized. Data covers 2012-07-02 to 2018-03-27.
    BBSI Stocker Initialized. Data covers 1993-06-14 to 2018-03-27.
    KCG Stocker Initialized. Data covers 2013-06-28 to 2017-07-19.
    CASY Stocker Initialized. Data covers 1983-10-20 to 2018-03-27.
    SUP Stocker Initialized. Data covers 1985-07-03 to 2018-03-27.
    BHLB Stocker Initialized. Data covers 2000-06-28 to 2018-03-27.
    MSEX Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CSG Stocker Initialized. Data covers 2013-05-21 to 2015-12-17.
    DAL Stocker Initialized. Data covers 2007-05-03 to 2018-03-27.
    SSYS Stocker Initialized. Data covers 1994-10-21 to 2018-03-27.
    FL Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    ZQK Stocker Initialized. Data covers 1990-03-26 to 2015-09-09.
    ADC Stocker Initialized. Data covers 1994-04-15 to 2018-03-27.
    NASB Stocker Initialized. Data covers 1999-08-06 to 2015-03-06.
    EGY Stocker Initialized. Data covers 1993-01-29 to 2018-03-27.
    OGXI Stocker Initialized. Data covers 1995-10-13 to 2017-08-02.
    NIHD Stocker Initialized. Data covers 2015-07-09 to 2018-03-27.
    HFC Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    SSNI Stocker Initialized. Data covers 2013-03-13 to 2018-01-05.
    MO Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    IRF Stocker Initialized. Data covers 1987-11-05 to 2015-01-13.
    FICO Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    DKS Stocker Initialized. Data covers 2002-10-16 to 2018-03-27.
    V Stocker Initialized. Data covers 2008-03-19 to 2018-03-27.
    EAC Stocker Initialized. Data covers 2012-04-11 to 2016-11-18.
    MTN Stocker Initialized. Data covers 1997-02-04 to 2018-03-27.
    PPS Stocker Initialized. Data covers 1993-07-16 to 2016-11-30.
    GOOG Stocker Initialized. Data covers 2014-03-27 to 2018-03-27.
    JCI Stocker Initialized. Data covers 1985-03-27 to 2018-03-27.
    CMRX Stocker Initialized. Data covers 2013-04-11 to 2018-03-27.
    AINV Stocker Initialized. Data covers 2004-05-05 to 2018-03-27.
    GOGO Stocker Initialized. Data covers 2013-06-21 to 2018-03-27.
    HPQ Stocker Initialized. Data covers 1962-01-02 to 2018-03-27.
    TAL Stocker Initialized. Data covers 2010-10-20 to 2018-03-27.
    UPS Stocker Initialized. Data covers 1999-11-10 to 2018-03-27.
    FNB Stocker Initialized. Data covers 1993-03-04 to 2018-03-27.
    EXP Stocker Initialized. Data covers 1994-04-12 to 2018-03-27.
    ATRI Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    HTGC Stocker Initialized. Data covers 2005-06-09 to 2018-03-27.
    LB Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    MAR Stocker Initialized. Data covers 1993-10-13 to 2018-03-27.
    MOVE Stocker Initialized. Data covers 1999-08-05 to 2014-11-13.
    NFBK Stocker Initialized. Data covers 2007-11-08 to 2018-03-27.
    MTD Stocker Initialized. Data covers 1997-11-14 to 2018-03-27.
    WEC Stocker Initialized. Data covers 1984-10-26 to 2018-03-27.
    CARB Stocker Initialized. Data covers 2011-08-11 to 2018-03-27.
    ASBC Stocker Initialized. Data covers 1984-09-07 to 2014-12-22.
    BAGL Stocker Initialized. Data covers 2007-06-08 to 2014-11-06.
    SUNE Stocker Initialized. Data covers 1995-07-13 to 2016-04-21.
    SWFT Stocker Initialized. Data covers 2010-12-16 to 2017-09-08.
    TSC Stocker Initialized. Data covers 2013-05-09 to 2018-03-27.
    UTX Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    CCMP Stocker Initialized. Data covers 2000-04-05 to 2018-03-27.
    CHK Stocker Initialized. Data covers 1993-02-16 to 2018-03-16.
    BDE Stocker Initialized. Data covers 1998-05-27 to 2017-08-11.
    ARQL Stocker Initialized. Data covers 1996-10-16 to 2018-03-27.
    ACW Stocker Initialized. Data covers 2010-03-03 to 2016-11-17.
    HCBK Stocker Initialized. Data covers 1999-07-13 to 2015-10-30.
    ARNA Stocker Initialized. Data covers 2000-07-28 to 2018-03-27.
    MSO Stocker Initialized. Data covers 1999-10-19 to 2015-12-04.
    NPTN Stocker Initialized. Data covers 2011-02-02 to 2018-03-27.
    ATSG Stocker Initialized. Data covers 2003-07-23 to 2018-03-27.
    BLDR Stocker Initialized. Data covers 2005-06-28 to 2018-03-27.
    CHEF Stocker Initialized. Data covers 2011-07-28 to 2018-03-27.
    DOV Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    IGTE Stocker Initialized. Data covers 1996-12-17 to 2015-07-01.
    WFD Stocker Initialized. Data covers 2002-05-02 to 2016-10-21.
    HIVE Stocker Initialized. Data covers 2014-03-28 to 2018-03-27.
    MMM Stocker Initialized. Data covers 1970-01-02 to 2018-03-07.
    LG Stocker Initialized. Data covers 1987-11-05 to 2016-04-28.
    NEE Stocker Initialized. Data covers 1983-06-10 to 2018-03-27.
    DBD Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    TGT Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    SGYP Stocker Initialized. Data covers 2008-11-19 to 2018-03-27.
    APAM Stocker Initialized. Data covers 2013-03-07 to 2018-03-27.
    DHR Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    VSH Stocker Initialized. Data covers 1988-01-04 to 2018-03-27.
    CMN Stocker Initialized. Data covers 1993-02-19 to 2016-12-02.
    ADI Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    HLSS Stocker Initialized. Data covers 2012-02-29 to 2015-04-28.
    SBAC Stocker Initialized. Data covers 1999-06-16 to 2018-03-27.
    GPRE Stocker Initialized. Data covers 2006-03-15 to 2018-03-27.
    ESS Stocker Initialized. Data covers 1994-06-07 to 2018-03-27.
    RTI Stocker Initialized. Data covers 1990-04-12 to 2015-07-22.
    BABY Stocker Initialized. Data covers 2001-07-31 to 2018-03-27.
    ALKS Stocker Initialized. Data covers 1991-07-16 to 2018-03-27.
    SGEN Stocker Initialized. Data covers 2001-03-09 to 2018-03-27.
    TPR Stocker Initialized. Data covers 2017-10-31 to 2018-03-27.
    G Stocker Initialized. Data covers 2007-08-02 to 2018-03-27.
    KAR Stocker Initialized. Data covers 2009-12-11 to 2018-03-27.
    QLGC Stocker Initialized. Data covers 1994-02-28 to 2016-08-16.
    BAC Stocker Initialized. Data covers 1986-05-29 to 2018-03-27.
    TREC Stocker Initialized. Data covers 2006-07-31 to 2018-03-27.
    VIAB Stocker Initialized. Data covers 2005-12-05 to 2018-03-27.
    AOS Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    CCL Stocker Initialized. Data covers 1989-01-05 to 2018-03-27.
    UTIW Stocker Initialized. Data covers 2000-11-02 to 2016-01-22.
    ROLL Stocker Initialized. Data covers 2005-08-10 to 2018-03-27.
    EROS Stocker Initialized. Data covers 2013-11-13 to 2018-03-27.
    RYN Stocker Initialized. Data covers 1994-02-17 to 2018-03-27.
    TRS Stocker Initialized. Data covers 2007-05-18 to 2018-03-27.
    CAH Stocker Initialized. Data covers 1987-12-31 to 2018-03-27.
    GHDX Stocker Initialized. Data covers 2005-09-29 to 2018-03-27.
    SGNT Stocker Initialized. Data covers 2011-04-20 to 2016-08-29.
    ABM Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    GLUU Stocker Initialized. Data covers 2007-03-22 to 2018-03-27.
    UMH Stocker Initialized. Data covers 1993-12-06 to 2018-03-27.
    GIFI Stocker Initialized. Data covers 1997-04-04 to 2018-03-27.
    VSI Stocker Initialized. Data covers 2009-10-28 to 2018-03-27.
    AIR Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    TTGT Stocker Initialized. Data covers 2007-05-17 to 2018-03-27.
    OMI Stocker Initialized. Data covers 1988-12-16 to 2018-03-27.
    CACI Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    JBHT Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    NHI Stocker Initialized. Data covers 1991-10-09 to 2018-03-27.
    TPLM Stocker Initialized. Data covers 2005-03-14 to 2017-03-24.
    DIN Stocker Initialized. Data covers 1991-07-12 to 2018-03-27.
    PTEN Stocker Initialized. Data covers 1993-11-02 to 2018-03-27.
    CRI Stocker Initialized. Data covers 2003-10-28 to 2018-03-27.
    JWN Stocker Initialized. Data covers 1986-07-09 to 2018-03-27.
    KIN Stocker Initialized. Data covers 2013-12-12 to 2018-03-27.
    ESRX Stocker Initialized. Data covers 1992-06-09 to 2018-03-27.
    AVNR Stocker Initialized. Data covers 1990-05-08 to 2015-01-12.
    SMCI Stocker Initialized. Data covers 2007-03-29 to 2018-03-27.
    ACO Stocker Initialized. Data covers 1987-08-13 to 2014-05-08.
    AFFX Stocker Initialized. Data covers 1996-06-06 to 2016-03-31.
    NBS Stocker Initialized. Data covers 1999-03-01 to 2015-06-05.
    CPS Stocker Initialized. Data covers 2010-05-27 to 2018-03-27.
    USTR Stocker Initialized. Data covers 1990-03-26 to 2015-05-29.
    PCYG Stocker Initialized. Data covers 1999-10-27 to 2018-03-27.
    ATU Stocker Initialized. Data covers 2000-07-24 to 2018-03-27.
    VICL Stocker Initialized. Data covers 1993-03-15 to 2018-03-27.
    PODD Stocker Initialized. Data covers 2007-05-15 to 2018-03-27.
    CYTX Stocker Initialized. Data covers 2000-11-16 to 2018-03-27.
    IHS Stocker Initialized. Data covers 2005-11-14 to 2016-07-12.
    GTIV Stocker Initialized. Data covers 2000-02-10 to 2015-02-02.
    ARSD Stocker Initialized. Data covers 2006-07-31 to 2014-06-17.
    BSRR Stocker Initialized. Data covers 1996-05-30 to 2018-03-27.
    STC Stocker Initialized. Data covers 1990-03-28 to 2018-03-27.
    EXPE Stocker Initialized. Data covers 2005-07-21 to 2018-03-27.
    SASR Stocker Initialized. Data covers 1996-04-17 to 2018-03-27.
    SGY Stocker Initialized. Data covers 1993-07-09 to 2018-03-27.
    SIAL Stocker Initialized. Data covers 1990-03-26 to 2015-11-18.
    TWO Stocker Initialized. Data covers 2009-10-30 to 2018-03-27.
    UA Stocker Initialized. Data covers 2016-04-08 to 2018-03-27.
    KR Stocker Initialized. Data covers 1977-01-03 to 2018-03-27.
    FIVN Stocker Initialized. Data covers 2014-04-04 to 2018-03-27.
    ETM Stocker Initialized. Data covers 1999-01-29 to 2018-03-27.
    NKSH Stocker Initialized. Data covers 1999-12-01 to 2018-03-27.
    PBF Stocker Initialized. Data covers 2012-12-13 to 2018-03-27.
    PENN Stocker Initialized. Data covers 1994-05-26 to 2018-03-27.
    RAI Stocker Initialized. Data covers 1999-06-01 to 2017-07-24.
    STBZ Stocker Initialized. Data covers 2011-01-26 to 2018-03-27.
    VTNR Stocker Initialized. Data covers 1997-01-02 to 2018-03-27.
    NWPX Stocker Initialized. Data covers 1995-11-30 to 2018-03-27.
    MBWM Stocker Initialized. Data covers 1999-07-20 to 2018-03-27.
    AMWD Stocker Initialized. Data covers 1986-07-21 to 2018-03-27.
    TPRE Stocker Initialized. Data covers 2013-08-15 to 2018-03-27.
    DRTX Stocker Initialized. Data covers 2012-07-19 to 2014-11-17.
    MYCC Stocker Initialized. Data covers 2013-09-20 to 2017-09-18.
    AMT Stocker Initialized. Data covers 1998-02-27 to 2018-03-27.
    LMCA Stocker Initialized. Data covers 2013-01-10 to 2017-01-24.
    OXM Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    SDRL Stocker Initialized. Data covers 2005-12-28 to 2018-03-27.
    EVDY Stocker Initialized. Data covers 2014-03-28 to 2016-12-05.
    ARRY Stocker Initialized. Data covers 2000-11-30 to 2018-03-27.
    EGBN Stocker Initialized. Data covers 1999-07-14 to 2018-03-27.
    UAM Stocker Initialized. Data covers 1990-03-26 to 2017-04-27.
    DEPO Stocker Initialized. Data covers 1997-12-03 to 2018-03-27.
    FISV Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    HRTG Stocker Initialized. Data covers 2014-05-23 to 2018-03-27.
    CHCO Stocker Initialized. Data covers 1993-02-19 to 2018-03-27.
    PCG Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    TDY Stocker Initialized. Data covers 1999-11-23 to 2018-03-27.
    DXCM Stocker Initialized. Data covers 2005-04-14 to 2018-03-27.
    MGEE Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TAYC Stocker Initialized. Data covers 2002-10-16 to 2014-08-19.
    CROX Stocker Initialized. Data covers 2006-02-08 to 2018-03-27.
    ARRS Stocker Initialized. Data covers 1993-09-17 to 2018-03-27.
    AVEO Stocker Initialized. Data covers 2010-03-12 to 2018-03-27.
    TESS Stocker Initialized. Data covers 1994-09-29 to 2018-03-27.
    WHF Stocker Initialized. Data covers 2012-12-06 to 2018-03-27.
    PVTB Stocker Initialized. Data covers 1999-06-30 to 2017-06-22.
    CVGI Stocker Initialized. Data covers 2004-08-09 to 2018-03-27.
    STWD Stocker Initialized. Data covers 2009-08-12 to 2018-03-27.
    GSM Stocker Initialized. Data covers 2009-07-30 to 2018-03-27.
    SB Stocker Initialized. Data covers 2008-05-30 to 2018-03-27.
    PLAB Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ABAX Stocker Initialized. Data covers 1992-01-23 to 2018-03-27.
    VRTS Stocker Initialized. Data covers 2009-01-02 to 2018-03-27.
    JCOM Stocker Initialized. Data covers 1999-07-23 to 2018-03-27.
    TPX Stocker Initialized. Data covers 2003-12-18 to 2018-03-27.
    LMNX Stocker Initialized. Data covers 2000-04-06 to 2018-03-27.
    TPH Stocker Initialized. Data covers 2013-01-31 to 2018-03-27.
    CORR Stocker Initialized. Data covers 2007-02-02 to 2018-03-27.
    CFFI Stocker Initialized. Data covers 1998-05-07 to 2018-03-27.
    SSI Stocker Initialized. Data covers 2001-08-30 to 2018-03-27.
    MDCO Stocker Initialized. Data covers 2000-08-08 to 2018-03-27.
    SBNY Stocker Initialized. Data covers 2004-03-23 to 2018-03-27.
    KNL Stocker Initialized. Data covers 2004-12-14 to 2018-03-27.
    FMI Stocker Initialized. Data covers 2013-09-25 to 2018-03-27.
    NMIH Stocker Initialized. Data covers 2013-11-08 to 2018-03-27.
    CWST Stocker Initialized. Data covers 1997-10-29 to 2018-03-27.
    MDCA Stocker Initialized. Data covers 1995-04-17 to 2018-03-27.
    BXC Stocker Initialized. Data covers 2004-12-14 to 2018-03-27.
    MXL Stocker Initialized. Data covers 2010-03-24 to 2018-03-27.
    I Stocker Initialized. Data covers 2013-04-18 to 2018-03-27.
    SF Stocker Initialized. Data covers 1983-07-19 to 2018-03-27.
    SPPI Stocker Initialized. Data covers 1996-09-27 to 2018-03-27.
    WAG Stocker Initialized. Data covers 1985-07-01 to 2014-12-30.
    KEG Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    RGC Stocker Initialized. Data covers 2002-05-09 to 2018-02-28.
    OKSB Stocker Initialized. Data covers 1993-12-17 to 2017-10-19.
    LMOS Stocker Initialized. Data covers 2011-10-31 to 2017-11-16.
    ESNT Stocker Initialized. Data covers 2013-10-31 to 2018-03-27.
    ATHN Stocker Initialized. Data covers 2007-09-20 to 2018-03-27.
    GRMN Stocker Initialized. Data covers 2000-12-08 to 2018-03-27.
    HAL Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    HRTX Stocker Initialized. Data covers 1987-08-27 to 2018-03-27.
    UBA Stocker Initialized. Data covers 1998-08-17 to 2018-03-27.
    ANCX Stocker Initialized. Data covers 2004-07-19 to 2018-03-27.
    RIG Stocker Initialized. Data covers 1993-05-28 to 2018-03-07.
    REGN Stocker Initialized. Data covers 1991-04-02 to 2018-03-27.
    OIS Stocker Initialized. Data covers 2001-02-09 to 2018-03-27.
    AMTG Stocker Initialized. Data covers 2011-07-22 to 2016-08-31.
    EGOV Stocker Initialized. Data covers 1999-07-15 to 2018-03-27.
    UFCS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TTEK Stocker Initialized. Data covers 1991-12-17 to 2018-03-27.
    GS Stocker Initialized. Data covers 1999-05-04 to 2018-03-27.
    LDL Stocker Initialized. Data covers 1990-01-12 to 2018-03-27.
    SCHN Stocker Initialized. Data covers 1993-11-16 to 2018-03-27.
    XLNX Stocker Initialized. Data covers 1990-06-18 to 2018-03-27.
    PEGA Stocker Initialized. Data covers 1996-07-19 to 2018-03-27.
    UBNK Stocker Initialized. Data covers 2005-08-17 to 2018-03-27.
    MNTA Stocker Initialized. Data covers 2004-06-22 to 2018-03-27.
    ITW Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    SVU Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    CZR Stocker Initialized. Data covers 2012-02-08 to 2018-03-27.
    HAS Stocker Initialized. Data covers 1984-12-18 to 2018-03-27.
    HCI Stocker Initialized. Data covers 2008-09-15 to 2018-03-27.
    ABMD Stocker Initialized. Data covers 1987-07-30 to 2018-03-27.
    AVGO Stocker Initialized. Data covers 2009-08-06 to 2018-03-27.
    NFG Stocker Initialized. Data covers 1987-09-01 to 2018-03-27.
    WLP Stocker Initialized. Data covers 2014-09-22 to 2014-12-02.
    ROIAK Stocker Initialized. Data covers 2000-06-07 to 2017-05-05.
    NBIX Stocker Initialized. Data covers 1996-05-23 to 2018-03-27.
    ANGO Stocker Initialized. Data covers 2004-06-01 to 2018-03-27.
    SPLK Stocker Initialized. Data covers 2012-04-19 to 2018-03-27.
    VLO Stocker Initialized. Data covers 1982-01-04 to 2018-03-27.
    WMGI Stocker Initialized. Data covers 2001-07-17 to 2018-03-27.
    AZO Stocker Initialized. Data covers 1991-04-02 to 2018-03-27.
    CIE Stocker Initialized. Data covers 2009-12-16 to 2017-12-13.
    NEM Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    GLOG Stocker Initialized. Data covers 2012-03-30 to 2018-03-27.
    WSBC Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    HOMB Stocker Initialized. Data covers 2006-06-23 to 2018-03-27.
    FOX Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    TAXI Stocker Initialized. Data covers 1996-05-23 to 2016-05-10.
    MNR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    KIM Stocker Initialized. Data covers 1991-11-22 to 2018-03-27.
    ORCL Stocker Initialized. Data covers 1986-03-12 to 2018-03-27.
    PKG Stocker Initialized. Data covers 2000-01-28 to 2018-03-27.
    LXU Stocker Initialized. Data covers 1980-01-02 to 2018-03-27.
    KKD Stocker Initialized. Data covers 2000-04-05 to 2016-07-27.
    XEC Stocker Initialized. Data covers 2002-09-25 to 2018-03-27.
    TRW Stocker Initialized. Data covers 2004-02-03 to 2015-05-15.
    QUIK Stocker Initialized. Data covers 1999-10-18 to 2018-03-27.
    BALT Stocker Initialized. Data covers 2010-03-10 to 2015-07-17.
    CACC Stocker Initialized. Data covers 1992-06-05 to 2018-03-27.
    SNDK Stocker Initialized. Data covers 1995-11-08 to 2016-05-11.
    XOOM Stocker Initialized. Data covers 2013-02-15 to 2015-11-11.
    LO Stocker Initialized. Data covers 2008-06-10 to 2015-06-11.
    AEP Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    PLL Stocker Initialized. Data covers 1991-08-21 to 2015-08-28.
    CYNO Stocker Initialized. Data covers 2005-12-09 to 2017-03-22.
    SEE Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    NSM Stocker Initialized. Data covers 2012-03-08 to 2018-03-27.
    DAR Stocker Initialized. Data covers 1994-09-09 to 2018-03-27.
    ERA Stocker Initialized. Data covers 2013-01-22 to 2018-03-27.
    ISCA Stocker Initialized. Data covers 1997-03-10 to 2018-03-27.
    FLIC Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    VLCCF Stocker Initialized. Data covers 1997-02-07 to 2015-03-31.
    BANR Stocker Initialized. Data covers 1995-11-01 to 2018-03-27.
    BKW Stocker Initialized. Data covers 2012-06-20 to 2014-12-12.
    KFX Stocker Initialized. Data covers 2013-12-05 to 2015-05-21.
    PTIE Stocker Initialized. Data covers 2000-07-14 to 2018-03-27.
    WLTW Stocker Initialized. Data covers 2016-01-05 to 2018-03-27.
    XXII Stocker Initialized. Data covers 2011-01-26 to 2018-03-27.
    AA Stocker Initialized. Data covers 2016-11-01 to 2018-03-27.
    INSM Stocker Initialized. Data covers 2000-06-01 to 2018-03-27.
    SIF Stocker Initialized. Data covers 1980-03-17 to 2018-03-27.
    AMPE Stocker Initialized. Data covers 2010-03-31 to 2018-03-27.
    NTLS Stocker Initialized. Data covers 2006-02-09 to 2016-05-06.
    TESO Stocker Initialized. Data covers 1996-12-02 to 2017-12-14.
    QUAD Stocker Initialized. Data covers 2010-07-06 to 2018-03-27.
    SWK Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    ISSC Stocker Initialized. Data covers 2000-08-04 to 2018-03-27.
    PCO Stocker Initialized. Data covers 2004-05-12 to 2017-12-15.
    BLUE Stocker Initialized. Data covers 2013-06-19 to 2018-03-27.
    CASH Stocker Initialized. Data covers 1993-09-21 to 2018-03-27.
    EQIX Stocker Initialized. Data covers 2000-08-11 to 2018-03-27.
    STRA Stocker Initialized. Data covers 1996-07-26 to 2018-03-27.
    WTI Stocker Initialized. Data covers 2005-01-28 to 2018-03-27.
    SKT Stocker Initialized. Data covers 1993-05-28 to 2018-03-27.
    BG Stocker Initialized. Data covers 2001-08-02 to 2018-03-27.
    FXCB Stocker Initialized. Data covers 2006-10-02 to 2016-06-30.
    N Stocker Initialized. Data covers 2007-12-20 to 2016-11-07.
    TXI Stocker Initialized. Data covers 1978-05-01 to 2014-07-01.
    PPC Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    PZG Stocker Initialized. Data covers 2006-05-08 to 2018-03-27.
    TCO Stocker Initialized. Data covers 1992-11-20 to 2018-03-27.
    VPG Stocker Initialized. Data covers 2010-06-23 to 2018-03-27.
    CNSL Stocker Initialized. Data covers 2005-07-22 to 2018-03-27.
    SCLN Stocker Initialized. Data covers 1992-03-17 to 2017-10-13.
    HRC Stocker Initialized. Data covers 1987-03-02 to 2018-03-27.
    AFH Stocker Initialized. Data covers 2013-02-12 to 2018-03-27.
    PZN Stocker Initialized. Data covers 2007-10-25 to 2018-03-27.
    MHGC Stocker Initialized. Data covers 2006-02-14 to 2016-11-30.
    CLDX Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    SALM Stocker Initialized. Data covers 1999-07-01 to 2018-03-27.
    BIRT Stocker Initialized. Data covers 1998-07-17 to 2015-01-15.
    LION Stocker Initialized. Data covers 1994-10-31 to 2018-03-27.
    NYLD Stocker Initialized. Data covers 2013-07-17 to 2018-03-27.
    BJRI Stocker Initialized. Data covers 1996-10-10 to 2018-03-27.
    RDEN Stocker Initialized. Data covers 1995-12-21 to 2016-09-07.
    FRED Stocker Initialized. Data covers 2017-04-26 to 2018-03-27.
    FGL Stocker Initialized. Data covers 2013-12-13 to 2017-11-30.
    VRNT Stocker Initialized. Data covers 2002-05-16 to 2018-03-27.
    GGG Stocker Initialized. Data covers 1986-07-09 to 2018-03-27.
    ICE Stocker Initialized. Data covers 2005-11-16 to 2018-03-27.
    AGO Stocker Initialized. Data covers 2004-04-23 to 2018-03-27.
    GBL Stocker Initialized. Data covers 1999-02-11 to 2018-03-27.
    TWIN Stocker Initialized. Data covers 1987-12-31 to 2018-03-27.
    LORL Stocker Initialized. Data covers 2005-07-27 to 2018-03-27.
    CKEC Stocker Initialized. Data covers 2001-01-18 to 2016-12-21.
    MTG Stocker Initialized. Data covers 1991-08-07 to 2018-03-27.
    WLK Stocker Initialized. Data covers 2004-08-12 to 2018-03-27.
    IXYS Stocker Initialized. Data covers 1998-09-24 to 2018-01-16.
    PTSI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CVX Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    GCO Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    JOE Stocker Initialized. Data covers 1992-03-10 to 2018-03-27.
    PGTI Stocker Initialized. Data covers 2006-06-28 to 2018-03-27.
    UNT Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    BBCN Stocker Initialized. Data covers 1998-01-29 to 2016-07-29.
    F Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    CF Stocker Initialized. Data covers 2005-08-11 to 2018-03-27.
    COV Stocker Initialized. Data covers 2007-06-14 to 2015-01-26.
    ICGE Stocker Initialized. Data covers 1999-08-05 to 2014-09-02.
    ANAD Stocker Initialized. Data covers 1995-04-21 to 2016-03-15.
    GPS Stocker Initialized. Data covers 1987-07-23 to 2018-03-27.
    CLR Stocker Initialized. Data covers 2007-05-15 to 2018-03-27.
    CAR Stocker Initialized. Data covers 1990-01-12 to 2018-03-27.
    CW Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    DRIV Stocker Initialized. Data covers 1998-08-12 to 2015-02-12.
    MEIP Stocker Initialized. Data covers 2003-12-18 to 2018-03-27.
    AOI Stocker Initialized. Data covers 1995-04-03 to 2018-03-27.
    NNBR Stocker Initialized. Data covers 1994-03-15 to 2018-03-27.
    LVLT Stocker Initialized. Data covers 1998-03-31 to 2017-10-31.
    ZAGG Stocker Initialized. Data covers 2007-09-04 to 2018-03-27.
    JNY Stocker Initialized. Data covers 1991-05-16 to 2014-04-08.
    ALSN Stocker Initialized. Data covers 2012-03-15 to 2018-03-27.
    FAST Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ICFI Stocker Initialized. Data covers 2006-09-28 to 2018-03-27.
    SYY Stocker Initialized. Data covers 1973-05-08 to 2018-03-27.
    MVC Stocker Initialized. Data covers 2000-06-26 to 2018-03-27.
    DSW Stocker Initialized. Data covers 2005-06-29 to 2018-03-27.
    WIFI Stocker Initialized. Data covers 2011-05-04 to 2018-03-27.
    IPGP Stocker Initialized. Data covers 2006-12-13 to 2018-03-27.
    QTWO Stocker Initialized. Data covers 2014-03-20 to 2018-03-27.
    PLKI Stocker Initialized. Data covers 2001-03-02 to 2017-03-27.
    FRGI Stocker Initialized. Data covers 2012-04-26 to 2018-03-27.
    MGM Stocker Initialized. Data covers 1990-01-12 to 2018-03-27.
    PLXS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AMSG Stocker Initialized. Data covers 1997-12-04 to 2016-12-01.
    ACFN Stocker Initialized. Data covers 1992-02-11 to 2015-07-23.
    LTM Stocker Initialized. Data covers 2004-07-26 to 2018-03-27.
    PKD Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    AVIV Stocker Initialized. Data covers 2013-03-21 to 2015-04-01.
    ZBRA Stocker Initialized. Data covers 1991-08-15 to 2018-03-27.
    YUM Stocker Initialized. Data covers 1997-09-17 to 2018-03-27.
    BIG Stocker Initialized. Data covers 1985-06-20 to 2018-03-27.
    CSV Stocker Initialized. Data covers 1996-08-09 to 2018-03-27.
    LBTYA Stocker Initialized. Data covers 2004-06-03 to 2018-03-27.
    LDR Stocker Initialized. Data covers 1992-03-17 to 2017-10-18.
    ATK Stocker Initialized. Data covers 1990-10-03 to 2015-02-09.
    AKRX Stocker Initialized. Data covers 2002-08-02 to 2018-03-27.
    FRBK Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    BCRX Stocker Initialized. Data covers 1994-03-04 to 2018-03-27.
    PSEM Stocker Initialized. Data covers 1997-10-31 to 2015-11-24.
    BRT Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    NPBC Stocker Initialized. Data covers 1990-03-27 to 2016-04-01.
    PSMI Stocker Initialized. Data covers 2012-08-08 to 2014-12-12.
    RNET Stocker Initialized. Data covers 2010-12-15 to 2018-03-27.
    GT Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    SNAK Stocker Initialized. Data covers 1996-12-06 to 2017-12-14.
    IBCA Stocker Initialized. Data covers 1998-06-03 to 2015-02-10.
    CNSI Stocker Initialized. Data covers 2012-10-24 to 2015-09-08.
    ALEX Stocker Initialized. Data covers 2012-06-14 to 2018-03-27.
    EBIO Stocker Initialized. Data covers 2014-02-06 to 2018-03-27.
    SPNS Stocker Initialized. Data covers 1998-03-05 to 2018-03-27.
    AJG Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    ECOL Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FR Stocker Initialized. Data covers 1994-06-24 to 2018-03-27.
    JAH Stocker Initialized. Data covers 1993-03-29 to 2016-04-15.
    CTS Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    ZEN Stocker Initialized. Data covers 2014-05-15 to 2018-03-27.
    A Stocker Initialized. Data covers 1999-11-18 to 2018-03-27.
    XYL Stocker Initialized. Data covers 2011-10-13 to 2018-03-27.
    GEO Stocker Initialized. Data covers 1994-07-28 to 2018-03-27.
    LTXC Stocker Initialized. Data covers 1990-03-26 to 2014-05-21.
    SSD Stocker Initialized. Data covers 1994-05-26 to 2018-03-27.
    CHDX Stocker Initialized. Data covers 1994-08-19 to 2014-09-29.
    RLYP Stocker Initialized. Data covers 2013-11-15 to 2016-09-01.
    SM Stocker Initialized. Data covers 1992-12-21 to 2018-03-27.
    VOXX Stocker Initialized. Data covers 1992-03-16 to 2018-03-27.
    FDP Stocker Initialized. Data covers 1997-10-24 to 2018-03-27.
    SFL Stocker Initialized. Data covers 2004-06-17 to 2018-03-27.
    FCE_A Stocker Initialized. Data covers 1983-10-25 to 2018-03-27.
    MTDR Stocker Initialized. Data covers 2012-02-02 to 2018-03-27.
    RSTI Stocker Initialized. Data covers 1996-09-26 to 2016-11-07.
    NM Stocker Initialized. Data covers 2005-01-06 to 2018-03-27.
    FCEL Stocker Initialized. Data covers 1997-02-27 to 2018-03-27.
    FUL Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    THC Stocker Initialized. Data covers 1982-01-04 to 2018-03-07.
    STSI Stocker Initialized. Data covers 1999-03-22 to 2014-06-03.
    VCYT Stocker Initialized. Data covers 2013-10-30 to 2018-03-27.
    FBHS Stocker Initialized. Data covers 2011-09-16 to 2018-03-27.
    MVNR Stocker Initialized. Data covers 2013-11-07 to 2015-04-28.
    ANH Stocker Initialized. Data covers 1998-03-12 to 2018-03-27.
    BDX Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    LMT Stocker Initialized. Data covers 1977-01-03 to 2018-03-27.
    ANN Stocker Initialized. Data covers 1991-05-17 to 2015-08-21.
    IIIN Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    CCK Stocker Initialized. Data covers 1984-12-18 to 2018-03-27.
    ENV Stocker Initialized. Data covers 2010-07-29 to 2018-03-27.
    HTZ Stocker Initialized. Data covers 2006-11-16 to 2018-03-27.
    TUES Stocker Initialized. Data covers 1999-04-22 to 2018-03-27.
    IP Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    HITK Stocker Initialized. Data covers 1992-08-04 to 2014-04-17.
    TRMB Stocker Initialized. Data covers 1992-03-03 to 2018-03-27.
    FWM Stocker Initialized. Data covers 2013-04-17 to 2016-05-13.
    WLH Stocker Initialized. Data covers 2013-05-16 to 2018-03-27.
    TIME Stocker Initialized. Data covers 2014-05-21 to 2018-01-31.
    SMTC Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    CYH Stocker Initialized. Data covers 2000-06-09 to 2018-03-27.
    GMCR Stocker Initialized. Data covers 1993-09-27 to 2016-03-02.
    NWS Stocker Initialized. Data covers 2013-06-19 to 2018-03-27.
    AIG Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    AFL Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    TSN Stocker Initialized. Data covers 1986-07-09 to 2018-03-27.
    EME Stocker Initialized. Data covers 1995-12-28 to 2018-03-27.
    KSU Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    SUN Stocker Initialized. Data covers 2012-09-20 to 2018-03-27.
    CRK Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    GEOS Stocker Initialized. Data covers 1997-11-21 to 2018-03-27.
    OFIX Stocker Initialized. Data covers 1992-04-24 to 2018-03-27.
    SFBS Stocker Initialized. Data covers 2014-05-14 to 2018-03-27.
    APOG Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    CRUS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AWK Stocker Initialized. Data covers 2008-04-23 to 2018-03-27.
    LAMR Stocker Initialized. Data covers 1996-08-02 to 2018-03-27.
    PBYI Stocker Initialized. Data covers 2012-04-24 to 2018-03-27.
    ORIT Stocker Initialized. Data covers 2007-01-24 to 2018-03-27.
    HD Stocker Initialized. Data covers 1981-09-22 to 2018-03-27.
    LGF Stocker Initialized. Data covers 1998-11-17 to 2016-12-08.
    PFIE Stocker Initialized. Data covers 2010-03-10 to 2018-03-27.
    FIBK Stocker Initialized. Data covers 2010-03-24 to 2018-03-27.
    ISH Stocker Initialized. Data covers 1991-10-24 to 2015-12-18.
    TIF Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    AYR Stocker Initialized. Data covers 2006-08-08 to 2018-03-27.
    TTS Stocker Initialized. Data covers 2012-08-22 to 2018-03-27.
    KMPR Stocker Initialized. Data covers 1991-09-18 to 2018-03-27.
    CMCSA Stocker Initialized. Data covers 1988-07-07 to 2018-03-27.
    HL Stocker Initialized. Data covers 1985-02-14 to 2018-03-27.
    CY Stocker Initialized. Data covers 1989-04-05 to 2018-03-27.
    OABC Stocker Initialized. Data covers 2010-01-21 to 2014-12-17.
    VMI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PII Stocker Initialized. Data covers 1987-09-16 to 2018-03-27.
    FCH Stocker Initialized. Data covers 1994-07-22 to 2017-08-31.
    TTC Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    NFLX Stocker Initialized. Data covers 2002-05-23 to 2018-03-27.
    AFAM Stocker Initialized. Data covers 1993-02-19 to 2018-03-27.
    HEAR Stocker Initialized. Data covers 2010-11-15 to 2018-03-27.
    OCR Stocker Initialized. Data covers 1987-12-30 to 2015-08-17.
    ANR Stocker Initialized. Data covers 2005-02-15 to 2015-07-16.
    HNR Stocker Initialized. Data covers 1989-11-07 to 2017-05-04.
    ELRC Stocker Initialized. Data covers 1990-03-28 to 2016-08-10.
    PEBO Stocker Initialized. Data covers 1993-02-11 to 2018-03-27.
    PH Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    TISI Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    BREW Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    RAVN Stocker Initialized. Data covers 1980-03-17 to 2018-03-27.
    PETS Stocker Initialized. Data covers 1999-04-26 to 2018-03-27.
    UVE Stocker Initialized. Data covers 2003-06-06 to 2018-03-27.
    AMED Stocker Initialized. Data covers 1994-08-18 to 2018-03-27.
    YHOO Stocker Initialized. Data covers 1996-04-12 to 2017-06-16.
    MXWL Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ENR Stocker Initialized. Data covers 2000-03-27 to 2018-03-27.
    AGTC Stocker Initialized. Data covers 2014-03-27 to 2018-03-27.
    HXL Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    CHGG Stocker Initialized. Data covers 2013-11-13 to 2018-03-27.
    MG Stocker Initialized. Data covers 2009-10-08 to 2018-03-27.
    KMB Stocker Initialized. Data covers 1984-12-17 to 2018-03-27.
    SHOS Stocker Initialized. Data covers 2012-10-12 to 2018-03-27.
    MBFI Stocker Initialized. Data covers 1995-04-07 to 2018-03-27.
    AMAG Stocker Initialized. Data covers 1986-06-12 to 2018-03-27.
    PFE Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    FSLR Stocker Initialized. Data covers 2006-11-17 to 2018-03-07.
    STNR Stocker Initialized. Data covers 1996-11-13 to 2015-12-09.
    ASEI Stocker Initialized. Data covers 1984-09-07 to 2016-09-09.
    OPK Stocker Initialized. Data covers 1995-11-02 to 2018-03-27.
    MTB Stocker Initialized. Data covers 1991-10-04 to 2018-03-27.
    FTD Stocker Initialized. Data covers 2013-10-10 to 2018-03-27.
    ABCB Stocker Initialized. Data covers 1994-05-19 to 2018-03-27.
    MNST Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    SYRG Stocker Initialized. Data covers 2008-02-28 to 2017-03-03.
    LIFE Stocker Initialized. Data covers 2015-05-07 to 2018-03-07.
    AKR Stocker Initialized. Data covers 1993-05-27 to 2018-03-27.
    RMTI Stocker Initialized. Data covers 1998-01-27 to 2018-03-27.
    PZZA Stocker Initialized. Data covers 1993-06-08 to 2018-03-27.
    ADS Stocker Initialized. Data covers 2001-06-15 to 2018-03-27.
    AMZN Stocker Initialized. Data covers 1997-05-16 to 2018-03-27.
    COTY Stocker Initialized. Data covers 2013-06-13 to 2018-03-27.
    ENZN Stocker Initialized. Data covers 1990-03-26 to 2016-05-19.
    SANM Stocker Initialized. Data covers 1993-06-22 to 2018-03-27.
    HTCO Stocker Initialized. Data covers 1995-03-29 to 2014-05-07.
    HAFC Stocker Initialized. Data covers 1997-05-09 to 2018-03-27.
    PM Stocker Initialized. Data covers 2008-03-17 to 2018-03-27.
    RBC Stocker Initialized. Data covers 1983-12-01 to 2018-03-27.
    MASI Stocker Initialized. Data covers 2007-08-08 to 2018-03-27.
    OCFC Stocker Initialized. Data covers 1996-07-03 to 2018-03-27.
    EIG Stocker Initialized. Data covers 2007-01-31 to 2018-03-27.
    GSBD Stocker Initialized. Data covers 2015-03-18 to 2018-03-27.
    REGI Stocker Initialized. Data covers 2012-01-19 to 2018-03-27.
    AMBA Stocker Initialized. Data covers 2012-10-10 to 2018-03-27.
    CNX Stocker Initialized. Data covers 1999-04-30 to 2018-03-07.
    SNI Stocker Initialized. Data covers 2008-06-12 to 2018-03-06.
    SJM Stocker Initialized. Data covers 1994-10-31 to 2018-03-27.
    ATLO Stocker Initialized. Data covers 2000-02-15 to 2018-03-27.
    USAP Stocker Initialized. Data covers 1994-12-28 to 2018-03-27.
    MRH Stocker Initialized. Data covers 2002-10-10 to 2015-07-31.
    SWC Stocker Initialized. Data covers 1994-12-19 to 2017-05-03.
    ACIW Stocker Initialized. Data covers 1995-02-27 to 2018-03-27.
    ZTS Stocker Initialized. Data covers 2013-02-01 to 2018-03-27.
    CTT Stocker Initialized. Data covers 2013-12-12 to 2018-03-27.
    TIVO Stocker Initialized. Data covers 1997-03-13 to 2018-03-27.
    VMC Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    BCEI Stocker Initialized. Data covers 2011-12-15 to 2018-03-27.
    ENTA Stocker Initialized. Data covers 2013-03-21 to 2018-03-27.
    CBT Stocker Initialized. Data covers 1980-11-05 to 2018-03-27.
    PAG Stocker Initialized. Data covers 1996-10-23 to 2018-03-27.
    CELG Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    UDR Stocker Initialized. Data covers 1990-03-07 to 2018-03-27.
    COBZ Stocker Initialized. Data covers 1998-06-18 to 2018-03-27.
    EPIQ Stocker Initialized. Data covers 1997-02-04 to 2016-09-30.
    EXXI Stocker Initialized. Data covers 2007-06-01 to 2018-03-20.
    FORR Stocker Initialized. Data covers 1996-11-27 to 2018-03-27.
    HUN Stocker Initialized. Data covers 2005-02-14 to 2018-03-27.
    MITT Stocker Initialized. Data covers 2011-06-30 to 2018-03-27.
    ITIC Stocker Initialized. Data covers 1990-03-27 to 2018-03-27.
    VASC Stocker Initialized. Data covers 2000-07-20 to 2017-02-17.
    CMLS Stocker Initialized. Data covers 2002-04-09 to 2017-11-21.
    FLXN Stocker Initialized. Data covers 2014-02-12 to 2018-03-27.
    OVTI Stocker Initialized. Data covers 2000-07-14 to 2016-01-28.
    SPGI Stocker Initialized. Data covers 2016-04-28 to 2018-03-27.
    FURX Stocker Initialized. Data covers 2010-06-01 to 2014-07-02.
    HBAN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ASCMA Stocker Initialized. Data covers 2008-09-18 to 2018-03-27.
    EHTH Stocker Initialized. Data covers 2006-10-20 to 2018-03-27.
    HVT Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    POL Stocker Initialized. Data covers 1999-09-13 to 2018-03-27.
    PHH Stocker Initialized. Data covers 2005-01-19 to 2018-03-27.
    CAP Stocker Initialized. Data covers 2007-05-16 to 2015-08-13.
    OGS Stocker Initialized. Data covers 2014-01-16 to 2018-03-27.
    TEX Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FFIV Stocker Initialized. Data covers 1999-06-04 to 2018-03-27.
    WBC Stocker Initialized. Data covers 2007-08-01 to 2018-03-27.
    WG Stocker Initialized. Data covers 1996-08-15 to 2018-03-26.
    PEGI Stocker Initialized. Data covers 2013-09-27 to 2018-03-27.
    RTIX Stocker Initialized. Data covers 2000-08-10 to 2018-03-27.
    VNTV Stocker Initialized. Data covers 2012-03-22 to 2018-01-12.
    MON Stocker Initialized. Data covers 2000-10-18 to 2018-03-27.
    BNFT Stocker Initialized. Data covers 2013-09-18 to 2018-03-27.
    BXP Stocker Initialized. Data covers 1997-06-18 to 2018-03-27.
    CBZ Stocker Initialized. Data covers 1995-04-27 to 2018-03-27.
    STML Stocker Initialized. Data covers 2013-01-29 to 2018-03-27.
    NOC Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    WWD Stocker Initialized. Data covers 2017-04-26 to 2018-03-27.
    CBST Stocker Initialized. Data covers 1996-10-25 to 2015-01-21.
    PPO Stocker Initialized. Data covers 2007-07-26 to 2015-08-25.
    QLTY Stocker Initialized. Data covers 2003-11-07 to 2015-08-17.
    SFE Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    APD Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    MORN Stocker Initialized. Data covers 2005-05-03 to 2018-03-27.
    NETE Stocker Initialized. Data covers 2008-10-17 to 2018-03-27.
    ENH Stocker Initialized. Data covers 2003-02-28 to 2017-03-28.
    TE Stocker Initialized. Data covers 1984-10-29 to 2016-06-30.
    ARPI Stocker Initialized. Data covers 2013-05-09 to 2016-02-29.
    AVY Stocker Initialized. Data covers 1983-12-29 to 2018-03-27.
    EFX Stocker Initialized. Data covers 1986-03-27 to 2018-03-27.
    ADMS Stocker Initialized. Data covers 2014-04-10 to 2018-03-27.
    BID Stocker Initialized. Data covers 1988-05-13 to 2018-03-27.
    PRGO Stocker Initialized. Data covers 1991-12-17 to 2018-03-27.
    UNM Stocker Initialized. Data covers 1986-11-06 to 2018-03-27.
    RESI Stocker Initialized. Data covers 2012-12-24 to 2018-03-27.
    CONE Stocker Initialized. Data covers 2013-01-18 to 2018-03-27.
    R Stocker Initialized. Data covers 1980-01-02 to 2018-03-07.
    COVS Stocker Initialized. Data covers 2013-09-26 to 2017-07-26.
    EXPD Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    EOX Stocker Initialized. Data covers 2004-08-10 to 2016-03-22.
    SHO Stocker Initialized. Data covers 2004-10-21 to 2018-03-27.
    AE Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    GOOD Stocker Initialized. Data covers 2003-08-14 to 2018-03-27.
    FCNCA Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    CSLT Stocker Initialized. Data covers 2014-03-14 to 2018-03-27.
    MRLN Stocker Initialized. Data covers 2003-11-12 to 2018-03-27.
    IDCC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CHS Stocker Initialized. Data covers 1993-03-24 to 2018-03-27.
    HASI Stocker Initialized. Data covers 2013-04-18 to 2018-03-27.
    CDNS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ETFC Stocker Initialized. Data covers 1996-08-16 to 2018-03-27.
    GSBC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    GPN Stocker Initialized. Data covers 2001-01-16 to 2018-03-27.
    LBMH Stocker Initialized. Data covers 2007-09-04 to 2016-01-21.
    AROW Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    CHMG Stocker Initialized. Data covers 1999-01-04 to 2018-03-27.
    QTM Stocker Initialized. Data covers 1999-08-02 to 2018-03-27.
    TIPT Stocker Initialized. Data covers 2010-10-15 to 2018-03-27.
    YRCW Stocker Initialized. Data covers 1986-07-09 to 2018-03-27.
    FXCM Stocker Initialized. Data covers 2010-12-02 to 2017-02-24.
    WBCO Stocker Initialized. Data covers 1998-06-23 to 2014-04-30.
    PDCO Stocker Initialized. Data covers 1992-10-28 to 2018-03-16.
    POOL Stocker Initialized. Data covers 1995-10-13 to 2018-03-27.
    TGH Stocker Initialized. Data covers 2007-10-10 to 2018-03-27.
    AFSI Stocker Initialized. Data covers 2006-11-28 to 2018-03-27.
    DAKT Stocker Initialized. Data covers 1994-02-10 to 2018-03-27.
    PNK Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TROX Stocker Initialized. Data covers 2010-12-01 to 2018-03-27.
    CAG Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    CLX Stocker Initialized. Data covers 1983-03-21 to 2018-03-27.
    FLWS Stocker Initialized. Data covers 1999-08-03 to 2018-03-27.
    MYE Stocker Initialized. Data covers 1987-09-08 to 2018-03-27.
    BPFH Stocker Initialized. Data covers 1994-02-14 to 2018-03-27.
    SXI Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    GAIN Stocker Initialized. Data covers 2005-06-23 to 2018-03-27.
    CLFD Stocker Initialized. Data covers 1986-08-07 to 2018-03-27.
    LQDT Stocker Initialized. Data covers 2006-02-27 to 2018-03-27.
    EQR Stocker Initialized. Data covers 1993-08-12 to 2018-03-27.
    HIIQ Stocker Initialized. Data covers 2013-02-08 to 2018-03-27.
    JEC Stocker Initialized. Data covers 1990-01-12 to 2018-03-27.
    SQI Stocker Initialized. Data covers 2010-09-24 to 2016-07-28.
    CIEN Stocker Initialized. Data covers 1997-02-07 to 2018-03-27.
    PNY Stocker Initialized. Data covers 1987-12-30 to 2016-10-03.
    CNL Stocker Initialized. Data covers 1987-11-05 to 2016-04-13.
    SCG Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    SIGM Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PCYC Stocker Initialized. Data covers 1995-10-24 to 2015-05-22.
    RVNC Stocker Initialized. Data covers 2014-02-06 to 2018-03-27.
    GBCI Stocker Initialized. Data covers 1992-01-27 to 2018-03-27.
    PTRY Stocker Initialized. Data covers 1999-06-10 to 2015-03-16.
    HLS Stocker Initialized. Data covers 1989-09-13 to 2017-12-29.
    HURN Stocker Initialized. Data covers 2004-10-13 to 2018-03-27.
    PACB Stocker Initialized. Data covers 2010-10-27 to 2018-03-27.
    WDFC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CYS Stocker Initialized. Data covers 2009-06-16 to 2018-03-27.
    TEG Stocker Initialized. Data covers 1988-01-05 to 2015-06-29.
    SAIC Stocker Initialized. Data covers 2013-09-16 to 2018-03-27.
    DTV Stocker Initialized. Data covers 2003-12-23 to 2018-03-07.
    PMCS Stocker Initialized. Data covers 1991-04-24 to 2016-01-14.
    AL Stocker Initialized. Data covers 2011-04-19 to 2018-03-27.
    CINF Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AVG Stocker Initialized. Data covers 2012-02-02 to 2016-11-07.
    LYV Stocker Initialized. Data covers 2005-12-21 to 2018-03-27.
    EZPW Stocker Initialized. Data covers 1991-08-27 to 2018-03-27.
    SCCO Stocker Initialized. Data covers 1996-01-05 to 2018-03-27.
    MEAS Stocker Initialized. Data covers 1993-04-26 to 2014-10-09.
    ETH Stocker Initialized. Data covers 1993-03-16 to 2018-03-27.
    WERN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ALCO Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    SNOW Stocker Initialized. Data covers 2014-01-31 to 2017-07-31.
    NL Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    CLI Stocker Initialized. Data covers 1994-08-25 to 2018-03-27.
    CSS Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    SUNS Stocker Initialized. Data covers 2011-02-25 to 2018-03-27.
    CUBI Stocker Initialized. Data covers 2012-03-14 to 2018-03-27.
    NU Stocker Initialized. Data covers 1984-08-29 to 2015-02-18.
    UNXL Stocker Initialized. Data covers 2006-03-07 to 2017-09-11.
    NWBI Stocker Initialized. Data covers 1994-11-08 to 2018-03-27.
    FDUS Stocker Initialized. Data covers 2011-06-21 to 2018-03-27.
    HPE Stocker Initialized. Data covers 2015-11-02 to 2018-03-27.
    PIKE Stocker Initialized. Data covers 2005-07-27 to 2014-12-22.
    UFI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    UFPT Stocker Initialized. Data covers 1993-12-17 to 2018-03-27.
    WAT Stocker Initialized. Data covers 1995-11-17 to 2018-03-27.
    MA Stocker Initialized. Data covers 2006-05-25 to 2018-03-27.
    LNCE Stocker Initialized. Data covers 1990-03-26 to 2018-03-23.
    CRY Stocker Initialized. Data covers 1993-02-12 to 2018-03-27.
    NBHC Stocker Initialized. Data covers 2012-09-20 to 2018-03-27.
    POZN Stocker Initialized. Data covers 2000-10-16 to 2016-02-05.
    SRPT Stocker Initialized. Data covers 1997-06-04 to 2018-03-27.
    CB Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    IDTI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    RNWK Stocker Initialized. Data covers 1997-11-21 to 2018-03-27.
    EXPO Stocker Initialized. Data covers 1990-08-17 to 2018-03-27.
    LWAY Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    MRTX Stocker Initialized. Data covers 2013-07-15 to 2018-03-27.
    EXTR Stocker Initialized. Data covers 1999-04-09 to 2018-03-27.
    ANF Stocker Initialized. Data covers 1996-09-26 to 2018-03-27.
    CALM Stocker Initialized. Data covers 1996-12-12 to 2018-03-27.
    TICC Stocker Initialized. Data covers 2003-11-24 to 2018-03-22.
    RPAI Stocker Initialized. Data covers 2012-04-09 to 2018-03-27.
    IDA Stocker Initialized. Data covers 1986-10-17 to 2018-03-27.
    BGFV Stocker Initialized. Data covers 2002-09-17 to 2018-03-27.
    MBII Stocker Initialized. Data covers 2013-08-02 to 2018-03-27.
    RSPP Stocker Initialized. Data covers 2014-01-17 to 2018-03-27.
    AIQ Stocker Initialized. Data covers 2001-07-31 to 2017-08-18.
    AMGN Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    AMTD Stocker Initialized. Data covers 1997-03-04 to 2018-03-27.
    AEPI Stocker Initialized. Data covers 1986-01-31 to 2017-01-20.
    LNT Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    CLC Stocker Initialized. Data covers 1990-03-26 to 2017-02-27.
    PLXT Stocker Initialized. Data covers 1999-04-06 to 2014-08-12.
    BTX Stocker Initialized. Data covers 1992-03-06 to 2018-03-27.
    HCKT Stocker Initialized. Data covers 1998-05-28 to 2018-03-27.
    NBL Stocker Initialized. Data covers 1982-01-04 to 2018-03-27.
    AMRI Stocker Initialized. Data covers 1999-02-04 to 2017-08-31.
    ETN Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    ROSE Stocker Initialized. Data covers 2006-02-13 to 2018-03-27.
    SUSS Stocker Initialized. Data covers 2006-10-19 to 2014-08-29.
    NEOG Stocker Initialized. Data covers 1994-02-10 to 2018-03-27.
    IGT Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TTEC Stocker Initialized. Data covers 1996-08-01 to 2018-03-27.
    LAYN Stocker Initialized. Data covers 1992-08-20 to 2018-03-27.
    HRL Stocker Initialized. Data covers 1990-01-02 to 2018-03-27.
    STJ Stocker Initialized. Data covers 1989-12-07 to 2017-01-04.
    BKD Stocker Initialized. Data covers 2005-11-22 to 2018-03-27.
    LECO Stocker Initialized. Data covers 1995-06-13 to 2018-03-27.
    CHH Stocker Initialized. Data covers 1996-10-16 to 2018-03-27.
    AWR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    KMI Stocker Initialized. Data covers 2011-02-11 to 2018-03-27.
    HTBK Stocker Initialized. Data covers 1998-07-20 to 2018-03-27.
    GTXI Stocker Initialized. Data covers 2004-02-03 to 2018-03-27.
    EEFT Stocker Initialized. Data covers 1997-03-07 to 2018-03-27.
    AXDX Stocker Initialized. Data covers 1996-11-19 to 2018-03-27.
    PRU Stocker Initialized. Data covers 2001-12-13 to 2018-03-27.
    SKH Stocker Initialized. Data covers 2007-05-15 to 2015-02-02.
    DRH Stocker Initialized. Data covers 2005-05-26 to 2018-03-27.
    GSIG Stocker Initialized. Data covers 1999-03-24 to 2016-05-11.
    REG Stocker Initialized. Data covers 1993-10-29 to 2018-03-27.
    EXR Stocker Initialized. Data covers 2004-08-16 to 2018-03-27.
    ALB Stocker Initialized. Data covers 1994-02-22 to 2018-03-27.
    OUTR Stocker Initialized. Data covers 1997-07-03 to 2016-09-26.
    EPL Stocker Initialized. Data covers 2009-09-23 to 2014-06-03.
    EQY Stocker Initialized. Data covers 1998-05-14 to 2017-03-01.
    RRC Stocker Initialized. Data covers 1992-12-28 to 2018-03-27.
    VRX Stocker Initialized. Data covers 1994-03-30 to 2018-03-27.
    METR Stocker Initialized. Data covers 1995-08-18 to 2016-02-12.
    NGVC Stocker Initialized. Data covers 2012-07-25 to 2018-03-27.
    PKI Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    JAKK Stocker Initialized. Data covers 1996-05-02 to 2018-03-27.
    THRM Stocker Initialized. Data covers 1993-06-10 to 2018-03-27.
    BOLT Stocker Initialized. Data covers 1995-02-01 to 2014-11-18.
    KRFT Stocker Initialized. Data covers 2012-09-17 to 2015-07-02.
    MITK Stocker Initialized. Data covers 1995-05-26 to 2018-03-27.
    OPLK Stocker Initialized. Data covers 2000-10-04 to 2014-12-23.
    SCMP Stocker Initialized. Data covers 2007-08-02 to 2018-02-13.
    GBLI Stocker Initialized. Data covers 2003-12-16 to 2018-03-27.
    PHX Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    TCPC Stocker Initialized. Data covers 2012-04-04 to 2018-03-27.
    ZLC Stocker Initialized. Data covers 1993-08-09 to 2014-05-29.
    CHUY Stocker Initialized. Data covers 2012-07-24 to 2018-03-27.
    PCTY Stocker Initialized. Data covers 2014-03-19 to 2018-03-27.
    ARUN Stocker Initialized. Data covers 2007-03-27 to 2015-05-18.
    CFNL Stocker Initialized. Data covers 1998-07-17 to 2017-04-21.
    WAC Stocker Initialized. Data covers 1998-03-24 to 2018-02-09.
    BK Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    CRL Stocker Initialized. Data covers 2000-06-23 to 2018-03-27.
    PLUS Stocker Initialized. Data covers 1996-11-15 to 2018-03-27.
    SYA Stocker Initialized. Data covers 2010-01-22 to 2016-01-29.
    LPI Stocker Initialized. Data covers 2011-12-15 to 2018-03-27.
    HTH Stocker Initialized. Data covers 2004-02-19 to 2018-03-27.
    POR Stocker Initialized. Data covers 2006-03-31 to 2018-03-27.
    HRZN Stocker Initialized. Data covers 2010-10-29 to 2018-03-27.
    VDSI Stocker Initialized. Data covers 1998-05-21 to 2018-03-27.
    RBCAA Stocker Initialized. Data covers 1998-07-22 to 2018-03-27.
    PANW Stocker Initialized. Data covers 2012-07-20 to 2018-03-27.
    KFRC Stocker Initialized. Data covers 1995-08-15 to 2018-03-27.
    NDSN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TMUS Stocker Initialized. Data covers 2007-04-19 to 2018-03-27.
    TQNT Stocker Initialized. Data covers 1993-12-14 to 2014-12-31.
    IMGN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ZNGA Stocker Initialized. Data covers 2011-12-16 to 2018-03-27.
    GTAT Stocker Initialized. Data covers 2008-07-25 to 2014-10-15.
    LTC Stocker Initialized. Data covers 1992-08-25 to 2018-03-27.
    RJET Stocker Initialized. Data covers 2004-05-27 to 2016-03-07.
    GOOGL Stocker Initialized. Data covers 2004-08-19 to 2018-03-27.
    PMT Stocker Initialized. Data covers 2009-07-30 to 2018-03-27.
    OCN Stocker Initialized. Data covers 1996-09-25 to 2018-03-27.
    GWR Stocker Initialized. Data covers 1996-06-25 to 2018-03-27.
    NBBC Stocker Initialized. Data covers 1990-03-26 to 2016-02-29.
    VSTM Stocker Initialized. Data covers 2012-01-27 to 2018-03-27.
    PXD Stocker Initialized. Data covers 1997-08-08 to 2018-03-27.
    SZMK Stocker Initialized. Data covers 2014-02-10 to 2016-09-26.
    CBF Stocker Initialized. Data covers 2012-09-20 to 2017-11-30.
    MATW Stocker Initialized. Data covers 1994-08-10 to 2018-03-27.
    LPG Stocker Initialized. Data covers 2014-05-08 to 2018-03-27.
    SLM Stocker Initialized. Data covers 1988-01-05 to 2018-03-07.
    PRTA Stocker Initialized. Data covers 2012-12-21 to 2018-03-27.
    CSU Stocker Initialized. Data covers 1997-10-31 to 2018-03-27.
    AKS Stocker Initialized. Data covers 1994-03-30 to 2018-03-27.
    MTOR Stocker Initialized. Data covers 2000-07-10 to 2018-03-27.
    TTPH Stocker Initialized. Data covers 2013-03-20 to 2018-03-27.
    CKP Stocker Initialized. Data covers 1986-11-12 to 2016-05-13.
    PTLA Stocker Initialized. Data covers 2013-05-22 to 2018-03-27.
    GHC Stocker Initialized. Data covers 1990-01-24 to 2018-03-27.
    D Stocker Initialized. Data covers 1984-10-03 to 2018-03-27.
    DDS Stocker Initialized. Data covers 1989-06-30 to 2018-03-27.
    DXC Stocker Initialized. Data covers 2017-04-03 to 2018-03-27.
    CRRS Stocker Initialized. Data covers 1999-05-03 to 2015-03-03.
    GXP Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    PF Stocker Initialized. Data covers 2013-03-28 to 2018-03-27.
    MOFG Stocker Initialized. Data covers 2008-01-29 to 2018-03-27.
    LINTA Stocker Initialized. Data covers 2006-05-10 to 2014-10-06.
    OXY Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    PHM Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    RNST Stocker Initialized. Data covers 1992-04-24 to 2018-03-27.
    SNA Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    MTH Stocker Initialized. Data covers 1988-12-16 to 2018-03-27.
    CMCO Stocker Initialized. Data covers 1996-02-28 to 2018-03-27.
    RJF Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    MC Stocker Initialized. Data covers 2014-04-16 to 2018-03-27.
    EXH Stocker Initialized. Data covers 2007-08-21 to 2015-11-03.
    ARC Stocker Initialized. Data covers 2005-02-04 to 2018-03-27.
    SPWH Stocker Initialized. Data covers 2014-04-17 to 2018-03-27.
    HVB Stocker Initialized. Data covers 1999-12-13 to 2015-06-30.
    AYI Stocker Initialized. Data covers 2001-12-03 to 2018-03-27.
    BMTC Stocker Initialized. Data covers 1985-08-08 to 2018-03-27.
    EXAC Stocker Initialized. Data covers 1996-05-30 to 2018-02-14.
    SCBT Stocker Initialized. Data covers 1997-01-28 to 2014-06-27.
    TAT Stocker Initialized. Data covers 2007-04-09 to 2018-03-27.
    LOGM Stocker Initialized. Data covers 2009-07-01 to 2018-03-27.
    GNCA Stocker Initialized. Data covers 2014-02-05 to 2018-03-27.
    TIS Stocker Initialized. Data covers 2005-07-15 to 2018-03-27.
    STMP Stocker Initialized. Data covers 1999-06-25 to 2018-03-27.
    BA Stocker Initialized. Data covers 1962-01-02 to 2018-03-27.
    XXIA Stocker Initialized. Data covers 2000-10-24 to 2017-04-18.
    THS Stocker Initialized. Data covers 2005-06-28 to 2018-03-27.
    NTAP Stocker Initialized. Data covers 1995-11-21 to 2018-03-27.
    MOS Stocker Initialized. Data covers 1988-01-26 to 2018-03-27.
    NYRT Stocker Initialized. Data covers 2014-04-15 to 2018-03-27.
    CRD_B Stocker Initialized. Data covers 1990-01-12 to 2018-03-27.
    ARCC Stocker Initialized. Data covers 2004-10-05 to 2018-03-27.
    CTRX Stocker Initialized. Data covers 2006-06-13 to 2015-07-23.
    HSTM Stocker Initialized. Data covers 2000-04-11 to 2018-03-27.
    CLF Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    TTI Stocker Initialized. Data covers 1990-04-03 to 2018-03-27.
    DTE Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    HRS Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    SGBK Stocker Initialized. Data covers 2007-05-01 to 2017-09-26.
    FE Stocker Initialized. Data covers 1997-11-10 to 2018-03-27.
    KBALB Stocker Initialized. Data covers 1990-03-26 to 2014-10-31.
    LH Stocker Initialized. Data covers 1990-03-29 to 2018-03-27.
    RGA Stocker Initialized. Data covers 2008-09-12 to 2018-03-27.
    TER Stocker Initialized. Data covers 1987-03-11 to 2018-03-27.
    DNB Stocker Initialized. Data covers 1983-06-10 to 2018-03-07.
    TMP Stocker Initialized. Data covers 1990-03-28 to 2018-03-27.
    UIS Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    ECL Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    VOYA Stocker Initialized. Data covers 2013-05-02 to 2018-03-27.
    LGND Stocker Initialized. Data covers 1992-11-18 to 2018-03-27.
    SAPE Stocker Initialized. Data covers 1996-04-04 to 2015-02-05.
    DFT Stocker Initialized. Data covers 2007-10-19 to 2017-09-13.
    PIR Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    RLOC Stocker Initialized. Data covers 2010-05-20 to 2016-08-09.
    FUEL Stocker Initialized. Data covers 2013-09-20 to 2017-09-05.
    CTAS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    KEYW Stocker Initialized. Data covers 2010-10-01 to 2018-03-27.
    MRC Stocker Initialized. Data covers 2012-04-12 to 2018-03-27.
    ANAT Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    ADT Stocker Initialized. Data covers 2012-10-01 to 2018-03-07.
    SKX Stocker Initialized. Data covers 1999-06-09 to 2018-03-27.
    SAIA Stocker Initialized. Data covers 2002-09-12 to 2018-03-27.
    DGII Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    SNMX Stocker Initialized. Data covers 2004-06-22 to 2018-03-27.
    CPRT Stocker Initialized. Data covers 1994-03-17 to 2018-03-27.
    WMAR Stocker Initialized. Data covers 1993-11-19 to 2017-09-13.
    AKBA Stocker Initialized. Data covers 2014-03-20 to 2018-03-27.
    UCP Stocker Initialized. Data covers 2013-07-18 to 2017-08-03.
    BOFI Stocker Initialized. Data covers 2005-03-16 to 2018-03-27.
    OFLX Stocker Initialized. Data covers 2005-08-01 to 2018-03-27.
    PBPB Stocker Initialized. Data covers 2013-10-04 to 2018-03-27.
    NLNK Stocker Initialized. Data covers 2011-11-11 to 2018-03-27.
    STT Stocker Initialized. Data covers 1986-07-09 to 2018-03-27.
    ANAC Stocker Initialized. Data covers 2010-11-24 to 2016-06-24.
    BKMU Stocker Initialized. Data covers 2001-03-06 to 2018-01-31.
    CNC Stocker Initialized. Data covers 2001-12-13 to 2018-03-27.
    KSS Stocker Initialized. Data covers 1992-05-19 to 2018-03-27.
    ESV Stocker Initialized. Data covers 1991-01-02 to 2018-03-07.
    SAVE Stocker Initialized. Data covers 2011-05-26 to 2018-03-27.
    VGR Stocker Initialized. Data covers 1987-10-09 to 2018-03-27.
    CVT Stocker Initialized. Data covers 2013-08-09 to 2016-11-28.
    LAZ Stocker Initialized. Data covers 2005-05-05 to 2018-03-27.
    COST Stocker Initialized. Data covers 1986-07-09 to 2018-03-27.
    SWSH Stocker Initialized. Data covers 2007-06-20 to 2016-01-14.
    X Stocker Initialized. Data covers 1991-04-12 to 2018-03-27.
    VLY Stocker Initialized. Data covers 1990-03-23 to 2018-03-27.
    AMSWA Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    MTZ Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    NSR Stocker Initialized. Data covers 2005-06-29 to 2017-08-07.
    ENPH Stocker Initialized. Data covers 2012-03-30 to 2018-03-27.
    CWEI Stocker Initialized. Data covers 1993-05-24 to 2017-04-24.
    ERII Stocker Initialized. Data covers 2008-07-02 to 2018-03-27.
    FFG Stocker Initialized. Data covers 1996-07-19 to 2018-03-27.
    ARII Stocker Initialized. Data covers 2006-01-23 to 2018-03-27.
    ORM Stocker Initialized. Data covers 2013-07-01 to 2018-03-27.
    EGP Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    RDC Stocker Initialized. Data covers 1983-04-06 to 2018-03-07.
    CGNX Stocker Initialized. Data covers 1989-10-09 to 2018-03-27.
    NDLS Stocker Initialized. Data covers 2013-06-28 to 2018-03-27.
    BANF Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    QLIK Stocker Initialized. Data covers 2010-07-16 to 2016-08-19.
    HCSG Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ALLE Stocker Initialized. Data covers 2013-11-18 to 2018-03-27.
    MHO Stocker Initialized. Data covers 1993-11-03 to 2018-03-27.
    EBIX Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BIDU Stocker Initialized. Data covers 2005-08-05 to 2018-03-27.
    BKCC Stocker Initialized. Data covers 2007-06-27 to 2018-03-27.
    MBVT Stocker Initialized. Data covers 1993-03-25 to 2017-05-12.
    COR Stocker Initialized. Data covers 2010-09-23 to 2018-03-27.
    EVC Stocker Initialized. Data covers 2000-08-02 to 2018-03-27.
    SONC Stocker Initialized. Data covers 1991-02-28 to 2018-03-27.
    ZIGO Stocker Initialized. Data covers 1992-03-03 to 2014-06-20.
    PTGI Stocker Initialized. Data covers 2009-07-13 to 2014-04-11.
    APTV Stocker Initialized. Data covers 2017-12-08 to 2018-03-27.
    ISRG Stocker Initialized. Data covers 2000-06-16 to 2018-03-27.
    MGAM Stocker Initialized. Data covers 1995-02-01 to 2014-12-19.
    LNC Stocker Initialized. Data covers 1984-10-05 to 2018-03-27.
    NKTR Stocker Initialized. Data covers 1994-05-03 to 2018-03-27.
    HCP Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    STSA Stocker Initialized. Data covers 1991-11-25 to 2014-04-21.
    MTX Stocker Initialized. Data covers 1992-10-26 to 2018-03-27.
    TBI Stocker Initialized. Data covers 1995-02-01 to 2018-03-27.
    INWK Stocker Initialized. Data covers 2006-08-16 to 2018-03-27.
    VLGEA Stocker Initialized. Data covers 1990-03-27 to 2018-03-27.
    LUB Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    PSB Stocker Initialized. Data covers 1991-03-27 to 2018-03-27.
    BKS Stocker Initialized. Data covers 1993-09-28 to 2018-03-27.
    FSYS Stocker Initialized. Data covers 1986-09-16 to 2016-06-01.
    ZEUS Stocker Initialized. Data covers 1994-03-10 to 2018-03-27.
    MWA Stocker Initialized. Data covers 2006-05-26 to 2018-03-27.
    CTSH Stocker Initialized. Data covers 1998-06-19 to 2018-03-27.
    DSCI Stocker Initialized. Data covers 1994-05-13 to 2017-02-23.
    HCCI Stocker Initialized. Data covers 2008-03-12 to 2018-03-27.
    AP Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    DVN Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    RARE Stocker Initialized. Data covers 2014-01-31 to 2018-03-27.
    TCBK Stocker Initialized. Data covers 1993-04-20 to 2018-03-27.
    HHS Stocker Initialized. Data covers 1993-11-04 to 2018-03-27.
    S Stocker Initialized. Data covers 1984-11-08 to 2018-03-27.
    WGO Stocker Initialized. Data covers 1984-11-01 to 2018-03-27.
    FDEF Stocker Initialized. Data covers 1993-07-21 to 2018-03-27.
    SPA Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    SCSS Stocker Initialized. Data covers 1998-12-04 to 2017-10-31.
    CAS Stocker Initialized. Data covers 1980-03-17 to 2016-12-06.
    CBOE Stocker Initialized. Data covers 2010-06-15 to 2018-03-27.
    PAYX Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BDC Stocker Initialized. Data covers 1993-11-24 to 2018-03-27.
    ACAT Stocker Initialized. Data covers 1990-06-27 to 2017-03-06.
    AGYS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ALE Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    DE Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    PERY Stocker Initialized. Data covers 1993-05-28 to 2018-03-27.
    FFBC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PFLT Stocker Initialized. Data covers 2011-04-08 to 2018-03-27.
    AGN Stocker Initialized. Data covers 1989-06-22 to 2018-03-27.
    NATL Stocker Initialized. Data covers 2005-01-28 to 2016-11-10.
    ITC Stocker Initialized. Data covers 2005-07-26 to 2016-10-13.
    CRAI Stocker Initialized. Data covers 1998-04-24 to 2018-03-27.
    GB Stocker Initialized. Data covers 2000-09-29 to 2016-06-30.
    KVHI Stocker Initialized. Data covers 1996-04-02 to 2018-03-27.
    PRE Stocker Initialized. Data covers 1993-10-29 to 2016-03-17.
    TDC Stocker Initialized. Data covers 2007-10-01 to 2018-03-07.
    UFS Stocker Initialized. Data covers 2007-03-07 to 2018-03-27.
    ATEC Stocker Initialized. Data covers 2006-06-12 to 2018-03-27.
    APC Stocker Initialized. Data covers 1986-09-09 to 2018-03-27.
    SQBG Stocker Initialized. Data covers 2004-07-02 to 2018-03-27.
    WDAY Stocker Initialized. Data covers 2012-10-12 to 2018-03-27.
    GRPN Stocker Initialized. Data covers 2011-11-04 to 2018-03-27.
    MLAB Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    JDSU Stocker Initialized. Data covers 1993-11-17 to 2015-08-03.
    MN Stocker Initialized. Data covers 2011-11-18 to 2018-03-27.
    BODY Stocker Initialized. Data covers 2010-10-15 to 2015-03-11.
    ASPX Stocker Initialized. Data covers 2014-02-05 to 2015-05-04.
    GORO Stocker Initialized. Data covers 2006-09-14 to 2018-03-27.
    SRCE Stocker Initialized. Data covers 1996-09-03 to 2018-03-27.
    NI Stocker Initialized. Data covers 1984-10-19 to 2018-03-27.
    THR Stocker Initialized. Data covers 2011-05-05 to 2018-03-27.
    BGC Stocker Initialized. Data covers 1997-05-16 to 2018-03-27.
    CUI Stocker Initialized. Data covers 1999-09-15 to 2018-03-27.
    ELY Stocker Initialized. Data covers 1992-02-28 to 2018-03-27.
    SO Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    IMMR Stocker Initialized. Data covers 1999-11-12 to 2018-03-27.
    MCRS Stocker Initialized. Data covers 1990-03-26 to 2014-09-08.
    WHR Stocker Initialized. Data covers 1983-06-10 to 2018-03-27.
    ADUS Stocker Initialized. Data covers 2009-10-28 to 2018-03-27.
    ALOG Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    CXW Stocker Initialized. Data covers 1997-07-15 to 2018-03-27.
    MTSI Stocker Initialized. Data covers 2012-03-15 to 2018-03-27.
    DHX Stocker Initialized. Data covers 2007-07-26 to 2018-03-27.
    LLTC Stocker Initialized. Data covers 1990-03-26 to 2017-03-10.
    WABC Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    CPSS Stocker Initialized. Data covers 1993-02-22 to 2018-03-27.
    MIDD Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    CHDN Stocker Initialized. Data covers 1993-03-29 to 2018-03-27.
    WLL Stocker Initialized. Data covers 2003-11-20 to 2018-03-27.
    NEWS Stocker Initialized. Data covers 2006-12-14 to 2017-12-22.
    GLNG Stocker Initialized. Data covers 2003-07-15 to 2018-03-27.
    AT Stocker Initialized. Data covers 2009-12-03 to 2018-03-27.
    PRGS Stocker Initialized. Data covers 1991-08-05 to 2018-03-27.
    MOH Stocker Initialized. Data covers 2003-07-02 to 2018-03-27.
    LEG Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    OMC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    GSIT Stocker Initialized. Data covers 2007-03-29 to 2018-03-27.
    SD Stocker Initialized. Data covers 2016-10-04 to 2018-03-27.
    VVC Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    CLVS Stocker Initialized. Data covers 2011-11-16 to 2018-03-27.
    BIOS Stocker Initialized. Data covers 1996-08-15 to 2018-03-27.
    SHW Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    BFIN Stocker Initialized. Data covers 2005-06-28 to 2018-03-27.
    PETX Stocker Initialized. Data covers 2013-06-27 to 2018-03-27.
    SSTK Stocker Initialized. Data covers 2012-10-11 to 2018-03-27.
    BOKF Stocker Initialized. Data covers 1991-09-05 to 2018-03-27.
    HBIO Stocker Initialized. Data covers 2001-03-19 to 2018-03-27.
    HOV Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    WBA Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    PEIX Stocker Initialized. Data covers 2005-03-24 to 2018-03-27.
    CLDT Stocker Initialized. Data covers 2010-04-16 to 2018-03-27.
    HPY Stocker Initialized. Data covers 2005-08-16 to 2016-04-22.
    HOME Stocker Initialized. Data covers 2016-08-04 to 2018-03-27.
    GBDC Stocker Initialized. Data covers 2010-04-15 to 2018-03-27.
    NWSA Stocker Initialized. Data covers 2013-06-19 to 2018-03-27.
    RYL Stocker Initialized. Data covers 1987-12-30 to 2015-09-30.
    AVA Stocker Initialized. Data covers 1987-11-16 to 2018-03-27.
    KFY Stocker Initialized. Data covers 1999-02-11 to 2018-03-27.
    ARTC Stocker Initialized. Data covers 1996-02-05 to 2014-05-29.
    CPLA Stocker Initialized. Data covers 2006-11-10 to 2018-03-27.
    ESC Stocker Initialized. Data covers 1995-11-20 to 2014-07-30.
    RLD Stocker Initialized. Data covers 2010-07-16 to 2016-03-22.
    MRCY Stocker Initialized. Data covers 1998-01-30 to 2018-03-27.
    FRM Stocker Initialized. Data covers 1977-05-16 to 2016-02-29.
    MIG Stocker Initialized. Data covers 1995-11-21 to 2015-07-07.
    NNVC Stocker Initialized. Data covers 2005-10-26 to 2018-03-27.
    FCX Stocker Initialized. Data covers 1995-07-10 to 2018-03-27.
    DOW Stocker Initialized. Data covers 1972-06-01 to 2017-08-31.
    IVR Stocker Initialized. Data covers 2009-07-01 to 2018-03-27.
    COF Stocker Initialized. Data covers 1994-11-16 to 2018-03-27.
    CLW Stocker Initialized. Data covers 2008-12-05 to 2018-03-27.
    SCI Stocker Initialized. Data covers 1987-07-23 to 2018-03-27.
    CFNB Stocker Initialized. Data covers 1987-04-09 to 2017-11-10.
    FUBC Stocker Initialized. Data covers 2008-04-10 to 2014-10-31.
    GPC Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    SLXP Stocker Initialized. Data covers 2000-11-21 to 2015-04-01.
    EMR Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    ACE Stocker Initialized. Data covers 1993-03-26 to 2016-01-14.
    AMSC Stocker Initialized. Data covers 1991-12-12 to 2018-03-27.
    SCAI Stocker Initialized. Data covers 2013-10-30 to 2017-03-23.
    HAWK Stocker Initialized. Data covers 2013-04-19 to 2018-03-27.
    FFIC Stocker Initialized. Data covers 1995-11-21 to 2018-03-27.
    TZOO Stocker Initialized. Data covers 2002-08-28 to 2018-03-27.
    GSVC Stocker Initialized. Data covers 2011-04-28 to 2018-03-27.
    HCT Stocker Initialized. Data covers 2014-04-07 to 2015-01-16.
    TWTC Stocker Initialized. Data covers 1999-05-13 to 2014-10-31.
    GTS Stocker Initialized. Data covers 2007-12-07 to 2018-03-27.
    MNKD Stocker Initialized. Data covers 2004-07-28 to 2018-03-27.
    PCLN Stocker Initialized. Data covers 1999-03-31 to 2018-02-26.
    SUBK Stocker Initialized. Data covers 1992-03-03 to 2015-12-17.
    GMAN Stocker Initialized. Data covers 2010-08-05 to 2017-03-21.
    OI Stocker Initialized. Data covers 1991-12-11 to 2018-03-07.
    AWI Stocker Initialized. Data covers 2006-10-18 to 2018-03-27.
    IPXL Stocker Initialized. Data covers 1995-12-19 to 2018-03-27.
    NVEC Stocker Initialized. Data covers 1996-09-11 to 2018-03-27.
    HTLF Stocker Initialized. Data covers 1999-01-04 to 2018-03-27.
    APL Stocker Initialized. Data covers 2000-01-28 to 2015-02-27.
    SIRO Stocker Initialized. Data covers 2002-01-23 to 2016-02-26.
    RNG Stocker Initialized. Data covers 2013-09-27 to 2018-03-27.
    UBSH Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    FCS Stocker Initialized. Data covers 1999-08-04 to 2016-09-19.
    WMC Stocker Initialized. Data covers 2012-05-11 to 2018-03-27.
    RTK Stocker Initialized. Data covers 1999-04-05 to 2017-10-13.
    CYTK Stocker Initialized. Data covers 2004-04-30 to 2018-03-27.
    JOUT Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    MU Stocker Initialized. Data covers 1989-05-16 to 2018-03-27.
    GSAT Stocker Initialized. Data covers 2014-04-04 to 2018-03-27.
    DHIL Stocker Initialized. Data covers 1997-05-09 to 2018-03-27.
    MILL Stocker Initialized. Data covers 1998-12-30 to 2015-07-30.
    EPAY Stocker Initialized. Data covers 1999-02-12 to 2018-03-27.
    EDIG Stocker Initialized. Data covers 1993-04-06 to 2015-03-06.
    FSS Stocker Initialized. Data covers 1982-03-01 to 2018-03-27.
    AEL Stocker Initialized. Data covers 2003-12-04 to 2018-03-27.
    CPST Stocker Initialized. Data covers 2000-06-30 to 2018-03-27.
    LCUT Stocker Initialized. Data covers 1991-06-05 to 2018-03-27.
    BSTC Stocker Initialized. Data covers 1991-11-15 to 2018-03-27.
    FSC Stocker Initialized. Data covers 2008-06-12 to 2017-10-17.
    FUR Stocker Initialized. Data covers 1973-05-03 to 2016-08-01.
    MOSY Stocker Initialized. Data covers 2001-07-17 to 2018-03-27.
    TOWR Stocker Initialized. Data covers 2010-10-15 to 2018-03-27.
    GD Stocker Initialized. Data covers 1977-01-03 to 2018-03-27.
    TMO Stocker Initialized. Data covers 1987-09-01 to 2018-03-27.
    NWBO Stocker Initialized. Data covers 2001-12-14 to 2016-12-16.
    WCG Stocker Initialized. Data covers 2004-07-01 to 2018-03-27.
    AMD Stocker Initialized. Data covers 1983-03-21 to 2018-03-27.
    AGX Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    LII Stocker Initialized. Data covers 1999-07-29 to 2018-03-27.
    DTSI Stocker Initialized. Data covers 2003-07-11 to 2016-12-01.
    RTEC Stocker Initialized. Data covers 1999-11-12 to 2018-03-27.
    BNCL Stocker Initialized. Data covers 2007-07-16 to 2018-03-27.
    HCN Stocker Initialized. Data covers 1992-03-17 to 2018-02-27.
    PRAA Stocker Initialized. Data covers 2002-11-08 to 2018-03-27.
    QDEL Stocker Initialized. Data covers 1992-03-03 to 2018-03-27.
    UNFI Stocker Initialized. Data covers 1996-11-01 to 2018-03-27.
    MYL Stocker Initialized. Data covers 1987-12-18 to 2018-03-27.
    CRR Stocker Initialized. Data covers 1996-04-23 to 2018-03-27.
    ABBV Stocker Initialized. Data covers 2013-01-02 to 2018-03-27.
    EIX Stocker Initialized. Data covers 1980-01-02 to 2018-03-27.
    PNFP Stocker Initialized. Data covers 2000-08-22 to 2018-03-27.
    DFS Stocker Initialized. Data covers 2007-06-14 to 2018-03-27.
    ALXN Stocker Initialized. Data covers 1996-02-28 to 2018-03-27.
    XOM Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    AXLL Stocker Initialized. Data covers 1988-10-05 to 2016-08-30.
    TYPE Stocker Initialized. Data covers 2007-07-25 to 2018-03-27.
    CRAY Stocker Initialized. Data covers 1995-09-27 to 2018-03-27.
    TAST Stocker Initialized. Data covers 2006-12-15 to 2018-03-27.
    OLBK Stocker Initialized. Data covers 2003-09-17 to 2018-03-27.
    BOBE Stocker Initialized. Data covers 1984-09-05 to 2018-01-11.
    LHO Stocker Initialized. Data covers 1998-04-24 to 2018-03-27.
    PBCT Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    GERN Stocker Initialized. Data covers 1996-07-31 to 2018-03-27.
    INTX Stocker Initialized. Data covers 2004-04-30 to 2018-03-27.
    JBLU Stocker Initialized. Data covers 2002-04-12 to 2018-03-27.
    OPHT Stocker Initialized. Data covers 2013-09-25 to 2018-03-27.
    CTRL Stocker Initialized. Data covers 2013-08-02 to 2018-03-27.
    TCBI Stocker Initialized. Data covers 2003-08-14 to 2018-03-27.
    SAMG Stocker Initialized. Data covers 2013-06-27 to 2018-03-27.
    BMR Stocker Initialized. Data covers 2004-08-09 to 2016-01-27.
    KTWO Stocker Initialized. Data covers 2014-05-08 to 2018-03-27.
    ROL Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    TYC Stocker Initialized. Data covers 1987-09-28 to 2016-09-02.
    VSAT Stocker Initialized. Data covers 1996-12-03 to 2018-03-27.
    COHU Stocker Initialized. Data covers 1986-11-12 to 2018-03-27.
    IBM Stocker Initialized. Data covers 1962-01-02 to 2018-03-27.
    MIND Stocker Initialized. Data covers 1994-12-28 to 2018-03-27.
    STAA Stocker Initialized. Data covers 1992-03-02 to 2018-03-27.
    DUK Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    TITN Stocker Initialized. Data covers 2007-12-13 to 2018-03-27.
    NTGR Stocker Initialized. Data covers 2003-07-31 to 2018-03-27.
    VOD Stocker Initialized. Data covers 1988-12-16 to 2018-03-27.
    KWR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PLOW Stocker Initialized. Data covers 2010-05-05 to 2018-03-27.
    NEWM Stocker Initialized. Data covers 2014-02-04 to 2018-03-27.
    ACAS Stocker Initialized. Data covers 1997-09-02 to 2017-01-03.
    STX Stocker Initialized. Data covers 2002-12-11 to 2018-03-27.
    ALGT Stocker Initialized. Data covers 2006-12-08 to 2018-03-27.
    ZINC Stocker Initialized. Data covers 2007-08-10 to 2016-02-10.
    WAIR Stocker Initialized. Data covers 2011-07-28 to 2018-03-27.
    AWH Stocker Initialized. Data covers 2006-07-12 to 2017-07-27.
    VOLC Stocker Initialized. Data covers 2006-06-15 to 2015-02-17.
    CIM Stocker Initialized. Data covers 2007-11-29 to 2018-03-27.
    HCC Stocker Initialized. Data covers 1992-10-28 to 2018-03-27.
    IBP Stocker Initialized. Data covers 2014-02-13 to 2018-03-27.
    IPG Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    NVAX Stocker Initialized. Data covers 1995-12-13 to 2018-03-27.
    SIGI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CALL Stocker Initialized. Data covers 1996-02-07 to 2018-03-27.
    OFC Stocker Initialized. Data covers 1991-12-31 to 2018-03-27.
    WTS Stocker Initialized. Data covers 1986-01-02 to 2018-03-27.
    XOMA Stocker Initialized. Data covers 1989-04-05 to 2018-03-27.
    MLI Stocker Initialized. Data covers 1991-02-25 to 2018-03-27.
    SLAB Stocker Initialized. Data covers 2000-03-24 to 2018-03-27.
    WTM Stocker Initialized. Data covers 1986-05-09 to 2018-03-27.
    JNJ Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    TMH Stocker Initialized. Data covers 2009-12-16 to 2017-02-03.
    FC Stocker Initialized. Data covers 1992-06-03 to 2018-03-27.
    IT Stocker Initialized. Data covers 1993-10-05 to 2018-03-27.
    EXEL Stocker Initialized. Data covers 2000-04-17 to 2018-03-27.
    NE Stocker Initialized. Data covers 1990-03-26 to 2018-03-07.
    OMEX Stocker Initialized. Data covers 1999-10-26 to 2018-03-27.
    RWT Stocker Initialized. Data covers 1995-08-04 to 2018-03-27.
    GBX Stocker Initialized. Data covers 1994-07-14 to 2018-03-27.
    MGI Stocker Initialized. Data covers 2004-08-12 to 2018-03-27.
    PTX Stocker Initialized. Data covers 1997-02-07 to 2018-03-27.
    SWX Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    LFVN Stocker Initialized. Data covers 2004-10-05 to 2018-03-27.
    NRZ Stocker Initialized. Data covers 2013-05-02 to 2018-03-27.
    UACL Stocker Initialized. Data covers 2005-02-11 to 2016-04-29.
    WASH Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    PNNT Stocker Initialized. Data covers 2007-04-19 to 2018-03-27.
    BIOL Stocker Initialized. Data covers 1992-11-12 to 2018-03-27.
    LFUS Stocker Initialized. Data covers 1992-09-23 to 2018-03-27.
    GUID Stocker Initialized. Data covers 2006-12-13 to 2017-09-13.
    FELE Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BLK Stocker Initialized. Data covers 1999-10-01 to 2018-03-27.
    KAI Stocker Initialized. Data covers 1992-11-03 to 2018-03-27.
    AIN Stocker Initialized. Data covers 1987-09-30 to 2018-03-27.
    SXT Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    RXN Stocker Initialized. Data covers 2012-03-29 to 2018-03-27.
    MSG Stocker Initialized. Data covers 2010-01-25 to 2018-03-27.
    OCLR Stocker Initialized. Data covers 2000-04-11 to 2018-03-27.
    VAC Stocker Initialized. Data covers 2011-11-08 to 2018-03-27.
    EGHT Stocker Initialized. Data covers 1997-07-02 to 2018-03-27.
    SPTN Stocker Initialized. Data covers 2000-08-02 to 2018-03-27.
    NXST Stocker Initialized. Data covers 2003-11-25 to 2018-03-27.
    NEWP Stocker Initialized. Data covers 1990-03-26 to 2016-04-29.
    HEES Stocker Initialized. Data covers 2006-01-31 to 2018-03-27.
    VNO Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    APAGF Stocker Initialized. Data covers 1981-07-21 to 2015-01-28.
    AXE Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    GTT Stocker Initialized. Data covers 2006-11-29 to 2018-03-27.
    HOLX Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PLCE Stocker Initialized. Data covers 1997-09-19 to 2018-03-27.
    SONS Stocker Initialized. Data covers 2000-05-25 to 2017-11-28.
    FTV Stocker Initialized. Data covers 2016-07-05 to 2018-03-27.
    GPOR Stocker Initialized. Data covers 1999-03-03 to 2018-03-27.
    SJI Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    DPZ Stocker Initialized. Data covers 2004-07-13 to 2018-03-27.
    AFOP Stocker Initialized. Data covers 2000-11-30 to 2016-06-06.
    BCC Stocker Initialized. Data covers 2013-02-06 to 2018-03-27.
    HP Stocker Initialized. Data covers 1980-10-15 to 2018-03-27.
    SALE Stocker Initialized. Data covers 2013-07-19 to 2017-05-22.
    CFX Stocker Initialized. Data covers 2008-05-08 to 2018-03-27.
    JBT Stocker Initialized. Data covers 2008-07-22 to 2018-03-27.
    BV Stocker Initialized. Data covers 2012-02-24 to 2018-01-31.
    LANC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FRME Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    MCHP Stocker Initialized. Data covers 1993-03-19 to 2018-03-27.
    NCMI Stocker Initialized. Data covers 2007-02-08 to 2018-03-27.
    DGX Stocker Initialized. Data covers 1996-12-26 to 2018-03-27.
    SAAS Stocker Initialized. Data covers 2003-07-15 to 2016-11-11.
    PVH Stocker Initialized. Data covers 1987-07-10 to 2018-03-27.
    KTOS Stocker Initialized. Data covers 1999-11-05 to 2018-03-27.
    DLX Stocker Initialized. Data covers 1987-07-23 to 2018-03-27.
    AMG Stocker Initialized. Data covers 1997-11-21 to 2018-03-27.
    FHN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    GIMO Stocker Initialized. Data covers 2013-06-12 to 2017-12-26.
    COHR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AAN Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    KEM Stocker Initialized. Data covers 1992-10-26 to 2018-03-27.
    WWW Stocker Initialized. Data covers 1984-12-18 to 2018-03-27.
    OII Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    MD Stocker Initialized. Data covers 1995-09-20 to 2018-03-27.
    JOY Stocker Initialized. Data covers 2001-05-25 to 2017-04-05.
    RE Stocker Initialized. Data covers 1995-10-03 to 2018-03-27.
    WWAV Stocker Initialized. Data covers 2012-10-26 to 2017-04-11.
    VSAR Stocker Initialized. Data covers 2014-03-21 to 2018-03-27.
    HGG Stocker Initialized. Data covers 2007-07-20 to 2017-02-27.
    IFF Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    ONE Stocker Initialized. Data covers 2010-06-17 to 2016-08-04.
    OXFD Stocker Initialized. Data covers 2013-11-22 to 2018-03-27.
    IMN Stocker Initialized. Data covers 1996-06-26 to 2017-02-21.
    LSI Stocker Initialized. Data covers 1995-06-21 to 2018-03-07.
    WFC Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    SPNC Stocker Initialized. Data covers 1992-01-21 to 2017-08-09.
    CALX Stocker Initialized. Data covers 2010-03-24 to 2018-03-27.
    HMPR Stocker Initialized. Data covers 2003-10-15 to 2016-07-29.
    BPOP Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    POST Stocker Initialized. Data covers 2012-01-27 to 2018-03-27.
    TREE Stocker Initialized. Data covers 2008-08-12 to 2018-03-27.
    MBRG Stocker Initialized. Data covers 2001-01-03 to 2017-03-31.
    OHI Stocker Initialized. Data covers 1992-08-07 to 2018-03-27.
    BLL Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    TDG Stocker Initialized. Data covers 2006-03-15 to 2018-03-27.
    BHF Stocker Initialized. Data covers 2017-08-08 to 2018-03-27.
    SIRI Stocker Initialized. Data covers 1994-09-13 to 2018-03-27.
    WSM Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BYI Stocker Initialized. Data covers 1982-01-12 to 2014-11-21.
    UNTD Stocker Initialized. Data covers 1999-09-24 to 2016-06-30.
    MKTX Stocker Initialized. Data covers 2004-11-05 to 2018-03-27.
    BAH Stocker Initialized. Data covers 2010-11-18 to 2018-03-27.
    ALK Stocker Initialized. Data covers 1983-01-03 to 2018-03-27.
    CONN Stocker Initialized. Data covers 2003-11-25 to 2018-03-27.
    OTTR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    MED Stocker Initialized. Data covers 1993-12-31 to 2018-03-27.
    WTSL Stocker Initialized. Data covers 1992-03-03 to 2015-01-26.
    HNI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ARWR Stocker Initialized. Data covers 1997-01-06 to 2018-03-27.
    MCY Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FANG Stocker Initialized. Data covers 2012-10-12 to 2018-03-27.
    PGI Stocker Initialized. Data covers 1996-03-05 to 2015-12-08.
    FLXS Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    FSGI Stocker Initialized. Data covers 2005-08-10 to 2015-10-30.
    POWL Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AFG Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    MSFT Stocker Initialized. Data covers 1986-03-13 to 2018-03-27.
    TGNA Stocker Initialized. Data covers 1985-07-01 to 2018-03-07.
    PQ Stocker Initialized. Data covers 1992-10-26 to 2018-03-27.
    USB Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    GLW Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    URI Stocker Initialized. Data covers 1997-12-18 to 2018-03-27.
    KORS Stocker Initialized. Data covers 2011-12-15 to 2018-03-27.
    CRMT Stocker Initialized. Data covers 1993-11-09 to 2018-03-27.
    BNCN Stocker Initialized. Data covers 2003-07-15 to 2017-06-15.
    DVR Stocker Initialized. Data covers 2006-12-14 to 2014-10-29.
    LTS Stocker Initialized. Data covers 1999-08-25 to 2018-03-27.
    NCLH Stocker Initialized. Data covers 2013-01-18 to 2018-03-27.
    C Stocker Initialized. Data covers 1977-01-03 to 2018-03-27.
    GMT Stocker Initialized. Data covers 1987-11-05 to 2016-06-30.
    MSI Stocker Initialized. Data covers 1977-01-03 to 2018-03-27.
    DLLR Stocker Initialized. Data covers 2005-01-28 to 2014-06-13.
    SNCR Stocker Initialized. Data covers 2006-06-15 to 2018-03-27.
    CAM Stocker Initialized. Data covers 1995-07-05 to 2016-04-01.
    CSE Stocker Initialized. Data covers 2003-08-07 to 2014-04-07.
    HPP Stocker Initialized. Data covers 2010-06-24 to 2018-03-27.
    TRGT Stocker Initialized. Data covers 2006-04-12 to 2015-08-20.
    IILG Stocker Initialized. Data covers 2008-08-12 to 2016-10-14.
    BPI Stocker Initialized. Data covers 2009-04-15 to 2018-03-27.
    IDRA Stocker Initialized. Data covers 1996-01-25 to 2018-03-27.
    NMFC Stocker Initialized. Data covers 2011-05-20 to 2018-03-27.
    CRM Stocker Initialized. Data covers 2004-06-23 to 2018-03-27.
    CBI Stocker Initialized. Data covers 1997-03-27 to 2018-03-27.
    MAS Stocker Initialized. Data covers 1983-06-10 to 2018-03-27.
    FIO Stocker Initialized. Data covers 2011-06-09 to 2014-07-23.
    FPO Stocker Initialized. Data covers 2003-10-23 to 2017-09-29.
    BRKR Stocker Initialized. Data covers 2000-08-04 to 2018-03-27.
    CHSP Stocker Initialized. Data covers 2010-01-26 to 2018-03-27.
    CUTR Stocker Initialized. Data covers 2004-03-31 to 2018-03-27.
    WPP Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ADBE Stocker Initialized. Data covers 1986-08-14 to 2018-03-27.
    NNA Stocker Initialized. Data covers 2008-07-07 to 2018-03-27.
    HAR Stocker Initialized. Data covers 1986-11-14 to 2017-03-10.
    BRDR Stocker Initialized. Data covers 2014-03-21 to 2015-06-09.
    IQV Stocker Initialized. Data covers 2017-11-15 to 2018-03-27.
    MATX Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    ICUI Stocker Initialized. Data covers 1992-03-31 to 2018-03-27.
    CGI Stocker Initialized. Data covers 1994-01-21 to 2018-03-27.
    PEG Stocker Initialized. Data covers 1980-01-02 to 2018-03-27.
    HE Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    RATE Stocker Initialized. Data covers 2011-06-17 to 2017-11-07.
    UTMD Stocker Initialized. Data covers 1999-03-08 to 2018-03-27.
    CCF Stocker Initialized. Data covers 1995-10-25 to 2018-03-27.
    OSIR Stocker Initialized. Data covers 2006-08-09 to 2017-03-13.
    ACCO Stocker Initialized. Data covers 2005-08-17 to 2018-03-27.
    CCRN Stocker Initialized. Data covers 2001-10-25 to 2018-03-27.
    AGEN Stocker Initialized. Data covers 2000-02-08 to 2018-03-27.
    CAT Stocker Initialized. Data covers 1962-01-02 to 2018-03-27.
    CBB Stocker Initialized. Data covers 1987-05-21 to 2018-03-27.
    ESRT Stocker Initialized. Data covers 2013-10-02 to 2018-03-27.
    NLS Stocker Initialized. Data covers 1999-05-05 to 2018-03-27.
    CNVR Stocker Initialized. Data covers 2000-03-31 to 2014-12-10.
    LUK Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    ATNM Stocker Initialized. Data covers 2012-12-27 to 2018-03-27.
    CCO Stocker Initialized. Data covers 2005-11-14 to 2018-03-27.
    AVB Stocker Initialized. Data covers 1994-03-11 to 2018-03-27.
    Q Stocker Initialized. Data covers 2013-05-09 to 2017-11-14.
    RST Stocker Initialized. Data covers 2009-04-16 to 2018-03-27.
    PDFS Stocker Initialized. Data covers 2001-07-31 to 2018-03-27.
    CSL Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    TECH Stocker Initialized. Data covers 1992-12-09 to 2018-03-27.
    MWW Stocker Initialized. Data covers 1996-12-13 to 2016-10-31.
    TWOU Stocker Initialized. Data covers 2014-03-28 to 2018-03-27.
    BRS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AWAY Stocker Initialized. Data covers 2011-06-29 to 2015-12-14.
    PAHC Stocker Initialized. Data covers 2014-04-11 to 2018-03-27.
    VTL Stocker Initialized. Data covers 2014-04-17 to 2018-03-27.
    SPF Stocker Initialized. Data covers 1987-12-30 to 2015-09-30.
    NYT Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    QEP Stocker Initialized. Data covers 2010-06-16 to 2018-03-07.
    GME Stocker Initialized. Data covers 2002-02-13 to 2018-03-27.
    PICO Stocker Initialized. Data covers 1991-03-21 to 2018-03-27.
    CVS Stocker Initialized. Data covers 1984-12-17 to 2018-03-27.
    PCYO Stocker Initialized. Data covers 1997-01-02 to 2018-03-27.
    RH Stocker Initialized. Data covers 2012-11-02 to 2018-03-27.
    LBY Stocker Initialized. Data covers 1993-06-18 to 2018-03-27.
    HDNG Stocker Initialized. Data covers 1995-05-25 to 2018-03-27.
    VMEM Stocker Initialized. Data covers 2013-09-27 to 2016-10-27.
    FSP Stocker Initialized. Data covers 2005-06-02 to 2018-03-27.
    CCI Stocker Initialized. Data covers 1998-08-18 to 2018-03-27.
    AKAO Stocker Initialized. Data covers 2014-03-12 to 2018-03-27.
    HBHC Stocker Initialized. Data covers 1991-06-04 to 2018-03-27.
    BMRN Stocker Initialized. Data covers 1999-07-26 to 2018-03-27.
    BCO Stocker Initialized. Data covers 1996-01-03 to 2018-03-27.
    LLY Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    ESI Stocker Initialized. Data covers 1994-12-20 to 2016-09-06.
    PDCE Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    LEAF Stocker Initialized. Data covers 2013-10-16 to 2015-11-25.
    KHC Stocker Initialized. Data covers 2015-07-06 to 2018-03-27.
    TNAV Stocker Initialized. Data covers 2010-05-13 to 2018-03-27.
    NRG Stocker Initialized. Data covers 2003-12-02 to 2018-03-27.
    ZUMZ Stocker Initialized. Data covers 2005-05-06 to 2018-03-27.
    CBM Stocker Initialized. Data covers 1987-09-23 to 2018-03-27.
    HUB_B Stocker Initialized. Data covers 1981-02-11 to 2015-12-23.
    CPSI Stocker Initialized. Data covers 2002-05-21 to 2018-03-27.
    NLY Stocker Initialized. Data covers 1997-10-08 to 2018-03-27.
    PGNX Stocker Initialized. Data covers 1997-11-19 to 2018-03-27.
    PFIS Stocker Initialized. Data covers 2002-06-05 to 2018-03-27.
    SPW Stocker Initialized. Data covers 1985-07-01 to 2015-09-25.
    SWHC Stocker Initialized. Data covers 1999-08-17 to 2016-12-30.
    PFMT Stocker Initialized. Data covers 2012-08-10 to 2018-03-27.
    XLRN Stocker Initialized. Data covers 2013-09-19 to 2018-03-27.
    TFSL Stocker Initialized. Data covers 2007-04-23 to 2018-03-27.
    BWINB Stocker Initialized. Data covers 1986-05-14 to 2018-03-27.
    HSNI Stocker Initialized. Data covers 2008-08-12 to 2017-12-29.
    JBL Stocker Initialized. Data covers 1993-05-03 to 2018-03-27.
    MRK Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    CWH Stocker Initialized. Data covers 2016-10-07 to 2018-03-27.
    JIVE Stocker Initialized. Data covers 2011-12-13 to 2017-06-09.
    ROIC Stocker Initialized. Data covers 2009-11-03 to 2018-03-27.
    KMX Stocker Initialized. Data covers 1997-02-04 to 2018-03-27.
    ODC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ABC Stocker Initialized. Data covers 1995-04-04 to 2018-03-27.
    RAD Stocker Initialized. Data covers 1984-12-17 to 2018-03-27.
    FLIR Stocker Initialized. Data covers 1993-06-22 to 2018-03-27.
    ACHN Stocker Initialized. Data covers 2006-11-09 to 2018-03-27.
    EXPR Stocker Initialized. Data covers 2010-05-13 to 2018-03-27.
    AOL Stocker Initialized. Data covers 2009-11-24 to 2015-06-22.
    CCC Stocker Initialized. Data covers 1987-06-03 to 2018-03-08.
    JACK Stocker Initialized. Data covers 1992-03-05 to 2018-03-27.
    GHM Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    AMZG Stocker Initialized. Data covers 2006-06-15 to 2015-05-11.
    UNS Stocker Initialized. Data covers 1985-08-30 to 2014-08-15.
    NCR Stocker Initialized. Data covers 1996-12-11 to 2018-03-27.
    RVBD Stocker Initialized. Data covers 2006-09-21 to 2015-04-24.
    NEU Stocker Initialized. Data covers 1985-08-06 to 2018-03-27.
    BTU Stocker Initialized. Data covers 2001-05-22 to 2018-03-27.
    RIGL Stocker Initialized. Data covers 2000-11-29 to 2018-03-27.
    PLT Stocker Initialized. Data covers 1994-01-20 to 2018-03-27.
    RDI Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    MFRM Stocker Initialized. Data covers 2011-11-18 to 2016-09-16.
    NATR Stocker Initialized. Data covers 2009-06-25 to 2018-03-27.
    GABC Stocker Initialized. Data covers 1993-05-21 to 2018-03-27.
    MKSI Stocker Initialized. Data covers 1999-03-30 to 2018-03-27.
    BGCP Stocker Initialized. Data covers 1999-12-10 to 2018-03-27.
    LADR Stocker Initialized. Data covers 2014-02-06 to 2018-03-27.
    SYK Stocker Initialized. Data covers 1988-02-01 to 2018-03-27.
    FINL Stocker Initialized. Data covers 1992-06-09 to 2018-03-27.
    VCRA Stocker Initialized. Data covers 2012-03-28 to 2018-03-27.
    NSC Stocker Initialized. Data covers 1982-06-02 to 2018-03-27.
    SWN Stocker Initialized. Data covers 1987-12-30 to 2018-03-07.
    WTR Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    WTBA Stocker Initialized. Data covers 1999-05-03 to 2018-03-27.
    FOR Stocker Initialized. Data covers 2007-12-13 to 2018-03-27.
    CAMP Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    STFC Stocker Initialized. Data covers 1991-06-28 to 2018-03-27.
    CSBK Stocker Initialized. Data covers 2004-05-11 to 2018-03-27.
    RCII Stocker Initialized. Data covers 1995-01-25 to 2018-03-27.
    ACGL Stocker Initialized. Data covers 1995-09-14 to 2018-03-27.
    EPZM Stocker Initialized. Data covers 2013-05-31 to 2018-03-27.
    USCR Stocker Initialized. Data covers 2010-10-15 to 2018-03-27.
    BTH Stocker Initialized. Data covers 1994-05-18 to 2015-10-14.
    FIZZ Stocker Initialized. Data covers 1991-09-16 to 2018-03-27.
    ARE Stocker Initialized. Data covers 1997-05-28 to 2018-03-27.
    CNBKA Stocker Initialized. Data covers 1990-03-27 to 2018-03-27.
    EWBC Stocker Initialized. Data covers 1999-02-03 to 2018-03-27.
    KYTH Stocker Initialized. Data covers 2012-10-16 to 2015-10-01.
    BMRC Stocker Initialized. Data covers 1999-12-23 to 2018-03-27.
    DX Stocker Initialized. Data covers 1989-06-30 to 2018-03-27.
    CPB Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    STNG Stocker Initialized. Data covers 2010-03-31 to 2018-03-27.
    CTRE Stocker Initialized. Data covers 2014-05-29 to 2018-03-27.
    ITT Stocker Initialized. Data covers 1995-12-18 to 2018-03-27.
    SKYW Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PPHM Stocker Initialized. Data covers 1996-04-01 to 2018-01-05.
    UCTT Stocker Initialized. Data covers 2004-03-25 to 2018-03-27.
    ADSK Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    CCBG Stocker Initialized. Data covers 1997-02-03 to 2018-03-27.
    JW_A Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TWI Stocker Initialized. Data covers 1993-05-20 to 2018-03-27.
    IIVI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    RMBS Stocker Initialized. Data covers 1997-05-14 to 2018-03-27.
    BF_B Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    SBH Stocker Initialized. Data covers 2006-11-17 to 2018-03-27.
    T Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    MNK Stocker Initialized. Data covers 2013-06-17 to 2018-03-27.
    COG Stocker Initialized. Data covers 1990-02-08 to 2018-03-27.
    VRA Stocker Initialized. Data covers 2010-10-21 to 2018-03-27.
    AON Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    AMP Stocker Initialized. Data covers 2005-09-15 to 2018-03-27.
    VR Stocker Initialized. Data covers 2007-08-01 to 2018-03-27.
    PSTB Stocker Initialized. Data covers 2007-02-13 to 2017-11-30.
    GNMK Stocker Initialized. Data covers 2010-05-28 to 2018-03-27.
    TILE Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    B Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    BPTH Stocker Initialized. Data covers 2008-03-04 to 2018-03-27.
    GNTX Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    WBS Stocker Initialized. Data covers 1986-12-12 to 2018-03-27.
    MSL Stocker Initialized. Data covers 1993-04-26 to 2018-03-27.
    GOV Stocker Initialized. Data covers 2009-06-04 to 2018-03-27.
    MCS Stocker Initialized. Data covers 1990-03-29 to 2018-03-27.
    MUSA Stocker Initialized. Data covers 2013-08-19 to 2018-03-27.
    SPSC Stocker Initialized. Data covers 2010-04-22 to 2018-03-27.
    WIBC Stocker Initialized. Data covers 1998-11-20 to 2016-07-29.
    MCRI Stocker Initialized. Data covers 1993-08-10 to 2018-03-27.
    AAOI Stocker Initialized. Data covers 2013-09-26 to 2018-03-27.
    ITRI Stocker Initialized. Data covers 1993-11-05 to 2018-03-27.
    CTCT Stocker Initialized. Data covers 2007-10-12 to 2016-02-09.
    ENSG Stocker Initialized. Data covers 2007-11-09 to 2018-03-27.
    TCB Stocker Initialized. Data covers 1989-06-30 to 2017-05-05.
    LIOX Stocker Initialized. Data covers 1999-08-20 to 2017-02-28.
    TW Stocker Initialized. Data covers 2000-10-11 to 2016-01-04.
    FRX Stocker Initialized. Data covers 1988-04-19 to 2014-06-30.
    SUPN Stocker Initialized. Data covers 2012-05-01 to 2018-03-27.
    XNCR Stocker Initialized. Data covers 2013-12-03 to 2018-03-27.
    PEB Stocker Initialized. Data covers 2009-12-09 to 2018-03-27.
    LOV Stocker Initialized. Data covers 2006-02-14 to 2018-03-27.
    ENTG Stocker Initialized. Data covers 2000-07-11 to 2018-03-27.
    PKY Stocker Initialized. Data covers 1973-05-03 to 2017-10-11.
    NBTB Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    CLH Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    SEB Stocker Initialized. Data covers 1980-03-17 to 2018-03-27.
    BWLD Stocker Initialized. Data covers 2003-11-24 to 2018-02-05.
    GFIG Stocker Initialized. Data covers 2005-02-01 to 2015-04-09.
    SFY Stocker Initialized. Data covers 1981-07-24 to 2015-12-18.
    JNS Stocker Initialized. Data covers 2000-06-26 to 2017-05-26.
    WEX Stocker Initialized. Data covers 2005-02-16 to 2018-03-27.
    CVLT Stocker Initialized. Data covers 2006-09-22 to 2018-03-27.
    EVRY Stocker Initialized. Data covers 2012-05-16 to 2015-04-16.
    CHFC Stocker Initialized. Data covers 1992-03-11 to 2018-03-27.
    SCM Stocker Initialized. Data covers 2012-11-08 to 2018-03-27.
    SE Stocker Initialized. Data covers 2007-01-03 to 2018-03-07.
    DXLG Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    LXFT Stocker Initialized. Data covers 2013-06-26 to 2018-03-27.
    SMRT Stocker Initialized. Data covers 1992-04-27 to 2018-03-27.
    RLJ Stocker Initialized. Data covers 2011-05-11 to 2018-03-27.
    ENTR Stocker Initialized. Data covers 2007-12-07 to 2018-03-27.
    CSCO Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FTR Stocker Initialized. Data covers 1990-03-26 to 2018-03-07.
    LRCX Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    REXI Stocker Initialized. Data covers 1990-03-27 to 2016-09-08.
    INO Stocker Initialized. Data covers 1998-12-08 to 2018-03-27.
    GDOT Stocker Initialized. Data covers 2010-07-22 to 2018-03-27.
    MPAA Stocker Initialized. Data covers 1994-03-23 to 2018-03-27.
    KS Stocker Initialized. Data covers 2007-03-01 to 2018-03-27.
    RPTP Stocker Initialized. Data covers 1999-02-16 to 2016-10-24.
    WGL Stocker Initialized. Data covers 1987-06-22 to 2018-03-27.
    GIII Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    IRC Stocker Initialized. Data covers 2004-05-05 to 2016-03-30.
    RCPT Stocker Initialized. Data covers 2013-05-09 to 2015-08-27.
    TRIP Stocker Initialized. Data covers 2011-12-07 to 2018-03-27.
    COKE Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    EVER Stocker Initialized. Data covers 2012-05-03 to 2017-06-08.
    DRI Stocker Initialized. Data covers 1995-05-09 to 2018-03-27.
    STBA Stocker Initialized. Data covers 1992-04-21 to 2018-03-27.
    USG Stocker Initialized. Data covers 1988-07-07 to 2018-03-27.
    AMRC Stocker Initialized. Data covers 2010-07-22 to 2018-03-27.
    EXL Stocker Initialized. Data covers 2010-04-23 to 2015-07-31.
    SBSI Stocker Initialized. Data covers 1998-05-13 to 2018-03-27.
    ANIK Stocker Initialized. Data covers 1993-05-04 to 2018-03-27.
    CMC Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    EW Stocker Initialized. Data covers 2000-03-27 to 2018-03-27.
    TXT Stocker Initialized. Data covers 1984-10-24 to 2018-03-27.
    RF Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ELNK Stocker Initialized. Data covers 1997-01-22 to 2017-02-24.
    GCAP Stocker Initialized. Data covers 2010-12-15 to 2018-03-27.
    DLB Stocker Initialized. Data covers 2005-02-17 to 2018-03-27.
    AVX Stocker Initialized. Data covers 1995-08-15 to 2018-03-27.
    SPG Stocker Initialized. Data covers 1993-12-14 to 2018-03-27.
    BEAV Stocker Initialized. Data covers 1990-04-25 to 2017-04-12.
    BEE Stocker Initialized. Data covers 2004-07-26 to 2015-12-11.
    UFPI Stocker Initialized. Data covers 1993-11-10 to 2018-03-27.
    DHT Stocker Initialized. Data covers 2005-10-13 to 2018-03-27.
    NGPC Stocker Initialized. Data covers 2004-11-10 to 2014-10-01.
    ACN Stocker Initialized. Data covers 2001-07-19 to 2018-03-27.
    CVI Stocker Initialized. Data covers 2007-10-23 to 2018-03-27.
    SEAC Stocker Initialized. Data covers 1996-11-06 to 2018-03-27.
    CNK Stocker Initialized. Data covers 2007-04-24 to 2018-03-27.
    CTL Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    OPEN Stocker Initialized. Data covers 2009-05-22 to 2014-07-24.
    RM Stocker Initialized. Data covers 2012-03-28 to 2018-03-27.
    CATM Stocker Initialized. Data covers 2007-12-13 to 2018-03-27.
    BEN Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    TRV Stocker Initialized. Data covers 2017-04-26 to 2018-03-27.
    CTB Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    GRIF Stocker Initialized. Data covers 1997-06-18 to 2018-03-27.
    HTWR Stocker Initialized. Data covers 2008-06-24 to 2016-08-23.
    MTGE Stocker Initialized. Data covers 2011-08-04 to 2018-03-27.
    COH Stocker Initialized. Data covers 2000-10-06 to 2017-10-30.
    AEGR Stocker Initialized. Data covers 2010-10-22 to 2016-11-29.
    RPT Stocker Initialized. Data covers 1988-12-28 to 2018-03-27.
    CFFN Stocker Initialized. Data covers 1999-04-01 to 2018-03-27.
    AERI Stocker Initialized. Data covers 2013-10-25 to 2018-03-27.
    CCXI Stocker Initialized. Data covers 2012-02-08 to 2018-03-27.
    LM Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    MHR Stocker Initialized. Data covers 2003-10-07 to 2015-11-10.
    LMNR Stocker Initialized. Data covers 2003-10-07 to 2018-03-27.
    PLUG Stocker Initialized. Data covers 1999-10-29 to 2018-03-27.
    APP Stocker Initialized. Data covers 2006-03-07 to 2015-10-05.
    BUSE Stocker Initialized. Data covers 1998-10-06 to 2018-03-27.
    SYNT Stocker Initialized. Data covers 1997-08-12 to 2018-03-27.
    INDB Stocker Initialized. Data covers 1990-03-27 to 2018-03-27.
    CQB Stocker Initialized. Data covers 1986-08-01 to 2015-01-06.
    CA Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    SLB Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    MDP Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    BBNK Stocker Initialized. Data covers 2003-01-27 to 2015-06-30.
    EV Stocker Initialized. Data covers 1990-03-27 to 2018-03-27.
    AVP Stocker Initialized. Data covers 1972-06-01 to 2018-03-07.
    O Stocker Initialized. Data covers 1994-10-18 to 2018-03-27.
    RAX Stocker Initialized. Data covers 2008-08-08 to 2016-11-02.
    FITB Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    NES Stocker Initialized. Data covers 2007-11-20 to 2018-03-27.
    SRCL Stocker Initialized. Data covers 1996-08-23 to 2018-03-27.
    VAL Stocker Initialized. Data covers 1992-03-17 to 2017-05-31.
    CWCO Stocker Initialized. Data covers 1995-06-01 to 2018-03-27.
    ODFL Stocker Initialized. Data covers 1991-10-24 to 2018-03-27.
    RMAX Stocker Initialized. Data covers 2013-10-02 to 2018-03-27.
    CALD Stocker Initialized. Data covers 2003-11-20 to 2018-03-27.
    NC Stocker Initialized. Data covers 1977-06-17 to 2018-03-27.
    SP Stocker Initialized. Data covers 2004-06-02 to 2018-03-27.
    PCTI Stocker Initialized. Data covers 1999-08-10 to 2018-03-27.
    EGAN Stocker Initialized. Data covers 1999-09-23 to 2018-03-27.
    GLRI Stocker Initialized. Data covers 2012-10-17 to 2016-09-29.
    SMP Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    TCRD Stocker Initialized. Data covers 2010-04-22 to 2018-03-27.
    COCO Stocker Initialized. Data covers 1999-02-05 to 2015-02-13.
    CPHD Stocker Initialized. Data covers 2000-06-23 to 2016-11-04.
    BAX Stocker Initialized. Data covers 1981-10-27 to 2018-03-27.
    EGN Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    FLT Stocker Initialized. Data covers 2010-12-15 to 2018-03-27.
    LXK Stocker Initialized. Data covers 1995-11-15 to 2016-11-28.
    USNA Stocker Initialized. Data covers 1995-02-01 to 2018-03-27.
    HWKN Stocker Initialized. Data covers 1993-10-27 to 2018-03-27.
    RSYS Stocker Initialized. Data covers 1995-10-20 to 2018-03-27.
    AXAS Stocker Initialized. Data covers 1991-05-08 to 2018-03-27.
    CBR Stocker Initialized. Data covers 1994-03-17 to 2017-04-10.
    HBNC Stocker Initialized. Data covers 2002-01-09 to 2018-03-27.
    HMSY Stocker Initialized. Data covers 1992-12-18 to 2018-03-27.
    MENT Stocker Initialized. Data covers 1984-01-18 to 2017-03-30.
    ALTR Stocker Initialized. Data covers 1988-04-04 to 2018-03-07.
    ESSA Stocker Initialized. Data covers 2007-04-04 to 2018-03-27.
    AHC Stocker Initialized. Data covers 2008-02-11 to 2018-03-27.
    CTO Stocker Initialized. Data covers 1992-09-08 to 2018-03-27.
    HOS Stocker Initialized. Data covers 2004-03-26 to 2018-03-27.
    OAS Stocker Initialized. Data covers 2010-06-17 to 2018-03-27.
    THLD Stocker Initialized. Data covers 2005-02-04 to 2017-08-01.
    PLD Stocker Initialized. Data covers 1997-11-21 to 2018-03-27.
    BHB Stocker Initialized. Data covers 1997-09-23 to 2018-03-27.
    ED Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    CIX Stocker Initialized. Data covers 1998-03-06 to 2018-03-27.
    CSGS Stocker Initialized. Data covers 1996-02-28 to 2018-03-27.
    PNX Stocker Initialized. Data covers 2001-06-20 to 2016-06-20.
    INVN Stocker Initialized. Data covers 2011-11-16 to 2017-05-17.
    IPAR Stocker Initialized. Data covers 1991-08-20 to 2018-03-27.
    AAP Stocker Initialized. Data covers 2001-11-29 to 2018-03-27.
    VRSK Stocker Initialized. Data covers 2009-10-07 to 2018-03-27.
    SEAS Stocker Initialized. Data covers 2013-04-19 to 2018-03-27.
    HII Stocker Initialized. Data covers 2011-03-22 to 2018-03-27.
    IOSP Stocker Initialized. Data covers 1998-05-13 to 2018-03-27.
    NWN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TRI Stocker Initialized. Data covers 2002-06-12 to 2018-03-27.
    WSBF Stocker Initialized. Data covers 2005-10-05 to 2018-03-27.
    WWWW Stocker Initialized. Data covers 2005-11-03 to 2015-11-09.
    ONVO Stocker Initialized. Data covers 2012-02-14 to 2018-03-27.
    ALDR Stocker Initialized. Data covers 2014-05-08 to 2018-03-27.
    DRC Stocker Initialized. Data covers 2005-08-05 to 2015-06-30.
    CAC Stocker Initialized. Data covers 1997-10-08 to 2018-03-27.
    TRLA Stocker Initialized. Data covers 2012-09-20 to 2017-09-26.
    ENDP Stocker Initialized. Data covers 2000-07-18 to 2018-03-27.
    UA_C Stocker Initialized. Data covers 2016-04-08 to 2016-12-06.
    MGRC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    HZNP Stocker Initialized. Data covers 2011-07-28 to 2018-03-27.
    FIVE Stocker Initialized. Data covers 2012-07-19 to 2018-03-27.
    SHOR Stocker Initialized. Data covers 2007-07-03 to 2017-09-22.
    VRNG Stocker Initialized. Data covers 2010-07-27 to 2016-05-06.
    STZ Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    GFN Stocker Initialized. Data covers 2006-07-06 to 2018-03-27.
    TASR Stocker Initialized. Data covers 2001-06-19 to 2017-04-05.
    CTWS Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    CATO Stocker Initialized. Data covers 1987-04-23 to 2018-03-27.
    ODP Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BCOV Stocker Initialized. Data covers 2012-02-17 to 2018-03-27.
    MSFG Stocker Initialized. Data covers 1992-01-08 to 2018-03-27.
    NSTG Stocker Initialized. Data covers 2013-06-26 to 2018-03-27.
    QRVO Stocker Initialized. Data covers 2015-01-02 to 2018-03-27.
    PTCT Stocker Initialized. Data covers 2013-06-20 to 2018-03-27.
    CPWR Stocker Initialized. Data covers 1992-12-16 to 2014-12-15.
    AEE Stocker Initialized. Data covers 1998-01-02 to 2018-03-27.
    MCC Stocker Initialized. Data covers 2011-01-21 to 2018-03-27.
    ANTM Stocker Initialized. Data covers 2001-10-30 to 2018-03-27.
    PCH Stocker Initialized. Data covers 1985-11-11 to 2018-03-27.
    SIGA Stocker Initialized. Data covers 1997-09-10 to 2018-03-27.
    TSRO Stocker Initialized. Data covers 2012-06-28 to 2018-03-27.
    CME Stocker Initialized. Data covers 2002-12-06 to 2018-03-27.
    ECOM Stocker Initialized. Data covers 2013-05-23 to 2018-03-27.
    CHTR Stocker Initialized. Data covers 2010-01-05 to 2018-03-27.
    FRF Stocker Initialized. Data covers 2010-12-17 to 2014-12-03.
    SGMS Stocker Initialized. Data covers 1992-04-23 to 2018-03-27.
    SCL Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    FSTR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BNNY Stocker Initialized. Data covers 2012-03-28 to 2014-10-20.
    PERI Stocker Initialized. Data covers 2006-01-31 to 2018-03-27.
    BONT Stocker Initialized. Data covers 1991-09-24 to 2017-11-07.
    BOH Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    EDR Stocker Initialized. Data covers 2005-01-26 to 2018-03-27.
    INGR Stocker Initialized. Data covers 1997-12-11 to 2018-03-27.
    RUTH Stocker Initialized. Data covers 2005-08-09 to 2018-03-27.
    CFR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    IDXX Stocker Initialized. Data covers 1991-06-24 to 2018-03-27.
    ACI Stocker Initialized. Data covers 1988-08-12 to 2016-01-11.
    STR Stocker Initialized. Data covers 1987-12-29 to 2016-09-16.
    DLPH Stocker Initialized. Data covers 2011-11-17 to 2018-03-07.
    CYTR Stocker Initialized. Data covers 1989-03-29 to 2018-03-27.
    QGEN Stocker Initialized. Data covers 1996-06-28 to 2018-03-27.
    WAFD Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    QTS Stocker Initialized. Data covers 2013-10-09 to 2018-03-27.
    ERIE Stocker Initialized. Data covers 1995-10-02 to 2018-03-27.
    RHT Stocker Initialized. Data covers 1999-08-11 to 2018-03-27.
    AOSL Stocker Initialized. Data covers 2010-04-29 to 2018-03-27.
    MDLZ Stocker Initialized. Data covers 2001-06-13 to 2018-03-27.
    FLR Stocker Initialized. Data covers 2000-12-01 to 2018-03-27.
    WSFS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    GST Stocker Initialized. Data covers 2006-01-05 to 2018-03-27.
    NHC Stocker Initialized. Data covers 1987-01-20 to 2018-03-27.
    RENT Stocker Initialized. Data covers 1992-03-03 to 2016-01-29.
    STI Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    WINA Stocker Initialized. Data covers 1993-08-25 to 2018-03-27.
    AGCO Stocker Initialized. Data covers 1992-04-20 to 2018-03-27.
    CTBI Stocker Initialized. Data covers 1993-05-17 to 2018-03-27.
    RGLS Stocker Initialized. Data covers 2012-10-09 to 2018-03-27.
    UEC Stocker Initialized. Data covers 2007-04-05 to 2018-03-27.
    VC Stocker Initialized. Data covers 2010-10-05 to 2018-03-27.
    DXYN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    LXRX Stocker Initialized. Data covers 2000-04-07 to 2018-03-27.
    SLGN Stocker Initialized. Data covers 1997-02-14 to 2018-03-27.
    DMD Stocker Initialized. Data covers 2011-01-27 to 2016-11-08.
    KRNY Stocker Initialized. Data covers 2005-02-24 to 2018-03-27.
    AAL Stocker Initialized. Data covers 2005-09-27 to 2018-03-27.
    NWL Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    ENT Stocker Initialized. Data covers 2011-06-17 to 2018-03-27.
    SNHY Stocker Initialized. Data covers 1997-01-09 to 2018-03-27.
    ORN Stocker Initialized. Data covers 2007-12-20 to 2018-03-27.
    TWC Stocker Initialized. Data covers 2007-01-10 to 2016-05-17.
    SPLS Stocker Initialized. Data covers 1990-03-26 to 2017-09-12.
    USMD Stocker Initialized. Data covers 2012-09-07 to 2016-09-30.
    GNW Stocker Initialized. Data covers 2004-05-25 to 2018-03-07.
    TJX Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    AMC Stocker Initialized. Data covers 2013-12-18 to 2018-03-27.
    LXP Stocker Initialized. Data covers 1993-10-22 to 2018-03-27.
    SPWR Stocker Initialized. Data covers 2005-11-17 to 2018-03-27.
    SIVB Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ATW Stocker Initialized. Data covers 1984-09-07 to 2017-10-05.
    IEX Stocker Initialized. Data covers 1989-06-30 to 2018-03-27.
    SCVL Stocker Initialized. Data covers 1993-03-16 to 2018-03-27.
    RT Stocker Initialized. Data covers 1990-03-26 to 2017-12-21.
    JNPR Stocker Initialized. Data covers 1999-06-25 to 2018-03-27.
    COL Stocker Initialized. Data covers 2001-06-15 to 2018-03-27.
    FLS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CHD Stocker Initialized. Data covers 1986-03-06 to 2018-03-27.
    CAKE Stocker Initialized. Data covers 1992-09-18 to 2018-03-27.
    CUBE Stocker Initialized. Data covers 2004-10-22 to 2018-03-27.
    USLM Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    OSTK Stocker Initialized. Data covers 2002-05-30 to 2018-03-27.
    BAS Stocker Initialized. Data covers 2005-12-09 to 2018-03-27.
    MMI Stocker Initialized. Data covers 2013-10-31 to 2018-03-27.
    HIG Stocker Initialized. Data covers 1995-12-15 to 2018-03-27.
    CECE Stocker Initialized. Data covers 1993-02-19 to 2018-03-27.
    ISIS Stocker Initialized. Data covers 1991-05-17 to 2015-12-21.
    PEI Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    INTU Stocker Initialized. Data covers 1993-03-22 to 2018-03-27.
    ISLE Stocker Initialized. Data covers 1992-10-06 to 2017-05-01.
    IPCM Stocker Initialized. Data covers 2008-01-25 to 2015-11-20.
    PLCM Stocker Initialized. Data covers 1996-04-30 to 2016-09-26.
    POWI Stocker Initialized. Data covers 1997-12-12 to 2018-03-27.
    TGI Stocker Initialized. Data covers 1996-10-25 to 2018-03-27.
    GNRC Stocker Initialized. Data covers 2010-02-11 to 2018-03-27.
    WY Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    CIT Stocker Initialized. Data covers 2009-12-10 to 2018-03-27.
    HALO Stocker Initialized. Data covers 2004-03-16 to 2018-03-27.
    OFG Stocker Initialized. Data covers 1990-03-28 to 2018-03-27.
    NADL Stocker Initialized. Data covers 2014-01-29 to 2017-09-12.
    ECYT Stocker Initialized. Data covers 2011-02-04 to 2018-03-27.
    BELFB Stocker Initialized. Data covers 1998-07-10 to 2018-03-27.
    ESIO Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    EIGI Stocker Initialized. Data covers 2013-10-25 to 2018-03-27.
    DG Stocker Initialized. Data covers 2009-11-13 to 2018-03-27.
    UPIP Stocker Initialized. Data covers 1999-06-11 to 2016-06-16.
    DIS Stocker Initialized. Data covers 1962-01-02 to 2018-03-27.
    ACET Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AMNB Stocker Initialized. Data covers 1999-04-13 to 2018-03-27.
    PNRA Stocker Initialized. Data covers 1991-06-10 to 2017-07-17.
    III Stocker Initialized. Data covers 2007-02-12 to 2018-03-27.
    Z Stocker Initialized. Data covers 2015-08-17 to 2018-03-27.
    ATEN Stocker Initialized. Data covers 2014-03-21 to 2018-03-27.
    ININ Stocker Initialized. Data covers 1999-09-23 to 2016-12-01.
    KAMN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AIRM Stocker Initialized. Data covers 1987-08-31 to 2017-04-20.
    PAYC Stocker Initialized. Data covers 2014-04-15 to 2018-03-27.
    UCBI Stocker Initialized. Data covers 2002-03-21 to 2018-03-27.
    DSPG Stocker Initialized. Data covers 1994-02-14 to 2018-03-27.
    CBU Stocker Initialized. Data covers 1985-11-27 to 2018-03-27.
    MANH Stocker Initialized. Data covers 1998-04-23 to 2018-03-27.
    HOFT Stocker Initialized. Data covers 2002-06-27 to 2018-03-27.
    MBUU Stocker Initialized. Data covers 2014-01-31 to 2018-03-27.
    MS Stocker Initialized. Data covers 1993-02-23 to 2018-03-27.
    ROG Stocker Initialized. Data covers 1980-03-17 to 2018-03-27.
    GNCMA Stocker Initialized. Data covers 1995-08-18 to 2018-03-08.
    BBX Stocker Initialized. Data covers 1996-03-12 to 2018-03-27.
    VNDA Stocker Initialized. Data covers 2006-04-12 to 2018-03-27.
    HF Stocker Initialized. Data covers 2007-01-31 to 2018-03-27.
    AME Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    REXR Stocker Initialized. Data covers 2013-07-19 to 2018-03-27.
    GFF Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    STRL Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    STE Stocker Initialized. Data covers 1992-06-01 to 2018-03-27.
    WRLD Stocker Initialized. Data covers 1991-12-02 to 2018-03-27.
    WPX Stocker Initialized. Data covers 2011-12-12 to 2018-03-27.
    FNGN Stocker Initialized. Data covers 2010-03-16 to 2018-03-27.
    FVE Stocker Initialized. Data covers 2001-12-17 to 2018-03-27.
    DRNA Stocker Initialized. Data covers 2014-01-30 to 2018-03-27.
    APH Stocker Initialized. Data covers 1991-11-08 to 2018-03-27.
    ACOR Stocker Initialized. Data covers 2006-02-10 to 2018-03-27.
    BRK_B Stocker Initialized. Data covers 1996-05-09 to 2018-03-27.
    FCF Stocker Initialized. Data covers 1992-06-10 to 2018-03-27.
    FMBI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BWA Stocker Initialized. Data covers 1993-08-13 to 2018-03-27.
    ACCL Stocker Initialized. Data covers 1995-12-06 to 2014-04-29.
    ANDV Stocker Initialized. Data covers 2017-08-03 to 2018-03-27.
    GAIA Stocker Initialized. Data covers 1999-10-29 to 2018-03-27.
    MOD Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CRWN Stocker Initialized. Data covers 2000-05-08 to 2016-04-29.
    CPN Stocker Initialized. Data covers 2008-01-10 to 2018-03-08.
    SENEA Stocker Initialized. Data covers 1998-06-03 to 2018-03-27.
    ASH Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    PCCC Stocker Initialized. Data covers 1998-03-03 to 2016-09-08.
    DATA Stocker Initialized. Data covers 2013-05-17 to 2018-03-27.
    TOL Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    COLB Stocker Initialized. Data covers 1992-06-16 to 2018-03-27.
    HUM Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    FNFG Stocker Initialized. Data covers 1998-04-21 to 2016-07-29.
    DCO Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    PFPT Stocker Initialized. Data covers 2012-04-20 to 2018-03-27.
    DECK Stocker Initialized. Data covers 1993-10-15 to 2018-03-27.
    REXX Stocker Initialized. Data covers 2007-07-25 to 2018-03-27.
    SLCA Stocker Initialized. Data covers 2012-02-01 to 2018-03-27.
    CRS Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    PTP Stocker Initialized. Data covers 2002-10-29 to 2015-03-02.
    TRN Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    PYPL Stocker Initialized. Data covers 2015-07-20 to 2018-03-27.
    EPAM Stocker Initialized. Data covers 2012-02-08 to 2018-03-27.
    RGLD Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    HMHC Stocker Initialized. Data covers 2013-11-14 to 2018-03-27.
    MKTO Stocker Initialized. Data covers 2013-05-17 to 2016-08-16.
    VIAS Stocker Initialized. Data covers 1994-05-27 to 2015-05-29.
    MTRX Stocker Initialized. Data covers 1992-02-26 to 2018-03-27.
    IPI Stocker Initialized. Data covers 2008-04-22 to 2018-03-27.
    FIX Stocker Initialized. Data covers 1997-06-27 to 2018-03-27.
    MDVN Stocker Initialized. Data covers 1997-01-13 to 2016-09-28.
    NYCB Stocker Initialized. Data covers 1993-11-23 to 2018-03-27.
    DGI Stocker Initialized. Data covers 2009-05-14 to 2017-10-04.
    NEO Stocker Initialized. Data covers 2004-03-16 to 2018-03-27.
    MRTN Stocker Initialized. Data covers 1992-02-26 to 2018-03-27.
    INN Stocker Initialized. Data covers 2011-02-09 to 2018-03-27.
    UNH Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    SAM Stocker Initialized. Data covers 1995-11-21 to 2018-03-27.
    KMG Stocker Initialized. Data covers 1997-01-28 to 2018-03-27.
    SATS Stocker Initialized. Data covers 2008-01-02 to 2018-03-27.
    KRA Stocker Initialized. Data covers 2009-12-17 to 2018-03-27.
    LNDC Stocker Initialized. Data covers 1996-02-15 to 2018-03-27.
    ENZ Stocker Initialized. Data covers 1980-06-12 to 2018-03-27.
    WNR Stocker Initialized. Data covers 2006-01-19 to 2017-06-01.
    CTG Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    PFG Stocker Initialized. Data covers 2001-10-23 to 2018-03-27.
    UHS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    EBS Stocker Initialized. Data covers 2006-11-15 to 2018-03-27.
    PROV Stocker Initialized. Data covers 1996-06-28 to 2018-03-27.
    PE Stocker Initialized. Data covers 2014-05-23 to 2018-03-27.
    TSLA Stocker Initialized. Data covers 2010-06-29 to 2018-03-27.
    CVCO Stocker Initialized. Data covers 2003-07-01 to 2018-03-27.
    SHLO Stocker Initialized. Data covers 1993-06-29 to 2018-03-27.
    MJN Stocker Initialized. Data covers 2009-02-11 to 2017-06-14.
    SCHW Stocker Initialized. Data covers 1989-06-30 to 2018-03-27.
    CUR Stocker Initialized. Data covers 2007-03-30 to 2018-03-27.
    WEYS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    DF Stocker Initialized. Data covers 1996-04-17 to 2018-03-27.
    URBN Stocker Initialized. Data covers 1993-11-09 to 2018-03-07.
    OLN Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    OMCL Stocker Initialized. Data covers 2001-08-09 to 2018-03-27.
    CRRC Stocker Initialized. Data covers 1990-03-27 to 2015-06-05.
    LKFN Stocker Initialized. Data covers 1997-08-14 to 2018-03-27.
    BRKL Stocker Initialized. Data covers 1998-03-25 to 2018-03-27.
    PCL Stocker Initialized. Data covers 1989-06-02 to 2016-02-19.
    CVGW Stocker Initialized. Data covers 2002-07-22 to 2018-03-27.
    NR Stocker Initialized. Data covers 1991-09-26 to 2018-03-27.
    LLNW Stocker Initialized. Data covers 2007-06-08 to 2018-03-27.
    AHH Stocker Initialized. Data covers 2013-05-08 to 2018-03-27.
    AIT Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    RCKB Stocker Initialized. Data covers 2005-08-17 to 2014-04-30.
    AGII Stocker Initialized. Data covers 1986-11-14 to 2018-03-27.
    KND Stocker Initialized. Data covers 2001-05-01 to 2018-03-27.
    LPLA Stocker Initialized. Data covers 2010-11-18 to 2018-03-27.
    ANGI Stocker Initialized. Data covers 2011-11-17 to 2018-03-27.
    REN Stocker Initialized. Data covers 2007-10-08 to 2018-03-27.
    HBI Stocker Initialized. Data covers 2006-09-06 to 2018-03-27.
    FB Stocker Initialized. Data covers 2012-05-18 to 2018-03-27.
    LLEN Stocker Initialized. Data covers 2009-01-05 to 2015-03-06.
    ATNY Stocker Initialized. Data covers 2006-11-07 to 2016-04-22.
    BGS Stocker Initialized. Data covers 2007-05-23 to 2018-03-27.
    BHGE Stocker Initialized. Data covers 2017-07-06 to 2018-03-27.
    CMCSK Stocker Initialized. Data covers 1990-03-26 to 2015-12-11.
    DRE Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    P Stocker Initialized. Data covers 2011-06-15 to 2018-03-27.
    IDIX Stocker Initialized. Data covers 2004-07-22 to 2014-08-05.
    KEX Stocker Initialized. Data covers 1991-08-21 to 2018-03-27.
    SCOR Stocker Initialized. Data covers 2007-06-27 to 2017-02-07.
    INT Stocker Initialized. Data covers 1990-07-30 to 2018-03-27.
    ROCK Stocker Initialized. Data covers 1993-11-05 to 2018-03-27.
    SPAR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TWMC Stocker Initialized. Data covers 1993-02-17 to 2018-03-27.
    ELX Stocker Initialized. Data covers 1990-03-26 to 2015-05-05.
    DXPE Stocker Initialized. Data covers 1998-05-07 to 2018-03-27.
    PL Stocker Initialized. Data covers 1990-03-26 to 2015-01-30.
    RGS Stocker Initialized. Data covers 1991-06-21 to 2018-03-27.
    TAP Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    AXL Stocker Initialized. Data covers 1999-01-29 to 2018-03-27.
    NVDA Stocker Initialized. Data covers 1999-01-22 to 2018-03-27.
    SBY Stocker Initialized. Data covers 2012-12-17 to 2017-05-08.
    WOR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TGTX Stocker Initialized. Data covers 2010-05-03 to 2018-03-27.
    HIFS Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    MCO Stocker Initialized. Data covers 1994-10-31 to 2018-03-27.
    PATR Stocker Initialized. Data covers 1990-03-26 to 2014-12-04.
    PCAR Stocker Initialized. Data covers 1986-07-09 to 2018-03-27.
    TWGP Stocker Initialized. Data covers 2004-10-21 to 2014-09-15.
    FRP Stocker Initialized. Data covers 2011-01-25 to 2017-07-03.
    FSL Stocker Initialized. Data covers 2011-05-26 to 2015-12-07.
    MFA Stocker Initialized. Data covers 1998-04-13 to 2018-03-27.
    CPF Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CEVA Stocker Initialized. Data covers 2002-11-01 to 2018-03-27.
    WEN Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    CPE Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FET Stocker Initialized. Data covers 2012-04-12 to 2018-03-27.
    ROP Stocker Initialized. Data covers 1992-02-13 to 2018-03-27.
    LVNTA Stocker Initialized. Data covers 2012-08-10 to 2018-03-09.
    CNMD Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    VNCE Stocker Initialized. Data covers 2013-11-22 to 2018-03-27.
    MSA Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BP Stocker Initialized. Data covers 1977-01-03 to 2018-03-27.
    WMT Stocker Initialized. Data covers 1972-08-25 to 2018-03-27.
    XRM Stocker Initialized. Data covers 2005-05-16 to 2018-03-27.
    GARS Stocker Initialized. Data covers 2013-03-27 to 2018-03-27.
    JRN Stocker Initialized. Data covers 2003-09-24 to 2015-03-31.
    GDP Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    SEM Stocker Initialized. Data covers 2009-09-25 to 2018-03-27.
    BC Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    VZ Stocker Initialized. Data covers 1983-11-21 to 2018-03-27.
    NXTM Stocker Initialized. Data covers 2005-10-27 to 2018-03-27.
    AZPN Stocker Initialized. Data covers 1994-10-26 to 2018-03-27.
    MGLN Stocker Initialized. Data covers 2004-02-25 to 2018-03-27.
    GRUB Stocker Initialized. Data covers 2014-04-04 to 2018-03-27.
    FAF Stocker Initialized. Data covers 2010-05-28 to 2018-03-27.
    CVD Stocker Initialized. Data covers 1996-12-17 to 2015-02-18.
    GCI Stocker Initialized. Data covers 1985-07-01 to 2018-03-07.
    MDSO Stocker Initialized. Data covers 2009-06-25 to 2018-03-27.
    FHCO Stocker Initialized. Data covers 1999-02-11 to 2017-08-04.
    AMCX Stocker Initialized. Data covers 2011-06-16 to 2018-03-27.
    YDKN Stocker Initialized. Data covers 2014-07-07 to 2017-03-10.
    DGAS Stocker Initialized. Data covers 1990-03-26 to 2017-09-20.
    STLD Stocker Initialized. Data covers 1996-11-22 to 2018-03-27.
    AGM Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    LKQ Stocker Initialized. Data covers 2003-10-06 to 2018-03-27.
    DCI Stocker Initialized. Data covers 1987-06-18 to 2018-03-27.
    HLT Stocker Initialized. Data covers 2017-06-19 to 2018-03-27.
    AREX Stocker Initialized. Data covers 2007-11-08 to 2018-03-27.
    ATI Stocker Initialized. Data covers 1999-11-29 to 2018-03-07.
    HURC Stocker Initialized. Data covers 1989-09-05 to 2018-03-27.
    SNX Stocker Initialized. Data covers 2003-11-25 to 2018-03-27.
    CAVM Stocker Initialized. Data covers 2007-05-02 to 2018-03-27.
    FBC Stocker Initialized. Data covers 1997-04-30 to 2018-03-27.
    VMW Stocker Initialized. Data covers 2007-08-15 to 2018-03-27.
    LOCK Stocker Initialized. Data covers 2012-10-03 to 2017-02-08.
    EFSC Stocker Initialized. Data covers 2003-07-15 to 2018-03-27.
    HSIC Stocker Initialized. Data covers 1995-11-03 to 2018-03-27.
    MRVL Stocker Initialized. Data covers 2000-06-30 to 2018-03-27.
    RPRX Stocker Initialized. Data covers 1993-03-26 to 2018-01-31.
    BCR Stocker Initialized. Data covers 1983-04-06 to 2017-12-28.
    CDE Stocker Initialized. Data covers 1990-04-12 to 2018-03-27.
    EMN Stocker Initialized. Data covers 1993-12-14 to 2018-03-27.
    JMBA Stocker Initialized. Data covers 2005-07-28 to 2018-03-27.
    MDT Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    RL Stocker Initialized. Data covers 1997-06-12 to 2018-03-27.
    SGK Stocker Initialized. Data covers 1987-11-05 to 2014-07-30.
    FISI Stocker Initialized. Data covers 1999-06-25 to 2018-03-27.
    FNHC Stocker Initialized. Data covers 1998-11-05 to 2018-03-27.
    CYNI Stocker Initialized. Data covers 2013-05-09 to 2015-07-31.
    HCA Stocker Initialized. Data covers 2011-03-10 to 2018-03-27.
    SRI Stocker Initialized. Data covers 1997-10-10 to 2018-03-27.
    IRET Stocker Initialized. Data covers 1997-10-17 to 2018-03-27.
    FRAN Stocker Initialized. Data covers 2011-07-22 to 2018-03-27.
    PGR Stocker Initialized. Data covers 1986-07-09 to 2018-03-27.
    APA Stocker Initialized. Data covers 1979-05-15 to 2018-03-27.
    HTS Stocker Initialized. Data covers 2008-04-30 to 2016-07-11.
    OKE Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    ONTY Stocker Initialized. Data covers 1991-11-19 to 2016-06-08.
    SXC Stocker Initialized. Data covers 2011-07-21 to 2018-03-27.
    TNET Stocker Initialized. Data covers 2014-03-27 to 2018-03-27.
    YELP Stocker Initialized. Data covers 2012-03-02 to 2018-03-27.
    BGG Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    HES Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    NAVG Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PAY Stocker Initialized. Data covers 2005-04-29 to 2018-03-27.
    NVR Stocker Initialized. Data covers 1985-07-22 to 2018-03-27.
    ZEP Stocker Initialized. Data covers 2007-11-01 to 2015-06-25.
    MWV Stocker Initialized. Data covers 1985-07-01 to 2015-07-01.
    UIHC Stocker Initialized. Data covers 2007-11-07 to 2018-03-27.
    NWY Stocker Initialized. Data covers 2004-10-07 to 2018-03-27.
    K Stocker Initialized. Data covers 1984-12-17 to 2018-03-27.
    PSIX Stocker Initialized. Data covers 2012-04-17 to 2017-04-18.
    DWDP Stocker Initialized. Data covers 2017-09-01 to 2018-03-27.
    DRII Stocker Initialized. Data covers 2013-07-19 to 2016-09-02.
    RSH Stocker Initialized. Data covers 1982-01-04 to 2015-02-02.
    GALT Stocker Initialized. Data covers 2002-09-09 to 2018-03-27.
    QNST Stocker Initialized. Data covers 2010-02-11 to 2018-03-27.
    XON Stocker Initialized. Data covers 2013-08-08 to 2018-03-27.
    ALR Stocker Initialized. Data covers 1996-08-06 to 2017-10-02.
    STRZA Stocker Initialized. Data covers 2006-05-15 to 2016-12-08.
    KBH Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    LSCC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    JGW Stocker Initialized. Data covers 2013-11-08 to 2016-06-17.
    PHMD Stocker Initialized. Data covers 1996-05-30 to 2017-10-31.
    BEAM Stocker Initialized. Data covers 1977-01-03 to 2014-04-30.
    ASPS Stocker Initialized. Data covers 2009-08-06 to 2018-03-27.
    CLUB Stocker Initialized. Data covers 2006-06-02 to 2018-03-27.
    BIIB Stocker Initialized. Data covers 1991-09-17 to 2018-03-27.
    DEST Stocker Initialized. Data covers 1993-03-16 to 2018-03-27.
    HAIN Stocker Initialized. Data covers 1994-01-20 to 2018-03-27.
    WRI Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    CLGX Stocker Initialized. Data covers 1990-03-23 to 2018-03-27.
    HI Stocker Initialized. Data covers 2008-03-28 to 2018-03-27.
    NDAQ Stocker Initialized. Data covers 2002-07-01 to 2018-03-27.
    INGN Stocker Initialized. Data covers 2014-02-14 to 2018-03-27.
    UCFC Stocker Initialized. Data covers 1998-07-09 to 2018-03-27.
    TREX Stocker Initialized. Data covers 1999-04-08 to 2018-03-27.
    UNIS Stocker Initialized. Data covers 2010-02-16 to 2017-04-20.
    VPFG Stocker Initialized. Data covers 2006-10-03 to 2014-12-31.
    AXS Stocker Initialized. Data covers 2003-07-01 to 2018-03-27.
    DYAX Stocker Initialized. Data covers 2000-08-15 to 2016-01-22.
    RVLT Stocker Initialized. Data covers 1994-03-24 to 2018-03-27.
    HWCC Stocker Initialized. Data covers 2006-06-15 to 2018-03-27.
    CVO Stocker Initialized. Data covers 1995-09-22 to 2018-02-12.
    CFI Stocker Initialized. Data covers 1990-03-26 to 2017-07-12.
    ENVE Stocker Initialized. Data covers 1995-03-29 to 2014-10-16.
    GSOL Stocker Initialized. Data covers 2000-04-17 to 2017-08-28.
    CNP Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    MNTX Stocker Initialized. Data covers 2005-02-15 to 2018-03-27.
    WWE Stocker Initialized. Data covers 1999-10-19 to 2018-03-27.
    GTN Stocker Initialized. Data covers 2002-08-30 to 2018-03-27.
    SWM Stocker Initialized. Data covers 1995-11-09 to 2018-03-27.
    HME Stocker Initialized. Data covers 1994-08-01 to 2015-10-07.
    WR Stocker Initialized. Data covers 1987-08-25 to 2018-03-27.
    CORT Stocker Initialized. Data covers 2004-04-14 to 2018-03-27.
    SMA Stocker Initialized. Data covers 2004-12-09 to 2014-12-04.
    POM Stocker Initialized. Data covers 1987-01-02 to 2016-03-23.
    UVSP Stocker Initialized. Data covers 1998-04-16 to 2018-03-27.
    DISCA Stocker Initialized. Data covers 2005-07-08 to 2018-03-27.
    MNRO Stocker Initialized. Data covers 1991-07-30 to 2018-03-27.
    BIO Stocker Initialized. Data covers 1980-02-27 to 2018-03-27.
    IVAC Stocker Initialized. Data covers 1995-11-21 to 2018-03-27.
    PLPM Stocker Initialized. Data covers 2008-11-20 to 2017-12-19.
    VVI Stocker Initialized. Data covers 2004-08-12 to 2018-03-27.
    DVAX Stocker Initialized. Data covers 2004-02-19 to 2018-03-27.
    ALL Stocker Initialized. Data covers 1993-06-03 to 2018-03-27.
    TUP Stocker Initialized. Data covers 1996-05-08 to 2018-03-27.
    SQBK Stocker Initialized. Data covers 2014-03-27 to 2015-10-06.
    IR Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    FFIN Stocker Initialized. Data covers 1993-11-01 to 2018-03-27.
    PSX Stocker Initialized. Data covers 2012-04-12 to 2018-03-27.
    FBNK Stocker Initialized. Data covers 2011-06-30 to 2018-03-27.
    FULT Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BRCM Stocker Initialized. Data covers 1998-04-17 to 2016-01-29.
    TBBK Stocker Initialized. Data covers 2004-02-03 to 2018-03-27.
    LOPE Stocker Initialized. Data covers 2008-11-20 to 2018-03-27.
    CEB Stocker Initialized. Data covers 1999-02-23 to 2017-04-04.
    ANV Stocker Initialized. Data covers 2007-05-10 to 2015-03-09.
    CLCT Stocker Initialized. Data covers 1999-11-05 to 2018-03-27.
    MINI Stocker Initialized. Data covers 1994-02-17 to 2018-03-27.
    SNSS Stocker Initialized. Data covers 2005-09-27 to 2018-03-27.
    DW Stocker Initialized. Data covers 1989-05-03 to 2016-12-30.
    HIW Stocker Initialized. Data covers 1994-06-08 to 2018-03-27.
    ELS Stocker Initialized. Data covers 1993-02-25 to 2018-03-27.
    HSC Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    INFA Stocker Initialized. Data covers 1999-04-29 to 2015-08-06.
    MW Stocker Initialized. Data covers 1992-04-15 to 2016-01-29.
    MPX Stocker Initialized. Data covers 2001-03-01 to 2018-03-27.
    WU Stocker Initialized. Data covers 2006-10-02 to 2018-03-27.
    IRM Stocker Initialized. Data covers 1996-02-01 to 2018-03-27.
    HEOP Stocker Initialized. Data covers 1999-04-23 to 2017-03-31.
    FWRD Stocker Initialized. Data covers 1993-11-16 to 2018-03-27.
    TDS Stocker Initialized. Data covers 1991-09-18 to 2018-03-27.
    CPGX Stocker Initialized. Data covers 2015-07-02 to 2016-06-30.
    BWS Stocker Initialized. Data covers 1984-09-07 to 2015-05-28.
    SCTY Stocker Initialized. Data covers 2012-12-13 to 2016-11-21.
    EBAY Stocker Initialized. Data covers 1998-09-24 to 2018-03-27.
    MPC Stocker Initialized. Data covers 2011-06-24 to 2018-03-27.
    AMKR Stocker Initialized. Data covers 1998-05-01 to 2018-03-27.
    TRNX Stocker Initialized. Data covers 2011-02-03 to 2015-10-01.
    IHC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TWTR Stocker Initialized. Data covers 2013-11-07 to 2018-03-27.
    ANIP Stocker Initialized. Data covers 2000-05-05 to 2018-03-27.
    HTCH Stocker Initialized. Data covers 1990-03-26 to 2016-10-05.
    NSP Stocker Initialized. Data covers 1997-01-29 to 2018-03-27.
    GGP Stocker Initialized. Data covers 1993-04-08 to 2018-03-27.
    LYTS Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CLMS Stocker Initialized. Data covers 2004-10-28 to 2017-02-21.
    SYKE Stocker Initialized. Data covers 1996-04-30 to 2018-03-27.
    NBCB Stocker Initialized. Data covers 2013-05-10 to 2014-12-31.
    MSCI Stocker Initialized. Data covers 2007-11-15 to 2018-03-27.
    CHKP Stocker Initialized. Data covers 1996-06-28 to 2018-03-27.
    ASGN Stocker Initialized. Data covers 1992-09-23 to 2018-03-27.
    PDLI Stocker Initialized. Data covers 1992-01-29 to 2018-03-27.
    PWR Stocker Initialized. Data covers 1998-02-12 to 2018-03-27.
    NWHM Stocker Initialized. Data covers 2014-01-31 to 2018-03-27.
    ARI Stocker Initialized. Data covers 2009-09-24 to 2018-03-27.
    JPM Stocker Initialized. Data covers 1983-12-30 to 2018-03-27.
    MMC Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    OMER Stocker Initialized. Data covers 2009-10-08 to 2018-03-27.
    RRD Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    WTW Stocker Initialized. Data covers 2001-11-15 to 2018-03-27.
    XPO Stocker Initialized. Data covers 2003-10-07 to 2018-03-27.
    MRIN Stocker Initialized. Data covers 2013-03-22 to 2018-03-27.
    AMCC Stocker Initialized. Data covers 1997-12-08 to 2017-01-26.
    HWAY Stocker Initialized. Data covers 1991-08-13 to 2017-01-10.
    CSCD Stocker Initialized. Data covers 2004-12-15 to 2016-06-24.
    USM Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    PRIM Stocker Initialized. Data covers 2008-08-06 to 2018-03-27.
    PETM Stocker Initialized. Data covers 1993-07-23 to 2015-03-11.
    GMED Stocker Initialized. Data covers 2012-08-03 to 2018-03-27.
    FDS Stocker Initialized. Data covers 1996-06-28 to 2018-03-27.
    WMK Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    KIRK Stocker Initialized. Data covers 2002-07-30 to 2018-03-27.
    CCE Stocker Initialized. Data covers 1986-11-24 to 2018-03-27.
    SFLY Stocker Initialized. Data covers 2006-09-29 to 2018-03-27.
    BCPC Stocker Initialized. Data covers 1986-06-03 to 2018-03-27.
    SGM Stocker Initialized. Data covers 2013-10-10 to 2017-05-31.
    ACAD Stocker Initialized. Data covers 2004-05-27 to 2018-03-27.
    HFWA Stocker Initialized. Data covers 1998-05-07 to 2018-03-27.
    MAC Stocker Initialized. Data covers 1994-03-10 to 2018-03-27.
    DRQ Stocker Initialized. Data covers 1997-10-23 to 2018-03-27.
    VFC Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    PRFT Stocker Initialized. Data covers 1999-07-29 to 2018-03-27.
    TXMD Stocker Initialized. Data covers 2007-05-09 to 2018-03-27.
    CSX Stocker Initialized. Data covers 1980-11-03 to 2018-03-27.
    PNR Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    RFMD Stocker Initialized. Data covers 1997-06-03 to 2014-12-31.
    MSCC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FMER Stocker Initialized. Data covers 1989-03-29 to 2016-08-15.
    SWKS Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    AHL Stocker Initialized. Data covers 2003-12-05 to 2018-03-27.
    FFNW Stocker Initialized. Data covers 2007-10-10 to 2018-03-27.
    OGE Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    HGR Stocker Initialized. Data covers 1992-03-17 to 2016-02-26.
    ECPG Stocker Initialized. Data covers 1999-07-09 to 2018-03-27.
    CMTL Stocker Initialized. Data covers 1992-02-18 to 2018-03-27.
    CIDM Stocker Initialized. Data covers 2003-11-10 to 2018-03-27.
    VHC Stocker Initialized. Data covers 1999-07-30 to 2018-03-27.
    ADM Stocker Initialized. Data covers 1983-04-05 to 2018-03-27.
    PNC Stocker Initialized. Data covers 1988-09-07 to 2018-03-27.
    MCRL Stocker Initialized. Data covers 1994-12-09 to 2015-08-03.
    KBR Stocker Initialized. Data covers 2006-11-16 to 2018-03-27.
    OEH Stocker Initialized. Data covers 2000-08-03 to 2014-07-25.
    RDN Stocker Initialized. Data covers 1992-10-30 to 2018-03-27.
    ORB Stocker Initialized. Data covers 1990-04-24 to 2015-02-09.
    UTEK Stocker Initialized. Data covers 1993-09-29 to 2017-05-25.
    GLT Stocker Initialized. Data covers 1984-05-16 to 2018-03-27.
    HRB Stocker Initialized. Data covers 1986-11-12 to 2018-03-27.
    INTC Stocker Initialized. Data covers 1980-03-17 to 2018-03-27.
    PES Stocker Initialized. Data covers 1995-02-01 to 2018-03-27.
    GVA Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    NOG Stocker Initialized. Data covers 2007-04-13 to 2018-03-27.
    CATY Stocker Initialized. Data covers 1990-12-17 to 2018-03-27.
    FTI Stocker Initialized. Data covers 2001-06-15 to 2018-03-27.
    GM Stocker Initialized. Data covers 2010-11-18 to 2018-03-27.
    SCHL Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    GBNK Stocker Initialized. Data covers 2005-10-03 to 2018-03-27.
    OLP Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    BBG Stocker Initialized. Data covers 2004-12-10 to 2018-03-19.
    TK Stocker Initialized. Data covers 1995-07-20 to 2018-03-27.
    WLT Stocker Initialized. Data covers 1995-10-10 to 2015-07-07.
    CNOB Stocker Initialized. Data covers 1996-05-30 to 2018-03-27.
    CVBF Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    DENN Stocker Initialized. Data covers 1998-01-08 to 2018-03-27.
    SPN Stocker Initialized. Data covers 1992-07-07 to 2018-03-27.
    USPH Stocker Initialized. Data covers 1992-05-29 to 2018-03-27.
    TDW Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    SALT Stocker Initialized. Data covers 2013-12-12 to 2018-03-27.
    VRSN Stocker Initialized. Data covers 1998-01-30 to 2018-03-27.
    LOW Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    DWA Stocker Initialized. Data covers 2004-10-28 to 2016-08-22.
    CRCM Stocker Initialized. Data covers 2014-01-24 to 2018-03-27.
    ADES Stocker Initialized. Data covers 2016-05-26 to 2018-03-27.
    ARG Stocker Initialized. Data covers 1986-12-22 to 2016-05-20.
    JJSF Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    DDR Stocker Initialized. Data covers 1993-02-02 to 2018-03-27.
    CNS Stocker Initialized. Data covers 2004-08-16 to 2018-03-27.
    NTRI Stocker Initialized. Data covers 2000-03-30 to 2018-03-27.
    SWAY Stocker Initialized. Data covers 2014-01-22 to 2016-01-05.
    CVEO Stocker Initialized. Data covers 2014-05-19 to 2018-03-27.
    HTLD Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PENX Stocker Initialized. Data covers 1987-08-19 to 2015-03-10.
    ACRE Stocker Initialized. Data covers 2012-04-27 to 2018-03-27.
    WIRE Stocker Initialized. Data covers 1992-07-20 to 2018-03-27.
    KEY Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    MAIN Stocker Initialized. Data covers 2007-10-09 to 2018-03-27.
    ATRC Stocker Initialized. Data covers 2005-08-05 to 2018-03-27.
    HITT Stocker Initialized. Data covers 2005-07-22 to 2014-07-22.
    NGS Stocker Initialized. Data covers 2002-10-22 to 2018-03-27.
    NJR Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    RHI Stocker Initialized. Data covers 1992-03-10 to 2018-03-27.
    MNI Stocker Initialized. Data covers 1989-06-30 to 2018-03-27.
    ARAY Stocker Initialized. Data covers 2007-02-08 to 2018-03-27.
    DWSN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ESGR Stocker Initialized. Data covers 1997-05-09 to 2018-03-27.
    PBH Stocker Initialized. Data covers 2005-02-10 to 2018-03-27.
    EE Stocker Initialized. Data covers 1989-07-07 to 2018-03-27.
    CPT Stocker Initialized. Data covers 1993-07-22 to 2018-03-27.
    MUR Stocker Initialized. Data covers 1983-04-06 to 2018-03-07.
    NATI Stocker Initialized. Data covers 1995-03-14 to 2018-03-27.
    IQNT Stocker Initialized. Data covers 2007-11-02 to 2017-02-09.
    RLGY Stocker Initialized. Data covers 2012-10-11 to 2018-03-27.
    IMI Stocker Initialized. Data covers 2011-11-18 to 2018-03-27.
    MDU Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    MSM Stocker Initialized. Data covers 1995-12-15 to 2018-03-27.
    RP Stocker Initialized. Data covers 2010-08-12 to 2018-03-27.
    SRE Stocker Initialized. Data covers 1998-06-29 to 2018-03-27.
    UTI Stocker Initialized. Data covers 2003-12-18 to 2018-03-27.
    SCS Stocker Initialized. Data covers 1998-02-18 to 2018-03-27.
    OSUR Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    RRGB Stocker Initialized. Data covers 2002-07-19 to 2018-03-27.
    SON Stocker Initialized. Data covers 1985-06-11 to 2018-03-27.
    ARIA Stocker Initialized. Data covers 1994-09-19 to 2017-02-15.
    UAA Stocker Initialized. Data covers 2005-11-18 to 2018-03-27.
    NCS Stocker Initialized. Data covers 1992-04-06 to 2018-03-27.
    TNK Stocker Initialized. Data covers 2007-12-13 to 2018-03-27.
    CLD Stocker Initialized. Data covers 2009-11-20 to 2018-03-27.
    PRGX Stocker Initialized. Data covers 1996-03-27 to 2018-03-27.
    PRI Stocker Initialized. Data covers 2010-04-01 to 2018-03-27.
    CETV Stocker Initialized. Data covers 1994-10-14 to 2018-03-27.
    RSO Stocker Initialized. Data covers 2006-02-07 to 2018-03-27.
    CODE Stocker Initialized. Data covers 2010-05-18 to 2015-03-12.
    STRT Stocker Initialized. Data covers 1995-02-24 to 2018-03-27.
    AEC Stocker Initialized. Data covers 1993-11-11 to 2015-08-06.
    DELL Stocker Initialized. Data covers 1988-08-17 to 2015-03-04.
    EPR Stocker Initialized. Data covers 1997-11-18 to 2018-03-27.
    CASS Stocker Initialized. Data covers 1996-01-02 to 2018-03-27.
    DISCK Stocker Initialized. Data covers 2008-09-18 to 2018-03-27.
    SJW Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    GMO Stocker Initialized. Data covers 2005-02-17 to 2018-03-27.
    MKL Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    NEON Stocker Initialized. Data covers 1992-03-03 to 2018-03-27.
    BANC Stocker Initialized. Data covers 2002-10-01 to 2018-03-27.
    CFG Stocker Initialized. Data covers 2014-09-24 to 2018-03-27.
    NOR Stocker Initialized. Data covers 2010-05-14 to 2015-11-25.
    PFBC Stocker Initialized. Data covers 1999-08-19 to 2018-03-27.
    TRMK Stocker Initialized. Data covers 1992-03-03 to 2018-03-27.
    CSII Stocker Initialized. Data covers 2006-06-28 to 2018-03-27.
    BDSI Stocker Initialized. Data covers 2002-07-25 to 2018-03-27.
    AIV Stocker Initialized. Data covers 1994-07-22 to 2018-03-27.
    WRK Stocker Initialized. Data covers 2015-06-24 to 2018-03-27.
    CHRW Stocker Initialized. Data covers 1997-10-16 to 2018-03-27.
    NANO Stocker Initialized. Data covers 1992-02-26 to 2018-03-27.
    ZIXI Stocker Initialized. Data covers 1989-11-10 to 2018-03-27.
    AZZ Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    HNH Stocker Initialized. Data covers 2005-08-22 to 2017-10-12.
    RFP Stocker Initialized. Data covers 2010-12-10 to 2018-03-27.
    AVT Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    OZRK Stocker Initialized. Data covers 1997-07-17 to 2018-03-27.
    WDR Stocker Initialized. Data covers 1998-03-05 to 2018-03-27.
    CVC Stocker Initialized. Data covers 1992-03-17 to 2016-06-20.
    GAS Stocker Initialized. Data covers 1973-05-03 to 2016-06-30.
    MWIV Stocker Initialized. Data covers 2005-08-03 to 2015-02-24.
    SPDC Stocker Initialized. Data covers 1993-12-17 to 2016-01-20.
    TSS Stocker Initialized. Data covers 1989-06-30 to 2018-03-27.
    DRL Stocker Initialized. Data covers 1992-02-25 to 2015-02-27.
    MPW Stocker Initialized. Data covers 2005-07-08 to 2018-03-27.
    MIL Stocker Initialized. Data covers 1996-05-08 to 2016-02-12.
    ICEL Stocker Initialized. Data covers 2013-07-25 to 2015-05-01.
    FEIC Stocker Initialized. Data covers 1995-06-01 to 2016-09-19.
    PVA Stocker Initialized. Data covers 1990-03-26 to 2016-01-12.
    SSS Stocker Initialized. Data covers 1995-06-21 to 2016-08-12.
    TSYS Stocker Initialized. Data covers 2000-08-09 to 2016-02-23.
    CBSH Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    SQNM Stocker Initialized. Data covers 2000-02-01 to 2016-09-06.
    BEAT Stocker Initialized. Data covers 2008-03-19 to 2018-03-27.
    TTMI Stocker Initialized. Data covers 2000-09-25 to 2018-03-27.
    PPBI Stocker Initialized. Data covers 1997-06-25 to 2018-03-27.
    IG Stocker Initialized. Data covers 1990-04-17 to 2015-10-23.
    DNR Stocker Initialized. Data covers 1995-09-06 to 2018-03-27.
    ONNN Stocker Initialized. Data covers 2000-05-02 to 2015-04-02.
    VOCS Stocker Initialized. Data covers 2005-12-07 to 2014-05-30.
    TYL Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    CRIS Stocker Initialized. Data covers 2000-08-01 to 2018-03-27.
    XRAY Stocker Initialized. Data covers 1991-04-25 to 2018-03-27.
    ADTN Stocker Initialized. Data covers 1994-08-10 to 2018-03-27.
    RGEN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    UGI Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    IM Stocker Initialized. Data covers 1996-11-01 to 2016-12-05.
    IDT Stocker Initialized. Data covers 2001-05-16 to 2018-03-27.
    PKE Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    FNSR Stocker Initialized. Data covers 1999-11-12 to 2018-03-27.
    ESE Stocker Initialized. Data covers 1990-10-01 to 2018-03-27.
    AEO Stocker Initialized. Data covers 1994-04-14 to 2018-03-27.
    BFS Stocker Initialized. Data covers 1993-08-19 to 2018-03-27.
    MAA Stocker Initialized. Data covers 1994-01-28 to 2018-03-27.
    OWW Stocker Initialized. Data covers 2007-07-20 to 2015-09-16.
    WLB Stocker Initialized. Data covers 1999-04-19 to 2018-03-27.
    SGMO Stocker Initialized. Data covers 2000-04-06 to 2018-03-27.
    MCHX Stocker Initialized. Data covers 2004-03-31 to 2018-03-27.
    CTXS Stocker Initialized. Data covers 1995-12-08 to 2018-03-27.
    DMRC Stocker Initialized. Data covers 1999-12-02 to 2018-03-27.
    WHG Stocker Initialized. Data covers 2002-06-13 to 2018-03-27.
    KO Stocker Initialized. Data covers 1962-01-02 to 2018-03-27.
    NICK Stocker Initialized. Data covers 1997-12-29 to 2018-03-27.
    GILD Stocker Initialized. Data covers 1992-01-22 to 2018-03-27.
    POWR Stocker Initialized. Data covers 1993-03-25 to 2016-05-06.
    FRSH Stocker Initialized. Data covers 2014-05-02 to 2018-03-27.
    VRNS Stocker Initialized. Data covers 2014-02-28 to 2018-03-27.
    MLNK Stocker Initialized. Data covers 1994-01-31 to 2018-02-26.
    QLYS Stocker Initialized. Data covers 2012-09-28 to 2018-03-27.
    TXRH Stocker Initialized. Data covers 2004-10-05 to 2018-03-27.
    WCN Stocker Initialized. Data covers 1998-05-22 to 2018-03-27.
    DFRG Stocker Initialized. Data covers 2012-07-27 to 2018-03-27.
    ES Stocker Initialized. Data covers 1984-08-29 to 2018-03-27.
    PWOD Stocker Initialized. Data covers 1996-05-30 to 2018-03-27.
    SREV Stocker Initialized. Data covers 2011-03-25 to 2018-03-27.
    ITG Stocker Initialized. Data covers 1994-05-04 to 2018-03-27.
    CSC Stocker Initialized. Data covers 1981-12-31 to 2017-03-31.
    H Stocker Initialized. Data covers 2009-11-05 to 2018-03-27.
    CERN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    EQT Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    ACRX Stocker Initialized. Data covers 2011-02-11 to 2018-03-27.
    EVHC Stocker Initialized. Data covers 2013-08-14 to 2018-03-27.
    MSTR Stocker Initialized. Data covers 1998-06-11 to 2018-03-27.
    ORLY Stocker Initialized. Data covers 1993-04-23 to 2018-03-27.
    TWX Stocker Initialized. Data covers 1992-03-19 to 2018-03-27.
    ZION Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FORM Stocker Initialized. Data covers 2003-06-12 to 2018-03-27.
    EXAS Stocker Initialized. Data covers 2001-02-01 to 2018-03-27.
    PGC Stocker Initialized. Data covers 1999-04-27 to 2018-03-27.
    LVS Stocker Initialized. Data covers 2004-12-15 to 2018-03-27.
    SIR Stocker Initialized. Data covers 2012-03-07 to 2018-03-27.
    SLG Stocker Initialized. Data covers 1997-08-15 to 2018-03-27.
    TRST Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ANSS Stocker Initialized. Data covers 1996-06-21 to 2018-03-27.
    FCBC Stocker Initialized. Data covers 1997-05-09 to 2018-03-27.
    CBG Stocker Initialized. Data covers 2004-06-10 to 2018-03-19.
    SSNC Stocker Initialized. Data covers 2010-03-31 to 2018-03-27.
    KPTI Stocker Initialized. Data covers 2013-11-06 to 2018-03-27.
    EBTC Stocker Initialized. Data covers 2005-02-14 to 2018-03-27.
    BCOR Stocker Initialized. Data covers 1998-12-15 to 2018-03-27.
    PMC Stocker Initialized. Data covers 2007-08-01 to 2017-12-07.
    RDNT Stocker Initialized. Data covers 1997-01-03 to 2018-03-27.
    VPRT Stocker Initialized. Data covers 2005-09-30 to 2014-11-12.
    MCP Stocker Initialized. Data covers 2010-07-29 to 2015-06-24.
    HILL Stocker Initialized. Data covers 1997-09-17 to 2015-10-05.
    ESL Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    PCRX Stocker Initialized. Data covers 2011-02-03 to 2018-03-27.
    CRVL Stocker Initialized. Data covers 1991-06-28 to 2018-03-27.
    TRAK Stocker Initialized. Data covers 2005-12-13 to 2015-09-30.
    ISBC Stocker Initialized. Data covers 2005-10-12 to 2018-03-27.
    AGNC Stocker Initialized. Data covers 2008-05-15 to 2018-03-27.
    CYT Stocker Initialized. Data covers 1993-12-22 to 2015-12-08.
    COUP Stocker Initialized. Data covers 2016-10-06 to 2018-03-27.
    HSP Stocker Initialized. Data covers 2004-05-03 to 2015-09-02.
    JKHY Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PLPC Stocker Initialized. Data covers 1999-04-28 to 2018-03-27.
    SNTA Stocker Initialized. Data covers 2007-02-06 to 2016-07-22.
    RMD Stocker Initialized. Data covers 1995-06-02 to 2018-03-27.
    QCOM Stocker Initialized. Data covers 1991-12-16 to 2018-03-27.
    MCGC Stocker Initialized. Data covers 2001-11-30 to 2015-08-17.
    CACQ Stocker Initialized. Data covers 2013-11-19 to 2017-10-05.
    KMT Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    ATR Stocker Initialized. Data covers 1993-04-23 to 2018-03-27.
    RPM Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CSGP Stocker Initialized. Data covers 1998-07-01 to 2018-03-27.
    APOL Stocker Initialized. Data covers 1995-01-04 to 2017-02-01.
    WETF Stocker Initialized. Data covers 1993-03-04 to 2018-03-27.
    WMB Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    UHT Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    TWER Stocker Initialized. Data covers 2007-01-24 to 2016-11-30.
    CMP Stocker Initialized. Data covers 2003-12-12 to 2018-03-27.
    BBW Stocker Initialized. Data covers 2004-10-28 to 2018-03-27.
    XEL Stocker Initialized. Data covers 1985-09-24 to 2018-03-27.
    IRWD Stocker Initialized. Data covers 2010-02-03 to 2018-03-27.
    FBP Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    JONE Stocker Initialized. Data covers 2013-07-24 to 2018-03-27.
    GNC Stocker Initialized. Data covers 2011-04-01 to 2018-03-27.
    PJC Stocker Initialized. Data covers 2004-01-02 to 2018-03-27.
    SLH Stocker Initialized. Data covers 2007-05-11 to 2016-03-03.
    DOC Stocker Initialized. Data covers 2013-07-19 to 2018-03-27.
    BRC Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    PG Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    CENTA Stocker Initialized. Data covers 2007-02-06 to 2018-03-27.
    SUSQ Stocker Initialized. Data covers 1990-03-26 to 2015-07-31.
    XL Stocker Initialized. Data covers 1991-07-19 to 2018-03-27.
    DFZ Stocker Initialized. Data covers 1992-03-16 to 2014-09-04.
    OPB Stocker Initialized. Data covers 2014-04-16 to 2018-03-27.
    NBR Stocker Initialized. Data covers 1991-02-28 to 2018-03-07.
    PRA Stocker Initialized. Data covers 1991-09-04 to 2018-03-27.
    PSEC Stocker Initialized. Data covers 2004-07-27 to 2018-03-27.
    BRCD Stocker Initialized. Data covers 1999-05-25 to 2017-11-17.
    ABG Stocker Initialized. Data covers 2002-03-21 to 2018-03-27.
    ACM Stocker Initialized. Data covers 2007-05-10 to 2018-03-27.
    GRT Stocker Initialized. Data covers 1994-01-20 to 2015-01-15.
    VIVO Stocker Initialized. Data covers 1992-02-26 to 2018-03-27.
    INFI Stocker Initialized. Data covers 2000-07-28 to 2018-03-27.
    CXO Stocker Initialized. Data covers 2007-08-03 to 2018-03-27.
    ORA Stocker Initialized. Data covers 2004-11-11 to 2018-03-27.
    CNA Stocker Initialized. Data covers 1985-07-11 to 2018-03-27.
    FRT Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    WM Stocker Initialized. Data covers 1991-09-30 to 2018-03-27.
    TMHC Stocker Initialized. Data covers 2013-04-10 to 2018-03-27.
    MEG Stocker Initialized. Data covers 1975-09-09 to 2017-01-17.
    ALIM Stocker Initialized. Data covers 2010-04-22 to 2018-03-27.
    DMND Stocker Initialized. Data covers 2005-07-21 to 2016-02-26.
    ACC Stocker Initialized. Data covers 2004-08-16 to 2018-03-27.
    DAVE Stocker Initialized. Data covers 1996-11-04 to 2018-03-27.
    AMBR Stocker Initialized. Data covers 2014-03-21 to 2018-03-27.
    HTBI Stocker Initialized. Data covers 2012-07-11 to 2018-03-27.
    BAGR Stocker Initialized. Data covers 2008-11-19 to 2015-11-06.
    BLOX Stocker Initialized. Data covers 2012-04-20 to 2016-11-04.
    HAE Stocker Initialized. Data covers 1991-05-10 to 2018-03-27.
    BOOM Stocker Initialized. Data covers 1989-01-05 to 2018-03-27.
    HW Stocker Initialized. Data covers 1995-08-24 to 2017-05-05.
    MPO Stocker Initialized. Data covers 2012-04-20 to 2018-03-27.
    BKU Stocker Initialized. Data covers 2011-01-28 to 2018-03-27.
    BXS Stocker Initialized. Data covers 1985-10-16 to 2018-03-27.
    NILE Stocker Initialized. Data covers 2004-05-20 to 2017-02-16.
    KELYA Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TSRE Stocker Initialized. Data covers 2008-07-07 to 2015-09-16.
    MLM Stocker Initialized. Data covers 1994-02-17 to 2018-03-27.
    BHI Stocker Initialized. Data covers 1987-04-07 to 2017-07-03.
    YORW Stocker Initialized. Data covers 1999-05-03 to 2018-03-27.
    RUSHA Stocker Initialized. Data covers 2003-10-07 to 2018-03-27.
    SNH Stocker Initialized. Data covers 2000-02-23 to 2018-03-27.
    WFM Stocker Initialized. Data covers 1992-01-23 to 2017-08-28.
    ALNY Stocker Initialized. Data covers 2004-06-01 to 2018-03-27.
    HALL Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    BXLT Stocker Initialized. Data covers 2015-07-01 to 2016-06-02.
    EPM Stocker Initialized. Data covers 1997-01-13 to 2018-03-27.
    KALU Stocker Initialized. Data covers 2006-07-07 to 2018-03-27.
    ZOES Stocker Initialized. Data covers 2014-04-11 to 2018-03-27.
    ACTG Stocker Initialized. Data covers 2002-12-16 to 2018-03-27.
    USMO Stocker Initialized. Data covers 2004-11-17 to 2014-07-08.
    PDM Stocker Initialized. Data covers 2010-02-10 to 2018-03-27.
    DCOM Stocker Initialized. Data covers 1996-06-26 to 2018-03-27.
    KNX Stocker Initialized. Data covers 1994-10-25 to 2018-03-27.
    MBI Stocker Initialized. Data covers 1987-07-02 to 2018-03-27.
    WDC Stocker Initialized. Data covers 1987-01-02 to 2018-03-27.
    CARA Stocker Initialized. Data covers 2014-01-31 to 2018-03-27.
    BYD Stocker Initialized. Data covers 1993-10-18 to 2018-03-27.
    REX Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    AEGN Stocker Initialized. Data covers 1989-04-24 to 2018-03-27.
    FOXA Stocker Initialized. Data covers 1996-03-11 to 2018-03-27.
    TSRA Stocker Initialized. Data covers 2003-11-20 to 2017-02-22.
    DOX Stocker Initialized. Data covers 1998-06-19 to 2018-03-27.
    ILMN Stocker Initialized. Data covers 2000-07-28 to 2018-03-27.
    MMS Stocker Initialized. Data covers 1997-06-13 to 2018-03-27.
    OSK Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PRKR Stocker Initialized. Data covers 1993-12-01 to 2018-03-27.
    BPZ Stocker Initialized. Data covers 2003-10-07 to 2015-03-02.
    IBKR Stocker Initialized. Data covers 2007-05-04 to 2018-03-27.
    SPB Stocker Initialized. Data covers 2009-09-02 to 2018-03-27.
    LEN Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    LSTR Stocker Initialized. Data covers 1993-03-05 to 2018-03-27.
    MTW Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FRO Stocker Initialized. Data covers 2001-08-06 to 2018-03-27.
    CHTP Stocker Initialized. Data covers 2005-11-10 to 2014-06-23.
    FBRC Stocker Initialized. Data covers 2007-06-08 to 2017-06-01.
    SIG Stocker Initialized. Data covers 1994-10-31 to 2018-03-27.
    GTY Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    BRSS Stocker Initialized. Data covers 2013-05-23 to 2018-03-27.
    IART Stocker Initialized. Data covers 1995-08-16 to 2018-03-27.
    CTRN Stocker Initialized. Data covers 2005-05-18 to 2018-03-27.
    BLT Stocker Initialized. Data covers 1999-08-20 to 2016-04-11.
    OC Stocker Initialized. Data covers 2006-11-01 to 2018-03-27.
    MDC Stocker Initialized. Data covers 1980-03-11 to 2018-03-27.
    HT Stocker Initialized. Data covers 1999-01-21 to 2018-03-27.
    TNGO Stocker Initialized. Data covers 2011-07-27 to 2017-03-13.
    DST Stocker Initialized. Data covers 1995-11-01 to 2018-03-27.
    DTLK Stocker Initialized. Data covers 1999-08-06 to 2017-01-06.
    LABL Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BSX Stocker Initialized. Data covers 1992-05-19 to 2018-03-27.
    HMN Stocker Initialized. Data covers 1991-11-15 to 2018-03-27.
    CSFL Stocker Initialized. Data covers 2001-01-30 to 2018-03-27.
    GLAD Stocker Initialized. Data covers 2002-08-02 to 2018-03-27.
    TKR Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    SHLM Stocker Initialized. Data covers 1986-07-09 to 2018-03-27.
    SIMG Stocker Initialized. Data covers 1999-10-06 to 2015-03-10.
    CKH Stocker Initialized. Data covers 1992-12-17 to 2018-03-27.
    PRXL Stocker Initialized. Data covers 1995-11-22 to 2017-09-29.
    ROVI Stocker Initialized. Data covers 1997-03-13 to 2016-09-07.
    FF Stocker Initialized. Data covers 2011-03-23 to 2018-03-27.
    SWI Stocker Initialized. Data covers 2009-05-20 to 2016-02-05.
    ABT Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    NUTR Stocker Initialized. Data covers 1998-02-20 to 2017-08-22.
    ATVI Stocker Initialized. Data covers 1993-10-25 to 2018-03-27.
    CIA Stocker Initialized. Data covers 1988-12-05 to 2018-03-27.
    SMG Stocker Initialized. Data covers 1992-01-31 to 2018-03-27.
    ASNA Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    ADNC Stocker Initialized. Data covers 2012-05-11 to 2015-06-30.
    ICPT Stocker Initialized. Data covers 2012-10-11 to 2018-03-27.
    VTG Stocker Initialized. Data covers 2007-06-08 to 2015-09-11.
    FARM Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PMFG Stocker Initialized. Data covers 1990-03-26 to 2015-09-03.
    BERY Stocker Initialized. Data covers 2012-10-04 to 2018-03-27.
    RECN Stocker Initialized. Data covers 2000-12-15 to 2018-03-27.
    UBNT Stocker Initialized. Data covers 2011-10-14 to 2018-03-27.
    UPL Stocker Initialized. Data covers 1999-09-24 to 2018-03-27.
    GPX Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    EGL Stocker Initialized. Data covers 2012-07-18 to 2018-03-27.
    EXAM Stocker Initialized. Data covers 2010-10-29 to 2016-07-27.
    URG Stocker Initialized. Data covers 2008-07-25 to 2018-03-27.
    DEI Stocker Initialized. Data covers 2006-10-25 to 2018-03-27.
    AAON Stocker Initialized. Data covers 1992-12-16 to 2018-03-27.
    MYRG Stocker Initialized. Data covers 2008-08-13 to 2018-03-27.
    BRK_A Stocker Initialized. Data covers 1980-03-17 to 2018-03-27.
    ALJ Stocker Initialized. Data covers 2005-07-28 to 2017-06-30.
    FIS Stocker Initialized. Data covers 2001-06-20 to 2018-03-27.
    RCL Stocker Initialized. Data covers 1993-04-28 to 2018-03-27.
    GRC Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    MCK Stocker Initialized. Data covers 1994-11-15 to 2018-03-27.
    CPK Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    WCIC Stocker Initialized. Data covers 2013-07-25 to 2017-02-10.
    MLR Stocker Initialized. Data covers 1994-08-02 to 2018-03-27.
    SCSC Stocker Initialized. Data covers 1994-03-18 to 2018-03-27.
    NUS Stocker Initialized. Data covers 1996-11-22 to 2018-03-27.
    OMN Stocker Initialized. Data covers 1999-09-27 to 2018-03-27.
    PNM Stocker Initialized. Data covers 1984-08-10 to 2018-03-27.
    NTCT Stocker Initialized. Data covers 1999-08-12 to 2018-03-27.
    WD Stocker Initialized. Data covers 2010-12-15 to 2018-03-27.
    SBGI Stocker Initialized. Data covers 1995-06-07 to 2018-03-27.
    TR Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    LBAI Stocker Initialized. Data covers 1999-01-04 to 2018-03-27.
    AI Stocker Initialized. Data covers 1997-12-23 to 2018-03-27.
    NMBL Stocker Initialized. Data covers 2013-12-13 to 2017-04-17.
    AMRS Stocker Initialized. Data covers 2010-09-28 to 2018-03-27.
    BURL Stocker Initialized. Data covers 2013-10-02 to 2018-03-27.
    HSH Stocker Initialized. Data covers 1986-05-05 to 2014-08-29.
    FLTX Stocker Initialized. Data covers 2012-10-09 to 2016-11-04.
    FN Stocker Initialized. Data covers 2010-06-25 to 2018-03-27.
    UMPQ Stocker Initialized. Data covers 1998-06-03 to 2018-03-27.
    DHI Stocker Initialized. Data covers 1992-06-05 to 2018-03-27.
    CAB Stocker Initialized. Data covers 2004-07-06 to 2017-09-25.
    EMCI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    KW Stocker Initialized. Data covers 2007-12-03 to 2018-03-27.
    WSR Stocker Initialized. Data covers 2010-08-26 to 2018-03-27.
    MOG_A Stocker Initialized. Data covers 1992-02-21 to 2018-03-27.
    SYMC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CVG Stocker Initialized. Data covers 1998-08-13 to 2018-03-27.
    CPA Stocker Initialized. Data covers 2005-12-15 to 2018-03-27.
    WIX Stocker Initialized. Data covers 2013-11-06 to 2018-03-27.
    Y Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    AMBC Stocker Initialized. Data covers 2013-05-01 to 2018-03-27.
    MMSI Stocker Initialized. Data covers 1992-02-26 to 2018-03-27.
    KCLI Stocker Initialized. Data covers 1995-08-18 to 2015-12-31.
    MCD Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    ROC Stocker Initialized. Data covers 2005-08-17 to 2015-01-12.
    TROW Stocker Initialized. Data covers 1989-09-13 to 2018-03-27.
    CHE Stocker Initialized. Data covers 1973-05-03 to 2018-03-27.
    DDD Stocker Initialized. Data covers 1990-11-05 to 2018-03-27.
    ACHC Stocker Initialized. Data covers 1994-03-04 to 2018-03-27.
    LPSN Stocker Initialized. Data covers 2000-04-07 to 2018-03-27.
    GPI Stocker Initialized. Data covers 1997-10-30 to 2018-03-27.
    LCNB Stocker Initialized. Data covers 1999-10-26 to 2018-03-27.
    TCS Stocker Initialized. Data covers 2013-11-01 to 2018-03-27.
    GEVA Stocker Initialized. Data covers 2011-07-01 to 2015-06-22.
    BSFT Stocker Initialized. Data covers 2010-06-16 to 2018-02-02.
    TUMI Stocker Initialized. Data covers 2012-04-19 to 2016-08-01.
    COO Stocker Initialized. Data covers 1983-12-30 to 2018-03-27.
    DOOR Stocker Initialized. Data covers 2009-07-24 to 2018-03-27.
    DLTR Stocker Initialized. Data covers 1995-03-09 to 2018-03-27.
    NOV Stocker Initialized. Data covers 1996-10-29 to 2018-03-27.
    ATMI Stocker Initialized. Data covers 1993-11-23 to 2014-04-30.
    PBY Stocker Initialized. Data covers 1987-12-30 to 2016-02-03.
    QCOR Stocker Initialized. Data covers 1993-03-04 to 2014-08-14.
    AGIO Stocker Initialized. Data covers 2013-07-24 to 2018-03-27.
    XNPT Stocker Initialized. Data covers 2005-06-02 to 2016-07-05.
    ANDE Stocker Initialized. Data covers 1996-02-20 to 2018-03-27.
    IBOC Stocker Initialized. Data covers 1996-05-30 to 2018-03-27.
    HELI Stocker Initialized. Data covers 2014-01-17 to 2016-02-01.
    PACR Stocker Initialized. Data covers 2002-06-21 to 2014-04-01.
    GLDD Stocker Initialized. Data covers 2006-12-27 to 2018-03-27.
    KERX Stocker Initialized. Data covers 2000-07-28 to 2018-03-27.
    AES Stocker Initialized. Data covers 1991-06-26 to 2018-03-27.
    BBRG Stocker Initialized. Data covers 2010-10-21 to 2018-03-27.
    REV Stocker Initialized. Data covers 1996-02-29 to 2018-03-27.
    ALG Stocker Initialized. Data covers 1993-03-19 to 2018-03-27.
    DNKN Stocker Initialized. Data covers 2011-07-27 to 2018-03-27.
    UIL Stocker Initialized. Data covers 1987-08-31 to 2015-12-16.
    BLKB Stocker Initialized. Data covers 2004-07-26 to 2018-03-27.
    ULTR Stocker Initialized. Data covers 2006-10-13 to 2016-10-18.
    KOG Stocker Initialized. Data covers 2006-05-15 to 2014-12-05.
    ALGN Stocker Initialized. Data covers 2001-01-30 to 2018-03-27.
    ATO Stocker Initialized. Data covers 1983-12-28 to 2018-03-27.
    CUZ Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    TIBX Stocker Initialized. Data covers 1999-07-14 to 2014-12-05.
    WYN Stocker Initialized. Data covers 2006-07-19 to 2018-03-27.
    ATRS Stocker Initialized. Data covers 1996-10-03 to 2018-03-27.
    XOXO Stocker Initialized. Data covers 1999-12-02 to 2018-03-27.
    HEI Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    TEAR Stocker Initialized. Data covers 2004-12-09 to 2017-11-07.
    UEIC Stocker Initialized. Data covers 1993-02-12 to 2018-03-27.
    RCAP Stocker Initialized. Data covers 2013-06-05 to 2015-12-31.
    KODK Stocker Initialized. Data covers 2013-09-23 to 2018-03-27.
    NCFT Stocker Initialized. Data covers 2013-11-07 to 2015-05-11.
    NTK Stocker Initialized. Data covers 2010-06-15 to 2016-08-30.
    TOWN Stocker Initialized. Data covers 1999-05-05 to 2018-03-27.
    RAIL Stocker Initialized. Data covers 2005-04-06 to 2018-03-27.
    TECUA Stocker Initialized. Data covers 1995-08-18 to 2014-05-01.
    WIN Stocker Initialized. Data covers 2005-02-09 to 2018-03-07.
    NAV Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    TG Stocker Initialized. Data covers 1990-01-12 to 2018-03-27.
    DXM Stocker Initialized. Data covers 2013-05-01 to 2016-01-06.
    WBMD Stocker Initialized. Data covers 2005-09-29 to 2017-09-15.
    M Stocker Initialized. Data covers 1992-02-05 to 2018-03-27.
    IRDM Stocker Initialized. Data covers 2008-03-20 to 2018-03-27.
    QSII Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    NSIT Stocker Initialized. Data covers 1995-01-25 to 2018-03-27.
    STCK Stocker Initialized. Data covers 2013-08-09 to 2016-06-03.
    GRA Stocker Initialized. Data covers 1982-01-04 to 2018-03-27.
    IBKC Stocker Initialized. Data covers 1995-04-10 to 2018-03-27.
    MKC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    IVC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FBIZ Stocker Initialized. Data covers 2005-11-09 to 2018-03-27.
    EVTC Stocker Initialized. Data covers 2013-04-12 to 2018-03-27.
    EL Stocker Initialized. Data covers 1995-11-17 to 2018-03-27.
    WSTL Stocker Initialized. Data covers 1995-12-01 to 2018-03-27.
    EXLS Stocker Initialized. Data covers 2006-10-20 to 2018-03-27.
    TRXC Stocker Initialized. Data covers 1992-11-12 to 2018-03-27.
    AEIS Stocker Initialized. Data covers 1995-11-17 to 2018-03-27.
    INFO Stocker Initialized. Data covers 2017-06-02 to 2018-03-27.
    SVVC Stocker Initialized. Data covers 2011-04-28 to 2018-03-27.
    CFN Stocker Initialized. Data covers 2009-08-21 to 2015-03-16.
    PGEM Stocker Initialized. Data covers 2013-05-23 to 2018-03-27.
    NP Stocker Initialized. Data covers 2004-11-17 to 2018-03-27.
    EDMC Stocker Initialized. Data covers 2009-10-02 to 2014-11-12.
    SNBC Stocker Initialized. Data covers 1996-08-29 to 2018-01-31.
    PRK Stocker Initialized. Data covers 1991-05-08 to 2018-03-27.
    DO Stocker Initialized. Data covers 1995-10-11 to 2018-03-27.
    LNG Stocker Initialized. Data covers 1994-04-04 to 2018-03-27.
    DNDN Stocker Initialized. Data covers 2000-06-19 to 2014-11-18.
    VECO Stocker Initialized. Data covers 1994-11-29 to 2018-03-27.
    ARR Stocker Initialized. Data covers 2007-12-03 to 2018-03-27.
    CSWC Stocker Initialized. Data covers 1990-03-27 to 2018-03-27.
    IACI Stocker Initialized. Data covers 1993-01-19 to 2016-01-20.
    RHP Stocker Initialized. Data covers 1991-10-24 to 2018-03-27.
    CBS Stocker Initialized. Data covers 2005-12-05 to 2018-03-27.
    MM Stocker Initialized. Data covers 2012-03-29 to 2015-10-22.
    RKUS Stocker Initialized. Data covers 2012-11-16 to 2016-05-26.
    MDW Stocker Initialized. Data covers 2007-10-19 to 2015-06-19.
    GCA Stocker Initialized. Data covers 2005-09-23 to 2015-08-21.
    ATRO Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    BHE Stocker Initialized. Data covers 1990-06-28 to 2018-03-27.
    VSEC Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    CMG Stocker Initialized. Data covers 2006-01-26 to 2018-03-27.
    FFBH Stocker Initialized. Data covers 1996-05-06 to 2014-06-02.
    CNQR Stocker Initialized. Data covers 1998-12-16 to 2014-12-04.
    VRTU Stocker Initialized. Data covers 2007-08-03 to 2018-03-27.
    RUBI Stocker Initialized. Data covers 2014-04-02 to 2018-03-27.
    SHOO Stocker Initialized. Data covers 1993-12-13 to 2018-03-27.
    GTLS Stocker Initialized. Data covers 2006-07-26 to 2018-03-27.
    NGHC Stocker Initialized. Data covers 2014-02-20 to 2018-03-27.
    GNE Stocker Initialized. Data covers 2011-10-26 to 2018-03-27.
    HK Stocker Initialized. Data covers 2004-06-16 to 2018-03-27.
    CL Stocker Initialized. Data covers 1977-01-03 to 2018-03-27.
    COB Stocker Initialized. Data covers 1996-11-15 to 2016-10-25.
    ZMH Stocker Initialized. Data covers 2001-07-25 to 2015-06-26.
    DORM Stocker Initialized. Data covers 1991-03-12 to 2018-03-27.
    VTSS Stocker Initialized. Data covers 1991-12-11 to 2015-04-27.
    HOG Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    CWT Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    L Stocker Initialized. Data covers 1987-07-10 to 2018-03-27.
    AMRE Stocker Initialized. Data covers 2012-07-27 to 2015-02-18.
    FOLD Stocker Initialized. Data covers 2007-05-31 to 2018-03-27.
    SAH Stocker Initialized. Data covers 1997-11-12 to 2018-03-27.
    PPL Stocker Initialized. Data covers 1985-04-08 to 2018-03-27.
    OHRP Stocker Initialized. Data covers 2007-05-01 to 2018-03-27.
    WCC Stocker Initialized. Data covers 1999-05-12 to 2018-03-27.
    HNRG Stocker Initialized. Data covers 1997-01-20 to 2018-03-27.
    ONB Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    COP Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    NYNY Stocker Initialized. Data covers 1993-11-05 to 2018-03-27.
    MPWR Stocker Initialized. Data covers 2004-11-19 to 2018-03-27.
    TEL Stocker Initialized. Data covers 2007-06-14 to 2018-03-27.
    IPHS Stocker Initialized. Data covers 2006-11-02 to 2018-03-27.
    AVAV Stocker Initialized. Data covers 2007-01-23 to 2018-03-27.
    NFX Stocker Initialized. Data covers 1993-11-12 to 2018-03-27.
    AIZ Stocker Initialized. Data covers 2004-02-05 to 2018-03-27.
    FMC Stocker Initialized. Data covers 1985-07-01 to 2018-03-27.
    MEI Stocker Initialized. Data covers 1990-03-23 to 2018-03-27.
    EFII Stocker Initialized. Data covers 1992-10-02 to 2018-03-27.
    RNDY Stocker Initialized. Data covers 2012-02-08 to 2015-12-18.
    SWY Stocker Initialized. Data covers 1990-04-26 to 2015-01-29.
    UBSI Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    FXEN Stocker Initialized. Data covers 1996-06-11 to 2015-12-31.
    RES Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    CZNC Stocker Initialized. Data covers 1996-05-30 to 2018-03-27.
    NKE Stocker Initialized. Data covers 1980-12-02 to 2018-03-27.
    GTI Stocker Initialized. Data covers 1995-08-10 to 2015-08-14.
    AAPL Stocker Initialized. Data covers 1980-12-12 to 2018-03-27.
    HRG Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    SBUX Stocker Initialized. Data covers 1992-06-26 to 2018-03-27.
    NUE Stocker Initialized. Data covers 1983-09-01 to 2018-03-27.
    TRIV Stocker Initialized. Data covers 2014-04-16 to 2016-02-03.
    FTK Stocker Initialized. Data covers 2005-07-27 to 2018-03-27.
    TXN Stocker Initialized. Data covers 1972-06-01 to 2018-03-27.
    CIFC Stocker Initialized. Data covers 2005-06-29 to 2016-11-21.
    REIS Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    MHK Stocker Initialized. Data covers 1992-04-01 to 2018-03-27.
    GALE Stocker Initialized. Data covers 2008-03-12 to 2017-12-29.
    MET Stocker Initialized. Data covers 2000-04-05 to 2018-03-27.
    FDO Stocker Initialized. Data covers 1985-02-25 to 2015-07-06.
    NLSN Stocker Initialized. Data covers 2011-01-27 to 2018-03-27.
    OPWR Stocker Initialized. Data covers 2014-04-04 to 2016-06-13.
    AVNW Stocker Initialized. Data covers 1991-02-07 to 2018-03-27.
    LGIH Stocker Initialized. Data covers 2013-11-07 to 2018-03-27.
    GEF Stocker Initialized. Data covers 1996-02-28 to 2018-03-27.
    SPRT Stocker Initialized. Data covers 2000-07-19 to 2018-03-27.
    FRNK Stocker Initialized. Data covers 2011-04-28 to 2015-01-02.
    IRBT Stocker Initialized. Data covers 2005-11-09 to 2018-03-27.
    APEI Stocker Initialized. Data covers 2007-11-09 to 2018-03-27.
    CDI Stocker Initialized. Data covers 1989-06-29 to 2017-09-12.
    REMY Stocker Initialized. Data covers 2010-03-26 to 2015-11-10.
    TFM Stocker Initialized. Data covers 2010-11-05 to 2016-04-27.
    VICR Stocker Initialized. Data covers 1991-11-27 to 2018-03-27.
    JBSS Stocker Initialized. Data covers 1991-12-04 to 2018-03-27.
    INTL Stocker Initialized. Data covers 1996-11-15 to 2018-03-27.
    HLIT Stocker Initialized. Data covers 1995-05-24 to 2018-03-27.
    MXIM Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    CLNE Stocker Initialized. Data covers 2007-05-25 to 2018-03-27.
    SZYM Stocker Initialized. Data covers 2011-05-27 to 2016-05-10.
    UTL Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    TBNK Stocker Initialized. Data covers 2009-07-13 to 2018-03-27.
    FNLC Stocker Initialized. Data covers 1999-07-14 to 2018-03-27.
    CMI Stocker Initialized. Data covers 1984-12-18 to 2018-03-27.
    KOP Stocker Initialized. Data covers 2006-02-01 to 2018-03-27.
    WAB Stocker Initialized. Data covers 1995-06-16 to 2018-03-27.
    CVA Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    VVUS Stocker Initialized. Data covers 1994-04-07 to 2018-03-27.
    EA Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    EAT Stocker Initialized. Data covers 1989-07-28 to 2018-03-27.
    NOW Stocker Initialized. Data covers 2012-06-29 to 2018-03-27.
    AVD Stocker Initialized. Data covers 1988-06-22 to 2018-03-27.
    CHFN Stocker Initialized. Data covers 2002-08-02 to 2018-03-27.
    SEMG Stocker Initialized. Data covers 2010-10-15 to 2018-03-27.
    HNT Stocker Initialized. Data covers 1991-11-07 to 2016-03-23.
    KLAC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    KOS Stocker Initialized. Data covers 2011-05-11 to 2018-03-27.
    UNP Stocker Initialized. Data covers 1980-01-02 to 2018-03-27.
    RTRX Stocker Initialized. Data covers 2012-11-08 to 2018-03-27.
    IPHI Stocker Initialized. Data covers 2010-11-12 to 2018-03-27.
    PHIIK Stocker Initialized. Data covers 1995-08-18 to 2018-03-27.
    ARCB Stocker Initialized. Data covers 1992-05-13 to 2018-03-27.
    RSE Stocker Initialized. Data covers 2011-12-28 to 2016-07-05.
    CIR Stocker Initialized. Data covers 1999-10-18 to 2018-03-27.
    SIX Stocker Initialized. Data covers 2010-05-11 to 2018-03-27.
    LNN Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    BECN Stocker Initialized. Data covers 2004-09-23 to 2018-03-27.
    HPT Stocker Initialized. Data covers 1995-08-17 to 2018-03-27.
    HCOM Stocker Initialized. Data covers 2011-01-26 to 2018-03-27.
    MRO Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    SSP Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    GK Stocker Initialized. Data covers 1990-03-26 to 2017-03-21.
    ESPR Stocker Initialized. Data covers 2013-06-26 to 2018-03-27.
    FFKT Stocker Initialized. Data covers 1993-03-04 to 2018-03-27.
    VITC Stocker Initialized. Data covers 2009-09-24 to 2014-08-19.
    FDML Stocker Initialized. Data covers 2008-01-02 to 2017-01-23.
    PSUN Stocker Initialized. Data covers 1993-03-16 to 2016-04-13.
    LPX Stocker Initialized. Data covers 1982-01-04 to 2018-03-27.
    TCAP Stocker Initialized. Data covers 2007-02-22 to 2018-03-27.
    ZLTQ Stocker Initialized. Data covers 2011-10-19 to 2017-04-27.
    ESBF Stocker Initialized. Data covers 1995-08-18 to 2015-02-10.
    PKOH Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    PCP Stocker Initialized. Data covers 1990-01-12 to 2016-01-29.
    CYN Stocker Initialized. Data covers 1990-03-26 to 2015-10-30.
    SHLD Stocker Initialized. Data covers 2003-05-01 to 2018-03-27.
    SN Stocker Initialized. Data covers 2011-12-15 to 2018-03-27.
    AAT Stocker Initialized. Data covers 2011-01-13 to 2018-03-27.
    PPG Stocker Initialized. Data covers 2017-04-26 to 2018-03-27.
    STAR Stocker Initialized. Data covers 1989-11-16 to 2018-03-27.
    GWRE Stocker Initialized. Data covers 2012-01-25 to 2018-03-27.
    PBI Stocker Initialized. Data covers 1972-06-01 to 2018-03-07.
    UAL Stocker Initialized. Data covers 2006-02-06 to 2018-03-27.
    HLX Stocker Initialized. Data covers 1997-07-01 to 2018-03-27.
    TLMR Stocker Initialized. Data covers 2014-02-12 to 2016-08-31.
    HTA Stocker Initialized. Data covers 2012-06-06 to 2018-03-27.
    BKYF Stocker Initialized. Data covers 1999-02-25 to 2015-06-19.
    TFX Stocker Initialized. Data covers 1988-02-18 to 2018-03-27.
    RLI Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    EMC Stocker Initialized. Data covers 1988-12-16 to 2016-09-06.
    THRX Stocker Initialized. Data covers 2004-10-05 to 2016-01-08.
    ARNC Stocker Initialized. Data covers 1962-01-02 to 2018-03-27.
    HON Stocker Initialized. Data covers 1970-01-02 to 2018-03-27.
    DWRE Stocker Initialized. Data covers 2012-03-15 to 2016-07-11.
    AHP Stocker Initialized. Data covers 2013-11-06 to 2018-03-27.
    INAP Stocker Initialized. Data covers 1999-09-29 to 2018-03-27.
    RAS Stocker Initialized. Data covers 1998-01-09 to 2018-03-27.
    RGDO Stocker Initialized. Data covers 2013-08-22 to 2015-05-04.
    ATML Stocker Initialized. Data covers 1991-03-19 to 2016-04-04.
    PB Stocker Initialized. Data covers 1998-11-12 to 2018-03-27.
    NUAN Stocker Initialized. Data covers 1995-12-11 to 2018-03-27.
    FLO Stocker Initialized. Data covers 1987-11-05 to 2018-03-27.
    GLPW Stocker Initialized. Data covers 2008-02-19 to 2016-03-30.
    SUPX Stocker Initialized. Data covers 1990-03-27 to 2014-04-01.
    PRLB Stocker Initialized. Data covers 2012-02-24 to 2018-03-27.
    HHC Stocker Initialized. Data covers 2010-11-05 to 2018-03-27.
    WOOF Stocker Initialized. Data covers 2001-11-28 to 2017-09-12.
    OMED Stocker Initialized. Data covers 2013-07-18 to 2018-03-27.
    OREX Stocker Initialized. Data covers 2007-04-30 to 2018-03-27.
    AHT Stocker Initialized. Data covers 2003-08-26 to 2018-03-27.
    ARCW Stocker Initialized. Data covers 1999-06-14 to 2018-03-27.
    USAK Stocker Initialized. Data covers 1992-03-20 to 2018-03-27.
    IMPV Stocker Initialized. Data covers 2011-11-09 to 2018-03-27.
    RRTS Stocker Initialized. Data covers 2010-05-13 to 2018-03-27.
    EBSB Stocker Initialized. Data covers 2008-01-23 to 2018-03-27.
    IFT Stocker Initialized. Data covers 2011-02-08 to 2015-08-31.
    HUBG Stocker Initialized. Data covers 1996-03-13 to 2018-03-27.
    ULTA Stocker Initialized. Data covers 2007-10-25 to 2018-03-27.
    CENX Stocker Initialized. Data covers 1996-03-29 to 2018-03-27.
    MDR Stocker Initialized. Data covers 1982-12-31 to 2018-03-27.
    WYNN Stocker Initialized. Data covers 2002-10-25 to 2018-03-27.
    ALX Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    CCNE Stocker Initialized. Data covers 1996-05-30 to 2018-03-27.
    MDRX Stocker Initialized. Data covers 1999-07-26 to 2018-03-27.
    CERS Stocker Initialized. Data covers 1997-01-31 to 2018-03-27.
    BBT Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    NAVB Stocker Initialized. Data covers 1992-11-16 to 2018-03-27.
    JLL Stocker Initialized. Data covers 1997-07-17 to 2018-03-27.
    LLL Stocker Initialized. Data covers 1998-05-19 to 2018-03-27.
    ESCA Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    GLF Stocker Initialized. Data covers 1997-05-01 to 2018-03-27.
    LZB Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    ABFS Stocker Initialized. Data covers 1992-05-13 to 2014-04-30.
    CJES Stocker Initialized. Data covers 2011-07-29 to 2016-07-20.
    IVZ Stocker Initialized. Data covers 1995-08-25 to 2018-03-27.
    NNI Stocker Initialized. Data covers 2003-12-12 to 2018-03-27.
    CECO Stocker Initialized. Data covers 1998-01-29 to 2018-03-27.
    BBOX Stocker Initialized. Data covers 1992-12-17 to 2018-03-27.
    ISIL Stocker Initialized. Data covers 2000-02-25 to 2017-02-23.
    WST Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    DLR Stocker Initialized. Data covers 2004-10-29 to 2018-03-27.
    BRO Stocker Initialized. Data covers 1992-03-03 to 2018-03-27.
    SFXE Stocker Initialized. Data covers 2013-10-09 to 2016-02-09.
    DPS Stocker Initialized. Data covers 2008-05-07 to 2018-03-27.
    DVA Stocker Initialized. Data covers 1995-10-31 to 2018-03-27.
    MGNX Stocker Initialized. Data covers 2013-10-10 to 2018-03-27.
    NAVI Stocker Initialized. Data covers 2014-04-17 to 2018-03-27.
    BRKS Stocker Initialized. Data covers 1995-02-02 to 2018-03-27.
    THO Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    HOT Stocker Initialized. Data covers 1987-11-05 to 2016-09-22.
    CSOD Stocker Initialized. Data covers 2011-03-17 to 2018-03-27.
    TBPH Stocker Initialized. Data covers 2014-05-16 to 2018-03-27.
    MLHR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    SGA Stocker Initialized. Data covers 1993-10-12 to 2018-03-27.
    WTFC Stocker Initialized. Data covers 1998-04-16 to 2018-03-27.
    CLNY Stocker Initialized. Data covers 2009-09-24 to 2017-01-10.
    CEMP Stocker Initialized. Data covers 2012-02-06 to 2017-11-03.
    ROK Stocker Initialized. Data covers 1981-12-31 to 2018-03-27.
    CSH Stocker Initialized. Data covers 1987-12-30 to 2016-09-01.
    NWE Stocker Initialized. Data covers 2007-12-28 to 2018-03-27.
    EVR Stocker Initialized. Data covers 2006-08-14 to 2018-03-27.
    PNW Stocker Initialized. Data covers 1984-07-19 to 2018-03-27.
    TRC Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    WSTC Stocker Initialized. Data covers 2013-03-22 to 2017-10-10.
    ZGNX Stocker Initialized. Data covers 2010-11-23 to 2018-03-27.
    EOG Stocker Initialized. Data covers 1989-10-04 to 2018-03-27.
    AKAM Stocker Initialized. Data covers 1999-10-29 to 2018-03-27.
    FST Stocker Initialized. Data covers 1990-03-26 to 2014-12-15.
    XONE Stocker Initialized. Data covers 2013-02-07 to 2018-03-27.
    TRUE Stocker Initialized. Data covers 2000-05-02 to 2018-03-27.
    RALY Stocker Initialized. Data covers 2013-04-12 to 2015-07-07.
    ISSI Stocker Initialized. Data covers 1995-02-03 to 2015-12-04.
    LUV Stocker Initialized. Data covers 1980-01-02 to 2018-03-27.
    TRMR Stocker Initialized. Data covers 2013-06-27 to 2017-09-25.
    GE Stocker Initialized. Data covers 1962-01-02 to 2018-03-27.
    AVHI Stocker Initialized. Data covers 2003-05-23 to 2018-03-27.
    RNR Stocker Initialized. Data covers 1995-07-27 to 2018-03-27.
    GY Stocker Initialized. Data covers 1981-02-02 to 2015-04-24.
    SKUL Stocker Initialized. Data covers 2011-07-20 to 2016-10-03.
    MODN Stocker Initialized. Data covers 2013-03-20 to 2018-03-27.
    CTIC Stocker Initialized. Data covers 1997-03-21 to 2018-03-27.
    FARO Stocker Initialized. Data covers 1997-09-18 to 2018-03-27.
    BLX Stocker Initialized. Data covers 1992-09-24 to 2018-03-27.
    CBEY Stocker Initialized. Data covers 2005-11-10 to 2014-07-18.
    UTHR Stocker Initialized. Data covers 1999-06-17 to 2018-03-27.
    IMKTA Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    LDOS Stocker Initialized. Data covers 2006-10-17 to 2018-03-27.
    PKT Stocker Initialized. Data covers 2003-06-26 to 2015-06-04.
    HELE Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    OMG Stocker Initialized. Data covers 1993-10-14 to 2015-10-27.
    GHL Stocker Initialized. Data covers 2004-05-06 to 2018-03-27.
    BFAM Stocker Initialized. Data covers 2013-01-25 to 2018-03-27.
    MTSC Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    SYUT Stocker Initialized. Data covers 2004-12-21 to 2017-05-15.
    ZIOP Stocker Initialized. Data covers 2005-08-24 to 2018-03-27.
    KOPN Stocker Initialized. Data covers 1992-04-15 to 2018-03-27.
    PSMT Stocker Initialized. Data covers 1997-09-02 to 2018-03-27.
    MANT Stocker Initialized. Data covers 2002-02-07 to 2018-03-27.
    NX Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    TNC Stocker Initialized. Data covers 1992-03-03 to 2018-03-27.
    FNF Stocker Initialized. Data covers 2005-10-14 to 2018-03-27.
    PRSC Stocker Initialized. Data covers 2003-08-20 to 2018-03-27.
    VVTV Stocker Initialized. Data covers 1993-04-29 to 2014-11-19.
    CREE Stocker Initialized. Data covers 1993-02-09 to 2018-03-27.
    CNDO Stocker Initialized. Data covers 2011-11-17 to 2015-04-27.
    BH Stocker Initialized. Data covers 1992-02-25 to 2018-03-27.
    KRO Stocker Initialized. Data covers 2003-12-09 to 2018-03-27.
    NMRX Stocker Initialized. Data covers 1994-03-04 to 2017-12-06.
    CBPX Stocker Initialized. Data covers 2014-02-05 to 2018-03-27.
    ARX Stocker Initialized. Data covers 2010-11-19 to 2014-09-12.
    EOPN Stocker Initialized. Data covers 2012-07-26 to 2015-03-25.
    SUI Stocker Initialized. Data covers 1993-12-09 to 2018-03-27.
    LAD Stocker Initialized. Data covers 1996-12-18 to 2018-03-27.
    CUNB Stocker Initialized. Data covers 2005-11-10 to 2017-10-20.
    PFSI Stocker Initialized. Data covers 2013-05-09 to 2018-03-27.
    INFN Stocker Initialized. Data covers 2007-06-07 to 2018-03-27.
    HAYN Stocker Initialized. Data covers 2007-03-21 to 2018-03-27.
    DV Stocker Initialized. Data covers 1991-06-28 to 2017-05-23.
    THFF Stocker Initialized. Data covers 1992-03-03 to 2018-03-27.
    AET Stocker Initialized. Data covers 1977-01-03 to 2018-03-27.
    FCSC Stocker Initialized. Data covers 2009-10-21 to 2018-03-27.
    BBY Stocker Initialized. Data covers 1985-04-19 to 2018-03-27.
    DCT Stocker Initialized. Data covers 2006-12-13 to 2018-03-27.
    UNF Stocker Initialized. Data covers 1988-01-05 to 2018-03-27.
    JCP Stocker Initialized. Data covers 1982-01-04 to 2018-03-27.
    AAWW Stocker Initialized. Data covers 2005-11-09 to 2018-03-27.
    EQU Stocker Initialized. Data covers 2000-04-25 to 2014-07-30.
    ACLS Stocker Initialized. Data covers 2000-07-11 to 2018-03-27.
    IRG Stocker Initialized. Data covers 2012-05-11 to 2017-03-13.
    SHEN Stocker Initialized. Data covers 1999-04-26 to 2018-03-27.
    ADP Stocker Initialized. Data covers 1983-04-06 to 2018-03-27.
    TTWO Stocker Initialized. Data covers 1997-04-15 to 2018-03-27.
    PFS Stocker Initialized. Data covers 2003-01-16 to 2018-03-27.
    LMIA Stocker Initialized. Data covers 1998-06-30 to 2017-06-26.
    RPXC Stocker Initialized. Data covers 2011-05-04 to 2018-03-27.
    SYBT Stocker Initialized. Data covers 1993-03-26 to 2018-03-27.
    DK Stocker Initialized. Data covers 2006-05-04 to 2018-03-27.
    SBCF Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    LNKD Stocker Initialized. Data covers 2011-05-19 to 2016-12-07.
    SGI Stocker Initialized. Data covers 2005-06-15 to 2016-10-31.
    UMBF Stocker Initialized. Data covers 1990-03-27 to 2018-03-27.
    CDR Stocker Initialized. Data covers 1993-02-19 to 2018-03-27.
    ADVS Stocker Initialized. Data covers 1995-11-16 to 2015-07-07.
    QADA Stocker Initialized. Data covers 2010-12-16 to 2018-03-27.
    BDBD Stocker Initialized. Data covers 2007-05-01 to 2016-01-15.
    KWK Stocker Initialized. Data covers 1992-03-17 to 2015-01-07.
    THG Stocker Initialized. Data covers 1995-10-11 to 2018-03-27.
    ARO Stocker Initialized. Data covers 2002-05-16 to 2016-04-21.
    URS Stocker Initialized. Data covers 1972-06-01 to 2014-10-16.
    ORBC Stocker Initialized. Data covers 2006-11-06 to 2018-03-27.
    HR Stocker Initialized. Data covers 1993-05-27 to 2018-03-27.
    FDX Stocker Initialized. Data covers 1978-04-12 to 2018-03-27.
    DIOD Stocker Initialized. Data covers 1992-03-17 to 2018-03-27.
    WRES Stocker Initialized. Data covers 2004-12-17 to 2016-06-07.
    CMA Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    HBCP Stocker Initialized. Data covers 2008-10-08 to 2018-03-27.
    CUDA Stocker Initialized. Data covers 2013-11-06 to 2018-02-09.
    GOLD Stocker Initialized. Data covers 2002-07-30 to 2018-03-27.
    MAT Stocker Initialized. Data covers 1982-01-04 to 2018-03-27.
    TMK Stocker Initialized. Data covers 1987-12-30 to 2018-03-27.
    LHCG Stocker Initialized. Data covers 2005-06-09 to 2018-03-27.
    SBRA Stocker Initialized. Data covers 2002-04-02 to 2018-03-27.
    ELLI Stocker Initialized. Data covers 2011-04-15 to 2018-03-27.
    RGR Stocker Initialized. Data covers 1990-03-26 to 2018-03-27.
    AMAT Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    ENS Stocker Initialized. Data covers 2004-08-02 to 2018-03-27.
    FOXF Stocker Initialized. Data covers 2013-08-08 to 2018-03-27.
    INSY Stocker Initialized. Data covers 2000-04-14 to 2018-03-27.
    BSET Stocker Initialized. Data covers 1984-09-07 to 2018-03-27.
    NSPH Stocker Initialized. Data covers 2007-11-01 to 2016-06-30.
    DAN Stocker Initialized. Data covers 2008-01-02 to 2018-03-27.
    OPY Stocker Initialized. Data covers 1993-08-16 to 2018-03-27.
    ULTI Stocker Initialized. Data covers 1998-06-17 to 2018-03-27.
    PSA Stocker Initialized. Data covers 1980-11-18 to 2018-03-27.
    


```python
agg_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>ex-dividend</th>
      <th>split ratio</th>
      <th>adj. open</th>
      <th>adj. high</th>
      <th>adj. low</th>
      <th>adj. close</th>
      <th>adj. volume</th>
      <th>ds</th>
      <th>y</th>
      <th>daily change</th>
      <th>ticker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1998-05-20</td>
      <td>15.25</td>
      <td>15.25</td>
      <td>15.00</td>
      <td>15.00</td>
      <td>21867.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.932029</td>
      <td>7.932029</td>
      <td>7.801996</td>
      <td>7.801996</td>
      <td>32800.5</td>
      <td>1998-05-20</td>
      <td>7.801996</td>
      <td>-0.130033</td>
      <td>MCBC</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1998-05-21</td>
      <td>15.25</td>
      <td>15.25</td>
      <td>14.88</td>
      <td>15.00</td>
      <td>23133.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.932029</td>
      <td>7.932029</td>
      <td>7.739580</td>
      <td>7.801996</td>
      <td>34699.5</td>
      <td>1998-05-21</td>
      <td>7.801996</td>
      <td>-0.130033</td>
      <td>MCBC</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1998-05-22</td>
      <td>15.00</td>
      <td>15.25</td>
      <td>15.00</td>
      <td>15.19</td>
      <td>1467.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.801996</td>
      <td>7.932029</td>
      <td>7.801996</td>
      <td>7.900821</td>
      <td>2200.5</td>
      <td>1998-05-22</td>
      <td>7.900821</td>
      <td>0.098825</td>
      <td>MCBC</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1998-05-26</td>
      <td>15.00</td>
      <td>15.25</td>
      <td>15.00</td>
      <td>15.00</td>
      <td>10533.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.801996</td>
      <td>7.932029</td>
      <td>7.801996</td>
      <td>7.801996</td>
      <td>15799.5</td>
      <td>1998-05-26</td>
      <td>7.801996</td>
      <td>0.000000</td>
      <td>MCBC</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1998-05-27</td>
      <td>15.25</td>
      <td>15.25</td>
      <td>15.00</td>
      <td>15.00</td>
      <td>9400.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.932029</td>
      <td>7.932029</td>
      <td>7.801996</td>
      <td>7.801996</td>
      <td>14100.0</td>
      <td>1998-05-27</td>
      <td>7.801996</td>
      <td>-0.130033</td>
      <td>MCBC</td>
    </tr>
  </tbody>
</table>
</div>




```python
agg_df.to_csv('./2012_2017_data.csv')
```

# Using Yahoo Finance Package


```python
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

yf.pdr_override()
```


```python
first = True
for tick in ticker_list:
    try:
        start_2018_df = yf.download(tick, start="2018-01-03", end="2018-01-03").reset_index(drop=True)
        start_2018_df = (
            start_2018_df
            .pipe(lambda x: x.assign(date=datetime.date(2018, 1, 3)))
            .pipe(lambda x: x.assign(ticker='{}'.format(tick)))
        )
        end_2018_df = yf.download(tick, start="2018-12-29", end="2018-12-29").reset_index(drop=True)
        end_2018_df = (
            end_2018_df
            .pipe(lambda x: x.assign(date=datetime.date(2018, 12, 29)))
            .pipe(lambda x: x.assign(ticker='{}'.format(tick)))
        )
    except:
        ValueError
    if first is True:
        df_2018 = pd.concat([start_2018_df, end_2018_df], join='outer', axis=0)
        first = False
    else:
        intermediate_df = pd.concat([start_2018_df, end_2018_df], join='outer', axis=0)
        df_2018 = pd.concat([df_2018, intermediate_df], join='outer', axis=0)
```

    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    [*********************100%***********************]  1 of 1 downloaded
    


```python
df_2018.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
      <th>date</th>
      <th>ticker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>26.450001</td>
      <td>27.10</td>
      <td>26.34</td>
      <td>27.030001</td>
      <td>27.030001</td>
      <td>275200</td>
      <td>2018-01-03</td>
      <td>PRO</td>
    </tr>
    <tr>
      <th>0</th>
      <td>31.160000</td>
      <td>31.16</td>
      <td>30.00</td>
      <td>30.780001</td>
      <td>30.780001</td>
      <td>168000</td>
      <td>2018-12-29</td>
      <td>PRO</td>
    </tr>
    <tr>
      <th>0</th>
      <td>9.990000</td>
      <td>10.13</td>
      <td>9.95</td>
      <td>10.000000</td>
      <td>9.775415</td>
      <td>67600</td>
      <td>2018-01-03</td>
      <td>MCBC</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_2018.to_csv('./2018_data.csv')
```
