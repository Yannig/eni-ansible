from ansiblelint.rules import AnsibleLintRule


class SELinuxNotOnUnarchive(AnsibleLintRule):
    version_changed = '0.0.0'
    id = 'no-setype-on-unarchive'
    shortdesc = 'setype not on unarchive'
    description = 'No field ``setype`` on ``unarchive`` module'
    tags = ["unarchive"]

    def matchtask(self, task, file):
        module = task["action"]["__ansible_module__"]
        return module == "unarchive" and \
               'setype' not in task['action']
