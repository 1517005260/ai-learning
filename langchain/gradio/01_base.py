# Gradio

# Gradio是一个开源的Python库，用于快速构建一个简单漂亮的用户界面，以便向客户、合作者、用户或学生展示机器学习模型。

# 注意，gradio仅作调试用，正式项目还是要正经前后端的。

# 官网：https://www.gradio.app/

# pip install gradio==4.9.0

import gradio as gr

def greet(name):
    return '你好 ' + name

# demo = gr.Interface(greet, inputs='text', outputs='text')  # 简写

# 定制
demo = gr.Interface(
    fn = greet, 
    inputs = [
        gr.Text(label='姓名', value="abc", lines=5),
    ], 
    outputs=[
        gr.Text(label='输出', lines=5),
    ]
)

if __name__ == '__main__':
    demo.launch()