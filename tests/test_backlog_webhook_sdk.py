import pytest

from backlog_webhook_sdk import __version__
from backlog_webhook_sdk.webhook import WebhookApp


def test_version():
    assert __version__ == "0.1.0"


class TestWebhookApp:
    @pytest.fixture
    def app(self):
        app = WebhookApp()
        app.create_issue(lambda: None)
        app.update_issue(lambda: None)
        app.add_comment(lambda: None)
        app.delete_issue(lambda: None)
        app.create_wiki(lambda: None)
        app.update_wiki(lambda: None)
        app.delete_wiki(lambda: None)
        app.commit_subversion(lambda: None)
        app.push_git(lambda: None)
        app.create_git(lambda: None)
        app.bulk_update_issue(lambda: None)
        app.join_project(lambda: None)
        app.leave_project(lambda: None)
        app.create_pull_request(lambda: None)
        app.update_pull_request(lambda: None)
        app.comment_pull_request(lambda: None)
        return app

    def test_create_issue(self, app: WebhookApp):
        event = {
            "created": "2017-07-19T11:02:22Z",
            "project": {
                "archived": False,
                "projectKey": "TEST",
                "name": "TestProject",
                "chartEnabled": False,
                "id": 100,
                "subtaskingEnabled": False,
            },
            "id": 10,
            "type": 1,
            "content": {
                "summary": "test issue",
                "key_id": 100,
                "customFields": [],
                "dueDate": "2017-07-19",
                "description": "test description",
                "priority": {
                    "name": "",
                    "id": None,
                },
                "resolution": {
                    "name": "",
                    "id": None,
                },
                "actualHours": None,
                "issueType": {
                    "color": "null",
                    "name": "Bug",
                    "displayOrder": None,
                    "id": 400,
                    "projectId": None,
                },
                "milestone": [
                    {
                        "archived": "false",
                        "releaseDueDate": "null",
                        "name": "prototype release",
                        "displayOrder": None,
                        "description": "",
                        "id": None,
                        "projectId": None,
                        "startDate": "null",
                    }
                ],
                "versions": [
                    {
                        "archived": "false",
                        "releaseDueDate": "null",
                        "name": "Version0.1",
                        "displayOrder": None,
                        "description": "",
                        "id": None,
                        "projectId": None,
                        "startDate": "null",
                    }
                ],
                "parentIssueId": None,
                "estimatedHours": None,
                "id": 100,
                "assignee": None,
                "category": [
                    {
                        "name": "Category1",
                        "displayOrder": None,
                        "id": None,
                    },
                    {
                        "name": "Category2",
                        "displayOrder": None,
                        "id": None,
                    },
                ],
                "startDate": "",
                "status": {"name": "In Progress", "id": 2},
            },
            "notifications": [],
            "createdUser": {
                "nulabAccount": None,
                "name": "John Doe",
                "mailAddress": None,
                "id": 103640,
                "roleType": 1,
                "userId": None,
            },
        }
        app.handle(event)

    def test_update_issue(self, app):
        event = {
            "created": "2017-07-19T11:45:58Z",
            "project": {
                "archived": False,
                "projectKey": "TEST",
                "name": "TestProject",
                "chartEnabled": False,
                "id": 100,
                "subtaskingEnabled": False,
            },
            "id": 10,
            "type": 2,
            "content": {
                "summary": "test issue",
                "key_id": 100,
                "changes": [
                    {
                        "field": "priority",
                        "old_value": "",
                        "type": "standard",
                        "new_value": "",
                    },
                    {
                        "field": "status",
                        "old_value": "1",
                        "new_value": "2",
                    },
                    {
                        "field": "description",
                        "old_value": "old statement",
                        "new_value": "new statement",
                    },
                ],
                "description": "test description",
                "comment": {
                    "id": 200,
                    "content": "test",
                },
                "id": 100,
            },
            "notifications": [],
            "createdUser": {
                "nulabAccount": None,
                "name": "John Due",
                "mailAddress": None,
                "id": 103640,
                "roleType": 1,
                "userId": None,
            },
        }
        app.handle(event)

    def test_update_issue_with_shared_files(self, app):
        event = {
            "created": "2017-07-19T11:45:58Z",
            "project": {
                "archived": False,
                "projectKey": "TEST",
                "name": "TestProject",
                "chartEnabled": False,
                "id": 100,
                "subtaskingEnabled": False,
            },
            "id": 10,
            "type": 2,
            "content": {
                "summary": "test issue",
                "key_id": 100,
                "changes": [],
                "description": "test description",
                "shared_files": [
                    {
                        "size": 100,
                        "name": "test.png",
                        "id": 999,
                        "dir": "/test",
                    }
                ],
                "comment": None,
                "id": 100,
            },
            "notifications": [],
            "createdUser": {
                "nulabAccount": None,
                "name": "John Due",
                "mailAddress": None,
                "id": 103640,
                "roleType": 1,
                "userId": None,
            },
        }
        app.handle(event)

    def test_add_comment(self, app):
        event = {
            "created": "2017-07-19T11:50:16Z",
            "project": {
                "archived": False,
                "projectKey": "TEST",
                "name": "TestProject",
                "chartEnabled": False,
                "id": 100,
                "subtaskingEnabled": False,
            },
            "id": 10,
            "type": 3,
            "content": {
                "summary": "test issue",
                "key_id": 100,
                "description": "test description",
                "comment": {
                    "id": 200,
                    "content": "test comment",
                },
                "id": 100,
            },
            "notifications": [],
            "createdUser": {
                "nulabAccount": None,
                "name": "John Due",
                "mailAddress": None,
                "id": 103640,
                "roleType": 1,
                "userId": None,
            },
        }
        app.handle(event)

    def test_delete_issue(self, app):
        event = {
            "created": "2017-07-19T11:55:35Z",
            "project": {
                "archived": False,
                "projectKey": "TEST",
                "name": "TestProject",
                "chartEnabled": False,
                "id": 100,
                "subtaskingEnabled": False,
            },
            "id": 10,
            "type": 4,
            "content": {
                "key_id": 100,
                "id": 100,
            },
            "notifications": [],
            "createdUser": {
                "nulabAccount": None,
                "name": "John Due",
                "mailAddress": None,
                "id": 103640,
                "roleType": 1,
                "userId": None,
            },
        }
        app.handle(event)

    def test_create_wiki(self, app):
        event = {
            "created": "2017-07-19T12:00:42Z",
            "project": {
                "archived": False,
                "projectKey": "TEST",
                "name": "TestProject",
                "chartEnabled": False,
                "id": 100,
                "subtaskingEnabled": False,
            },
            "id": 10,
            "type": 5,
            "content": {
                "name": "test wiki",
                "id": 100,
                "content": "test content",
            },
            "notifications": [],
            "createdUser": {
                "nulabAccount": None,
                "name": "John Due",
                "mailAddress": None,
                "id": 103640,
                "roleType": 1,
                "userId": None,
            },
        }
        app.handle(event)

    def test_update_wiki(self, app):
        event = {
            "created": "2017-07-19T12:02:57Z",
            "project": {
                "archived": False,
                "projectKey": "TEST",
                "name": "TestProject",
                "chartEnabled": False,
                "id": 100,
                "subtaskingEnabled": False,
            },
            "id": 10,
            "type": 6,
            "content": {
                "name": "test wiki",
                "diff": "1c1\n<test content---\n>test",
                "id": 100,
                "version": 3,
                "content": "test content",
            },
            "notifications": [],
            "createdUser": {
                "nulabAccount": None,
                "name": "John Due",
                "mailAddress": None,
                "id": 103640,
                "roleType": 1,
                "userId": None,
            },
        }
        app.handle(event)

    def test_delete_wiki(self, app):
        event = {
            "created": "2017-07-19T12:05:24Z",
            "project": {
                "archived": False,
                "projectKey": "TEST",
                "name": "TestProject",
                "chartEnabled": False,
                "id": 100,
                "subtaskingEnabled": False,
            },
            "id": 10,
            "type": 7,
            "content": {
                "name": "test wiki",
                "id": 100,
                "content": "test content",
            },
            "notifications": [],
            "createdUser": {
                "nulabAccount": None,
                "name": "John Due",
                "mailAddress": None,
                "id": 103640,
                "roleType": 1,
                "userId": None,
            },
        }
        app.handle(event)

    def test_commit_subversion(self, app):
        event = {
            "created": "2017-07-19T12:07:35Z",
            "project": {
                "archived": False,
                "projectKey": "TEST",
                "name": "TestProject",
                "chartEnabled": False,
                "id": 100,
                "subtaskingEnabled": False,
            },
            "id": 10,
            "type": 11,
            "content": {
                "rev": 100,
                "comment": "test commit",
            },
            "notifications": [],
            "createdUser": {
                "nulabAccount": None,
                "name": "John Due",
                "mailAddress": None,
                "id": 103640,
                "roleType": 1,
                "userId": None,
            },
        }
        app.handle(event)

    def test_push_git(self, app):
        event = {
            "project": {
                "archived": False,
                "name": "TestProject",
                "chartEnabled": False,
                "subtaskingEnabled": False,
                "id": 100,
                "projectKey": "TEST",
            },
            "created": "2017-07-20T16:10:04Z",
            "content": {
                "revision_count": 1,
                "change_type": "update",
                "repository": {
                    "name": "app",
                    "id": 3,
                },
                "revision_type": "commit",
                "ref": "refs/heads/test",
                "revisions": [
                    {
                        "comment": "test",
                        "rev": "e1cf1103242ea1ce59382ac2e2ab4de43751524d",
                    }
                ],
            },
            "notifications": [],
            "createdUser": {
                "roleType": 1,
                "name": "John Due",
                "userId": None,
                "nulabAccount": None,
                "mailAddress": None,
                "id": 103640,
            },
            "type": 12,
            "id": 10,
        }
        app.handle(event)

    def test_create_git(self, app):
        event = {
            "project": {
                "archived": False,
                "name": "TestProject",
                "chartEnabled": False,
                "subtaskingEnabled": False,
                "id": 100,
                "projectKey": "TEST",
            },
            "created": "2017-07-20T16:10:09Z",
            "content": {
                "repository": {
                    "description": "description",
                    "id": 100,
                    "name": "test",
                },
            },
            "notifications": [],
            "createdUser": {
                "roleType": 1,
                "name": "John Due",
                "userId": None,
                "nulabAccount": None,
                "mailAddress": None,
                "id": 103640,
            },
            "type": 13,
            "id": 10,
        }
        app.handle(event)

    def test_bulk_update_issue(self, app):
        event = {
            "project": {
                "archived": False,
                "name": "TestProject",
                "chartEnabled": False,
                "subtaskingEnabled": False,
                "id": 100,
                "projectKey": "TEST",
            },
            "created": "2017-07-20T16:09:19Z",
            "content": {
                "link": [
                    {
                        "key_id": "100",
                        "id": "100",
                        "title": "test issue1",
                    },
                    {
                        "key_id": "101",
                        "id": "101",
                        "title": "test issue2",
                    },
                ],
                "changes": [
                    {
                        "field": "priority",
                        "type": "standard",
                        "new_value": "高",
                    }
                ],
                "tx_id": "200",
            },
            "notifications": [],
            "createdUser": {
                "roleType": 1,
                "name": "John Due",
                "userId": None,
                "nulabAccount": None,
                "mailAddress": None,
                "id": 103640,
            },
            "type": 14,
            "id": 10,
        }
        app.handle(event)

    def test_join_project(self, app):
        event = {
            "project": {
                "archived": False,
                "name": "TestProject",
                "chartEnabled": False,
                "subtaskingEnabled": False,
                "id": 100,
                "projectKey": "TEST",
            },
            "created": "2017-07-20T16:10:13Z",
            "content": {
                "comment": "",
                "users": [
                    {
                        "id": 100,
                        "name": "test user",
                        "nulabAccount": {
                            "nulabId": "snGjFs8agNSJeI4ZdeiVXsTiKJd0jPJAoD60apGa0VS8RPspt4",  # noqa
                            "name": "matsu ( Yusuke Matsuura )",
                            "uniqueId": "matsuzj",
                        },
                    }
                ],
            },
            "notifications": [],
            "createdUser": {
                "roleType": 1,
                "name": "John Due",
                "userId": None,
                "nulabAccount": None,
                "mailAddress": None,
                "id": 103640,
            },
            "type": 15,
            "id": 10,
        }
        app.handle(event)

    def test_leave_project(self, app):
        event = {
            "project": {
                "archived": False,
                "name": "TestProject",
                "chartEnabled": False,
                "subtaskingEnabled": False,
                "id": 100,
                "projectKey": "TEST",
            },
            "created": "2017-07-20T16:10:18Z",
            "content": {
                "users": [
                    {
                        "id": 100,
                        "name": "test user",
                        "nulabAccount": {
                            "nulabId": "snGjFs8agNSJeI4ZdeiVXsTiKJd0jPJAoD60apGa0VS8RPspt4",  # noqa
                            "name": "matsu ( Yusuke Matsuura )",
                            "uniqueId": "matsuzj",
                        },
                    }
                ],
            },
            "notifications": [],
            "createdUser": {
                "roleType": 1,
                "name": "John Due",
                "userId": None,
                "nulabAccount": None,
                "mailAddress": None,
                "id": 103640,
            },
            "type": 16,
            "id": 10,
        }
        app.handle(event)

    def test_create_pull_request(self, app):
        event = {
            "project": {
                "archived": False,
                "name": "TestProject",
                "chartEnabled": False,
                "subtaskingEnabled": False,
                "id": 100,
                "projectKey": "TEST",
            },
            "created": "2017-07-20T16:10:23Z",
            "content": {
                "comment": None,
                "description": "test description",
                "repository": {
                    "description": "test description",
                    "id": 100,
                    "name": "test repository",
                },
                "changes": [],
                "number": 100,
                "summary": "test pull request",
                "assignee": {
                    "name": "test",
                    "id": 100000,
                    "roleType": 1,
                    "lang": None,
                    "userId": "test",
                },
                "base": "master",
                "branch": "feature",
                "diff": None,
                "issue": {
                    "summary": "summary",
                    "key_id": 100,
                    "description": "description",
                    "id": 100000,
                },
                "id": 100,
            },
            "notifications": [],
            "createdUser": {
                "roleType": 1,
                "name": "John Due",
                "userId": None,
                "nulabAccount": None,
                "mailAddress": None,
                "id": 103640,
            },
            "type": 18,
            "id": 10,
        }
        app.handle(event)

    def test_update_pull_request(self, app):
        event = {
            "project": {
                "archived": False,
                "name": "TestProject",
                "chartEnabled": False,
                "subtaskingEnabled": False,
                "id": 100,
                "projectKey": "TEST",
            },
            "created": "2017-07-20T16:10:27Z",
            "content": {
                "comment": None,
                "description": "test description",
                "repository": {
                    "description": "test description",
                    "id": 100,
                    "name": "test repository",
                },
                "changes": [
                    {
                        "field": "description",
                        "old_value": "descriptions",
                        "new_value": "descriptions\nadd",
                    },
                    {
                        "field": "assigner",
                        "old_value": "John Due",
                        "new_value": "Jane Due",
                    },
                    {
                        "field": "issue",
                        "old_value": "TEST-10",
                        "new_value": "",
                    },
                    {
                        "field": "status",
                        "old_value": "1",
                        "new_value": "2",
                    },
                ],
                "number": 100,
                "summary": "test pull request",
                "assignee": None,
                "base": "master",
                "branch": "feature",
                "diff": "1c1\n<test description---\n>test",
                "issue": None,
                "id": 100,
            },
            "notifications": [],
            "createdUser": {
                "roleType": 1,
                "name": "John Due",
                "userId": None,
                "nulabAccount": None,
                "mailAddress": None,
                "id": 103640,
            },
            "type": 19,
            "id": 10,
        }
        app.handle(event)

    def test_comment_pull_request(self, app):
        event = {
            "project": {
                "archived": False,
                "name": "TestProject",
                "chartEnabled": False,
                "subtaskingEnabled": False,
                "id": 100,
                "projectKey": "TEST",
            },
            "created": "2017-07-20T16:10:32Z",
            "content": {
                "comment": {
                    "content": "test comment",
                    "id": 100,
                },
                "description": "test description",
                "repository": {
                    "description": "test description",
                    "id": 100,
                    "name": "test repository",
                },
                "changes": [],
                "number": 100,
                "summary": "test pull request",
                "assignee": None,
                "base": "master",
                "branch": "feature",
                "diff": None,
                "issue": None,
                "id": 100,
            },
            "notifications": [],
            "createdUser": {
                "roleType": 1,
                "name": "John Due",
                "userId": None,
                "nulabAccount": None,
                "mailAddress": None,
                "id": 103640,
            },
            "type": 20,
            "id": 10,
        }
        app.handle(event)
