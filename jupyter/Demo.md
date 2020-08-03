# Jupyter Notebook 保护隐私（上锁）、直接用浏览器打开
![](https://img-blog.csdnimg.cn/20200803223420751.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNzI5ODIy,size_16,color_FFFFFF,t_70)

* Jupyter Notebook，一把尼泊尔军刀，敌无不斩，斩无不断，几乎接近完美的利器（当然了，在小橙子心中，Pychrome天下第一），哈哈哈哈

#### 备注：我使用的是：Anaconda Navigator(对与初学者来说很友善的，几乎需要的包都自带了，不需要来额外的下载)
* 官网：https://www.anaconda.com/
![](https://img-blog.csdnimg.cn/20200803223533485.png)

## 那么如何来保护隐私呢，我们需要给Jupyter Notebook,来加一把锁~

### 1、首先寻找Jupyter的配置文件
* 但这个配置文件一开始并不存在，需要手动生成。方式很简单，在命令行输入jupyter notebook --generate-config并执行，配置文件就创建好了，它的位置是在C:\Users\Administrator\.jupyter\中
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200803223620846.png)
* 打开生成的.jupyer文件夹，形式如下：
![](https://img-blog.csdnimg.cn/20200803223740516.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNzI5ODIy,size_16,color_FFFFFF,t_70)
### 2、用记事本打开配置文件jupyter_notebook_config.py
![](https://img-blog.csdnimg.cn/20200803224151803.png)

* Crtl + F组合键找到c.NotebookApp.allow_password_change元素，修改为：NotebookApp.allow_password_change=False，并且删掉前面的注释#，保存文件；
* 如果没有找的话，直接插入 NotebookApp.allow_password_change=False 该语句就OK
![](https://img-blog.csdnimg.cn/20200803224646965.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNzI5ODIy,size_16,color_FFFFFF,t_70)
### 3、输入新密码
![](https://img-blog.csdnimg.cn/20200803225029391.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNzI5ODIy,size_16,color_FFFFFF,t_70)
* 找到jupyter_notebook_config.json，并复制密码的哈希值
![](https://img-blog.csdnimg.cn/20200803225334322.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNzI5ODIy,size_16,color_FFFFFF,t_70)

### 4、再一次打开配置文件jupyter_notebook_config.py
* 插入该语句：c.NotebookApp.password~，其中粘贴一复制的哈希值，形式如图所示
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020080322575269.png)
### 5、保存重启
* 从浏览器输入：http://localhost:8888/
* 效果如下：
![](https://img-blog.csdnimg.cn/20200803230258637.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNzI5ODIy,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200803230340553.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNzI5ODIy,size_16,color_FFFFFF,t_70)
## 一般我们在运行框中，还需要把网址直接复制到浏览器中，很麻烦
* so ~
### 1、找到chrome浏览器的地址
![](https://img-blog.csdnimg.cn/20200803230948217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNzI5ODIy,size_16,color_FFFFFF,t_70)
### 2、用记事本打开配置文件jupyter_notebook_config.py
* 直接插入下列代码，保存退出
```python
# 直接用浏览器打开
import webbrowser
webbrowser.register('chrome', None, webbrowser.GenericBrowser(u'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'))
c.NotebookApp.browser = 'chrome'
```
