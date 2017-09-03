insert into user (id, username, password, email, created, modified) VALUES (1, 'cbi', 'test', 'cbisig@gmail.com', date('now'), date('now'));
insert into project (id, title, description, creator_id, created, modified) VALUES (1, 'Dummy Project', 'First dummy project', 1, date('now'), date('now'));
insert into task (id, title, description, duedate, creator_id, assignee_id, project_id, finished, created, modified) VALUES (1, 'Dummy Task', 'Frist dummy task', '2017-09-15 14:00:00.000', 1, 1, 1, 0, date('now'), date('now'));
insert into note (id, note, creator_id, task_id, created, modified) VALUES (1, 'Dummy note', 1, 1, date('now'), date('now'));

