from flask import Flask, request, jsonify
import sqlite3
import os
import matplotlib.pyplot as plt


app = Flask(__name__)
conn = sqlite3.connect('../decisions.db', check_same_thread=False)

@app.route('/')
class Decision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    decision1 = db.Column(db.String(80))
    decision2 = db.Column(db.String(80))
    decision1_rating = db.Column(db.Integer)
    decision2_rating = db.Column(db.Integer)

    def __repr__(self):
        return '<Decision {}: {} vs {}>'.format(self.id, self.decision1, self.decision2)


def weigh_decisions():
    decision1 = input("Enter the first decision: ")
    decision2 = input("Enter the second decision: ")

    decision1_rating = 0
    decision2_rating = 0

    self_efficacy = input("Which decision will make you feel more confident and capable? ({} or {}): enter 1 or 2)  ".format(decision1, decision2)).lower()
    if self_efficacy == "1":
        decision1_rating += 1
    else:
        decision2_rating += 1
    growth = input("Which decision will offer you more opportunities to grow and develop as a person? ({} or {}): ".format(decision1, decision2)).lower()
    if growth == "1":
        decision1_rating += 1
    else:
        decision2_rating += 1

    meaning = input("Which decision will give you greater meaning in life? (choose 1 or 2")
    if meaning == "1":
        decision1_rating += 1
    else:
        decision2_rating += 1
    regret = input("Are you more likely to regret not make which decision {} or {}? (choose 1 or 2): ".format(decision1, decision2,)).lower()
    if regret == "1":
        decision1_rating += 1
    else:
        decision2_rating += 1
    wise_counsel = input("What would the wisest version of yourself counsel you to do? ({} or {}): ".format(decision1, decision2)).lower()
    if wise_counsel == "1":
        decision1_rating += 1
    else:
        decision2_rating += 1

    # Connect to database
    conn = sqlite3.connect("../decisions.db")
    c = conn.cursor()
    # Create table if it doesn't already exist
    c.execute('''CREATE TABLE IF NOT EXISTS decisions
                 (decision text, rating integer)''')

    # Insert the two decisions and their ratings into the database
    c.execute("INSERT INTO decisions VALUES (?, ?)", (decision1, decision1_rating))
    c.execute("INSERT INTO decisions VALUES (?, ?)", (decision2, decision2_rating))
    conn.commit()

    if decision1_rating > decision2_rating:
        print("Go ahead with {}: ".format(decision1))
    else:
        print("Go ahead with {}: ".format(decision2))

    # Plot the ratings of all the decisions stored in the database
    c.execute("SELECT * from decisions")
    rows = c.fetchall()
    decision_names = [row[0] for row in rows]
    decision_ratings = [row[1] for row in rows]
    plt.bar(decision_names, decision_ratings)
    plt.show()

    conn.close()
if __name__ == '__main__':
    app.run()