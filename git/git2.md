基础操作

1.克隆github或者码云上代码到本地,一般拉取下来的代码，当前分支都在master分支上

	git clone 分支名仓库名地址

2.创建自己的分支

	git checkout -b 你的名字
3.查看当前修改文件的状态

	git status
4.添加要上传的文件

	git add 修改后的文件
5.提交添加文件的注解

	git commit -m '注解'
6.文件到本地分支中

	git push origin 你的名字
7.合并添加上传文件和添加上传文件注解到本地分支的操作
	
	git commit -am '注解'
8.下拉远程自己分支代码到本地自己分支
	
	git pull origin 你的名字
9.代码分支合并，tag提交将自己分支代码合并到测试分支以便测试人员测试 先切换版本到dev分支

	git checkout dev
当前dev分支在合并wanghaifei分支

	git merge 你的名字
提交dev分支合并的代码到远程dev分支上

	git push origin dev
10.上线代码需要打tag，在master分支打tag 打版本v1.0.0.0
	
	git tag -a 版本号 -m '注解'
   
   提交版本v1.0.0.0

	git push origin v1.0.0.0

分支版本处理

11.删除本地分支
	
	git branch -D 你的名字
12.删除git远程分支
	
	git push origin --delete 你的名字
13.删除本地tag
	
	git tag -d v1.0.0.0
14.删除git远程tag

	git push origin --delete tag v1.0.0.0
15.查看dev分支和wanghaifei分支的不同
	
	git diff dev 你的名字

---
缓存机制，在某一个分支修改了代码，但是不想提交该分支，又想切换到另外一个分支在修改相同的代码，就需要使用stash命令


16.缓存本地修改的代码

	git stash

17.查看缓存的片段
	
	git stash list


18.还原缓存的代码

	git stash apply stash@{0}

---
查看某次提交的详情，退回代码到某一次提交

19.查看提交的日志记录

	git log

20.查看某次提交的内容

	git show commit-id
21.退回代码 回退到当前版本用HEAD表示当前版本，上一个版本是HEAD^,或者使用HEAD~1，表示上一个版本。HEAD后面是数字可以一直往大了写，只要有那么多老版本
	
	git reset --hard