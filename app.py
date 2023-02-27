from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///decisions.db'
db = SQLAlchemy(app)

class Decision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    decision1 = db.Column(db.String(80))
    decision2 = db.Column(db.String(80))
    decision1_rating = db.Column(db.Integer)
    decision2_rating = db.Column(db.Integer)

    def __repr__(self):
        return '<Decision {}: {} vs {}>'.format(self.id, self.decision1, self.decision2)


def weigh_decisions():
    decision1 = request.json['decision1']
    decision2 = request.json['decision2']
    decision1_rating = request.json['decision1_rating']
    decision2_rating = request.json['decision2_rating']

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

    decision = Decision(decision1=decision1, decision2=decision2, decision1_rating=decision1_rating, decision2_rating=decision2_rating)

    db.session.add(decision)
    db.session.commit()

    if decision1_rating > decision2_rating:
        print("Go ahead with {}: ".format(decision1))
    else:
        print("Go ahead with {}: ".format(decision2))

    decisions = Decision.query.all()
    decision_names = [d.decision1 + " vs " + d.decision2 for d in decisions]
    decision_ratings = [d.decision1_rating + d.decision2_rating for d in decisions]

    plt.bar(decision_names, decision_ratings)
    plt.show()

if __name__ == '__main__':
    app.run()
