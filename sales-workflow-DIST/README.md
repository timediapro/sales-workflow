# Sales Workflow - 销售需求自动汇总工作流
> 一键安装包 for OpenClaw

## 📦 分发内容

两个文件：
- `sales-workflow.skill` — Skill 安装包（推荐）
- `skills/sales-workflow/` — 完整源码

---

## 🚀 快速安装（新 OpenClaw 部署）

### 方法一：Skill 包安装（推荐）

```bash
# 在目标机器的 OpenClaw workspace 下执行
openclaw skills install /path/to/sales-workflow.skill
```

### 方法二：手动复制

```bash
# 1. 把 sales-workflow/ 目录复制到目标 workspace/skills/
cp -r sales-workflow /path/to/your/workspace/skills/

# 2. 修改权限
chmod +x /path/to/your/workspace/skills/sales-workflow/scripts/setup.sh

# 3. 运行设置脚本
bash /path/to/your/workspace/skills/sales-workflow/scripts/setup.sh
```

---

## 📋 安装后验证

```bash
# 检查 Cron 任务
openclaw cron list

# 检查智能表格
# 打开 /workspace/sales-workflow-config.json 中的 table_url
```

---

## 🔧 架构说明

```
销售人员发消息
    ↓ 企业微信群
MaxEcho 机器人（wecom）
    ↓ 实时接收
OpenClaw Agent
    ↓ 每5分钟 Cron
读取消息 → NLP解析 → 入库
    ↓
企业微信智能表格（📋销售需求汇总）
```

---

## ⚙️ 自定义修改

编辑 `skills/sales-workflow/scripts/setup.sh`：

| 参数 | 位置 | 说明 |
|------|------|------|
| CRON_INTERVAL_MS | 脚本顶部 | 轮询间隔，默认 300000ms（5分钟） |
| TABLE_NAME | 脚本 | 智能表格名称 |
| FIELDS | 阶段4 | 字段定义 |

修改后重新打包：
```bash
python3 <openclaw-dir>/skills/skill-creator/scripts/package_skill.py \
  /path/to/sales-workflow /path/to/output/
```

---

## ❓ 故障排除

**Q: 授权链接打不开？**
A: 确保在企业微信 App 内打开，不是微信

**Q: 智能表格创建失败？**
A: 检查企业微信机器人的「文档」权限是否过期

**Q: Cron 没运行？**
A: `openclaw cron list` 查看状态，确保 isolated session 可用

---

## 📄 配置文件

安装后配置写入：`/workspace/sales-workflow-config.json`

```json
{
  "docid": "dcXXX",
  "sheet_id": "q979lj",
  "table_name": "📋 销售需求汇总",
  "table_url": "https://doc.weixin.qq.com/smartsheet/...",
  "bot_id": "aibuak-...",
  "setup_at": "2026-04-18T12:00:00Z"
}
```

---

版本：v1.0 | 适用于 OpenClaw 2.x | MaxClaw Platform
