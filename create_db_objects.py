import sqlite3


con = sqlite3.connect("DB/HomeEvents.db")

cursor = con.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Task;
DROP TABLE IF EXISTS TaskLogExtended;
""")

con.execute(r"""
CREATE TABLE Task
(
     id           INTEGER PRIMARY KEY AUTOINCREMENT /* Идентификатор задачи   */
    ,name         TEXT NOT NULL                     /* Название               */
    ,createDtm    TEXT                              /* Дата время создания    */
    ,executorName TEXT                              /* Имя того, кто выполнил */
    ,completeDtm  TEXT                              /* Дата время выполнения  */
    ,costPoint    TEXT                              /* Стоимость баллов       */
    ,decription   TEXT                              /* Описание               */
    ,isComplete   INTEGER                           /* Завершена или нет      */

)
""")

con.execute("""
CREATE TABLE TaskLogExtended
(
     taskId      INTEGER
    ,paramId     INTEGER
    ,value       TEXT
)
""")

