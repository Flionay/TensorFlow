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