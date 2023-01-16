import git
from datetime import datetime, timezone, timedelta


class AnalyseRepo:

    def __init__(self, path: str):
        self.repo_path = path
        self.local_repo = None
        self.init_checks()

    def init_checks(self):
        '''
        - Raises ValueErrors if either :
        a> Provided path is not a valid git repository
        b> There are no commits on provided repository
        - Initialises local_repo variable to local repo.
        :return: None
        '''
        # Check to see whether we have a valid git repository
        if self.is_git_repo():
            self.local_repo = git.Repo(self.repo_path)
        else:
            raise ValueError("Provided path is not a valid git repository.")

        # Check to see whether we have commits on this repository - necessary for answers to part c, part d.
        if not self.commits_available():
            raise ValueError("No commits on specified git repository.")

    def commits_available(self):
        '''
        - Returns true if repository has > 0 commits.
        :return: bool
        '''
        return True if len(list(self.local_repo.iter_commits())) > 0 else False

    def is_git_repo(self) -> bool:
        '''
        - Checks if provided path is a valid git repository
        :return: bool
        '''
        try:
            _ = git.Repo(self.repo_path).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False

    def get_active_branch(self) -> str:
        # Test this out by creating a new branch
        '''
        - Returns name of the active git branch
        :return: str
        '''
        return self.local_repo.head.ref.name

    def check_for_local_changes(self) -> bool:
        '''
        - Checks for repository files that have been modified.
        - This does NOT check for non-repository / untracked files.
        :return: bool
        '''
        diff_list = self.local_repo.git.diff(name_only=True)
        return True if diff_list else False

    def head_commit_within_last_week(self) -> bool:
        '''
        - Picks up latest commit time in UTC, and time from exactly a week ago in UTC.
        - Compares the two and returns True if commit was within the week.
        :return: bool
        '''

        latest_commit = next(self.local_repo.iter_commits())
        # Both times compared in UTC
        latest_commit_time_utc = datetime.fromtimestamp(latest_commit.authored_date, timezone.utc)
        one_week_ago_time_utc = datetime.now(timezone.utc) - timedelta(days=7)
        return True if latest_commit_time_utc >= one_week_ago_time_utc else False

    def head_commit_author_name(self) -> bool:
        '''
        - Checks to see author of the head commit - returns True if author is "Rufus"
        :return: bool
        '''
        latest_commit = next(self.local_repo.iter_commits())
        return True if str(latest_commit.author) == "Rufus" else False
