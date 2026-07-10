"""
跳板机场景示例（文档型）

目标：把“直连/单跳/双跳/简化跳板”四类典型拓扑固定成模板，减少跑偏与试错。
"""


def main() -> None:
    print(
        """
单跳板机（推荐：在 `~/.ssh/config` 中配置 ProxyJump）：

  python ../scripts/ssh_execute.py internal-app-01 "whoami && hostname"

双跳板机：

  python ../scripts/ssh_execute.py internal-db-01 "whoami && hostname"

简化写法：

  python ../scripts/ssh_execute.py internal-cache-01 "uptime"

注意：
- 示例 alias 需要先在 `~/.ssh/config` 中配置完成。
- 跳板链路交给 `ProxyJump`，日常执行仍统一走本 skill。
"""
    )


if __name__ == "__main__":
    main()
