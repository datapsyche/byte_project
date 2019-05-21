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
        python_list.append([item[0]])
    return python_list
    # print(python_list)
# show()







if __name__=='__main__':
    init_db()
