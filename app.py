# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    if request.method == 'POST':
        try:
            # 获取用户输入
            layers = int(request.form.get('layers', 40))
            hidden_size = int(request.form.get('hidden_size', 5120))
            precision = float(request.form.get('precision', 2))  # bytes per element
            tokens = int(request.form.get('tokens', 2000))
            concurrency = int(request.form.get('concurrency', 10))
            cache_percentage = float(request.form.get('cache_percentage', 30))  # percentage

            # 计算每个标记的KV缓存内存
            kv_per_token = layers * hidden_size * precision * 2  # key + value
            kv_per_token_kb = kv_per_token / 1024  # 转换为 KB

            # 总KV缓存内存
            total_kv = kv_per_token * tokens * concurrency
            total_kv_gb = total_kv / (1024 ** 3)  # 转换为 GB

            # 估算所需GPU内存
            gpu_memory_gb = total_kv_gb / (cache_percentage / 100)

            # 将结果格式化
            results = {
                'kv_per_token_kb': f"{kv_per_token_kb:.2f} KB",
                'total_kv_gb': f"{total_kv_gb:.2f} GB",
                'gpu_memory_gb': f"{gpu_memory_gb:.2f} GB"
            }

        except ValueError:
            results = {'error': '请输入有效的数值。'}

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)