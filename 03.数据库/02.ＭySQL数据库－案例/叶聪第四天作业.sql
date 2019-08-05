#1.查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。
SELECT d.*,COUNT(*)
FROM dept d
JOIN emp e
ON d.deptno=e.deptno
GROUP BY d.deptno;

#2.列出薪金比关羽高的所有员工。
SELECT *
FROM emp
WHERE ename!='关羽' AND sal>(SELECT sal FROM emp WHERE ename='关羽');

#3列出所有员工的姓名及其直接上级的姓名。
SELECT e.ename,e.mgr,m.empno,m.ename
FROM emp e
LEFT JOIN emp m
ON e.mgr=m.empno;

#4列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
SELECT e.empno,e.ename,d.dname,e.mgr,e.hiredate,m.hiredate,m.empno,m.ename
FROM emp e
LEFT JOIN emp m
ON e.mgr=m.empno
LEFT JOIN dept d
ON e.deptno=d.deptno
WHERE e.hiredate<m.hiredate;

#5列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
SELECT d.dname,e.*
FROM dept d
LEFT JOIN emp e
ON d.deptno=e.deptno;

#6列出所有文员的姓名及其部门名称，部门的人数。
SELECT e.ename,de.dname,de.coun
FROM emp e
LEFT JOIN 
(
	SELECT d.dname, e.deptno,COUNT(*) coun
	FROM emp e
	JOIN dept d
	ON e.deptno=d.deptno
	GROUP BY e.deptno) de
ON e.deptno=de.deptno
WHERE e.job='文员';


#7列出最低薪金大于15000的各种工作及从事此工作的员工人数。
SELECT * ,COUNT(*)
FROM emp
GROUP BY job
HAVING MIN(sal+IFNULL(comm,0))>15000;

#8列出在销售部工作的员工的姓名，假定不知道销售部的部门编号。
SELECT *
FROM emp e
JOIN dept d
ON e.deptno=d.deptno
WHERE d.dname='销售部';

#9列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
SELECT emp.*,dept.dname,ep.ename,sg.grade
FROM emp
JOIN dept
ON emp.deptno=dept.deptno
LEFT JOIN emp ep
ON emp.mgr=ep.empno
JOIN salgrade sg
ON emp.sal BETWEEN sg.losal AND sg.hisal
WHERE (emp.sal+IFNULL(emp.comm,0))>(SELECT AVG(sal+IFNULL(comm,0)) FROM emp);

SELECT t1.ename , dname , t2.ename mgr,grade 
FROM emp t1
JOIN emp t2
ON t1.mgr=t2.empno
JOIN dept t3
ON t1.deptno=t3.deptno
JOIN salgrade
ON t1.sal BETWEEN losal AND  hisal
WHERE t1.sal>(SELECT AVG(sal) FROM emp);

#10列出与庞统从事相同工作的所有员工及部门名称。
SELECT *
FROM emp
JOIN dept
ON emp.deptno=dept.deptno
JOIN (SELECT deptno,job FROM emp WHERE ename='庞统') pan
WHERE emp.deptno=pan.deptno AND emp.job=pan.job AND ename!='庞统';

#11
SELECT *
FROM emp
WHERE sal>ALL(SELECT sal FROM emp WHERE deptno=30);


#12
SELECT dept.dname, COUNT(emp.ename),AVG(sal)
FROM dept
LEFT JOIN emp
ON dept.deptno=emp.deptno
GROUP BY dept.deptno;







