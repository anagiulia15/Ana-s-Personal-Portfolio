def replace_line(file_path, target_line, replacement_line):
    try:
        # Read the contents of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Replace the target line with the replacement line
        with open(file_path, 'w') as file:
            for line in lines:
                if line.strip() == target_line:
                    file.write(replacement_line + '\n')
                    print(f"Successfully replaced '{target_line}' with '{replacement_line}' in {file_path}")
                    SystemExit(0)
                else:
                    file.write(line)

            print("The replacement could not be done")

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


replace_line("./build/landing/index.html", '<link rel="stylesheet" href="./styles.css" />',
             '<link rel="stylesheet" href="./output.css" />')
