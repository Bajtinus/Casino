def get_latest_changes(changelog_path):
    with open(changelog_path, 'r') as file:
        lines = file.readlines()

    # Find the index of the second occurrence of a line starting with '## '
    # This is where the latest changes end
    end_index = next(i for i, line in enumerate(lines) if line.startswith('## ') and i != 0)

    # Return the latest changes as a string
    return ''.join(lines[1:end_index])

def update_readme(readme_path, latest_changes):
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    # Find the index of the line containing 'Check out the latest changes'
    index = next(i for i, line in enumerate(lines) if 'Check out the latest changes' in line)

    # Replace this line with the latest changes
    lines[index] = '## Latest Changes\n\n' + latest_changes

    # Write the updated lines back to the README file
    with open(readme_path, 'w') as file:
        file.writelines(lines)

# Get the latest changes from the CHANGELOG file
latest_changes = get_latest_changes('CHANGELOG.md')

# Update the README file with the latest changes
update_readme('README.md', latest_changes)