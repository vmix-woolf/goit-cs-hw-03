-- Отримати всі завдання певного користувача
SELECT * FROM tasks WHERE user_id = 1;
-- Вибрати завдання за певним статусом
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');
-- Оновити статус конкретного завдання
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'completed') WHERE id = 3;
-- Отримати список користувачів, які не мають жодного завдання
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);
-- Додати нове завдання для конкретного користувача
INSERT INTO tasks (title, description, status_id, user_id)
  VALUES (
          'Learn graph theory',
          'graph theory is the study of graphs, which are mathematical structures used to model pairwise relations between objects',
          (SELECT id FROM status WHERE name = 'new'),
          3
  );
-- Отримати всі завдання, які ще не завершено
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');
-- Видалити конкретне завдання
DELETE FROM tasks WHERE id = 21;
-- Знайти користувачів з певною електронною поштою
SELECT * FROM users WHERE email LIKE '%example.com';
-- Оновити ім'я користувача
UPDATE users SET fullname = 'Vladimir Zelensky' WHERE id = 9;
-- Отримати кількість завдань для кожного статусу
SELECT s.name, COUNT(t.id) FROM status s LEFT JOIN tasks t ON s.id = t.status_id GROUP BY s.name;
-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
SELECT t.* FROM tasks t INNER JOIN users u ON t.user_id = u.id WHERE u.email LIKE '%example.net';
-- Отримати список завдань, що не мають опису
SELECT * FROM tasks WHERE description IS NULL OR description = '';
-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
SELECT u.fullname, t.title FROM users u INNER JOIN tasks t ON u.id = t.user_id WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');
-- Отримати користувачів та кількість їхніх завдань
SELECT u.fullname, COUNT(t.id) FROM users u LEFT JOIN tasks t ON u.id = t.user_id GROUP BY u.fullname;