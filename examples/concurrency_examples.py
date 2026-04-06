"""
并发/批量场景示例（文档型）

建议把“批量执行/并发上传下载”收敛到固定入口，避免在不同项目里临时拼装命令。
"""


def main() -> None:
    print(
        """
多服务器（servers 字典）选择某个环境执行：

  python ../scripts/ssh_cluster.py "uptime" --environment development --parallel

如需对多台机器并发执行，请使用 ssh_cluster.py（更适合运维批量操作）：

  python ../scripts/ssh_cluster.py "df -h" --hosts "dev-web-01,dev-web-02" --parallel
"""
    )


if __name__ == "__main__":
    main()
