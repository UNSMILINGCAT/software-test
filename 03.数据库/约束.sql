# 约束
/*
  6大约束：
  主键约束  Primary Key
  非空约束  Not NULL
  唯一约束  unique
  检查约束  check  mysql不支持
  外键约束  
  默认约束  default
*/
-- 主键约束  不能为NULL，且不能重复
CREATE TABLE testPK(
 id INT PRIMARY KEY
);
-- 非空
INSERT INTO testPK VALUES(NULL);
-- 唯一
INSERT INTO testPK VALUES(100);

-- 非空约束
DROP TABLE testPK;
CREATE TABLE testPK(
 id INT PRIMARY KEY,
 NAME VARCHAR(20) NOT NULL
);

INSERT INTO testpk VALUES(101,'aa');
INSERT INTO testpk VALUES(101,NULL);

-- 唯一约束
DROP TABLE testPK;
CREATE TABLE testPK(
 id INT PRIMARY KEY,
 NAME VARCHAR(20) UNIQUE
);

INSERT INTO testpk VALUES(102,'aa');
INSERT INTO testpk VALUES(103,'aa1');


-- 外键约束
CREATE TABLE score(
  sid INT PRIMARY KEY,
  SUBJECT VARCHAR(20),
  score INT,
  stuid INT
);
-- 添加外键
ALTER TABLE score ADD CONSTRAINT student_score_fk FOREIGN KEY(stuid)
REFERENCES student(stuid);

CREATE TABLE student(
  stuid INT PRIMARY KEY,
  sname VARCHAR(20)
);

DELETE FROM student WHERE stuid=1001;