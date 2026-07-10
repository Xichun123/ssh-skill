"""
配置加载示例（文档型）

本文件用于给人/AI 提供“正确范式”，避免在不同项目中手写 `ssh/scp`。
更完整的索引请看：README.md
"""


def main() -> None:
    print(
        """
最常见用法（推荐：走 CLI 入口，稳定且不依赖 Python 导入路径）：

  # 单机（密钥认证）
  python ../scripts/ssh_execute.py prod-web-01 "whoami && hostname"

  # 单跳板机
  python ../scripts/ssh_execute.py internal-server "uptime"

  # 多服务器按别名逐台执行
  python ../scripts/ssh_execute.py dev-web-01 "hostname"

配置建议：
- 使用 `~/.ssh/config` 中的 Host alias 作为统一入口
- 在注释元数据中维护 description/environment/tags/location
- 需要批量执行时，改用 `ssh_cluster.py`
"""
    )


if __name__ == "__main__":
    main()
