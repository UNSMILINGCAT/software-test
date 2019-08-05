# 多表查询
-- 需求：查询所有员工的员工姓名和部门名称
/*
  笛卡尔积：
  产生的原因？没有连接条件
  解决：给上连接条件
*/
SELECT ename,dname
FROM emp,dept;

SELECT ename,dname
FROM emp,dept
WHERE emp.deptno = dept.deptno;

# 表也可以取别名   取别名主要就是简化表名
SELECT e.ename,d.dname,e.deptno
FROM emp e,dept d
WHERE e.deptno = d.deptno;


-- 合并结果集
-- 案例1：查询员工姓名和工资，以及学生的姓名和年龄
SELECT ename,sal
FROM emp
UNION ALL
SELECT sname,age
FROM stu;

/*
  UNION 与UNION ALL的区别？
  UNION合并结果集并去重，
  UNION ALL合并结果集不去重
  
  要求：被合并的两个结果：列数、列类型必须相同。
*/


-- 连接查询
/*
 内连接：
 SQL99语法：
 select 查询列表
 from 表1
 【inner】 join 表2
 on 连接条件
*/
-- 需求：查询所有员工的员工姓名和部门名称
SELECT e.ename,d.dname
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno;

-- 外连接
/*
 语法：
 select 查询列表
 from 表1
 left|right 【outer】 join 表2
 on 连接条件
*/
-- 案例2：查询没有员工的部门编号和部门名称
SELECT d.deptno,d.dname
FROM dept d
LEFT OUTER JOIN emp e
ON d.deptno = e.deptno
WHERE e.empno IS NULL;

-- 案例3：查询没有员工的部门编号和部门名称
SELECT d.deptno,d.dname
FROM emp e
RIGHT OUTER JOIN dept d
ON d.deptno = e.deptno
WHERE e.empno IS NULL;


-- 案例4：查询没有部门的员工姓名
SELECT e.ename
FROM emp e
LEFT JOIN dept d
ON e.deptno = d.deptno
WHERE d.deptno IS NULL;


-- 自然连接（了解） 一般不使用
-- 案例5：查询员工的姓名和部门编号
SELECT ename,dname
FROM emp
NATURAL JOIN dept;










