USE day4;

#1
SELECT Sname,Ssex,Class 
FROM student;

#2
SELECT DISTINCT depart
FROM teacher;

#3
SELECT * 
FROM student;

#4
SELECT * 
FROM score
WHERE degree>60 AND degree<80;

#5
SELECT * 
FROM score
WHERE degree=85 OR degree=86 OR degree=88;

#6
SELECT *
FROM student
WHERE class=95031 OR ssex='女';

#7
SELECT *
FROM student
ORDER BY class DESC;

#8
SELECT *
FROM score
ORDER BY cno ASC,degree DESC;

#9查询“95031”班的学生人数。
SELECT COUNT(*)
FROM student
WHERE class=95031;

#10查询Score表中的最高分的学生学号和课程号。（子查询或者排序）
SELECT *
FROM score
WHERE degree=(SELECT MAX(degree) FROM score);


#11查询每门课的平均成绩。
SELECT cname,AVG(degree) 
FROM score
JOIN course
ON score.cno=course.cno
GROUP BY score.cno;

#12
SELECT AVG(degree)
FROM score sc
JOIN student st
ON sc.sno=st.sno
WHERE cno LIKE '3%'
GROUP BY cno 
HAVING COUNT(*)>5;

#13
SELECT DISTINCT sno FROM score
WHERE degree>70 AND degree<90;

#14查询所有学生的Sname、Cno和Degree列。
SELECT sname,cno,degree
FROM student st
LEFT JOIN score s
ON st.sno=s.sno;

#15查询所有学生的Sno、Cname和Degree列。
SELECT st.sno,cname,degree
FROM student st
LEFT JOIN score s
ON st.sno=s.sno
LEFT JOIN course c
ON s.cno=c.cno;


#16查询所有学生的Sname、Cname和Degree列。
SELECT sname,cname,degree
FROM student st
LEFT JOIN score s
ON st.sno=s.sno
LEFT JOIN course c
ON s.cno=c.cno;

#17
SELECT AVG(degree)
FROM student st
LEFT JOIN score s
ON st.sno=s.sno
WHERE st.class=95031;

#19
SELECT *
FROM score 
WHERE cno='3-105' AND degree>
	(SELECT MAX(degree) 
	FROM score
	WHERE cno='3-105' AND sno=109)
	;
	
#21
SELECT *
FROM score
WHERE degree>ALL(SELECT degree FROM score WHERE sno=109 AND cno='3-105');


#22
SELECT sno,sname,sbirthday
FROM student
WHERE YEAR(sbirthday) IN (SELECT YEAR(sbirthday) 
FROM student WHERE sno=101 OR sno=108)
AND sno NOT IN (101,108);

#23
SELECT degree 
FROM score s
JOIN course c
ON s.cno=c.cno
JOIN teacher t
ON c.tno=t.tno
WHERE t.tname='张旭';

#24
SELECT * FROM teacher t
JOIN course c
ON t.tno=c.tno
WHERE c.cno IN (
	SELECT cno
	FROM score
	GROUP BY cno
	HAVING COUNT(*)>5);

#25
SELECT *
FROM student
WHERE class=95033 OR class= 95031;

#26查询存在有85分以上成绩的课程Cno。
SELECT cno
FROM score
WHERE degree>85
GROUP BY cno;

#27查询出“计算机系“教师所教课程的成绩表。
SELECT s.* FROM score s
JOIN course c
ON s.cno=c.cno
JOIN teacher t
ON c.tno=t.tno
WHERE t.depart='计算机系';

#28
SELECT tname,prof
FROM teacher
WHERE depart IN ('计算机系','电子工程系')
GROUP BY prof
HAVING COUNT(*)=1;


#29
SELECT cno,sno,degree
FROM score
WHERE cno='3-105' 
AND degree >ANY(SELECT degree FROM score WHERE cno='3-245')
ORDER BY degree DESC;

#30
SELECT cno,sno,degree
FROM score
WHERE cno='3-105'
AND degree>ALL(SELECT degree FROM score WHERE cno='3-245');

#31
SELECT sname,ssex,sbirthday FROM student
UNION
SELECT tname,tsex,tbirthday FROM teacher;


#32
SELECT sname,ssex,sbirthday FROM student WHERE ssex='女'
UNION 
SELECT tname,tsex,tbirthday FROM teacher WHERE tsex='女';

#33
SELECT s.*,avgs.av FROM score s
JOIN(
SELECT  cno,AVG(degree) av
FROM score 
GROUP BY cno) avgs
ON s.cno=avgs.cno
WHERE s.degree<avgs.av;

#34
SELECT tname,depart
FROM teacher t
JOIN course c
ON c.tno=t.tno;

#36
SELECT class
FROM student 
WHERE ssex='男'
GROUP BY class
HAVING COUNT(*)>=2;

#37
SELECT * 
FROM student
WHERE sname NOT LIKE '王%';

#38
SELECT sname,YEAR(NOW())-YEAR(sbirthday)
FROM student;

#39
SELECT MAX(sbirthday),MIN(sbirthday)
FROM student;


#40
SELECT * 
FROM student
ORDER BY class DESC,sbirthday ASC;

#41
SELECT t.*,c.cname 
FROM teacher t
JOIN course c
ON t.tno=c.tno
WHERE t.tsex='男';

#42
SELECT sno,cno,degree
FROM score
WHERE degree=(SELECT MAX(degree) FROM score);

#43
SELECT sname
FROM student
WHERE ssex=(SELECT ssex FROM student WHERE sname='李军')
AND sname!='李军';

#44
SELECT sname
FROM student s
JOIN(
SELECT ssex,class
FROM student 
WHERE sname='李军') li
ON s.class=li.class
AND s.ssex=li.ssex
WHERE sname!='李军';

#45
SELECT score.*
FROM score
JOIN course
ON score.cno=course.cno
JOIN student st
ON st.sno=score.sno
WHERE course.cname='计算机导论'
AND st.ssex='男';



