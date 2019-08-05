USE exam;

SELECT * FROM emp WHERE deptno=30;

SELECT ename,empno '编号',deptno  '部门编号' FROM emp WHERE job='销售员';

SELECT * FROM emp WHERE comm> sal;

SELECT * FROM emp WHERE comm>sal*60/100;

SELECT * FROM emp WHERE deptno=10 AND job='经理' OR deptno=20 AND job='销售员';

SELECT * FROM emp WHERE comm  IS NOT NULL;

SELECT * FROM emp WHERE deptno=10 AND job='经理' OR deptno=20 AND job='销售员' OR job !='经理' AND job!='销售员' AND sal>=20000;

SELECT * FROM emp WHERE comm IS NULL OR comm<1000;

SELECT * FROM emp WHERE ename LIKE '___';

SELECT * FROM emp WHERE YEAR(hiredate) BETWEEN 2000 AND 2000;

SELECT * FROM emp ORDER BY empno ASC;

SELECT * FROM emp ORDER BY sal DESC , hiredate ASC;

SELECT deptno,AVG(sal) FROM emp GROUP BY deptno;

SELECT deptno,COUNT(*) FROM emp GROUP BY deptno HAVING COUNT(*)>3;

SELECT job, MAX(sal),MIN(sal),COUNT(*) 
FROM emp 
GROUP BY job;

SELECT job,SUM(sal) total  
FROM emp 
WHERE job!='销售员' 
GROUP BY job 
HAVING total>50000 
ORDER BY total ASC;

