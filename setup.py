def create_config_env_file():
    """creates an env file by taking user input"""

    lines = []
    token = input("your bot token: ")
    lines.append(f"TOKEN={token}")
    prefix = input("your command prefix: ")
    lines.append(f"PREFIX={prefix}")
    cogs_dir = input("the directory with all your juicy cogs")
    lines.append(f'COGS_DIR={cogs_dir}')

    file_content = "\n".join(lines)

    with open(".env", "w", encoding="utf-8") as file:
        file.write(file_content)

    print("the bot should be ready now\n"
          "start it with './start.sh'")


if __name__ == '__main__':
    create_config_env_file()
