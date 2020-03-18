第一題正解
SELECT CASE 
    WHEN jobpay.paytype = 2 THEN 'paytype2 '
    WHEN jobpay.paytype = 1 THEN 'paytype1 ' 
        END AS paytype_name ,COUNT(jobpay.paytype) as paycount 
    FROM jobmas,jobpay 
    WHERE jobmas.Status = 'Done' AND jobpay.paytype <> '' AND jobpay.JOBID = jobmas.JOBID 
    GROUP BY jobpay.paytype


第二題

--Original = 原始任務數/ Done = 完成任務數 / AGC_Done = AGC完成任務數--
SELECT COUNT(a.Status) AS Orignal,COUNT(b.Status)AS Done,COUNT(c.Status)AS AGC_Done 
    FROM    (SELECT* FROM jobmas m WHERE m.JOBTIME BETWEEN '2018-09-01 08:%' AND '2018-09-28 09:%')AS a 
        LEFT OUTER JOIN 
            (SELECT* FROM jobmas m WHERE m.Status = 'Done' AND m.JOBTIME BETWEEN '2018-09-01 08:%' AND '2018-09-28 09:%') AS b ON a.JOBID = b.JOBID 
        LEFT OUTER JOIN 
            (SELECT* FROM jobmas m WHERE m.Status = 'Done' AND m.Comefrom <> 'APP'AND m.JOBTIME BETWEEN '2018-09-01 08:%' AND '2018-09-28 09:%') AS c ON a.JOBID =c.JOBID




