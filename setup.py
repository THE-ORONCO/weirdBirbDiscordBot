def create_config_env_file():
    # TODO do some string sanitation
    # TODO maybe split up secret and public information for integration with other services later on
    lines = []
    token = input("your bot token: ")
    lines.append(f"TOKEN={token}")
    prefix = input("your command prefix: ")
    lines.append(f"PREFIX={prefix}")
    cogs_dir = input("the directory with all your juicy cogs")
    lines.append(f'COGS_DIR={cogs_dir}')

    file_content = "\n".join(lines)

    with open(".env", "w") as file:
        file.write(file_content)

    print("the bot should be ready now\n"
          "start it with './start.sh'")


if __name__ == '__main__':
    # TODO allow for the creation of an empty .env file with only the required variables / default values
    create_config_env_file()
