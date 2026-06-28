# STELLAR Login - 银河粒子登录系统

> 一个基于 Three.js 3D 粒子系统的炫酷登录界面，以螺旋星系为背景，支持鼠标拖拽旋转、滚轮缩放等交互。

---

## 效果预览

- **50,000 颗 3D 粒子**构成螺旋星系，蓝色为主、白色点缀
- **鼠标拖拽**任意旋转视角
- **滚轮缩放**拉近拉远
- **自动旋转**，松手后恢复
- 极简英文登录界面
- 右上角品牌标识

---

## 技术栈

| 技术 | 用途 |
|---|---|
| **Three.js** | 3D 粒子渲染引擎 (r160, ES Module) |
| **Python** | HTTP 后端服务 (3.12+, 标准库) |
| **HTML5 + CSS3** | 页面结构 + 毛玻璃效果 + 动画 |
| **JavaScript (ES Module)** | 前端交互逻辑 |
| **Inter Font** | 英文字体 (Google Fonts) |
| **jsdelivr CDN** | Three.js 库分发 |

---

## 项目结构

`
AI_FastApi_Test/
├── server.py              # Python HTTP 后端（零外部依赖）
├── static/
│   └── index.html         # 前端登录页面
├── README.md              # 本文档
├── .env                   # 环境变量
└── pyproject.toml         # Python 配置
`

---

## 快速启动

### 1. 运行后端

`ash
cd AI_FastApi_Test
python server.py
`

### 2. 打开浏览器

访问 **http://127.0.0.1:3000**

### 3. 登录

| 用户名 | 密码 |
|---|---|
| liuchuan | lc112233 |

---

## 交互说明

| 操作 | 效果 |
|---|---|
| **鼠标拖拽** | 任意角度旋转银河 |
| **滚轮向上** | 镜头拉近，粒子视觉变大 |
| **滚轮向下** | 镜头拉远，粒子视觉变小 |
| **松手** | 2 秒后恢复自动旋转 |
| **Enter / Sign in** | 提交登录 |

---

## 粒子系统

- **粒子数量**: 50,000
- **旋臂数量**: 3 条
- **颜色**: 蓝色约 92% + 白色约 8%
- **运动**: 每颗粒子独立沿轨道自转
- **背景星**: 5,000 颗
- **渲染**: Three.js PointsMaterial + AdditiveBlending

---

## API 接口

### POST /api/login

`json
// 请求
{ "username": "liuchuan", "password": "lc02514" }

// 成功
{ "success": true, "message": "登录成功", "token": "test-token-liuchuan-2026" }

// 失败
{ "success": false, "message": "用户名或密码错误" }
`

---

## 依赖

- **前端**: Three.js (jsdelivr CDN) + Inter Font (Google Fonts)
- **后端**: Python 标准库，零第三方依赖

---

## 后续规划

- 接入 AI 大模型 API 测试接口
- 更多粒子效果切换
- JWT 身份验证
