from datetime import datetime, timedelta
from .database import Table, session


class Interface:
    def __init__(self):
        self.menu_items = ["1) Today's tasks", "2) Week's tasks", "3) All tasks", "4) Missed tasks", "5) Add task",
                           "6) Delete task", "0) Exit"]
        self.start()
        self.rows = None

    def menu(self):
        print()
        for option in self.menu_items:
            print(option)

    def today(self):
        date_beg = datetime.today()
        self.rows = session.query(Table).filter(Table.deadline == date_beg.date()).all()
        print()
        print('Today {}:'.format(date_beg.strftime('%d %b')))
        self.task_display(1)
        self.start()

    def week(self):
        date_beg = datetime.today()
        print()
        for var_date in (date_beg.date() + timedelta(i) for i in range(7)):
            self.rows = session.query(Table).filter(Table.deadline == var_date).all()
            print('{}:'.format(var_date.strftime('%A %d %b')))
            self.task_display(1)
            print()
        self.start()

    def all(self):
        print()
        print('All Tasks:')
        self.rows = session.query(Table).order_by(Table.deadline).all()
        self.task_display(2)
        self.start()

    def missed(self):
        print()
        print('Missed tasks:')
        date_beg = datetime.today()
        self.rows = session.query(Table) \
            .filter(Table.deadline < date_beg.date()) \
            .order_by(Table.deadline).all()
        self.task_display(2, 'Nothing is Missed')
        self.start()

    def add(self):
        task = input('Enter task\n')
        deadline = datetime.strptime(input('Enter deadline\n'), '%Y-%m-%d')
        new_row = Table(task=task, deadline=deadline)
        session.add(new_row)
        session.commit()
        print('The task has been added!')
        self.start()

    def delete(self):
        print('\nChoose the number of the task you want to delete:')
        self.rows = session.query(Table).order_by(Table.deadline).all()
        self.task_display(2)
        id_delete = int(input())
        delete_task = self.rows[id_delete - 1]
        session.delete(delete_task)
        session.commit()
        self.start()

    def task_display(self, display_type, empty_message=None):
        if self.rows:
            if display_type == 1:
                n = 1
                for row in self.rows:
                    print('{}. {}'.format(n, row.task))
                    n += 1
            else:
                n = 1
                for row in self.rows:
                    print('{}. {}. {}'.format(n, row.task, row.deadline.strftime('%d %b')))
                    n += 1
        else:
            if empty_message is None:
                print('Nothing to do!')
            else:
                print(empty_message)

    def start(self):
        self.menu()
        choice = int(input())

        if choice == 1:
            self.today()
        elif choice == 2:
            self.week()
        elif choice == 3:
            self.all()
        elif choice == 4:
            self.missed()
        elif choice == 5:
            self.add()
        elif choice == 6:
            self.delete()
        else:
            print('Bye!')
            exit()


if __name__ == "__main__":
    Interface()
