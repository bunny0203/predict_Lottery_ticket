# Prospectus Verification Assistant v0.1.0

这是港股英文招股书验证清单本地网页工具的完整归档版本。

因为当前环境不能直接通过 Git 凭证推送二进制 zip，所以完整 zip 已拆成 6 个 base64 分块上传：

- `prospectus_verification_app_v0.1.0.zip.b64.part01`
- `prospectus_verification_app_v0.1.0.zip.b64.part02`
- `prospectus_verification_app_v0.1.0.zip.b64.part03`
- `prospectus_verification_app_v0.1.0.zip.b64.part04`
- `prospectus_verification_app_v0.1.0.zip.b64.part05`
- `prospectus_verification_app_v0.1.0.zip.b64.part06`

## 还原方式

在本目录下运行：

```bash
cat prospectus_verification_app_v0.1.0.zip.b64.part* | base64 -d > prospectus_verification_app_v0.1.0.zip
unzip prospectus_verification_app_v0.1.0.zip
cd prospectus_verification_app
python3 -m pip install -r requirements.txt
python3 -m uvicorn main:app --reload --port 8765
```

然后打开：`http://127.0.0.1:8765`

也可以运行：

```bash
python3 restore_prospectus_verification_app.py
```

## 校验信息

- 原始 zip 文件大小：`44170` bytes
- SHA-256：`5cd29fe2dd4a9de784627a88d7e24ae8b7480f0924800066b8bf6c8389fb9ee5`

## 归档内容

本版本包括：

- 本地网页端程序
- PDF 拆句逻辑
- 逐句验证需求清单生成逻辑
- DeepSeek / Gemini / OpenAI-compatible 接口支持
- Prompt 1：英文招股书拆句判断
- Prompt 2：逐句生成中文验证需求清单
- `verification_playbook.md` 风格和规则手册
- `golden_examples.xlsx` 空模板

注意：该 GitHub 仓库是 public。不要在后续版本中上传 API Key、客户未公开资料或保密文件。