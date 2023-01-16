from analyser import AnalyseRepo
import sys
import os

if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise ValueError("Please provide only one argument: full repository path")

    path = sys.argv[1]

    if os.path.exists(path):

        repo_analyser = AnalyseRepo(path)

        result_string = ""
        result_string += f"active branch: {repo_analyser.get_active_branch()} \n"
        result_string += f"local changes: {repo_analyser.check_for_local_changes()} \n"
        result_string += f"recent commit: {repo_analyser.head_commit_within_last_week()} \n"
        result_string += f"blame Rufus: {repo_analyser.head_commit_author_name()} \n"

        print(result_string)

    else:
        raise ValueError("Invalid repository path.")


