def get_latest_inflation():
    return """
        SELECT * FROM recommendation.inflation ORDER BY year DESC,
                 CASE month
                     WHEN 'JANUARY' THEN 1
                     WHEN 'FEBRUARY' THEN 2
                     WHEN 'MARCH' THEN 3
                     WHEN 'APRIL' THEN 4
                     WHEN 'MAY' THEN 5
                     WHEN 'JUNE' THEN 6
                     WHEN 'JULY' THEN 7
                     WHEN 'AUGUST' THEN 8
                     WHEN 'SEPTEMBER' THEN 9
                     WHEN 'OCTOBER' THEN 10
                     WHEN 'NOVEMBER' THEN 11
                     WHEN 'DECEMBER' THEN 12
                     ELSE 0
                 END DESC
        LIMIT 2;
    """