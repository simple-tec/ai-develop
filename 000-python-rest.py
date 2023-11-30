from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/ai', methods=['POST'])
def ai():
    # 检查请求内容是否为JSON格式
    if not request.is_json:
        return jsonify({'error': 'Invalid JSON format'}), 400

    # 获取请求中的问题
    question = request.json.get('question')

    # 根据问题生成答案
    answer = "Beijing"

    # 返回答案
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(port=8989)
