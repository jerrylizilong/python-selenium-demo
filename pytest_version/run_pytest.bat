set YYYYmmdd=%date:~0,4%%date:~5,2%%date:~8,2%
set hhmiss=%time:~0,2%%time:~3,2%%time:~6,2%
set reportname="test_report_%YYYYmmdd%-%hhmiss%.html"

pytest -q --html=%reportname%