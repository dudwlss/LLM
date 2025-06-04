import gradio as gr

def add(num1, num2):
    return num1 + num2

interface = gr.Interface(
    fn=add,
    inputs= ['number', 'number'],
    outputs='number',
    title="계산기",
    description="두 숫자를 입력하면 합을 계산합니다.",   
    flagging_mode="never" # flag를 하지 않음
)

interface.launch()