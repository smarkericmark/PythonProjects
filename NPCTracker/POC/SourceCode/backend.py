"""

The Backend of my app

"""

import sqlite3

def connect():
	conn=sqlite3.connect("npcs.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS npc (id INTEGER PRIMARY KEY, name text, hp integer, info  text, ac integer, stre text, dex text, con text, inte text, wis text, cha text, saves text, cr integer, skills text, blurb text)")
	conn.commit()
	conn.close()

def insert(name,hp,info,ac,stre,dex,con,inte,wis,cha,saves,cr,skills,blurb):
	conn=sqlite3.connect("npcs.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO npc VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(name,hp,info,ac,stre,dex,con,inte,wis,cha,saves,cr,skills,blurb))
	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect("npcs.db")
	cur=conn.cursor()
	#cur.execute("SELECT id || name || ' the ' || info || ' CR: ' || cr FROM npc") #, SELECT info, cr FROM npc)
	cur.execute("SELECT * FROM npc")
	rows=cur.fetchall()
	conn.close()
	return rows

def search(name='',hp='',info='',ac='',stre='',dex='',con='',inte='',wis='',cha='',saves='',cr='',skills='',blurb=''):
	conn=sqlite3.connect("npcs.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM npc where name=? OR hp=? OR info=? OR ac=? OR stre=? OR dex=? OR con=? OR inte=? OR wis=? OR cha=? OR saves=? OR cr=? OR skills=? OR blurb=?" ,(name,hp,info,ac,stre,dex,con,inte,wis,cha,saves,cr,skills,blurb))
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn=sqlite3.connect("npcs.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM npc where id=?",(id,))
	conn.commit()
	conn.close()

def update(id,name,hp,info,ac,stre,dex,con,inte,wis,cha,saves,cr,skills,blurb):
	conn=sqlite3.connect("npcs.db")
	cur=conn.cursor()
	cur.execute("UPDATE npc SET name=?, hp=?, info=?, ac=?, stre=?, dex=?, con=?, inte=?, wis=?, cha=?, saves=?, cr=?, skills=?, blurb=? WHERE id =?", (name,hp,info,ac,stre,dex,con,inte,wis,cha,saves,cr,skills,blurb,id))
	conn.commit()
	conn.close()

connect()

# Testing the Backend commands
#insert('Milton', 20, 'Elf Assassin',14,'(12)+1','(12)+1','(12)+1','(12)+1','(12)+1','(12)+1','Dex +5',3,'Stealth +10','Lots of words will go here')
#print(view())