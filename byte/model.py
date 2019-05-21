import sqlite3


def init_db():
    conn = sqlite3.connect('skill.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM fullstacktable")
    except:
        c.execute("""create table fullstacktable (name TEXT,id REAL)""")
    conn.commit()
    conn.close()

def show():
    conn=sqlite3.connect('skill.db')
    c=conn.cursor()
    full_stack_results=c.execute("SELECT * FROM fullstacktable;")
    python_list=[]
    for item in full_stack_results:
        python_list.append([item[1]])
    return python_list
    # print(python_list)
# show()

def datasci():
    conn=sqlite3.connect('skill.db')
    c=conn.cursor()
    data=c.execute("SELECT * from datascience datascience;")
    science = []
    for item in data:
        science.append([item[1]])
    return science

def get_score(players):
    conn = sqlite3.connect('skill.db')
    c = conn.cursor()
    l = []
    for item in players:
        value = c.execute("SELECT [value] FROM fullstacktable WHERE [name]=(:uname)",{'uname':item}).fetchall()
        # print(type(value))
        l.extend(value)
    # print(type(l))
    s = 0
    for i in l:
        s+=sum(i)
    return s


        # l.append(value)
    # print(l)

if __name__=='__main__':
    init_db()
