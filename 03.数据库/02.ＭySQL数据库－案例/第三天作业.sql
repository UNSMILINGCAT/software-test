CREATE TABLE student(
	sid INT,
	sname VARCHAR(4)
);


INSERT INTO student(sid,sname) VALUES(1,'张三');
INSERT INTO student(sid,sname) VALUES(2,'李四');
INSERT INTO student(sid,sname) VALUES(3,'王五');
INSERT INTO student(sid,sname) VALUES(4,'马六');
INSERT INTO student(sid,sname) VALUES(5,'陈七');

CREATE TABLE teacher(
	tid INT ,
	tname VARCHAR(4)
);

INSERT INTO teacher(tid,tname) VALUES(1,'包包');
INSERT INTO teacher(tid,tname) VALUES(2,'老向');
INSERT INTO teacher(tid,tname) VALUES(3,'老张');
INSERT INTO teacher(tid,tname) VALUES(4,'春哥');

CREATE TABLE course(
	cid INT,
	cname VARCHAR(10),
	tid INT COMMENT '教师编号'
); 

INSERT INTO course(cid,cname,tid) VALUES(1,'语文',1);
INSERT INTO course(cid,cname,tid) VALUES(2,'数学',2);
INSERT INTO course(cid,cname,tid) VALUES(3,'英语',3);
INSERT INTO course(cid,cname,tid) VALUES(4,'日语',4);

CREATE TABLE sc(
	sid INT ,
	cid INT ,
	score DECIMAL(4,1) COMMENT '成绩'
);


INSERT INTO sc VALUES(1,1,30);
INSERT INTO sc VALUES(1,2,60);
INSERT INTO sc VALUES(1,3,70);
INSERT INTO sc VALUES(2,1,60);
INSERT INTO sc VALUES(2,2,70);
INSERT INTO sc VALUES(3,2,30);
INSERT INTO sc VALUES(3,3,80);
INSERT INTO sc VALUES(4,1,70);
INSERT INTO sc VALUES(4,2,60);
INSERT INTO sc VALUES(4,3,80);
INSERT INTO sc VALUES(4,4,90);
INSERT INTO sc VALUES(5,1,90);
INSERT INTO sc VALUES(5,4,90);



SELECT st.sid,st.sname,COUNT(*),SUM(s.score) FROM student st JOIN sc s 
ON st.sid=s.sid 
GROUP BY sid;

/*2*/
SELECT st.sid,AVG(s.score) avs 
FROM student st 
JOIN sc s 
ON st.sid=s.sid 
GROUP BY sid 
HAVING avs>60;

/*3*/
SELECT st.sid,st.sname 
FROM student st 
JOIN sc s 
ON st.sid=s.sid 
GROUP BY st.sid 
HAVING COUNT(cid)>=3;

/*4*/
SELECT st.sname,c.cname,s.score 
FROM student st 
JOIN sc s 
ON st.sid=s.sid 
JOIN course c 
ON c.cid=s.cid 
WHERE s.cid=2 AND s.score>=60;

/*5*/
SELECT st.sname,c.cname 
FROM student st 
JOIN sc s ON st.sid=s.sid 
JOIN course c ON c.cid=s.cid 
WHERE c.cname LIKE '%语%'  
GROUP BY st.sid HAVING COUNT(c.cid)>=2;

/*6*/
SELECT * 
FROM student st 
JOIN sc s 
ON st.sid=s.sid 
WHERE s.score<60 
GROUP BY st.sid 
HAVING COUNT(*)>2;

/*7*/
SELECT * 
FROM (
	SELECT s.sid,s.score 
	FROM course c 
	JOIN sc s 
	ON c.cid=s.cid 
	WHERE c.cname='语文') yuwen 
JOIN (
	SELECT s.sid,s.score
	FROM course c 
	JOIN sc s ON c.cid=s.cid 
	WHERE c.cname='数学'
	) shuxue 
ON yuwen.sid=shuxue.sid AND yuwen.score>shuxue.score
JOIN student st 
ON st.sid=shuxue.sid;


/*8*/
SELECT * 
FROM student st 
JOIN sc s ON st.sid=s.sid JOIN course c ON s.cid= c.cid JOIN teacher t ON c.tid= t.tid WHERE t.tname  NOT LIKE '老%' GROUP BY st.sid;

/*9*/
SELECT DISTINCT st.sid,st.sname
FROM student st 
JOIN sc s 
ON st.sid=s.sid ;

/*9*/
SELECT COUNT(DISTINCT st.sid)
FROM student st
RIGHT JOIN sc
ON st.sid=sc.sid;