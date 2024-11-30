# 常见场景之对话问答界面
# https://www.gradio.app/docs/chatinterface

import gradio as gr
import time

def bot(message, history):
    pos = message.find('吗')
    time.sleep(1)
    if pos != -1:
        return message[:pos]
    else:
        return '嗯'

css = '''
.gradio-container { max-width:850px !important; margin:20px auto !important;}
.message { padding: 10px !important; font-size: 14px !important;}
'''

demo = gr.ChatInterface(
    css=css,
    fn=bot, 
    title = '聊天机器人',
    chatbot = gr.Chatbot(height=400, bubble_full_width=False),
    theme = gr.themes.Default(spacing_size='sm', radius_size='sm'),
    textbox=gr.Textbox(placeholder="开始跟聊天吧~", container=False, scale=7),
    examples = ['在吗', '你好吗？'],
    submit_btn = gr.Button('提交', variant='primary'),
    clear_btn = gr.Button('清空记录'),
    retry_btn = None,
    undo_btn = None,
)

if __name__ == "__main__":
    demo.launch(debug=True)