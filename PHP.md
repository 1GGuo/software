# 1.PHP简介 *本周看了一点点，还学了电工学这是能说的嘛（*
PHP是一种脚本语言
PHP文件：包含文本、HTML、JavaScript代码和 PHP 代码,以.php结尾
# 2.基本语法
## 2.1框架

    <?php
    代码段
    ?>

## 2.2注释

    //是php的单行注释
    /*是
    多行
    */

## 2.3输出
2.3.1区别：echo输出一个或多个字符串，print只输出一个字符串，echo无返回值，print返回值为1

    echo"说点什么";
    echo"<h1>这是一个标题</h1>";
    echo"$x"//输出一个变量;
    echo"$x行写的这个"//变量和字符串一起输出;
    print"只输出一个字符串";
    print"在$x学习"//变量和字符串一起输出;

echo可包含HTML标签

# 3.变量
## 3.1规则
3.1.1以$符号开始，即$X
3.1.2必须以字母或下划线作开头，只包含字母数字和下划线
3.1.3区分大小写
3.1.4无声明命令，赋值时被创建
## 3.2变量作用域
3.2.1local、global、static、parameter
*函数中访问全局变量 使用global关键字*
3.2.2全局变量存储在一个名为 $GLOBALS[index] 的数组中。 这个数组可以在函数内部访问，也可以用来更新全局变量。
    $GLOBALS['X']=...//在后面可知是超级全局变量的应用
3.2.3static:在函数完成后保留局部变量用static声明，但变量仍为局部变量

# 4.EOF
定义字符串的方法
# 4.1结构
    <<<EOF
    代码
    代码
    EOF;
    //结束独占一行且前后无空格

标记间的变量可以被正常解析，函数无法被正常解析，变量不需要符号拼接

# 5.数据类型
包括字符串、整型、浮点型、布尔型、数组、对象、空、资源类型(resource)，用var_dump() 返回数据类型
## 5.1字符串
可用""或''引用
## 5.2整型
可用十进制、十六进制（0x）、八进制（0），指定
## 5.3数组

    $x=array(1,2,3,4);

## 5.4对象
用class声明
## 5.5NULL
用于指定空值和清空变量数据
## 5.6resource
包括打开文件、数据库链接、图形画布区域等
## 5.7类型比较

    ==//只比较值，不比较类型
    ===//都比较

# 6.常量
## 6.1设置方法
用define("name","contend")函数设置

    define("GREETING","巴拉巴拉")//区分大小写
    define("GREETING","巴拉巴拉",true)//区分大小写

*常量为全局变量*

# 7.字符串变量
## 7.1字符串并置

    $x="122"
    $y="554"
    $z=$x.$y

## 7.2获取长度

    strlen()

## 7.3文本查找

    strpos(x,y)//在x中寻找y，返回值为第一个匹配的字符的位置
## 7.4其余字符串相关函数
见(https://www.runoob.com/php/php-ref-string.html)

# 8.运算符
基本运算符与c++用法一致
组合比较符：$x<=>$y//x大返回值为1，相等为0，小于为-1
[其余符号以及运算顺序见](https://www.runoob.com/php/php-operators.html)

# 9.数组
## 9.1获取长度

    count()

## 9.2关联数组

    $a=array("x"=>"111","y"=>"222");//x、y为指定的键
    echo "x is".$a['x']." years old";

## 9.3遍历
9.3.1常规数组：用for循环用法与c++中相同
9.3.2关联数组：可用foreach循环
有两种语法：

    foreach($array1 as $x=>$x_value)
    {

    }；

    foreach($array1 as $key)
    {

    }；

## 9.4数组排序

    sort()//对数组升序排列
    rsort()//对数组降序排列
    asort()//根据关联数组的 值，升序排列
    ksort()//根据键升序排序
    arsort()//同上三，降序排序
    krsort()//同上四，降序排序

## 9.5超级全局变量（超级玛丽）

    $GLOBAL[]//引用全局部变量，键的名字为变量名
    $_SERVER//包含了头信息、路径、脚本位置等信息

    echo $_SERVER['PHP_SELF'];//当前执行脚本的文件名
    echo $_SERVER['SERVER_NAME'];//服务器的主机名
    echo $_SERVER['HTTP_HOST'];//请求头中HOST:的内容
    echo $_SERVER['HTTP_REFERER'];//一般为引导用户到前一页的地址，但也可能为其他信息，可信度较低
    echo $_SERVER['HTTP_USER_AGENT'];//
    echo $_SERVER['SCRIPT_NAME'];//脚本路径

    $_PEQUEST//学到这里，发现HTML学的还是太浅了，下次接着学
    $_POST[]
    $_GET[]
    $_FILES[]
    $_ENV[]
    $_COOKIE[]
    $_SESSION[]

