1、ssh-keygen：

	SSH 为 Secure Shell 的缩写，SSH 为建立在应用层基础上的安全协议。
	SSH 是目前较可靠，专为远程登录会话和其他网络服务提供安全性的协议。利用 SSH 协议可以有效防止远程管理过程中的信息泄露问题。
	从客户端来看，SSH提供两种级别的安全验证：
	ssh-keygen有很多的参数，比如这里的-t -b -C都是他的一些参数。

2、-t rsa：t是type的缩写

	-t即指定密钥的类型，密钥的类型有两种，一种是RSA，一种是DSA：
	
	RSA：RSA加密算法是一种非对称加密算法，是由三个麻省理工的牛人弄出来的，RSA是他们三个人姓的开头
	首字母组合。

	DSA：Digital Signature Algorithm (DSA)是Schnorr和ElGamal签名算法的变种。
	
	为了让两个linux机器之间使用ssh不需要用户名和密码。所以采用了数字签名RSA或者DSA来完成这个操作。ssh-keygen默认使用rsa密钥，所以不加-t rsa也行，如果你想生成dsa密钥，就需要加参数-t dsa。

3、-b 4096：b是bit的缩写

	-b 指定密钥长度。对于RSA密钥，最小要求768位，默认是2048位。
	命令中的4096指的是RSA密钥长度为4096位。
	DSA密钥必须恰好是1024位(FIPS 186-2 标准的要求)。

4、-C "邮箱"：C是comment的缩写

	-C表示要提供一个新注释，用于识别这个密钥，所以“”里面不一定非要填邮箱，可以是任何内容，邮箱仅仅是识别用的key

5、 接下来实际操作一下

1）进入用户主目录下，创建自己的密钥

![](https://i.imgur.com/wEcFKEr.png)

该命令将在用户的主目录/.ssh目录下面产生一对密钥

id_rsa     私钥

id_rsa.pub 公钥


2）进入用户主目录/.ssh目录下，查看自己的公钥

![](https://i.imgur.com/chXyBny.png)

3）然后复制自己的公钥到需要的地方就可以了