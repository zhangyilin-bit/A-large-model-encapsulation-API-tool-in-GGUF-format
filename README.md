项目结构：
main.py: FastAPI主入口，定义API路由
model_loader.py: 模型加载和推理模块
requirements.txt: 项目依赖
核心模块功能：
model_loader.py:

MODEL_PATH: 定义模型文件绝对路径
load_model(): 单例模式加载模型
使用llama_cpp_python库加载GGUF格式模型
配置模型参数：上下文长度2048，线程数4，GPU层数0
generate(): 执行模型推理
调用create_completion生成文本
支持max_tokens和temperature参数
设置停止符：换行符、句号、感叹号、问号
main.py:

定义FastAPI应用
PromptRequest: 请求体结构
prompt: 输入文本
max_tokens: 最大生成token数
temperature: 采样温度
/generate路由：
加载模型
调用generate函数生成文本
返回JSON格式结果
技术栈：
FastAPI: 高性能API框架
llama-cpp-python: GGUF模型推理库
Pydantic: 数据验证
部署方式：
使用uvicorn作为ASGI服务器
支持热重载(--reload参数)
默认运行在127.0.0.1:8000
调用示例：
请求： POST /generate { "prompt": "你好，", "max_tokens": 50 }
响应： { "response": "生成的文本内容" }
扩展性：
可添加更多模型参数控制
支持批量请求处理
可集成模型缓存机制
API使用指南：

启动服务：
确保在项目目录下运行： cd /home/ai/workspace/zyl_workspace/models/Qwen2.5-0.5B-train/api
启动服务： uvicorn main:app --reload
测试API：
使用curl命令测试：
curl -X POST "http://localhost:8000/generate" 

-H "Content-Type: application/json" 

-d '{"prompt": "你好，", "max_tokens": 50}'

使用Python requests库调用：
import requests

response = requests.post(
"http://localhost:8000/generate",
json={"prompt": "你好，", "max_tokens": 50}
)
print(response.json())

参数说明：
prompt: 输入文本（必填）
max_tokens: 最大生成token数（默认100）
temperature: 采样温度（默认0.7）
查看API文档：
访问 http://localhost:8000/docs
可查看API文档并直接测试
性能优化建议：
调整n_threads参数提升推理速度
增加n_gpu_layers参数启用GPU加速
适当调整max_tokens控制生成长度
部署建议：
使用gunicorn+uvicorn生产部署
配置反向代理（如Nginx）
设置API访问权限控制
