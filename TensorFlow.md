# TensorFlow 第一天

1. 深度学习和机器学习的区别

   机器学习特征提取是人工完成的

   深度学习 特征提取也是神经网络学习的一部分，特征提取是机器学习自动完成的

2. 算法代表
	* 机器学习— 朴素贝叶斯
	  
	* 深度学习— 神经网络
	
3. 应用场景

   机器学习

   深度学习  — 图像处理   自然语言处理   语音识别
## 深度学习框架对比
|   框架名   | 主语言 |       从语言       | 灵活性 | 上手难易 |      开发者      |
| :--------: | :----: | :----------------: | :----: | :------: | :--------------: |
| TensorFlow |  C++   |       Python       |   好   |    难    |      Google      |
|   Caffe    |  C++   | Cuda/python/matlab |  一般  |   中等   |      贾杨清      |
|  PyTorch   | Python |       c/c++        |   好   |   中等   |     FaceBook     |
|   Torch    |  lua   |       c/cuda       |   好   |   中等   |     FaceBook     |
|   Mxnet    |  C++   |    Cud/R/julia     |   好   |   中等   |      李沐等      |
|   Theano   | Python |      c++/cuda      |   好   |   中等   | 蒙特利尔理工学院 |

## TensorFlow 安装

1. [安装指南](https://tensorflow.google.cn/install/pip)
2. 更方便的可行的方法：用Anaconda-Navigator 图形界面安装

	* CPU 版本

    综合能力比较强

	* Gpu 版本

    术业有专攻，专做某一件事很好 

## Tensorflow 的基本结构

   ### TensorFlow First demo
  ```Python
  import tensorflow as tf

def tensorflow_demo():
    # 原生Python加法运算    
    a =2 
    b =3 
    c = a+b 
    print("common add is \n",c)
     # tensor flow 加法   
    a_t = tf.constant(2)
    b_t = tf.constant(3)
    c_t = a_t +b_t
    print("tensorflow add is \n",c_t)

    # 开启会话
    with tf.Session() as sess:
        
        c_t_value = sess.run(c_t)
        print('tensorflow add result is {}'.format(c_t_value))

if __name__ == "__main__":
    tensorflow_demo()
  ```


1. 构建图阶段

   数据和执行的步骤被描述成为图，可以理解为定义了计算流程。

   流程图： 定义了数据和操作

   ​                张量：（tensor）；操作（节点Operation）

2. 执行图阶段

   调用各方资源，将定义好的数据和操作执行起来

   

### 图的相关操作

``` python
def graph_demo():
  """
  图的演示
  """
  #方法2 查看默认图
  default_g = tf.get_default_graph()
  print("default_g: \n",default_g)
  
  
```

1. 查看默认图

   *  `tf.get_default_graph()`

   * `.graph`

2. 创建图

   1. `new_g = tf.Graph()`

      ```python 
      new_g = tf.Graph()
      with new_g.as.default():
        a_new = tf.constant(20)
        b_new = tf.constant(30)
        c_new = a_new + b_new
        print('c_new',c_new)
      ```

      