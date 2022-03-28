"""
 * Project name(项目名称)：Python生成器
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 22:13
 * Version(版本): 1.0
 * Description(描述)：
 定义一个以 yield 关键字标识返回值的函数；
调用刚刚创建的函数，即可创建一个生成器。
 """


def intNum():
    print("开始执行:", end=" ")
    for i in range(5):
        yield i
        print("继续执行:", end=" ")


if __name__ == '__main__':
    num = intNum()
    # 调用 next() 内置函数
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))

    print("--------------------")

    num = intNum()
    # 通过for循环遍历生成器
    for i in num:
        print(i)

    print()
    print("--------------------")

    num = intNum()
    print(list(num))
    num = intNum()
    print(tuple(num))

    print()
    print("--------------------")

    num = intNum()
    # 调用 __next__() 方法
    print(num.__next__())
    print(num.send(None))
    print(num.send(None))
    print(num.send("hello"))

    print("--------------------")

    num = intNum()
    # 调用 __next__() 方法
    print(num.__next__())
    print(num.__next__())
    print(num.__next__())
    # num.close()
    print(num.__next__())
    print(num.__next__())
