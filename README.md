# API使用指南

### 启动服务：

确保在项目目录下运行：

```
 cd /api
```

启动服务： 

```
uvicorn main:app --reload
```

### 测试API：

#### 1.使用curl命令测试：

```
curl -X POST "http://localhost:8000/generate" 
-H "Content-Type: application/json" 
-d '{"prompt": "你好，", "max_tokens": 50}'
```

#### 2.使用Python requests库调用：

```
import requests

response = requests.post(
"http://localhost:8000/generate",
json={"prompt": "你好，", "max_tokens": 50}
)
print(response.json())
```

### 参数说明：

**prompt**: 输入文本（必填）
**max_tokens:** 最大生成token数（默认100）
**temperature:** 采样温度（默认0.7）

### 查看API文档：

访问 http://localhost:8000/docs
可查看API文档并直接测试

### 性能优化建议：

调整n_threads参数提升推理速度
增加n_gpu_layers参数启用GPU加速
适当调整max_tokens控制生成长度

### 部署建议：

使用gunicorn+uvicorn生产部署
配置反向代理（如Nginx）
设置API访问权限控制
